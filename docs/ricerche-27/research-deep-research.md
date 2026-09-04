# Gemini Deep Research: architettura da fonti primarie (verifica 2026-09-04)

## 0. Premessa importante
Google NON descrive pubblicamente Deep Research come sistema multi-agente con ruoli separati. Le fonti primarie
(blog, docs API, intervista al team DeepMind) lo descrivono come **un unico modello post-addestrato ad hoc**
(RL multi-step per la ricerca) che esegue un loop agentico "Plan → Search → Read → Iterate → Output" con tool
(Google Search, URL context, code execution, File Search, MCP). Il parallelismo è a livello di *tool call*
(più ricerche lanciate insieme), non di *agenti* distinti. La survey arXiv 2506.18096 lo classifica esplicitamente
come "single-agent architecture". Le "fasi" sotto sono quindi fasi del loop, non ruoli/modelli diversi.

## 1. Pipeline a fasi (fase → cosa fa → input/output)
1. **Pianificazione (research plan / "editable chain of thought")**
   - Cosa fa: il modello scompone la query in un piano multi-punto ("piani di ricerca personalizzati divisi in più
     punti"); nell'app Gemini l'utente lo rivede/modifica/approva prima dell'esecuzione ("a multi-step research plan
     for you to either revise or approve"). Nell'API: opzione per restituire "a proposed research plan instead of
     executing immediately" con raffinamento multi-turno. Scelta deliberata: piano invece di domande di chiarimento.
   - Input: prompt utente (+ file caricati/Drive/Gmail se consentito). Output: piano approvato.
2. **Ricerca breadth-first in parallelo**
   - Cosa fa: il modello "figures out which of the sub steps that it can start exploring in parallel"; esplora tutti
     gli aspetti del piano ("breadth first idea") con due tool: search e lettura pagina ("double click").
   - Input: piano. Output: risultati/pagine tenuti *interamente in contesto* (long context 1M, no RAG:
     "hold all the research material across dances"; nel loop la ricerca precedente informa la successiva).
3. **Iterazione / approfondimento depth-first (gap detection e rilancio ricerche)**
   - Cosa fa: "formulates queries, reads results, identifies knowledge gaps, and searches again"; approfondisce dove
     trova incoerenze o informazioni parziali; "reacts to real-time information", "continuously refines its analysis".
   - Input: contesto accumulato. Output: corpus di fonti "sufficiente" (criterio di stop non documentato).
4. **Analisi e scrittura del report ("analysis mode")**
   - Cosa fa: risolve incoerenze tra fonti, genera outline, bozza, poi "the model tries to revise that by self
     critiquing itself" e finalizza; citazioni granulari; export in Google Docs / Audio Overview.
   - Input: contesto completo. Output: report citato (nell'API anche immagini generate; JSON schema promesso).
Orchestrazione: piattaforma asincrona custom ("job scheduling, state management, failure recovery, and progress
tracking") perché il job dura minuti e l'utente può chiudere il browser; nell'API è obbligatorio background=true
(+ store=true), polling o streaming con "thought summaries"; riconnessione dello stream dopo 600 s.

## 2. Dettagli quantitativi pubblici
- Durata: app "about five minutes" (esisteva un "hardcore mode" ~15 min, scartato); API: "most tasks within 20 min",
  max 60 min. Stima ZenML/Latent Space: 5-10 min.
- Ampiezza: "centinaia di siti web" (app). API (docs, 04/2026): Deep Research ≈ 80 query di ricerca, ~250k token
  input (50-70% cached), ~60k output, ~$1-3/task; Deep Research Max ≈ 160 query, ~900k input, ~80k output, ~$3-7.
- Modelli: Gemini 1.5 Pro "special edition" post-addestrata (12/2024) → 2.0 Flash Thinking (02/2025) → 2.5 Pro →
  Gemini 3 Pro con "multi-step reinforcement learning for search" (12/2025). Agent id API: deep-research-preview-04-2026
  e deep-research-max-preview-04-2026. Tool di default: Google Search, URL Context, Code Execution; opzionali File
  Search e server MCP remoti; niente function calling custom.
- Benchmark (12/2025, Gemini 3 Pro DR): HLE 46,4 %, DeepSearchQA 66,1 %, BrowseComp 59,2 %; "significant performance
  gains when allowing the agent to perform more searches and reasoning steps" (scaling a inference time).
- Contesto: 1M token; il team dichiara di preferire il long context al RAG (dot product debole con query multi-attributo).

## 3. Confronto con OpenAI e Anthropic (solo dove la fonte primaria descrive l'architettura)
| | Gemini Deep Research | OpenAI deep research | Anthropic Research (Claude) |
|---|---|---|---|
| Pattern | singolo agente, loop Plan/Search/Read/Iterate, tool call paralleli | singolo modello (o3 fine-tuned) con RL end-to-end su browsing+python | orchestrator-workers: LeadResearcher + 3-10+ subagenti paralleli + CitationAgent |
| Fase iniziale | piano editabile approvato dall'utente | domande di chiarimento prima di partire | il lead pianifica e salva il piano in Memory |
| Modelli/ruoli | stesso modello, stesso contesto (long context) | stesso modello | Opus 4 lead, Sonnet 4 subagenti, ciascuno con contesto proprio; +90,2 % vs Opus singolo |
| Parallelismo | ricerche parallele dentro un solo contesto | trajectory sequenziale con backtracking | subagenti concorrenti + tool call parallele: fino a -90 % tempo |
| Verifica/citazioni | self-critique nella stesura; citazioni granulari | citazioni a frasi specifiche | agente dedicato che aggiunge citazioni al report finale |
| Costo/durata | ~5 min app; 80-160 ricerche (API) | 5-30 min | ~15x token di una chat; 1 agente/3-10 call semplice, 2-4 subagenti/10-15 call medio |
Differenza chiave: Anthropic separa esplicitamente i ruoli (pianificatore, ricercatori paralleli, citatore) in
istanze distinte con contesti isolati; Google e OpenAI ottengono pianificazione/ricerca/sintesi come fasi di un
unico modello addestrato con RL, con parallelismo (Google) o backtracking (OpenAI) interni al singolo loop.

## 4. Fonti (URL, data)
- Google blog, "Try Deep Research and our new experimental model in Gemini", 2024-12-11:
  https://blog.google/products/gemini/google-gemini-deep-research/
- Google blog, "Build with Gemini Deep Research" (Interactions API, Gemini 3 Pro), 2025-12-11:
  https://blog.google/technology/developers/deep-research-agent-gemini-api/
- Google AI for Developers, docs "Gemini Deep Research agent" (versione 04/2026): https://ai.google.dev/gemini-api/docs/deep-research
- gemini.google, overview Deep Research (planning/searching/reasoning/reporting): https://gemini.google/overview/deep-research/
- Latent Space, intervista ad Aarush Selvan (PM) e Mukund Sridhar (Tech Lead), Google DeepMind, 2025-02-18:
  https://www.latent.space/p/gdr (fonte primaria "orale"; riassunto: zenml.io/llmops-database/building-gemini-deep-research-...)
- Anthropic Engineering, "How we built our multi-agent research system", 2025-06-13:
  https://www.anthropic.com/engineering/built-multi-agent-research-system
- OpenAI, "Introducing deep research", 2025-02-02: https://openai.com/index/introducing-deep-research/ (pagina 403 al fetch:
  citazioni riprese da snippet di ricerca; system card cdn.openai.com/deep-research-system-card.pdf non parsata)
- Survey arXiv 2506.18096 "Deep Research Agents: A Systematic Examination and Roadmap" (classifica Gemini DR single-agent).

## 5. Cosa NON è documentato pubblicamente (Google)
- Nessun paper/system card: non esiste descrizione di ruoli/agenti separati (planner, worker, verifier, writer); il
  numero di ricerche parallele per step, il criterio di stop, la profondità massima di iterazione.
- Come funziona il self-critique (quanti passaggi, stesso modello?), se esista un passo di verifica citazioni separato.
- Dettagli del post-training/RL (dati, reward), dimensione del contesto effettivamente usato, uso di RAG oltre il limite.
- Differenze interne tra "Deep Research" e "Deep Research Max" oltre a budget di ricerche/token.
- Se l'app consumer e l'agente API condividano esattamente la stessa pipeline; le stime "80/160 ricerche" sono
  medie di costo dichiarate nella doc, non limiti architetturali.
