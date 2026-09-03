# Slide realizzate — Incontro 26

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation/presentation.html`, figure usate.
Per commentare, scrivi sotto la riga della slide.

---


## Copertina — «Agentic AI: da LLM ad agenti»  
`#cover`


## Separatore di sezione — «Cosa è un agente?»  
`#div-sec1`

- **01 · Cosa è un agente? Le aspettative** — `#slide-1` — *nessuna figura*
	- "Ci aspettiamo che porti a termine un task — non che risponda a una domanda" deve essere un blocco evidenziato e centrato nero, come in altre slide
- **02 · Lo spazio delle soluzioni** — `#slide-2` — `slide2-spazio-soluzioni.svg`
	- *Figura*. Ragionamento diventa Ragionamento matematico e ha lo stesso ampiezza di contesto di coding e gli stessi colori. Rimpiazza Conversazione Stateful con Ragionamento strategico aziendale
	- *Testo* 
		- Rimpiazza "Dove gli agenti funzionano già, e dove serve rinforzo: due assi — quanto contesto richiede il task, quanto è verificabile il risultato." con "La *Jagged frontier* , non tutti i task sono uguali"
		- Rimpiazza "Tutto ciò che il corso costruisce — tool, knowledge base, skills, orchestrazione — è un modo di rinforzare i task dove il modello da solo è fragile. E la frontiera si sposta di mese in mese." con "La frontiera si sposta costantemente. La verificabilità deterministica del risultato è l'elemento determinante per poter addestrare gli LLM ad abilitare correttamente gli agenti"
- **03 · Un agente è un sistema composto** — `#slide-3` — `slide3-formula-agent.svg`
	- Rimpiazza "Il resto è il software installato — ed è il software che distingue un agente da un altro." con "Il resto è come se fosse il software che, a parità di infrastruttura, organizza il lavoro a seconda dell'obiettivo"
- **04 · Il ruolo dell'harness** — `#slide-4` — `slide4-ruolo-harness.svg`
	- *Figura* Questi i blocchi intorno all'llm, che raggrupperei in 3 categorie distinte da colori
		- Context management. sottoblocchi
			- Context Initialization
			- Context Optimization (compaction, pruning, etc.)
			- Memory management
			- Skill management
		- Agentic loop management
		- Environment management
			- Tool Calling execution and response management
			- Execution Sandbox
			- Skill execution management
		* Togliere "Harness l'esoscheletro simbolico"

## Separatore di sezione — «L'LLM: cos'è e come genera»  
`#div-sec2`

- **05 · Che cos'è un modello linguistico** — `#slide-5` — `slide5-modello-linguistico.svg`
	- *Testo* rimuovi : non è una metafora, è un teorema. Lo ritroveremo.
- **06 · La generazione: un token alla volta** — `#slide-6` — `slide6-generazione-autoregressiva.svg`
	  *Testo.* aggiungi dopo "successivo." "Da questo punto di vista il modello è stateless e ragiona solo in termini di parola successiva"
- **07 · Il golfista** — `#slide-7` — `slide7-golfista.svg`
	- *Figura* I colpi del golfista devono riflettere i colpi tipici. Primo colpo lungo, poi progressivamente più corto
- **08 · Il 1° loop: la generazione** — `#slide-8` — *nessuna figura*
	- RIMUOVERE LA SLIDE
- **09 · Il 2° loop: la conversazione** — `#slide-9` — `slide9-secondo-loop.svg`
	- Questa deve diventare una slide di comparazione. A sx ricopia la generazione come da `#slide-6` della frase sul gatto, a dx fai vedere un giro di conversazione come negli svg recuperati da https://francescogianferraripini.github.io/gsom-april-2026/lezione-mba/presentation.html#/slide-meccanica-conversazione, https://francescogianferraripini.github.io/gsom-april-2026/lezione-mba/presentation.html#/slide-meccanica-conversazione/0,https://francescogianferraripini.github.io/gsom-april-2026/lezione-mba/presentation.html#/slide-meccanica-conversazione/1

## Separatore di sezione — «Perché funziona»  
`#div-sec3`

