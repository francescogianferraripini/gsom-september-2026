# PC AI: 28 — Agentic AI: la preparazione della KB, regole per l'organizzazione dei dati

# Conoscenza: Dati, Informazioni, Significato e Conoscenza

## Organizziamo lo spazio

- L'importanza di modellare la conoscenza: i requisiti di una conoscenza utile in ambito aziendale
  - Ricercabile in modo progressivo
  - Non ridondante
  - Veritiera
  - Compounding
- Modellare la conoscenza non è solo per l'ai, ma l'ai ne ha dato evidenza.
  É un problema che viene da lontano (ricerca storia su Dewey, organizzazione delle biblioteche da Umberto Eco a J Edgar Hoover)?
- Know what VS Know how
- Lo spettro Strutturato VS Non Strutturato --> Dato: Strutturato = Informazione: Non Strutturato
- 

# Know what

## Dato Strutturato

Forma: Relazionale vs Document (JSON) based Fine: Transazionale vs Analitico

Tipizzazione del dato

Relazionale, standard comunque imprescindibile: Tabelle, Colonne, Tipi, PK, FK Il ruolo del sql: select dati e metriche, from - join, where, group by modelli transazionali vs analitico, da excel al dwh di kimball

I requisiti dei modelli relazionali transazionali: massimizzazione performance operativa e semplicità del coding.
La normalizzazione.
Check sui requisiti

I modelli relazionali analitici, derivazione che doveva sfuttare i DBMS nati per il transazionale.
Fatti e dimensioni.
La denormalizzazione.
Le metriche, il grano, le join, il fanout, le query multimetrica con subqueries.
Sicurezza: table, column e row level security.

Il Data Management come trasformazione di forma

Check sui requisiti

Qualità, completezza, ownership, dipendenze: punti aperti per spunti successivi.
L'antipattern fondamentale: una pipeline per report.
- la perdita di compounding

Un fatto naturale é che la struttura del dato strutturato deriva sempre da quella del sistema transazionale che lo gestisce, soprattutto su granularità

Pregi del modello di kimball

Limiti del modello di kimball e soluzioni, cenni al data vault.

Spettro dei tool: da Databricks a DuckDB

## Dato Non Strutturato

Non strutturato: da fatto (elemento informativo strutturato ex ante) a informazione spuria.
Da problema di analisi a problema di search.

I pattern di search:

- Keyword Search: bm25
- Semantic Search: embeddings

La retrieve è facile, il problema è la relevance:

- GraphRank
- Reranking - Colbert

## In mezzo allo spettro: i grafi

Il grafo in generale, da Eulero a Berners Lee Il property graph Mini focus su Cypher Perchè non un db relazionale?
Il problema di traversal e shortest path Il grafo come modello dei dati, spesso indipendente dalla sua implementazione tecnica: da Neo4j a DuckDB

# Pattern agentici di accesso al dato

Text2Sql.
Requisiti informativi del Text2Sql Problemi

Rag 1.0 Search as tool - Agentic search Problemi - sintesi di concetti al di là del contenuto dei singoli chunk Graphrag Lexical Graph Community detection

## Superare i limiti del Data Management

- Managing data as a product
- Semantic modeling e ontologie
  - Ontologie e knowledge graphs
  - Nel dato strutturato
  - Nel dato non strutturato
  - Approccio convergente

# Know how

Skill: esempio quantyca Skill + Ontologie per governance dei
