# Ricerca: pattern agentici di accesso al dato (Text2SQL, RAG, agentic search, GraphRAG, semantic layer)

Ricerca dell'8 settembre 2026 a supporto della sezione 6 (e della 7 per il semantic layer) dell'incontro 28. Fonti primarie verificate; le cautele indicano ciò che spesso si dice in modo impreciso.

## 1. GraphRAG di Microsoft

- Paper: Edge et al., *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, arXiv 2404.16130, v1 24 aprile 2024, v2 19 febbraio 2025. Blog Microsoft Research "GraphRAG: Unlocking LLM discovery on narrative private data", 13 febbraio 2024.
- Pipeline: documenti → chunk (600 token, overlap 100) → estrazione con LLM di entità, relazioni e *claim* → grafo (istanze aggregate in nodi/archi con descrizioni riassunte) → community detection gerarchica con **Leiden** → *community summaries/report* generati dall'LLM per ogni livello (C0 radice … C3 foglie) → **global search** map-reduce (ogni community report produce una risposta parziale, poi sintesi). La doc del repo aggiunge **local search** (entità + vicini + chunk sorgente), **DRIFT search** e **basic search** (vector RAG top-k, come confronto).
- Problema risolto: domande "globali" di sensemaking sull'intero corpus ("quali sono i temi principali?"), dove la RAG a chunk fallisce perché la vector search non aggrega; esempio del blog "What has Novorossiya done?" → la RAG base risponde "no specific information".
- Benchmark del paper: due corpora (podcast ~1M token, 1.669 chunk → 8.564 nodi/20.691 archi; notizie ~1,7M token, 3.197 chunk → 15.754 nodi/19.520 archi). LLM-as-judge su 4 criteri: Graph RAG batte la naive RAG in **comprehensiveness (72-83% win rate)** e **diversity (62-82%)**; misto su *empowerment*; **directness vinta dalla naive RAG** (criterio di controllo). Fedeltà (SelfCheckGPT) simile.
- Costi: README "GraphRAG indexing can be an expensive operation… start small". Indicizzazione del podcast (1M token): 281 minuti con gpt-4-turbo. Al query time i summary di radice usano il 2-3% dei token rispetto al testo sorgente (9-43× meno).

Fonti: https://arxiv.org/abs/2404.16130 · https://microsoft.github.io/graphrag/ · https://github.com/microsoft/graphrag · https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/

Cautele: i vantaggi misurati sono su comprehensiveness/diversity con giudice LLM, non su accuratezza fattuale; sulla directness perde. Confronto solo su domande globali generate dall'LLM. I nodi sono entità estratte dall'LLM, non documenti. Il costo è all'indicizzazione, non alla query.

## 2. Lexical graph (Neo4j)

- graphrag.com è mantenuto da Neo4j (CC BY 4.0). Il *lexical graph* è il grafo `Document` → `Chunk` con relazioni **`PART_OF`** (chunk→documento) e **`NEXT`** (chunk→chunk successivo); i nodi Chunk hanno `text` ed `embedding`. È il pattern base del Basic Retriever.
- Variante "Lexical Graph with Extracted Entities": nodi `Entity` collegati ai chunk con **`HAS_ENTITY`** e fra loro con relazioni tipizzate (genericamente `RELATES_TO`); serve al Graph-Enhanced Vector Search. Altre varianti: hierarchical, parent-child, sibling, hypothetical questions, community summaries; memory graphs. Distinzione lexical graph vs **domain graph**.
- Retriever elencati: Basic (vector top-k sui chunk), Parent-Child, Hypothetical Question, Graph-Enhanced Vector Search (traversal dai chunk trovati), Local, Global Community Summary, Text2Cypher, Cypher Templates, Dynamic Cypher Generation, Metadata Filtering, Pattern Matching.

Fonti: https://graphrag.com/reference/ · https://graphrag.com/reference/knowledge-graph/lexical-graph/ · "The GraphRAG Field Guide", Neo4j developer blog, 16 settembre 2024, https://neo4j.com/blog/developer/graphrag-field-guide-rag-patterns/

Cautele: per Neo4j "GraphRAG" è un ombrello di pattern; il GraphRAG di Microsoft corrisponde a Global Community Summary + Local Retriever. Il lexical graph da solo non contiene entità. In slide: "PART_OF + NEXT" citando il Field Guide.

## 3. Agentic search / agentic RAG vs RAG classica

