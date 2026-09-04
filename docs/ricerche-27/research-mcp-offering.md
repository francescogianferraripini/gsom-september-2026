# Ricerca: stato MCP, offerta Anthropic, framework di harness (4 settembre 2026)

## 1. MCP (Model Context Protocol)

### Versioni della specifica (identificate per data, non per "1.0/2.0")
MCP non ha mai avuto numeri di versione tipo 1.0/2.0: ogni revisione è identificata da una data (`YYYY-MM-DD`).
| Revisione | Novità principali | Fonte |
|---|---|---|
| 2024-11-05 | Prima release: JSON-RPC, stdio, trasporto **HTTP+SSE** (endpoint SSE + endpoint POST), handshake `initialize` | modelcontextprotocol.io/specification/2024-11-05 |
| 2025-03-26 | **Streamable HTTP** sostituisce HTTP+SSE (un solo endpoint POST/GET, SSE opzionale); OAuth 2.1; tool annotations; batching JSON-RPC | modelcontextprotocol.io/specification/2025-03-26/changelog |
| 2025-06-18 | **Elicitation**; structured tool output; server MCP come OAuth Resource Server (RFC 8707); header `MCP-Protocol-Version`; rimosso batching | modelcontextprotocol.io/specification/2025-06-18/changelog |
| 2025-11-25 | Tasks (sperimentale), URL-mode elicitation, icone, sampling con tools, OIDC discovery, Client ID Metadata Documents; governance/SDK tiering | modelcontextprotocol.io/specification/2025-11-25/changelog |
| **2026-07-28** (corrente) | **Core stateless**: rimossi handshake `initialize`, sessioni e `Mcp-Session-Id`; versione+capabilities in `_meta` di ogni richiesta; `server/discover`; MRTR; `subscriptions/listen`; Tasks come estensione; **deprecati Roots, Sampling, Logging** e HTTP+SSE | modelcontextprotocol.io/specification/2026-07-28/changelog ; blog.modelcontextprotocol.io/posts/2026-07-28/ |

### Come si chiama davvero "MCP 1.0 stateful vs 2.0 stateless"
- Non esiste "MCP 2.0". Il passaggio a cui il docente allude è reale ma va nominato così: **revisioni 2024-11-05 → 2025-11-25 = protocollo stateful** (handshake `initialize`, sessione `Mcp-Session-Id`, stream SSE GET per messaggi server→client, richieste server-initiated come `sampling/createMessage`), **revisione 2026-07-28 = core stateless** ("MCP is a stateless protocol: every request is self-contained" — pagina Architecture 2026-07-28).
- Attenzione a un secondo equivoco possibile: già dal 2025-03-26 Streamable HTTP permetteva server "stateless" *di fatto* (la sessione era `MAY`, non obbligatoria), ma il protocollo restava basato su handshake. La statelessness *di protocollo* arriva solo con 2026-07-28.
- Terzo equivoco: "SSE" non è la vecchia versione. Il trasporto 2024-11-05 si chiamava **HTTP+SSE** (deprecato dal 2025-03-26); SSE come *formato di streaming* è ancora usato da Streamable HTTP 2026-07-28 per le risposte scoped alla singola richiesta e per `subscriptions/listen`.
- Dettagli 2026-07-28 (transports/streamable-http): un solo endpoint POST; niente GET/DELETE (rispondono 405); header obbligatori `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name` (routing a livello di gateway senza parsare il body); niente resumability `Last-Event-ID`; stato cross-call via handle espliciti passati come argomenti dei tool; `tools/list` deterministico + `ttlMs`/`cacheScope` per il caching.
- Retrocompatibilità: finestra di deprecazione minima 12 mesi (feature lifecycle policy); i client moderni fanno fallback a `initialize` se il server è "legacy".

