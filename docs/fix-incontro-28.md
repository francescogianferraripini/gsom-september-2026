# Slide realizzate — Incontro 28

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation-28/presentation.html`, figure usate (in `presentation-28/svg/`).
Per commentare, scrivi sotto la riga della slide.

---


## Copertina — «Agentic AI: dietro i tool, la conoscenza»  
`#cover`


## Separatore di sezione 1 — «La conoscenza»  
`#div-sec1`

- **01 · Ieri chi esegue, oggi che cosa sa** — `#slide-1` — *nessuna figura*
- **02 · La formula: oggi la KB** — `#slide-2` — `slide2-formula-kb.svg`
- **03 · Dalla piramide: dati, informazione, conoscenza, intelligenza** — `#slide-3` — `slide3-piramide-1.svg` · `slide3-piramide-2.svg` · `slide3-piramide-3.svg` · `slide3-piramide-4.svg`
- **04 · I quattro requisiti di una conoscenza utile** — `#slide-4` — *nessuna figura*
- **05 · Non è un problema dell'AI** — `#slide-5` — *immagine da reperire (placeholder)*
- **06 · Know-what e know-how** — `#slide-6` — *nessuna figura*
- **07 · Lo spettro: dal dato strutturato al non strutturato** — `#slide-7` — `slide7-spettro.svg`

## Separatore di sezione 2 — «Il dato strutturato, 1/2: dove nasce»  
`#div-sec2` — `minimap-sec2.svg`

- **08 · Forma e fine: due assi** — `#slide-8` — `slide8-due-assi.svg`
- **09 · Il modello relazionale: tabelle, tipi, chiavi** — `#slide-9` — `slide9-chiavi.svg`
- **10 · Il SQL: quattro verbi** — `#slide-10` — `slide10-sql-1.svg` · `slide10-sql-2.svg` · `slide10-sql-3.svg` · `slide10-sql-4.svg`
- **11 · Il transazionale: per chi è fatto** — `#slide-11` — *nessuna figura*
- **12 · La normalizzazione** — `#slide-12` — `slide12-normalizzazione.svg`
- **13 · La pagella del transazionale, e la cerniera** — `#slide-13` — `slide13-assi-cerniera.svg`

## Separatore di sezione 3 — «Il dato strutturato, 2/2: dove si interroga»  
`#div-sec3` — `minimap-sec3.svg`

- **14 · Da Excel al data warehouse** — `#slide-14` — `slide14-excel-dwh.svg`
- **15 · Data warehouse: dove e come nasce** — `#slide-15` — `slide15-etl.svg`
- **16 · Fatti e dimensioni: lo star schema** — `#slide-16` — `slide16-star.svg`
- **17 · La denormalizzazione, di proposito** — `#slide-17` — `slide17-dimensione.svg`
- **18 · Il grano e le metriche** — `#slide-18` — `slide18-grano.svg`
- **19 · Join e fanout** — `#slide-19` — `slide19-fanout.svg`
- **20 · Sicurezza: tabella, colonna, riga** — `#slide-20` — `slide20-sicurezza.svg`
- **21 · Il data management come trasformazione di forma** — `#slide-21` — `slide21-lineage.svg`
- **22 · L'antipattern: una pipeline per report** — `#slide-22` — `slide22-pipeline-per-report.svg`
- **23 · Pregi di Kimball** — `#slide-23` — `slide23-conformi.svg`
- **24 · Limiti di Kimball, e cenni al data vault** — `#slide-24` — `slide24-star-vault-1.svg` · `slide24-star-vault-2.svg`
- **25 · Lo spettro dei tool: da Databricks a DuckDB** — `#slide-25` — *nessuna figura*
- **26 · Qualità, completezza, ownership, dipendenze** — `#slide-26` — *nessuna figura*
- **27 · La pagella dell'analitico, e la cerniera** — `#slide-27` — `slide27-spettro-mini.svg`

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