- (a) RAG a un colpo: Anthropic "Contextual Retrieval" (19 set 2024): chunk → embedding (+ BM25) → top-k → prompt. Weaviate "What is Agentic RAG" (5 nov 2024): *vanilla/naive RAG*, "retrieve once, generate once". **Nessuna fonte primaria usa "RAG 1.0"**: etichetta didattica.
- (b) Search come tool ripetuto: Anthropic "Building effective agents" (19 dic 2024): l'*augmented LLM* genera le proprie query, sceglie i tool; agenti = LLM che usano tool in un loop sul feedback ambientale; "aggiungere complessità solo quando migliora dimostrabilmente". Anthropic "Effective context engineering for AI agents" (29 set 2025): retrieval *just-in-time* con identificatori leggeri caricati a runtime via tool; Claude Code usa `glob`/`grep`/`head`/`tail` senza indice; raccomandata una **strategia ibrida**. Weaviate: l'agente decide se recuperare, con quale tool, riformula, ri-recupera, valida.
- Claude Code: Boris Cherny (Pragmatic Engineer, 4 marzo 2026): provati vector DB locali e indicizzazione, "tutti con svantaggi (indici stale, complessità dei permessi)"; "plain glob and grep, driven by the model, beat everything".
- (c) Contextual Retrieval: metrica = **1 − recall@20** (failure rate). Baseline 5,7% → contextual embeddings + contextual BM25 **2,9% (−49%)** → con reranking **1,9% (−67%)**. Costo one-off con prompt caching: 1,02 $ per milione di token. Consiglio: sotto ~200k token (~500 pagine) tutto nel contesto, senza RAG.

Fonti: https://www.anthropic.com/news/contextual-retrieval · https://www.anthropic.com/research/building-effective-agents · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · https://weaviate.io/blog/what-is-agentic-rag · https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny

Cautele: il 49%/67% è riduzione relativa del failure rate a top-20 (da 5,7% a 1,9%), non "accuratezza +49%". Non esiste un post Anthropic ufficiale "grep batte RAG": è un'intervista al creatore di Claude Code, e vale per codice su filesystem. "Agentic RAG" non ha definizione canonica. Anthropic raccomanda l'ibrido.

## 4. Text2SQL: benchmark e limiti

- BIRD (Li et al., NeurIPS 2023; arXiv 2305.03111): 12.751 coppie, 95 DB, 33,4 GB, 37 domini; metrica Execution Accuracy; ChatGPT 2023 40,08% vs **umani 92,96%** (dev). Leaderboard test (26 ago 2026): SiriusAI-SQL (Tencent) **82,28%**; DataGallery (Huawei) 82,22%; AskData+GPT-4o 81,95%; Agentar-Scale-SQL 81,67%; Sber 81,33%.
- Spider 2.0 (Lei et al., ICLR 2025; arXiv 2411.07763): 632 task enterprise (>1.000 colonne, SQL >100 righe, BigQuery/Snowflake); o1-preview **21,3%** contro 91,2% su Spider 1.0 e 73,0% su BIRD. Top a settembre 2026: Snow 96,70 (Genloop Sentinel v2 Pro), Lite 76,23, DBT 65,6.
- Modi di fallimento (Spider 2.0 §4.2, 300 esempi): analisi dati errata 35,5% (dialetto 10,3%, calcoli 7,5%, query planning CTE/nested 17,7%); **schema linking sbagliato 27,6%** (colonne 16,6%, tabelle 10,1%); **JOIN errate 8,3%** ("i DB spesso mancano di foreign key esplicite"). BIRD: valori di DB e conoscenza esterna.
- Requisiti informativi (vendor, punto 5): descrizioni di tabelle/colonne, sinonimi, valori di esempio, definizioni delle metriche, join/relazioni, query verificate.
- Qualità dei benchmark: Jin et al., "Text-to-SQL Benchmarks are Broken", CIDR 2026: errori di annotazione nel **52,8% di BIRD Mini-Dev** e **66,1% di Spider 2.0-Snow**; ricalcolo di 5 agenti: variazioni da −2 a +19 punti.
- dbt, 7 apr 2026 (11 domande × 20 run, ACME Insurance): Claude Sonnet 4.6 90,0% → 98,2%, GPT-5.3-Codex 84,1% → 100% con semantic layer; "with text-to-SQL, failure looks like a plausible but incorrect answer; with the Semantic Layer, failure looks like an error message". Rumiantsau & Fokeev, arXiv 2604.25149 (28 apr 2026): Contoso, 100 domande, 3 modelli, schema solo 45,5-50,5% → +17/+23 punti con un documento semantico di 4 KB.