### Modello e primitive (spec 2026-07-28)
- **Host** (app LLM: crea/gestisce i client, consenso utente, aggrega contesto) → **Client** (1:1 con un server) → **Server** (espone capacità). JSON-RPC 2.0.
- Primitive **server-side**: **Tools** (funzioni per il modello), **Resources** (dati/contesto), **Prompts** (template per l'utente).
- Primitive **client-side**: **Elicitation** (server chiede input all'utente). **Sampling** (server chiede completions all'LLM) e **Roots** (perimetro filesystem) esistono ancora ma sono **deprecati** in 2026-07-28; oggi viaggiano tramite MRTR (`InputRequiredResult` → il client ritenta la richiesta con `inputResponses`).
- **Estensioni** opt-in: Tasks (operazioni lunghe con polling), MCP Apps (UI inline), Skills over MCP, Enterprise Managed Authorization.
- **Trasporti**: stdio (locale, subprocess) e Streamable HTTP (remoto). HTTP+SSE deprecato. Custom transport ammessi.
- Governance: dal 9 dic 2025 MCP è progetto fondatore della **Agentic AI Foundation** (Linux Foundation; co-fondata da Anthropic, Block, OpenAI). Fonte: blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ ; anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- Roadmap 22 ago 2026: messaging agentico (eventi server-initiated), unificazione trasporto HTTP, identità agenti (DPoP, WIF), "progressive discovery" dei tool. Fonte: blog.modelcontextprotocol.io/posts/mcp-roadmap/

### Registry ufficiale e numeri pubblici
- **Official MCP Registry** (registry.modelcontextprotocol.io): lanciato in preview l'8 set 2025, ancora "in preview" (modelcontextprotocol.io/registry/about). È un *metaregistry* (metadati `server.json`, namespace verificati via DNS/GitHub), pensato per essere consumato da aggregatori/marketplace, non direttamente dagli host. Backers: Anthropic, GitHub, PulseMCP, Microsoft.
- Numeri: Anthropic (9 dic 2025): "10.000 server attivi", 97M download SDK/mese. Registry API (dato terzo, safedep.io, 24 mag 2026): ~9.650 server "latest", ~29.000 record server/versione. Blog MCP (28 lug 2026): "close to half-a-billion downloads a month" degli SDK Tier 1; SDK TS e Python oltre 1 miliardo di download cumulati.

### Come progettare i tool (guidance ufficiale Anthropic)
- **"Writing effective tools for agents"** (anthropic.com/engineering/writing-tools-for-agents, 11 set 2025): non mappare le API 1:1; pochi tool mirati a workflow ad alto impatto; consolidare operazioni (es. `schedule_event` invece di `list_users`+`list_events`+`create_event`); namespacing per prefissi; restituire contesto semantico (nomi leggibili, non UUID), `response_format` conciso/dettagliato; paginazione/truncation; errori con istruzioni; descrizioni scritte "come per un nuovo collega".
- **Advanced tool use** (anthropic.com/engineering/advanced-tool-use, nov 2025) e doc **Tool Search Tool** (platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool): con `defer_loading: true` le definizioni non entrano nel contesto; Claude le cerca (varianti regex `tool_search_tool_regex_20251119` o BM25) e l'API espande solo i `tool_reference` trovati. Esempio ufficiale: 5 server MCP ≈ 55K token → ≈ 8.7K; accuratezza Opus 4.5 79,5% → 88,1%. Consigli: 3–5 tool più usati non-deferred; usare tool search sopra ~10 tool o >10K token di definizioni; con MCP connector si imposta `defer_loading` sul `mcp_toolset`. Complementari: **Programmatic Tool Calling** (orchestrazione via codice, −37% token) e **Tool Use Examples**.
- La stessa idea ("progressive discovery") è ora nella roadmap MCP ufficiale (ago 2026).

## 2. Offerta Anthropic (settembre 2026)
| Prodotto | Posizionamento (una riga) | Fonte |
|---|---|---|
| **Claude.ai** (web/mobile) | Chat consumer/prosumer; host MCP via "connettori" remoti; da ago 2026 ospita anche sessioni Cowork e Claude Code on the web (claude.ai/code). | support.claude.com/en/articles/11725091 ; claude.com/blog/cowork-web-mobile |
| **Claude Desktop** | App macOS/Windows: unico host che esegue **server MCP locali** (stdio, `claude_desktop_config.json`, Desktop Extensions one-click); contiene tab Cowork e Code. | support.claude.com/en/articles/10949351 ; anthropic.com/engineering/desktop-extensions |
| **Claude Cowork** | Harness "Claude Code senza codice" per knowledge worker: file, connettori, skills, browser integrato; desktop da gen 2026, web/mobile (cloud) da lug–ago 2026 per tutti i piani a pagamento. | support.claude.com/en/articles/13345190 ; claude.com/blog/cowork-web-mobile |
| **Claude Code** | Harness agentico per sviluppatori: CLI, IDE, desktop, web; espone MCP, hooks, skills, subagent, plugin, routines; stesso engine su tutte le superfici. | code.claude.com/docs/en/overview |
| **Claude Agent SDK** | Libreria Python/TypeScript che espone lo stesso agent loop, tool e context management di Claude Code, eseguito nel processo dello sviluppatore (ex "Claude Code SDK", rinominato set 2025). | code.claude.com/docs/en/agent-sdk/overview |
| **Claude Managed Agents** | Beta pubblica dall'8–9 apr 2026 (header `managed-agents-2026-04-01`): harness + sandbox + sessioni **hosted da Anthropic** via REST; concetti Agent/Environment/Session/Events; $0,08/session-hour; prodotto separato dall'SDK. | platform.claude.com/docs/en/managed-agents/overview |
| **Claude in Chrome** | Estensione browser-use (vede la pagina, clicca, compila form con i login dell'utente); dal 12 ago 2026 il side panel è una sessione Cowork (Max/Team, Pro in rollout). | claude.com/blog/cowork-chrome-side-panel |
| **Claude Tag (Slack)** | Dal 23 giu 2026, beta per Team/Enterprise: "@Claude" come collega condiviso nel canale, con memoria, scheduled task e connettori scoped per canale; descritto come evoluzione di Claude Code/Cowork. | anthropic.com/news/introducing-claude-tag |

## 3. Framework/harness open e SDK dei provider
| Framework | Filosofia | Maturità | Fonte |
|---|---|---|---|
| **smolagents** (Hugging Face) | **Code-agent**: `CodeAgent` scrive azioni in Python (composizione nativa: loop, condizioni), sandbox via E2B/Modal/Docker; c'è anche `ToolCallingAgent` JSON; model-agnostic; tool da server MCP. | ~1.000 righe di core, ottimo per prototipi; sicurezza dell'esecuzione a carico dell'utente. | huggingface.co/docs/smolagents/index |
| **LangChain / LangGraph** | LangChain = framework agenti (astrazioni modelli/tool); LangGraph = **runtime di orchestrazione a grafo/state machine**: durable execution, persistenza, streaming, human-in-the-loop, mix di passi deterministici e LLM. | Il più "enterprise-ready" fra gli open; v1.x stabile. | docs.langchain.com/oss/python/langgraph/overview |
| **Agno** (ex Phidata) | Agenti, team e workflow Python con memoria/knowledge/guardrail; **AgentOS** come runtime di produzione + Control Plane; deploy multi-canale (REST, MCP server, Slack). | Apache 2.0, orientato a "agenti come servizi". | docs.agno.com/introduction |
| **OpenAI Agents SDK** | Tool-calling minimalista: primitive **Agents, Handoffs, Guardrails, Sessions**; tracing integrato; varianti realtime/voice/sandbox; supporta MCP. | Production-ready secondo OpenAI; nativo per Responses API. | openai.github.io/openai-agents-python |
| **Google ADK** | Code-first, "production agents, not prototypes": workflow agent Sequential/Parallel/Loop, multi-agente, A2A + MCP; Python/TS/Go/Java/Kotlin. | ADK 2.0 GA (graph workflows). | adk.dev |
| **CrewAI** | **Role-based**: Crews (agenti con ruolo che collaborano) + Flows (event-driven, state management). | "Production-ready", forte community (100k+ certificati). | docs.crewai.com/en/introduction |
| **Pydantic AI** | **Type-safe end-to-end**: output strutturati, dependency injection, model-agnostic; `capabilities=[MCP(url)]`; durable execution via Temporal/DBOS/Prefect. | Maturo, focus su correttezza e testabilità. | pydantic.dev/docs/ai/overview |
| **Claude Agent SDK** (per confronto) | Harness "batteries-included" identico a Claude Code (tool file/bash, subagent, hooks, MCP, skills); non model-agnostic. | Production; vedi sezione 2. | code.claude.com/docs/en/agent-sdk/overview |

Tassonomia utile per la lezione: (a) **code-agent** (smolagents CodeAgent, Programmatic Tool Calling di Anthropic) vs **tool-calling JSON** (OpenAI Agents SDK, Pydantic AI, ToolCallingAgent); (b) **graph/orchestration** (LangGraph, ADK workflow agents, CrewAI Flows); (c) **harness completi con runtime** (Claude Code/Agent SDK, Managed Agents, Agno AgentOS). Tutti i framework elencati oggi consumano server MCP come sorgente di tool.