- **10 · La base di tutto: a ogni parola il suo vettore** — `#slide-10` — `slide10-parola-vettore.svg`
- **10b · Che cos'è un vettore** — `#slide-10b` — `slide10b-che-cos-e-un-vettore.svg`
- **11 · Vettori e prodotto scalare** — `#slide-11` — `slide11-vettori-prodotto-scalare.svg`
- **11b · La somma: spostarsi nello spazio** — `#slide-11b` — `slide11b-somma-vettori.svg`
- **12 · La scala del calcolo: vettori e matrici** — `#slide-12` — `slide12-scala-del-calcolo.svg`
- **13 · Embeddings: lo spazio delle idee** — `#slide-13` — `slide13-embeddings.svg`
- **14 · La tokenizzazione** — `#slide-14` — `slide14-tokenizzazione.svg`
- **15 · L'architettura, in un colpo d'occhio** — `#slide-15` — `slide15a-scatola-nera.svg`, `slide15b-torre.svg`, `slide15c-torre-aperta.svg`
- **16 · Fanout: il matching concettuale** — `#slide-16` — `minimap-fc.svg`, `slide16-fanout.svg`
- **17 · Compressione: la sovrapposizione** — `#slide-17` — `minimap-somma.svg`, `slide17-compressione.svg`
- **18 · Attention: domande e chiavi** — `#slide-18` — `minimap-attn.svg`, `slide18-griglia-qk.svg`
- **19 · Softmax: il budget di ascolto** — `#slide-19` — `minimap-attn.svg`, `slide19-griglia-softmax.svg`
- **20 · V: la consegna** — `#slide-20` — `minimap-attn.svg`, `slide20-griglia-v.svg`
- **20b · Lo stesso token, due contesti** — `#slide-20b` — `minimap-attn.svg`, `slide20b-contesto-frase1.svg`, `slide20b-contesto-frase2.svg`
- **21 · Positional encoding: l'ordine conta** — `#slide-21` — `minimap-pos.svg`, `slide21-positional-encoding.svg`
- **22 · Reverse embedding: tornare ai token** — `#slide-22` — `minimap-testa.svg`, `slide22-reverse-embedding.svg`
- **23 · Il contesto ha un costo** — `#slide-23` — `minimap-corsie.svg`, `slide23-costo-contesto.svg`
- **24 · La conoscenza è nei pesi** — `#slide-24` — `slide24-conoscenza-nei-pesi.svg`
- **25 · L'LLM come compressore lossy** — `#slide-25` — `slide25-compressore-lossy.svg`
- **26 · Conseguenze della compressione** — `#slide-26` — *nessuna figura*
- **27 · MoE: non tutti i pesi lavorano sempre** — `#slide-27` — `minimap-fc.svg`, `slide27-moe.svg`

## Separatore di sezione — «Come viene addestrato»  
`#div-sec4`

- **28 · Le tre fasi** — `#slide-28` — `slide28-tre-fasi.svg`
- **29 · Pretraining: indovinare il prossimo token** — `#slide-29` — `slide29-pretraining.svg`, `slide29-scala-dati.svg`
- **30 · Gradient descent: sbaglia, misura, correggi** — `#slide-30` — `slide30-gradient-descent.svg`
- **31 · RLHF: arriva la mira** — `#slide-31` — `slide31-rlhf.svg`
- **32 · RL agentico: traiettorie** — `#slide-32` — `slide32-rl-agentico.svg`
- **33 · Nasce il 3° loop** — `#slide-33` — `slide33-terzo-loop.svg`
- **34 · Il modello è stateless: il contesto è tutto** — `#slide-34` — `slide34-stateless.svg`
- **35 · Il modello è figlio dei suoi training set** — `#slide-35` — *nessuna figura*

## Separatore di sezione — «Il modello nel mondo»  
`#div-sec5`

- **36 · Context rot** — `#slide-36` — `slide36-context-rot.svg`
- **37 · Multimodality** — `#slide-37` — `slide37-multimodality.svg`
- **38 · Reasoning** — `#slide-38` — `slide38-reasoning.svg`
- **39 · I costi: training, inferenza, distillazione** — `#slide-39` — `slide39-costi.svg`
- **40 · Il prezzo per token** — `#slide-40` — `slide40-prezzo-per-token.svg`
- **41 · Il valore delle traiettorie** — `#slide-41` — *nessuna figura*
- **42 · Closed, open weights, open source** — `#slide-42` — *nessuna figura*
- **43 · Quando closed, quando open** — `#slide-43` — *nessuna figura*
- **44 · Fine-tuning: riprendere la discesa** — `#slide-44` — `slide44-fine-tuning.svg`
- **45 · LoRA: la correzione a basso rango** — `#slide-45` — `slide45-lora.svg`
- **46 · La fotografia del mercato** — `#slide-46` — *nessuna figura*
- **47 · La formula, riletta** — `#slide-47` — *nessuna figura*

## Chiusura — «Il modello sa volere. Non sa eseguire.»  
`#closing`

