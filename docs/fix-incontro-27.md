# Slide realizzate — Incontro 27

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation-27/presentation.html`, figure usate (in `presentation-27/svg/`).
Per commentare, scrivi sotto la riga della slide.

---


## Copertina — «Agentic AI: dentro l'harness»  
`#cover`


## Separatore di sezione 1 — «Tutto ciò che non è il modello»  
`#div-sec1` — `minimap-sec1.svg`

- **01 · Ieri il modello, oggi chi esegue** — `#slide-1` — *nessuna figura*
- **02 · Dalle aspettative ai requisiti** — `#slide-2` — *nessuna figura*
- **03 · La formula: oggi il sistema operativo** — `#slide-3` — `slide3-formula-harness.svg`
- **04 · La mappa dell'harness** — `#slide-4` — `slide4-mappa-harness.svg`
- **05 · I tre anelli: dove si infila il loop agentico** — `#slide-5` — `slide5-tre-anelli.svg`
- **06 · L'harness più semplice possibile** — `#slide-6` — `slide6-harness-minimo.svg`

## Separatore di sezione 2 — «Context Initialization»  
`#div-sec2` — `minimap-sec2.svg`

- **07 · La finestra al giro zero** — `#slide-7` — `slide7-finestra-strati-0.svg`
- **08 · Il system prompt: ruolo e regole** — `#slide-8` — `slide7-finestra-strati-1.svg`
- **09 · Le istruzioni di progetto: AGENTS.md, CLAUDE.md** — `#slide-9` — `slide7-finestra-strati-1b.svg`
- **10 · Com'è fatta una chiamata al modello** — `#slide-10` — `slide10-chiamata-api.svg`
- **11 · La dichiarazione dei tool: un contratto** — `#slide-11` — `slide7-finestra-strati-2.svg`
- **12 · Le skill, al giro zero: solo l'indice** — `#slide-12` — `slide7-finestra-strati-3.svg`
- **13 · La finestra piena, e l'utente non ha ancora scritto** — `#slide-13` — `slide7-finestra-strati-4.svg`
- **14 · Ora l'utente scrive** — `#slide-14` — `slide14-giro-uno.svg`

## Separatore di sezione 3 — «Environment management»  
`#div-sec3` — `minimap-sec3.svg`

- **15 · Il giro, visto dall'harness** — `#slide-15` — `slide15-sequence-giro.svg`
- **16 · Errori come feedback** — `#slide-16` — *nessuna figura*
- **17 · Chiamate parallele nello stesso giro** — `#slide-17` — `slide17-parallele.svg`
- **18 · Un tool non è un'API** — `#slide-18` — `slide18-tool-vs-api.svg`
- **19 · Il risultato è testo: la prompt injection** — `#slide-19` — `slide19-trifecta.svg`
- **20 · Bash: un tool come gli altri, che può fare tutto** — `#slide-20` — *nessuna figura*
- **21 · Perché non gira in produzione: il sandbox** — `#slide-21` — `slide21-sandbox.svg`
- **22 · Dal contratto al protocollo: MCP** — `#slide-22` — `slide22-mcp-specchio.svg`
- **23 · Le primitive di MCP: tools, resources, prompts** — `#slide-23` — `slide23-primitive-mcp.svg`
- **24 · Da stateful a stateless: un protocollo che cresce** — `#slide-24` — `slide24-mcp-timeline.svg`
- **25 · Non mappare 1:1 le API: il costo nascosto** — `#slide-25` — `slide25-peso-mcp.svg`
- **26 · Che cos'è una skill** — `#slide-26` — *nessuna figura*
- **27 · Come entra: dall'indice al corpo** — `#slide-27` — `slide27-skill-caricamento.svg`
- **28 · Quando la skill porta uno script** — `#slide-28` — `slide28-skill-script.svg`

## Separatore di sezione 4 — «Context management»  
`#div-sec4` — `minimap-sec4.svg`

