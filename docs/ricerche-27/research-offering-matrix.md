# Matrice di confronto: offerta Anthropic vs framework open (verificata al 4 settembre 2026)

Legenda: **sì** / **no** / **parz.** (parziale) + dettaglio. `[NV]` = cella NON verificata su fonte primaria (inferenza o assenza di doc). Fonti numerate in fondo; nelle celle si cita `[n]`.

## Tabella A — Prodotti Anthropic

| Colonna | Claude.ai (web) | Claude Desktop | Claude Cowork | Claude Code | Claude Agent SDK | Managed Agents |
|---|---|---|---|---|---|---|
| 1. Chi lo usa / superficie | Chat web + mobile per utenti finali; da lug-ago 2026 ospita anche Cowork e Claude Code on the web [10][11] | App macOS/Windows (Linux beta); contiene tab Chat, Cowork e Code [4][6] | Knowledge worker: desktop (esperienza completa), web, mobile, side panel Chrome [10][11] | Sviluppatori: CLI, VS Code/JetBrains, desktop app, web (claude.ai/code), CI, Slack [1] | Sviluppatori: libreria Python/TypeScript; altre lingue via CLI subprocess `-p` [2] | Sviluppatori: API REST hosted (+SDK Py/TS/Go/Java/C#/PHP/Ruby, CLI `ant`) [3] |
| 2. Chi ospita l'harness | **Anthropic** (chat, tool, sandbox file lato server) [5] | **Utente sul device** per l'app e i server MCP locali; il code-exec della chat resta in sandbox Anthropic [4][5]; Cowork locale = loop nativo su device + VM locale [9] | **Anthropic** di default (cloud beta: "agent loop and code execution run in an isolated, temporary sandbox on Anthropic-managed infrastructure"); alternativa **locale** su desktop [9] | **Utente sul device** (CLI/IDE/desktop); **Anthropic** per sessioni cloud (VM isolate) o **infra dell'organizzazione** via self-hosted environments [1][17] | **Sviluppatore sulla propria infra**: "spawns and supervises a `claude` CLI subprocess" nel tuo container [8] | **Anthropic** (cloud sandbox) oppure **self-hosted sandbox** sulla tua infra, sempre con harness gestito da Anthropic [3] |
| 3. Loop agentico incluso | sì — scritto da Anthropic, non configurabile [5] `[NV: nessuna doc descrive il loop]` | sì — come Claude.ai; Cowork/Code integrati [4][9] | sì — "extends the agentic capabilities of Claude Code" [6] | sì — loop di Claude Code, scritto da Anthropic [1] | sì — "runs the agent loop in your own process"; stesso loop di Claude Code [2] | sì — "Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment" [3] |
| 4. Sandbox / esecuzione codice | Container sandbox **Anthropic**, mai condiviso fra utenti, no rete verso l'esterno (Enterprise: whitelisting domini) [5] | Chat: sandbox Anthropic [5]; Cowork locale: **VM Linux locale** (Hyper-V / Apple Virtualization) isolata dall'host [9]; Code: sandbox locale di Claude Code [15] | Cloud: sandbox effimera Anthropic per sessione, no accesso a indirizzi privati/metadata [9]; locale: VM dedicata su device [9] | Locale: bash sandbox opt-in (`/sandbox`: Seatbelt su macOS, bubblewrap su Linux/WSL2, no Windows nativo) [15]; web: VM Anthropic isolate o self-hosted [17] | **Tuo**: la doc raccomanda container/sandbox (Docker, gVisor, Firecracker, provider SaaS); nessuna sandbox inclusa [8] | Sandbox **Anthropic** (cloud) o **self-hosted** ("Environment"); tool bash/file/glob/grep girano lì; web_search/fetch girano sui server Anthropic anche con sandbox self-hosted [3][21] |
| 5. Supporto MCP | **parz.** — client MCP solo per **connettori remoti** (Streamable HTTP/OAuth); niente stdio locale [4] | **sì** — client MCP remoti + **server locali stdio** via Desktop Extensions `.mcpb` (Node/Python/binari, Node.js incluso) e `claude_desktop_config.json` [4][7] | **parz.** — connettori remoti; token "never enter the sandbox" (chiamate server-side); server MCP locali solo in esecuzione locale desktop [9] | **sì** — client stdio, HTTP (raccomandato), SSE (deprecato), WebSocket; OAuth 2.1; scope local/project/user; **è anche server MCP** (`claude mcp serve`) [12] | **sì** — stdio, HTTP/SSE, **server MCP in-process** (SDK MCP server); OAuth: nessun flusso interattivo, passi tu il token negli header [13] | **parz.** — solo server **remoti** (`type: "url"`, Streamable HTTP, SSE via fallback), auth tramite vault; server privati/locali via **MCP tunnels** (research preview) [22][19] |
| 6. Skills (SKILL.md) | **sì** — skill Anthropic (xlsx/docx/pptx/pdf) + custom (zip con SKILL.md), richiede code execution; Free→Enterprise [18] | **sì** — stesse skill dell'account claude.ai; Cowork le sincroniza a inizio sessione [18][16] | **sì** — carica le skill abilitate sull'account claude.ai, non `~/.claude/skills/` [16] | **sì** — `.claude/skills/<name>/SKILL.md`, standard aperto Agent Skills (agentskills.io) con estensioni Claude Code; commands fusi nelle skills [16] | **sì** — carica skills/commands/memory da `.claude/` e `~/.claude/` "same as Claude Code" [2] | **sì** — skill Anthropic pre-built + custom via Skills API (`skill_*`), o auto-discovery da `.claude/skills` di un repo GitHub montato; fino a 500 per sessione [20] |
| 7. Memoria persistente | **sì** — memoria per entry categorizzate + project memory; Free/Pro/Max on di default, Team/Enterprise off di default; import/export [14] | **sì** — stessa memoria claude.ai `[NV: doc desktop non esplicita]`; Cowork locale **non** condivide la memoria con la chat [14] | **parz.** — "Memory across Cowork and chat only works when Cowork runs in the cloud" [14] | **sì** — CLAUDE.md (managed/user/project/local) + **auto memory** (`~/.claude/projects/<p>/memory/MEMORY.md`, prime 200 righe/25 KB, machine-local) + memoria per subagent [23][24] | **sì** — stessi file di Claude Code, ma su disco locale del container: `SessionStore` mirrora solo i transcript, non CLAUDE.md/auto memory; multi-tenant richiede `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` [8] | **sì** — **memory store** (`memstore_*`, header beta `agent-memory-2026-07-22`) montato in `/mnt/memory/`, max 8 per sessione, versioni immutabili con redact, "dreaming" in research preview [25] |
| 8. Observability / tracing | **parz.** — Compliance API per Team/Enterprise `[NV: dettaglio non verificato]`; nessun tracing esposto all'utente | **parz.** — come Claude.ai `[NV]` | **parz.** — sessioni web/mobile "captured in the Compliance API" [6]; nessun tracing utente | **sì** — OpenTelemetry: metriche + eventi/log (prompt, tool_result, tool_decision, api_request); tracce distribuite **beta** (`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`); hooks; transcript JSONL [26] | **sì** — eredita OTel di Claude Code (span, metriche, log); prompt/tool input **esclusi di default** dagli export; hooks; messaggi stream tipizzati [8][2] | **sì** — event stream persistito server-side (`agent.tool_use`, `agent.mcp_tool_use`, `span.model_request_*` con usage, `session.usage`); webhooks; **nessuna integrazione OTel documentata** [19][21] |
| 9. Subagenti / multi-agente | **no** in chat `[NV: la doc non espone subagenti in chat]` | **parz.** — tramite Cowork/Code integrati [4] | **sì** — "breaks complex work into smaller tasks and coordinates parallel workstreams" [6] | **sì** — subagent markdown in `.claude/agents/` con contesto/tool/modello propri, limite 20 concorrenti, memoria persistente per subagent; agent teams sperimentali; background agents [27][1] | **sì** — subagenti via `AgentDefinition`; pattern multi-agent container; nessuna deadline wall-clock per subagent [2][8] | **sì** — `multiagent` coordinator con roster (≤20 agenti, 1 livello), thread persistenti, sandbox condivisa, contesto isolato; advisor thread [28] |
| 10. Modello | Solo Claude | Solo Claude | Solo Claude | Claude, ma via **Anthropic / Bedrock / Claude Platform on AWS / Google Agent Platform (ex Vertex) / Microsoft Foundry** + LLM gateway; cloud sessions solo con account Anthropic [29][17] | Claude via api.anthropic.com o Bedrock / Google Agent Platform [8] | Solo Claude "4.5 and later" (es. `claude-opus-5`); anche su Claude Platform on AWS [3][30] |
| 11. Maturità e data | GA; memoria per entry e Cowork/Code integrati nel 2026 [14][11] | GA su macOS/Windows; **beta su Ubuntu/Debian** [1] | **Beta** su web/mobile (lancio 7 lug 2026, rollout da Max); desktop per tutti i piani a pagamento; Chrome side panel in rollout [11][10] | GA (CLI ≥ v2.1.2xx); **web = research preview**; tracce OTel beta [1][17][26] | GA come libreria, versioni **< 1.0** (TS v0.3.x, Python v0.2.x, semver); ex "Claude Code SDK" [8][2] | **Beta pubblica** (header `managed-agents-2026-04-01`, abilitata di default per tutti gli account API); MCP tunnels e dreaming in research preview; non idoneo a ZDR/HIPAA [3] |

## Tabella B — Framework open

| Colonna | smolagents (Hugging Face) | LangChain / LangGraph | Agno |
|---|---|---|---|
| Filosofia (verificata) | **Code-agent**: `CodeAgent` "writes its actions in code" (composizione, loop, condizionali); `ToolCallingAgent` JSON come alternativa. Corretto. [31][32] | LangGraph = "low-level orchestration framework and runtime" a **grafo esplicito** (state, nodes, edges) con **durable execution**; LangChain `create_agent` gira sopra LangGraph. Corretto. [35][40] | **Agenti + runtime**: SDK (agents/teams/workflows) + **AgentOS** ("the FastAPI for agents", self-hosted, con Control Plane). Corretto. [41][42] |
| 1. Superficie | Libreria Python + CLI `smolagent`/`webagent` [31] | Libreria Python/JS; LangSmith Deployment per hosting [35][39] | Libreria Python; AgentOS espone REST, WebSocket, MCP server, Slack/Telegram/WhatsApp [42] |
| 2. Chi ospita | Sviluppatore (proprio processo) [31] | Sviluppatore; opzionale **LangSmith Deployment** (cloud gestito, hybrid, self-hosted, standalone Docker/K8s) [39] | Sviluppatore: "AgentOS runs in your infrastructure and writes runtime state to databases you configure" (Railway, Docker, AWS, GCP, K8s…) [42][41] |
| 3. Loop agentico | sì — ReAct multi-step, `max_steps`, ~1000 righe di core [31] | sì — `create_agent` (LangChain) o grafo custom (LangGraph) [40] | sì — `Agent.run()` con tool loop; Teams e Workflows [41] |
| 4. Sandbox | Default **locale non sicuro** (`LocalPythonExecutor` AST-based con import allowlist, "no local python sandbox can ever be completely secure"); remoto via `executor_type` = **Blaxel / E2B / Modal / Docker** (ma non supporta managed agents) [32] | **no** nativo — LangGraph non esegue codice; sandbox a carico dello sviluppatore `[NV: assenza di doc]` | **parz.** — nessuna sandbox di codice documentata; AgentOS isola via RBAC/JWT `[NV]` |
| 5. Supporto MCP | **sì** — `MCPClient` / `ToolCollection.from_mcp`: **stdio** e **Streamable HTTP** (+SSE), più server insieme, `structured_output` (spec 2025-06-18) [33] | **sì** — `MCPAdapter` (su FastMCP): URL HTTP, script locale via stdio, server in-process, `MCPConfig` multi-server; richiede `langchain[mcp]>=1.4.0`, **API in beta** [36] | **sì** — `MCPTools` stdio (default), Streamable HTTP, SSE (deprecato in v3.0.4); `MultiMCPTools`; AgentOS **è anche server MCP** [43][42] |
| 6. Skills | **no** — nessuna doc su SKILL.md `[NV: assenza di doc]` | **parz.** — pattern "Skills" nella doc multi-agent ("specialized prompts and knowledge loaded on-demand"), non il formato SKILL.md `[NV: compatibilità agentskills.io non verificata]` [37] | **sì** — "implements Anthropic's Agent Skills specification": SKILL.md + scripts/ + references/, loader `LocalSkills`, Team Skills [44] |
| 7. Memoria persistente | **parz.** — `agent.memory.steps` in RAM, modificabile via step callbacks; nessuna persistenza cross-run nativa (si copia `memory.steps` a mano) [34] | **sì** — **checkpointer** (InMemory/Sqlite/Postgres) per thread + **Store** con namespace per memoria cross-thread [38] | **sì** — user memories in DB (`agno_memories`), modalità automatica (`update_memory_on_run`) o agentica (`enable_agentic_memory`); sessioni e summary in DB [45] |
| 8. Observability | **sì** — **OpenTelemetry** via `SmolagentsInstrumentor` (OpenInference) → Phoenix/Langfuse; MLflow autolog; `agent.replay()` [34][31] | **sì** — **LangSmith** (`LANGSMITH_TRACING=true`), tracing automatico di `create_agent`; LangSmith ingerisce/esporta **OTLP** (`LANGSMITH_OTEL_ENABLED`) [37b][39b] | **sì** — tracing nativo **OpenTelemetry** salvato in DB Agno, `tracing=True`, visibile nel Control Plane/API; metriche, evals [46] |
| 9. Multi-agente | **sì** — `managed_agents=[...]` con `name`/`description`; manager `CodeAgent` chiama sub-agent come tool; non compatibile con sandbox snippet remote [32][47] | **sì** — 5 pattern documentati: subagents (as tools), handoffs, skills, router, custom workflow LangGraph [37] | **sì** — **Teams** (leader delega; modi coordinate/route/broadcast/tasks; team annidati) [48] |
| 10. Modello | **Multi-provider**: HF Inference providers, LiteLLM (OpenAI, Anthropic…), Transformers locale, Ollama [31] | **Multi-provider**: "all major model providers" via pacchetti (OpenAI, Anthropic, Google, Bedrock, HF, OpenRouter…), `init_chat_model` [38b] | **Multi-provider**: classe modello sceglie l'API (`openai:gpt-5.5`, Anthropic, …) [49] |
| 11. Maturità | Docs a **v1.26.0**; nessuna dichiarazione "production" [33] | **LangGraph v1** "stability-focused release", core API stabili; LangChain 1.4+; MCP adapter in beta [40][36] | **v3.x** (menzione "Agno v3.0.4"); nessuna dichiarazione GA formale trovata `[NV data release]` [43] |

## Fonti (accesso 4 set 2026)
1. https://code.claude.com/docs/en/overview
2. https://code.claude.com/docs/en/agent-sdk/overview
3. https://platform.claude.com/docs/en/managed-agents/overview
4. https://support.claude.com/en/articles/11725091 (connettori web vs desktop)
5. https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
6. https://support.claude.com/en/articles/13345190 (Get started with Cowork)
7. https://support.claude.com/en/articles/10949351 (Desktop Extensions / MCP locali)
8. https://code.claude.com/docs/en/agent-sdk/hosting
9. https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
10. https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
11. https://claude.com/blog/cowork-web-mobile
12. https://code.claude.com/docs/en/mcp
13. https://code.claude.com/docs/en/agent-sdk/mcp
14. https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
15. https://code.claude.com/docs/en/sandboxing
16. https://code.claude.com/docs/en/skills
17. https://code.claude.com/docs/en/claude-code-on-the-web
18. https://support.claude.com/en/articles/12512180-use-skills-in-claude
19. https://platform.claude.com/docs/en/managed-agents/reference
20. https://platform.claude.com/docs/en/managed-agents/skills
21. https://platform.claude.com/docs/en/managed-agents/tools ; https://platform.claude.com/docs/en/managed-agents/events-and-streaming
22. https://platform.claude.com/docs/en/managed-agents/mcp-connector
23. https://code.claude.com/docs/en/memory
24. https://code.claude.com/docs/en/sub-agents (memoria subagent)
25. https://platform.claude.com/docs/en/managed-agents/memory
26. https://code.claude.com/docs/en/monitoring-usage
27. https://code.claude.com/docs/en/sub-agents
28. https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration
29. https://code.claude.com/docs/en/third-party-integrations
30. https://platform.claude.com/docs/en/managed-agents/agent-setup
31. https://huggingface.co/docs/smolagents/index
32. https://huggingface.co/docs/smolagents/tutorials/secure_code_execution
33. https://huggingface.co/docs/smolagents/tutorials/tools
34. https://huggingface.co/docs/smolagents/tutorials/memory ; https://huggingface.co/docs/smolagents/tutorials/inspect_runs
35. https://docs.langchain.com/oss/python/langgraph/overview
36. https://docs.langchain.com/oss/python/langchain/mcp
37. https://docs.langchain.com/oss/python/langchain/multi-agent ; 37b. https://docs.langchain.com/oss/python/langchain/observability
38. https://docs.langchain.com/oss/python/langgraph/memory ; https://docs.langchain.com/oss/python/langgraph/durable-execution ; 38b. https://docs.langchain.com/oss/python/langchain/models
39. https://docs.langchain.com/langsmith/deployments ; 39b. https://docs.langchain.com/langsmith/trace-with-opentelemetry
40. https://docs.langchain.com/oss/python/releases/langgraph-v1
41. https://docs.agno.com/introduction
42. https://docs.agno.com/agent-os/introduction
43. https://docs.agno.com/tools/mcp/overview
44. https://docs.agno.com/skills/overview
45. https://docs.agno.com/memory/overview
46. https://docs.agno.com/agent-os/tracing/overview
47. https://huggingface.co/docs/smolagents/examples/multiagents
48. https://docs.agno.com/teams/overview
49. https://docs.agno.com/models/overview ; https://docs.agno.com/introduction/quickstart