Fonti: https://bird-bench.github.io/ · https://arxiv.org/abs/2305.03111 · https://spider2-sql.github.io/ · https://arxiv.org/abs/2411.07763 · https://www.vldb.org/cidrdb/papers/2026/p5-jin.pdf · https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026

Cautele: "fanout" e "colonne inventate" non sono categorie dei paper (schema linking e JOIN lo sono): presentarli come esempi. Il 96,7% su Spider2-Snow è di sistemi agentici commerciali: in aula "da ~20% (2024) a >90% (2026) sul sottoinsieme Snow, ~76% su Lite", ricordando CIDR 2026. Il 92,96% umano è sul dev set. I numeri dbt sono di vendor su 11 domande.

## 5. Semantic layer per agenti e MCP

- **Snowflake Cortex Analyst** (blog 15 ago 2024): "raw schemas often lack semantic information"; il semantic model YAML dà "names for measures and dimension columns, default aggregations, synonyms, descriptions, sample values"; claim "~90% or higher accuracy", "close to 2X more accurate than single-shot SQL generation". Oggi il modello è la **semantic view** (oggetto di schema): logical tables, relationships, facts, dimensions, metrics, sinonimi, descrizioni, **verified queries**, custom instructions. **MCP**: Snowflake-managed MCP server, GA 4 nov 2025; espone Cortex Analyst, Cortex Search, Cortex Agents, SQL execution.
- **Databricks**: best practices Genie: "quality table and column descriptions in Unity Catalog are critical for Genie accuracy"; gerarchia: SQL expressions per metriche/filtri, example SQL, testo libero come ultima risorsa; "metric views are particularly effective… pre-define metrics, dimensions, and aggregations"; "cinque tabelle o meno". Metric views UC: YAML con source, joins, dimensions, measures. 2026: Genie → "Genie One" (9 giu 2026), Genie Spaces → "Genie Agents" (9 lug 2026), **Genie Ontology** public preview 11 giu 2026, di default 6 ago 2026 ("governed semantic layer"); Genie One MCP server in Beta (doc 28 ago 2026).
- **dbt**: "Introducing the dbt MCP Server" (21 apr 2025, open source): discovery, querying via Semantic Layer + SQL, comandi dbt; tool `list_metrics`, `get_dimensions`, `query_metrics`; "LLM-generated analyses are based on rigorous definitions instantiated as code". Remote dbt MCP server e dbt Agents: 14 ott 2025 ("without shared context, an agent guesses").

Fonti: https://www.snowflake.com/en/blog/cortex-analyst-ai-self-service-analytics/ · https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst · https://docs.snowflake.com/en/user-guide/views-semantic/overview · https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp · https://docs.databricks.com/aws/en/genie/best-practices · https://docs.databricks.com/aws/en/metric-views/ · https://docs.databricks.com/aws/en/agents/mcp-tools/genie-mcp · https://docs.getdbt.com/blog/introducing-dbt-mcp-server · https://www.getdbt.com/blog/dbt-agents-remote-dbt-mcp-server-trusted-ai-for-analytics · https://docs.getdbt.com/docs/dbt-ai/about-mcp

Cautele: il "~90%" di Snowflake è un claim di vendor. Metric views UC: dire "GA nel 2026". Remote dbt MCP: "disponibile da ottobre 2025". Snowflake: "semantic view (ex semantic model YAML)".

## Cose da dire con cautela in aula

1. GraphRAG "vince" solo su completezza e diversità giudicate da un LLM, su domande globali; sulla directness vince la RAG classica, e l'indicizzazione costa ore e milioni di token.
2. "RAG 1.0" e "agentic RAG" sono etichette didattiche: le fonti parlano di *naive RAG* e di *retrieval come tool in loop*; Anthropic raccomanda l'ibrido.
3. Il 49%/67% di Contextual Retrieval è una riduzione relativa del failure rate a top-20 (da 5,7% a 1,9%).
4. I benchmark Text2SQL hanno errori di annotazione nel 53-66% dei casi (CIDR 2026): percentuali come ordini di grandezza; i migliori risultati sono di sistemi agentici multi-passo.
5. Le prove che "il semantic layer rende affidabile il Text2SQL" sono di vendor o su piccoli set; il risultato robusto è qualitativo: con il semantic layer l'errore diventa un rifiuto, senza diventa un numero plausibile ma sbagliato.