- **29 · Costo fisso e costo a richiesta** — `#slide-29` — `slide29-costo-fisso-richiesta.svg`
- **30 · Quando conviene cosa** — `#slide-30` — *nessuna figura*
- **31 · La finestra a ogni giro: tre parti, tre velocità** — `#slide-31` — `slide31-finestra-giri.svg`
- **32 · Il prefisso non si tocca: prefix caching** — `#slide-32` — `slide32-prefix-caching.svg`
- **33 · Che cosa rompe la cache** — `#slide-33` — `slide33-cache-regole.svg`
- **34 · Non basta che ci stia: il context rot** — `#slide-34` — `slide36b-tool-context-rot.svg`
- **35 · Pruning e compaction: togliere e riassumere** — `#slide-35` — `slide35-pruning-compaction.svg`
- **36 · Offload su file: spostare, non perdere** — `#slide-36` — `slide36-offload.svg`
- **37 · La memoria: ciò che l'agente salva da solo** — `#slide-37` — `slide37-memoria-agente.svg`
- **38 · La memoria è un tool** — `#slide-38` — *nessuna figura*
- **39 · Le tre domande della memoria** — `#slide-39` — *nessuna figura*

## Separatore di sezione 5 — «Observability: osservare e migliorare»  
`#div-sec5` — `minimap-sec5.svg`

- **40 · Le leve di miglioramento** — `#slide-40` — `slide40-leve.svg`
- **41 · Tre livelli di successo, e la traiettoria** — `#slide-41` — `slide41-tre-livelli.svg`
- **42 · Il rischio del vibe eval** — `#slide-42` — `slide42-vibe-eval.svg`
- **43 · Il processo, in un colpo d'occhio** — `#slide-43` — `slide43-processo-eval.svg`
- **44 · Chi giudica: una persona sola, e le tracce a mano** — `#slide-44` — `slide43-mini-1.svg`, `slide44-traccia-annotata.svg`, `slide44-annotazione-ui.svg`
- **45 · Il dataset di test: cento casi, per dimensioni** — `#slide-45` — `slide43-mini-2.svg`, `slide45-dataset-dimensioni.svg`
- **46 · Clusterizzare i fallimenti, e risalire alla leva** — `#slide-46` — `slide43-mini-3.svg`, `slide46-cluster-leve.svg`
- **47 · Checker deterministici, poi il giudice** — `#slide-47` — `slide43-mini-45.svg`, `slide47-checker-giudice.svg`
- **48 · Gli errori nei tool deterministici e nei tool non deterministici** — `#slide-48` — `slide43-mini-3.svg`, `slide48-errori-tool.svg`
- **49 · In produzione: il ciclo che non finisce** — `#slide-49` — `slide43-mini-6.svg`, `slide49-ciclo-produzione.svg`
- **50 · Tre usi del logging** — `#slide-50` — `slide50-traccia-tre-usi.svg`

## Separatore di sezione 6 — «Orchestrazione: quando un agente non basta»  
`#div-sec6` — `minimap-sec6.svg`

- **51 · Quando un agente non basta: il criterio** — `#slide-51` — `slide51-workflow-vs-agente.svg`
- **52 · Pattern 1: il subagente come tool** — `#slide-52` — `slide52-subagente-tool.svg`
- **53 · Pattern 2: worker paralleli** — `#slide-53` — `slide53-worker-paralleli.svg`
- **54 · Pattern 3: evaluator / reviewer** — `#slide-54` — `slide54-reviewer.svg`
- **55 · Swarm e multi-agente conversazionale: un giudizio** — `#slide-55` — `slide55-swarm.svg`
- **56 · Deep research: com'è fatto davvero** — `#slide-56` — `slide56-deep-research.svg`
- **57 · Deep research: i tre pattern, colorati** — `#slide-57` — `slide56-deep-research.svg`, `slide57-deep-research-pattern.svg`

## Separatore di sezione 7 — «L'offerta di harness»  
`#div-sec7` — `minimap-sec7.svg`

- **58 · L'offerta Anthropic: stesso harness, superfici diverse** — `#slide-58` — `slide58-superfici-anthropic.svg`
- **59 · L'offerta Anthropic: che cosa espongono** — `#slide-59` — *nessuna figura*
- **60 · L'offerta open: tre filosofie** — `#slide-60` — `slide60-tre-filosofie.svg`
- **61 · L'offerta open: sulle stesse colonne** — `#slide-61` — *nessuna figura*
- **62 · La formula, riletta** — `#slide-62` — `slide62-formula-riletta.svg`
- **63 · Dietro i tool, la conoscenza** — `#slide-63` — *nessuna figura*
