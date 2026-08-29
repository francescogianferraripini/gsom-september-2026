# PC AI: 27 — Agentic AI: agenti e pattern di orchestrazione, tool call, protocollo MCP

# Apertura: tutto ciò che non è il modello
 
- Ribaltamento dell'incontro 1: ieri il modello (cosa sa, come genera, come impara a *volere* un tool). Oggi chi esegue quella volontà.
- Ripresa breve della parte funzionale (aspettative da un agente: autonomia, affidabilità, verificabilità) riletta come **requisiti dell'harness**: sono le ragioni per cui esistono loop, sandbox, logging.
- La formula Agent = LLM + Harness + Context + Tools + KB + Skills, con LLM sbiadito e Harness in evidenza.
- Harness = Context Initialization + Tool Calling Execution + Execution Sandbox + Skills access + Context Management + Memory + Logging + Loop. L'ordine dei capitoli segue l'ordine in cui i problemi si presentano.
# Loop e system prompt (Context Initialization)
 
- Dal 1° loop (fino al token di stop) al 2° loop (fino al task completato). Continuità con l'incontro 1. Il 3° loop è quello conversazionale
- Il loop nudo: `while not done: chiama il modello, leggi, decidi`.
- Il system prompt come contenuto della finestra al giro zero: ruolo, regole, definizioni dei tool.
- Nota tecnica: le definizioni dei tool si passano come parametro API separato, il provider le renderizza nel formato su cui il modello è stato addestrato (aggancio GRPO). Concettualmente system prompt, tecnicamente un campo a parte — è il punto in cui MCP si innesta.
- Immagine: la finestra al giro zero, a strati.
# Tool Calling Execution
 
- Lato modello (incontro 1): la volontà di chiamare. Lato harness (oggi): parsing, dispatch, esecuzione, iniezione del risultato nel contesto, giro successivo.
- Lo schema del tool come contratto (nome, descrizione, parametri): è documentazione per il modello.
- Errori come feedback: il risultato di un tool fallito rientra nel loop ed è informazione, non eccezione.
- Chiamate parallele nello stesso giro.
- Immagine: sequence diagram modello ↔ harness ↔ tool su due giri.
# Execution Sandbox
 
- Bash / code execution come tool universale: meccanicamente un tool come gli altri, ma quello che rende possibili tutti gli altri.
- Perché non gira sulla macchina di produzione: isolamento, filesystem effimero, rete controllata.
- Anticipazione: da qui in poi "tool" non vuol dire solo "funzione con schema JSON".
# MCP
 
- Il problema: ogni integrazione riscritta per ogni harness. MCP come standardizzazione del contratto tool appena visto.
- Primitive: tools, resources, prompts. Client / server. Chi espone cosa.
- Perché esiste e cosa è diventato sul mercato (offerta di server, registry).
- Il costo nascosto: N server = N definizioni nel prefisso a ogni giro, lette o no. Ponte al capitolo successivo.
- Immagine: harness al centro, server MCP intorno, con il "peso" in token di ogni server nella finestra.
# Skills
 
