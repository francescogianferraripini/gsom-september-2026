# Slide realizzate — Incontro 28

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation-28/presentation.html`, figure usate (in `presentation-28/svg/`).
Per commentare, scrivi sotto la riga della slide.

---


## Copertina — «Agentic AI: dietro i tool, la conoscenza»  
`#cover`


## Separatore di sezione 1 — «La conoscenza»  
`#div-sec1`

- **01 · Ieri chi esegue, oggi che cosa sa** — `#slide-1` — *nessuna figura*
	- Testo: Rendere evidente, anche dall'esperienza consulenziale Quantyca, che il blocco principale all'adozione dell'AI, assieme a tutta una serie di dinamiche organizzative e legate alle persone, è sui Dati. Le aziende mediamente sono indietro sull'organizzazione dei loro Dati, e i tentativi di innesto dell'AI rendono ancora più evidenti questi Gap. Lo scopo della lezione è dare una visione di come dovrebbe essere strutturato l'insieme dei dati in modo da supportare al meglio gli agenti
	- → fatto: quarto punto «Quello che vediamo nei progetti» (il blocco è sui dati, le aziende indietro, il gap che l'AI rende evidente); lo scopo della lezione è passato nel blocco nero in fondo.
- **02 · La formula: oggi la KB** — `#slide-2` — `slide2-formula-kb.svg`
- **03 · Dalla piramide: dati, informazione, conoscenza, intelligenza** — `#slide-3` — `slide3-piramide-1.svg` · `slide3-piramide-2.svg` · `slide3-piramide-3.svg` · `slide3-piramide-4.svg`
	- Togliere Gestire i dati non basta: ogni gradino in più rende ciò che sotto c'è già riutilizzabile, da una persona e da un agente. Dalla presentazione Quantyca "Information Architecture", 2025.
	- → fatto: nota tolta. Il credito alla presentazione Quantyca resta solo nelle note del relatore (concordato).
- **04 · I quattro requisiti di una conoscenza utile** — `#slide-4` — *nessuna figura*
- **05 · Non è un problema dell'AI** — `#slide-5` — `assets/images/uploads/labyrinthus-aedificium.svg`
	- Immagine da https://it.wikipedia.org/wiki/Il_nome_della_rosa#/media/File:Labyrinthus_Aedificium.svg
	- → fatto: scaricata da Wikimedia Commons in `assets/images/uploads/labyrinthus-aedificium.svg` (CC BY-SA 4.0, attribuzione richiesta: il credito è nella didascalia). Nota: la scheda di Commons attribuisce il disegno a Eco/Bompiani — per l'aula va bene, se il deck circola fuori la licenza va riverificata.
- **06 · Know-what e know-how** — `#slide-6` — *nessuna figura*
- **07 · Lo spettro: dal dato strutturato al non strutturato** — `#slide-7` — `slide7-spettro.svg`

## Separatore di sezione 2 — «Il dato strutturato, 1/2: dove nasce»  
`#div-sec2` — `minimap-sec2.svg`

- **08 · Forma e fine: due assi** — `#slide-8` — `slide8-due-assi.svg`
	- Rendere "transazionale: registrare ciò che succede, una riga alla volta, in fretta e senza perdere nulla. Analitico: rispondere a domande su ciò che è successo, leggendo milioni di righe insieme." una lista puntata
	- -rendere "relazionale: tabelle con colonne fisse, lo schema deciso prima, le relazioni per chiave. Document: un record è un documento JSON, con i campi che servono a lui, annidati; lo schema lo decide chi scrive." una lista puntata
	- → fatto: i due punti sono ora liste puntate annidate (relazionale/document, transazionale/analitico), con il pallino piccolo grigio.
	- - **Dove vive l'AI**l'agente scrive poco e chiede molto: quasi tutto ciò che vediamo oggi sta nella colonna analitica. Il transazionale lo raggiunge solo attraverso i tool, e la slide 11 dice perché. <-- discutiamone
	- → fatto: il punto diventa «Da dove entra l'agente», in tre voci: analitico diretto in SQL; transazionale mediato da tool o API; document diretto se la struttura è semplice, eventi e log nel sandbox con bash.
	- Rivediamo anche la figura
	- → fatto: quattro porte d'ingresso, una per cella, e un'iconcina della forma del dato in ognuna (tabelle collegate, stella, blocchi JSON, listato). Tolta la freccia «la struttura deriva da qui»; aggiunta la freccia dagli eventi al data warehouse, «spesso riversati qui».
- **09 · Il modello relazionale: tabelle, tipi, chiavi** — `#slide-9` — `slide9-chiavi.svg`
	- Rendi la slide a 3 colonne. a sinistra il testo, in mezzo il sql, a dx lo schema disegnato, in modo più ordinato. riduci pure il font dello schema
	- → fatto: tre colonne 25/43/32. Lo schema è ridisegnato in verticale come due riquadri di colonne (ordini sopra, spedizioni sotto, PK e FK marcate) con lo stesso valore 4471 accanto alle due chiavi e la freccia che risale; font più piccolo, sia nel DDL sia nello schema.
	- lo schema non è ben ordinato
	- → fatto: rifatto. I due riquadri sono allineati e della stessa larghezza, le sigle PK e FK incolonnate, le righe chiave in evidenza in tutti e due; la freccia risale in un corridoio a sinistra invece di girare intorno, e i due `4471` che galleggiavano diventano un'etichetta sola sulla freccia: «lo stesso valore: 4471».
- **10 · Il SQL: quattro verbi** — `#slide-10` — `slide10-sql-1.svg` · `slide10-sql-2.svg` · `slide10-sql-3.svg` · `slide10-sql-4.svg`
- **11 · Il DB transazionale: per chi è fatto** — `#slide-11` — *nessuna figura*
	- Chiamarlo "Il DB transazionale".
	- Per l'esempio, va bene, è il classico caso in cui bisogna andare sul transazionale. Però lo contestualizzerei, dicendo che in questo caso non si va diretti sul db, ma viene wrappato in un tool o in una api.
	- → fatto: titolo «Il DB transazionale: per chi è fatto»; sotto l'esempio dell'ordine 4471 due frasi in più: è il caso classico in cui la risposta sta solo qui, ma l'agente non ci va diretto, quella lettura gliela fa un tool o un'API.
- **12 · La normalizzazione** — `#slide-12` — `slide12-normalizzazione.svg`
- **13 · La pagella del transazionale, e la cerniera** — `#slide-13` — `slide13-assi-cerniera.svg`
	- ricercabile in modo progressivo è X. 
	- → fatto: voto ✗, con il perché riscritto: trovare per chiave non è cercare in modo progressivo, si trova solo ciò di cui si sa già il numero.
	* nel visual, in ogni cella, disegnamo un modello relazionale transazionale, un datamart, una serie di blocchi con dentro del json piccolo, un json molto grande presentato come listato 
	- → fatto: i quattro disegni sono nelle celle, in grande; sono gli stessi oggetti delle iconcine della slide 8, stessa famiglia grafica. Via anche qui la freccia «la struttura deriva da qui».

## Separatore di sezione 3 — «Il dato strutturato, 2/2: dove si interroga»  
`#div-sec3` — `minimap-sec3.svg`

- **14 · Da Excel al data warehouse** — `#slide-14` — `slide14-excel-dwh.svg`
- **15 · Data warehouse: dove e come nasce** — `#slide-15` — `slide15-etl.svg`
- **16 · Fatti e dimensioni: lo star schema** — `#slide-16` — `slide16-star.svg`
	- Vorrei una transizione tra sql e star schema, così vedo bene grandi entrambi
	- → fatto: due tempi sullo stesso spazio (nuova classe `.swap`): prima il DDL a tutta colonna, al click lo star schema a tutta colonna al suo posto.
- **17 · La denormalizzazione, di proposito** — `#slide-17` — `slide17-dimensione.svg`
- **18 · La granularità e le metriche** — `#slide-18` — `slide18-grano.svg`
	- Non mi piace la frase "una riga è una spedizione" è una frase che va scritta prima di ogni altra. Cambia tutto: una riga per spedizione risponde a "quanti ritardi per corriere"; una riga per collo risponde anche a "quanti colli in ritardo"; una riga per ordine non risponde a nessuna delle due se un ordine ha due spedizioni
	- → fatto: «grano» diventa **granularità** in tutto il deck (titolo della slide compreso, e nelle figure 44, 45, 54, 56); il punto ha un attacco nuovo e un tono più piano: dice che cosa rappresenta una riga, e che va decisa prima perché stabilisce a quali domande la tabella può rispondere.
- **19 · Join e fanout** — `#slide-19` — `slide19-fanout.svg`
- **20 · Sicurezza: tabella, colonna, riga** — `#slide-20` — `slide20-sicurezza.svg`
- **21 · Il data management come trasformazione di forma** — `#slide-21` — `slide21-lineage.svg`
	- Non mi piace l'svg. parliamone
	- → fatto: rifatto. Le fonti sono un DB transazionale vero (tabelle normalizzate legate da molte join, con `data_prevista` evidenziata dentro `spedizioni`), il data warehouse è disegnato a stella, i consumatori sono disegnati: il report con le barre, la dashboard, l'agente con il suo `esegui_sql`. L'onda di impatto arriva a tutti e tre.
- **22 · L'antipattern: una pipeline per report** — `#slide-22` — `slide22-1.svg` · `slide22-2.svg` · `slide22-3.svg`
	- Assolutamente da rifare il visual
	- → fatto: tre tempi (`slide22-1/2/3.svg`), sincronizzati con i tre punti di testo. Arriva la richiesta e nasce la prima pipeline; se ne aggiungono altre, ognuna che riparte dal transazionale con il suo numero; alla fine la riunione con 3,8 · 3,2 · 4,1 e nessuno che sappia quale sia quello giusto.
- **23 · Pregi di Kimball** — `#slide-23` — `slide23-1.svg` · `slide23-2.svg` · `slide23-3.svg`
	- assolutamente da rifare il visual
	- → fatto: tre tempi (`slide23-1/2/3.svg`), con lo stile a stella delle altre slide. Le dimensioni conformi stanno in una fascia centrale: prima `fatto_spedizioni`, poi `fatto_reclami` che riusa le stesse, infine il fatto nuovo che si aggancia a ciò che c'è già.
- **24 · Limiti di Kimball, e cenni al data vault** — `#slide-24` — `slide24-star-vault-1.svg` · `slide24-star-vault-2.svg`
	- la transizione non fa sparire lo star schema sottostante
	- → fatto: due cause. La stella del tempo 1 restava sotto (ora è un fragment `fade-out`, sparisce al click); e dentro `slide24-star-vault-2.svg` c'era una copia della stella a opacity 0.06, tolta. Resta solo la stellina al 50% in basso a destra.
- **25 · Lo spettro dei tool: da Databricks a DuckDB** — `#slide-25` — *nessuna figura*
	- Questo è interessante: "- **Il motore piccolo entra nel sandbox**nel 27 (slide 20) il modello aveva scritto quattro righe di Python su `ordini_08.json`. Con DuckDB nel sandbox scrive SQL sullo stesso file. Stessa lingua del data warehouse, senza il data warehouse, sui dati che ha davanti." separa questo e "[user]Quanti ordini di agosto sono in ritardo, e per quale corriere?

[assistant]→ esporta_ordini(mese="2026-08")

[tool]salvato in ordini_08.json (12.480 righe): cerca o elabora con bash

[assistant]→ bash("duckdb -c \"SELECT corriere, COUNT(*) AS n  
  FROM 'ordini_08.json' WHERE consegna > prevista  
  GROUP BY corriere ORDER BY n DESC\"")

[tool]SpedFast 121 · Corriere Nord 44 · PostaPro 22" in una slide separata.

Togli Per l'agente conta la seconda riga: il data warehouse lo interroga attraverso un tool (sezione 6); un export, un file, un risultato salvato li interroga nel sandbox, con lo stesso SQL. Due porte, una lingua.

	- → fatto: la 25 resta la tabella dei tre motori (ingrandita, ora che è sola) con il solo punto «Stesso linguaggio, tre scale»; il resto è la nuova 25b. Nota tolta.
- **25b · Il motore piccolo entra nel sandbox** — `#slide-25b` — *nessuna figura* — **nuova**
	- Il punto del sandbox in due tempi (nel 27 era Python, con DuckDB è SQL) e, a destra, il riquadro-payload con la query DuckDB. Il riferimento incrociato della slide 46 ora punta alla 25b.

- **26 · La pagella dell'analitico** — `#slide-26` — `slide26-spettro-mini.svg`
	- Inverti questa slide con la successiva
	- → fatto: scambiate. La **26** è ora «La pagella dell'analitico» (senza cerniera) e la **27** è «Qualità, completezza, ownership, dipendenze», che chiude la sezione e porta il blocco nero della cerniera verso la sezione 4. Rinominata la figura in `slide26-spettro-mini.svg`; sistemati i riferimenti incrociati (la pagella rimanda alla governance della 27, la slide 54 ai quattro punti della 27).
- **27 · Qualità, completezza, ownership, dipendenze** — `#slide-27` — *nessuna figura* — porta la cerniera verso la sezione 4

## Separatore di sezione 4 — «Il dato non strutturato: da analisi a search»  
`#div-sec4` — `minimap-sec4.svg`

- **28 · Dove sta il non strutturato** — `#slide-28` — `slide28-dove-sta.svg`
- **29 · Il fatto dentro il testo** — `#slide-29` — `slide29-fatto-nel-testo.svg`
- **30 · Da problema di analisi a problema di search** — `#slide-30` — `slide30-analisi-search.svg`
- **31 · Cercare per parole: BM25** — `#slide-31` — *nessuna figura*
- **32 · Dal token al chunk: l'embedding di un passaggio** — `#slide-32` — `slide32-chunk-embedding.svg`
- **33 · Cercare per significato: l'indice vettoriale** — `#slide-33` — `slide33-indice-vettoriale.svg`
- **34 · Trovare è facile, ordinare è difficile** — `#slide-34` — `slide34-relevance.svg`
- **35 · Reranking: il secondo passaggio** — `#slide-35` — `slide35-reranking.svg`
- **36 · La pagella del non strutturato, e la cerniera** — `#slide-36` — `slide36-spettro-mini.svg`

## Separatore di sezione 5 — «In mezzo allo spettro: i grafi»  
`#div-sec5` — `minimap-sec5.svg`

- **37 · Le relazioni, scritte una per una** — `#slide-37` — `slide37-nodi-archi.svg`
- **38 · Il property graph** — `#slide-38` — `slide38-property-graph.svg`
- **39 · Cypher: un mini focus** — `#slide-39` — `slide39-cypher-1.svg` · `slide39-cypher-2.svg` · `slide39-cypher-3.svg` · `slide39-cypher-4.svg` · `slide39-cypher-5.svg`
- **40 · Perché non un database relazionale** — `#slide-40` — `slide40-traversal.svg`
- **41 · Il grafo è un modello, non un motore** — `#slide-41` — `slide41-modello-motore.svg`
- **42 · La pagella dei grafi, e la cerniera** — `#slide-42` — `slide42-spettro-mini.svg`

## Separatore di sezione 6 — «Pattern agentici di accesso al dato»  
`#div-sec6` — `minimap-sec6.svg`

- **43 · Tre pattern, un lettore** — `#slide-43` — `slide43-tre-pattern.svg`
- **44 · Text2SQL: com'è fatto** — `#slide-44` — `slide44-finestra-schema.svg` · `slide44-text2sql-sequence.svg`
- **45 · Text2SQL: i requisiti informativi** — `#slide-45` — `slide45-requisiti.svg`
- **46 · Text2SQL: dove sbaglia** — `#slide-46` — *nessuna figura*
- **47 · Naive RAG: un colpo solo** — `#slide-47` — `slide47-naive-rag.svg`
- **48 · Il modo agentico: iterare, e incrociare le fonti** — `#slide-48` — *nessuna figura*
- **49 · Il limite: sintetizzare oltre il chunk** — `#slide-49` — `slide49-oltre-il-chunk.svg`
- **50 · GraphRAG: il lexical graph** — `#slide-50` — `slide50-lexical-graph-1.svg` · `slide50-lexical-graph-2.svg` · `slide50-lexical-graph-3.svg` · `slide50-lexical-graph-4.svg` · `slide50-lexical-graph-5.svg` · `slide50-lexical-graph-6.svg`
- **51 · GraphRAG: community detection** — `#slide-51` — `slide51-community.svg`
- **52 · La pagella dei pattern, e la cerniera** — `#slide-52` — `slide52-spettro-mini.svg`

## Separatore di sezione 7 — «Superare i limiti, e il know-how»  
`#div-sec7` — `minimap-sec7.svg`

- **53 · Il gradino della semantica** — `#slide-53` — `slide3-piramide-4.svg`
- **54 · Managing data as a product** — `#slide-54` — `slide54-data-product.svg`
- **55 · Semantic modeling: l'ontologia** — `#slide-55` — `slide55-ontologia.svg`
- **56 · Nel dato strutturato: il semantic linking** — `#slide-56` — `slide56-semantic-linking.svg`
- **57 · Nel dato non strutturato: l'ontologia guida l'estrazione** — `#slide-57` — `slide57-estrazione-guidata.svg`
- **58 · L'approccio convergente** — `#slide-58` — `slide58-convergente.svg`
- **59 · Know-how: le skill** — `#slide-59` — *nessuna figura*
- **60 · La formula, completa** — `#slide-60` — `slide60-formula-completa.svg`