- Skill = istruzioni + eventuali script, caricate a richiesta. Indice (nome + descrizione) sempre presente, corpo solo quando serve: **progressive disclosure**.
- Confronto quantitativo con MCP: costo fisso nel prefisso vs costo a richiesta.
- Skill che espongono CLI o script: l'agente lancia un pezzo di codice nel sandbox che fa dieci chiamate e riporta il risultato finale, invece di dieci giri con dieci risultati interi nel contesto. Meno giri, meno contesto, risultati intermedi che non entrano mai nella finestra.
- Skill come luogo in cui l'organizzazione mette il proprio know-how a disposizione dell'agente (anticipazione dell'incontro 3, sezione Know how).
- Immagine: stesso task fatto con 10 tool call MCP vs 1 skill + script, confronto giri/token.
# Context Management
 
Confine con Memory: qui tutto ciò che succede *dentro* una sessione.
 
- Anatomia della finestra a ogni giro: prefisso stabile (system prompt + tool), storia che cresce, risultati dei tool come parte che cresce più in fretta. Immagine: la finestra a strati al giro 1, 5, 20.
- Perché è un problema, parte 1 — costo: ritorno alla complessità quadratica e alla KV cache. Prefix caching: perché non si tocca mai il prefisso, e perché i tool MCP inutilizzati costano comunque.
- Perché è un problema, parte 2 — degrado: il modello peggiora con contesto lungo anche quando ci sta. Grafico (già disponibile).
- Tecniche: pruning dei risultati vecchi, compaction / riassunto, offload su file.
- L'offload su file è il momento in cui il contesto diventa memoria.
# Memory
 
Confine: tutto ciò che sopravvive *tra* sessioni.
 
- Tesi deflazionistica: nella pratica attuale la memoria degli agenti è quasi sempre file (note, istruzioni di progetto, scratchpad), non database vettoriali.
- Le tre domande: cosa vale la pena ricordare, chi lo scrive, chi lo legge.
- Ponte all'incontro 3: memoria di un agente e KB di un'organizzazione sono lo stesso problema a scale diverse. I requisiti (progressiva, non ridondante, veritiera, compounding) valgono per entrambe.
# Come monitoro e miglioro la performance dell'agente?

* Le leve di miglioramento, in ordine cresente di complessità: Prompt, Knowledge Base, Tool, Harness, Modello.
* Un tema non è solo quello del miglioramento della performance dell'agente, ma anche quello di garantirsi libertà nel momento in cui si cambiano i LLM sottostanti
* Da successo del task single shot, al successo end2end nelle chiamate dei tool all'interno del singolo step conversazionale, al successo del processo complessivo.
- La traiettoria è l'artefatto primario dell'agente, non la risposta.
- Rischio del vibe eval: non solo non è stabile, ma tipicamente un 
- Step di Hamel:
	- Individuare una persona sola che, nel caso 
	- Guardare fisicamente, a mano, le tracce di conversazione, se ci sono già
	- Crearsi dei dataset di test, anche in modo sintetico e dimensionale (in contesti semplici, ad esempio NON in medicina e legge), e analizzare l'output dell'agente. Idealmente la definizione di questo dataset dovrebbe essere contestuale all'attività di design dell'agente, di circa 100 
	- Clusterizzare le modalità di fallimento. Già al primo giro emergono dei cluster evidenti di failure, continuare a clusterizzare finchè non finiscono le categorie. Molto spesso categorie molto frequenti sono anche quelle più facili da fixare specificando meglio le cose a livello di prompt
	- Creare il prima possibile dei checker deterministici di successo (anche con l'aiuto dell'AI)
	- Dopo lo score deterministico, lavorare sugli LLM as a Judge, costruendo il giudice e validandolo statisticamente, sfruttando l'esperto di dominio umano.
	- Un agente ha tipicamente accesso a dei tool. Alcuni di questi sono deterministici (e.g. API di sw applicativo) ed il fallimento è tipicamente legato a chiamate errate o non comprensione del tool. Altri tool sono a loro volta AI o simile: esempio classico la RAG, in cui il problema si scompone in qualità del retrieval/ranking e in qualità della sintesi successiva.
	- Questi step vanno operazionalizzati, man mano che l'agente è in produzione i dataset aumentano di tracce, che vanno analizzzate a mano (e.g. 100 tracce al mese) incrementando il processo precedente.
	- Chiaramente la catena di valutazione si fa rigirare se si tocca qualcosa (modifica ai prompt, cambio di modello e di tool, etc.) per individuare regressioni o miglioramenti se si tratta di fix
- Tre usi del logging: debug (perché ha fatto quella chiamata?), eval (si confrontano traiettorie, non output), training set per RL privato (chiusura del cerchio con l'incontro 1: le traiettorie di oggi sono i dati di domani).
- Immagine: una traiettoria reale annotata giro per giro.
# Orchestrazione: quando un agente non basta
 
Criterio: si aggiunge un secondo agente quando il contesto del primo non basta più, non prima. Ogni pattern è motivato da un problema di harness già visto.
 
- Workflow vs agente: un `if` nell'harness (chaining, routing) non è un secondo agente. Distinzione esplicita.
- Pattern 1 — **Subagente come tool** (orchestrator-workers). Motivazione: isolamento del contesto. Venti giri di ricerca nel figlio, un paragrafo nel padre. Stesso contratto del tool calling: un agente è un tool per un altro agente.
- Pattern 2 — **Worker paralleli**. Motivazione: tempo, task decomponibili. Caveat: solo se indipendenti; il merge è il punto fragile.
- Pattern 3 — **Evaluator / reviewer**. Motivazione: un contesto pulito giudica meglio di quello che ha lavorato. Aggancio a logging: il reviewer legge la traiettoria.
- Cenno e giudizio sulle architetture swarm / conversazionali multi-agente: instabili, costose, quasi sempre sostituibili dal pattern 1.
- Esempio finale — **Deep research** (Google / Gemini): agente di raffinamento query → agenti paralleli di ricerca → agente di controllo che assembla e rilancia ricerche → agente di scrittura del report. Diagramma unico, poi colorato con i tre pattern. Gli "agenti" sono ruoli dell'harness: stesso modello, contesti e tool diversi.

# Offering di Harness

* Un esempio: offering di Anthropic:
	* Claude.ai
	* Claude Desktop
	* Claude Cowork
	* Claude Code
	* Agent SDK
* Offering Open:
	* Smolagents
	* Langchain/Langgraph
	* Agno

# Chiusura
 
- La formula riletta con tutto ciò che si è visto.
- Cliffhanger per l'incontro 3: abbiamo dato all'agente tool, skill, memoria — ma cosa c'è dietro i tool? La conoscenza, e come va organizzata perché un agente la possa usare.
