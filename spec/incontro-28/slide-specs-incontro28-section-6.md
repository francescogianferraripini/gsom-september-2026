# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 6 — Pattern agentici di accesso al dato**
**Obiettivo di apprendimento**: il partecipante sa come un agente entra in ciascuna forma dello spettro (Text2SQL sulle tabelle, search sui documenti, traversal sui grafi) e che ogni pattern è un tool nel senso del 27; sa che cosa deve stare nella finestra perché il Text2SQL esca giusto e in quali quattro modi sbaglia; distingue la naive RAG (un colpo, una fonte) dal modo agentico (iterare, incrociare le fonti); sa quale classe di domande nessuna search risolve e che cosa aggiunge GraphRAG (lexical graph, entità estratte, comunità e riassunti); e sa che i pattern ereditano la pagella della forma che leggono.
**Messaggio chiave (takeaway)**: L'agente non aggiunge conoscenza: aggiunge un lettore che sbaglia con sicurezza dove la conoscenza è tenuta male.
**Budget**: ~24 min, 10 slide + separatore. Ripartizione: i pattern come tool 1, Text2SQL 3, naive RAG e modo agentico 2, il limite e GraphRAG 3, pagella 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec6.html` | Separatore — Sezione 6: Pattern agentici di accesso al dato |
| `slides/slide43-tre-pattern.html` | Slide 43 — Tre pattern, un lettore |
| `slides/slide44-text2sql.html` | Slide 44 — Text2SQL: com'è fatto |
| `slides/slide45-requisiti-text2sql.html` | Slide 45 — Text2SQL: i requisiti informativi |
| `slides/slide46-text2sql-errori.html` | Slide 46 — Text2SQL: dove sbaglia |
| `slides/slide47-naive-rag.html` | Slide 47 — Naive RAG: un colpo solo |
| `slides/slide48-modo-agentico.html` | Slide 48 — Il modo agentico: iterare, e incrociare le fonti |
| `slides/slide49-oltre-il-chunk.html` | Slide 49 — Il limite: sintetizzare oltre il chunk |
| `slides/slide50-lexical-graph.html` | Slide 50 — GraphRAG: il lexical graph |
| `slides/slide51-community.html` | Slide 51 — GraphRAG: community detection |
| `slides/slide52-pagella-pattern.html` | Slide 52 — La pagella dei pattern, e la cerniera |

---

> **Filo della sezione.** La fascia dei pattern dello spettro si accende: ogni pattern è un tool (43). Text2SQL in tre slide: com'è fatto, con lo schema nel system prompt e il modello che scrive il SQL da solo (44); i sei requisiti informativi (45); i quattro modi in cui sbaglia, quasi tutti con un numero plausibile (46). Poi la naive RAG (47) e il modo agentico come risposta ai suoi errori e a quelli del Text2SQL, su due assi: iterare e incrociare le fonti (48). Il limite che nessuna search supera, la sintesi oltre il chunk (49), e GraphRAG in due slide: il lexical graph con le entità estratte, percorso da un agente (50), e le comunità con i riassunti per le domande globali (51). Pagella ereditata e cerniera verso il significato condiviso (52). La mini-mappa dei separatori accende la fascia dei pattern agentici.
>
> **Nomi**: la RAG a un colpo si chiama **naive RAG** (il nome delle fonti: "retrieve once, generate once"); il modo agentico non si chiama "RAG 2.0" né "agentic RAG" in slide. Il tool Text2SQL si chiama `esegui_sql(query)`: lo schema sta nel system prompt e il SQL lo scrive il modello; la variante con un modello dentro il tool non è in slide.
>
> **Dispositivo delle tre slide a tempi**: la Slide 50 usa lo stesso dispositivo delle Slide 10 (SQL) e 39 (Cypher): punti a sinistra, riquadro al centro in cui compaiono le righe, figura a destra che si accende. Qui il riquadro è la traccia dell'agente e la figura è il lexical graph.
>
> **Riprese**: tool ≠ API e "salva e cerca" (27, slide 18 → Slide 43 e 46); la finestra a strati e il system prompt (27, slide 7–8 → Slide 44 e 45); errori come feedback (27, slide 16 → Slide 44 e 48); RAG in due stadi (27, slide 48 → Slide 47); context rot e tool a scalini (26, slide 44–45 → Slide 47); la traccia della slide 20 del 27 rifatta per la terza volta (Slide 44). Eyebrow *dall'incontro 26* / *dall'incontro 27* dove la figura è ripresa.
>
> **Fatti verificati (8 set 2026)** in `docs/ricerche-28/research-pattern-agentici.md`: GraphRAG di Microsoft (paper apr 2024: chunk → entità e relazioni estratte dall'LLM → Leiden gerarchico → community report → global search map-reduce; batte la naive RAG su comprehensiveness 72–83% e diversity 62–82% con giudice LLM, perde su directness; indicizzazione di 1M token in 281 minuti); il lexical graph di Neo4j (`Document` → `Chunk` con `PART_OF` e `NEXT`, entità con `HAS_ENTITY`); Text2SQL (Spider 2.0: da ~20% nel 2024 a >90% nel 2026 sul sottoinsieme Snow con sistemi agentici; fallimenti: schema linking 27,6%, join 8,3%; CIDR 2026: annotazioni sbagliate nel 53–66% dei benchmark); Claude Code e `grep`/`glob` (intervista a Boris Cherny, mar 2026); il risultato qualitativo dbt (apr 2026): *senza semantic layer l'errore è un numero plausibile, con il semantic layer è un messaggio di errore*. Le fonti vanno nelle note del relatore.
>
> **Esempio Acme in questa sezione**: la domanda della slide 20 del 27 per la terza volta (Slide 44); il reclamo #88 di Rossi sull'ordine 4471 (SpedFast, 5 giorni di ritardo); il contratto SpedFast 2026 art. 7 (penale 2% oltre il terzo giorno lavorativo) contro la versione 2023; la policy rimborsi 2026 (buono del 10%); i quattromila reclami e l'istogramma motivo × corriere; la colonna `giorni_lavorativi_ritardo` di `fatto_spedizioni` (aggiunta al DDL della Slide 16).
>
> **Codice in questa sezione**: il SQL nelle pill delle tracce (Slide 44, 46, 48), i pattern Cypher nelle tracce (Slide 50); sempre corti, con la lettura a fianco.

---

## Slide 43 — Tre pattern, un lettore

> Ripresa della slide 18 del 27 (un tool non è un'API), eyebrow *dall'incontro 27*.

**Messaggio**: l'agente entra nella conoscenza con tre pattern, uno per forma dello spettro, e ogni pattern è un tool: dichiarato al giro zero, eseguito dall'harness, con il risultato che rientra nella finestra. Il lettore è sempre lo stesso modello; ciò che cambia è ciò che trova, e come sbaglia.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 6 · PATTERN AGENTICI DI ACCESSO AL DATO*
- Titolo: *Tre pattern, un lettore*
- Punti:
  1. **Tre pattern, tre tool**: *Text2SQL per le tabelle (il modello scrive la query, il tool la esegue); search per i documenti (il tool cerca, il modello legge i chunk); traversal per i grafi (il modello scrive il pattern, il tool lo percorre). Sono tool nel senso del 27: nome, descrizione, parametri, e un risultato che rientra come testo.*
  2. **Chi sceglie il pattern**: *il modello, dalla domanda e dalle descrizioni dei tool (il 27, slide 11): "quanti" va alle tabelle, "che cosa prevede" ai documenti, "come sono collegati" al grafo. Se le descrizioni sono vaghe, sceglie il pattern sbagliato, e il risultato sembra giusto lo stesso.*
  3. **Che cosa non cambia**: *la conoscenza è quella delle sezioni 2–5, con la sua pagella. L'agente non la migliora: la legge. Un tool su un data warehouse ben fatto risponde bene; lo stesso tool su dieci pipeline per report risponde con tre verità.*
- Nota in basso: *Ripresa del 27 (slide 18): un tool non è un'API. Un tool Text2SQL non espone il database: espone "esegui questa query"; l'identità, il salvataggio del risultato grande, i limiti stanno nell'adattatore. Vale per tutti e tre i pattern.*

**Visual**: `slide43-tre-pattern.svg`.

**Prompt per schema SVG**:
> **In alto**, la fascia dei pattern agentici dello spettro (dalla Slide 7), accesa: `Text2SQL` · `GraphRAG` · `RAG · agentic search`.
>
> **Al centro**, un unico blocco `modello` con tre frecce verso tre riquadri-definizione affiancati, nell'idioma dei riquadri del 27:
> - `esegui_sql` — *"Esegue una query SQL sul data warehouse vendite e logistica. Lo schema è nel system prompt. Usalo per totali, confronti, andamenti."* — `query: string`
> - `cerca_documenti` — *"Cerca nei contratti, nelle policy e nei reclami. Usalo per clausole, regole, casi."* — `query: string · filtri: {tipo, corriere, anno}`
> - `percorri_grafo` — *"Trova come sono collegati clienti, ordini, corrieri e contratti."* — `pattern: string`
>
> **Sotto ciascun riquadro**, la forma che sta dietro, in miniatura: una stella, una pila di documenti, un grafo.
>
> **Elemento focale**: le tre descrizioni, che sono ciò che decide il pattern.

## Slide 44 — Text2SQL: com'è fatto

> Ripresa della finestra a strati del 27 (slide 7–8) e della traccia della slide 20 del 27, per la terza volta (Python su file nel 27; DuckDB su file nella Slide 25; SQL sul data warehouse qui). Eyebrow *dall'incontro 27*.

**Messaggio**: la domanda della slide 20 del 27, senza export e senza script: lo schema del data warehouse sta nel system prompt, il modello scrive il SQL della slide 10, il tool lo esegue con l'identità dell'utente, e torna una tabella piccola. Il modello fa una cosa sola: scrive la query.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~30%); al centro (~25%) la finestra a strati del 27 con la fascia dello schema in evidenza; a destra (~45%) il sequence diagram; nota in basso.

**Testo**:
- Titolo: *Text2SQL: com'è fatto*
- Punti:
  1. **Lo schema entra al giro zero**: *nel system prompt, sotto le regole, c'è la descrizione del data warehouse: il DDL di `fatto_spedizioni` e delle dimensioni (slide 16), con una riga di descrizione per tabella e per colonna, e il grano dichiarato: "una riga è una spedizione". È il 27, slide 8: ciò che il modello deve sapere, l'harness glielo mette davanti prima della prima parola.*
  2. **Il modello scrive il SQL**: *legge la domanda, legge lo schema, e chiama `esegui_sql` con la query della slide 10. Non c'è un secondo modello dentro il tool: il tool esegue, e basta.*
  3. **L'harness esegue, con l'identità giusta**: *la query gira sul data warehouse come Marco (slide 20); se fallisce, l'errore rientra come testo (il 27, slide 16) e il modello la riscrive; se riesce, rientrano tre righe: `SpedFast 121 · Corriere Nord 44 · PostaPro 22`. Il conto l'ha fatto il database.*
- Nota in basso: *Nel 27 il modello aveva scritto Python su un file; nella slide 25 SQL su un file con DuckDB; qui SQL sul data warehouse, attraverso un tool. Tre volte la stessa domanda: cambia dove sta il dato e chi fa il conto. Che cosa mettere nel system prompt perché il SQL esca giusto è la prossima slide.*

**Visual**: `slide44-finestra-schema.svg` (la finestra a strati del 27, ripresa) + `slide44-text2sql-sequence.svg` (sequence diagram).

**Prompt per schema SVG** (finestra): la finestra a strati della sezione 2 del 27, stesso viewBox e stessi strati (`system prompt` · `dichiarazione dei tool` · `indice delle skill` · `messaggi`), con lo strato `system prompt` diviso in due fasce: `ruolo e regole` attenuata e `schema del data warehouse: DDL + descrizioni + grano` piena e in evidenza; nello strato dei tool, la riga `esegui_sql` evidenziata. **Elemento focale**: la fascia dello schema.

**Prompt per schema SVG** (sequence):
> Sequence diagram nell'idioma della slide 15 del 27, linee di vita `modello` · `harness` · `tool: esegui_sql` (dentro il riquadro dell'harness) · `data warehouse` (tratteggiata, come l'API del 27). **Giro 1**: `harness → modello` `chiamata: la finestra (con lo schema) + la domanda`; `modello → harness` `tool_use: esegui_sql("SELECT s.corriere, COUNT(*) … GROUP BY s.corriere")` con `stop_reason: tool_use`; `tool → data warehouse` la query, con l'etichetta `come: Marco`; ritorno `3 righe`; `harness → modello` `tool_result: SpedFast 121 · Corriere Nord 44 · PostaPro 22`. **Giro 2**: il modello risponde in italiano, `stop_reason: end_turn`.
>
> **Elemento focale**: la pill con la query scritta dal modello e l'etichetta `come: Marco`.

## Slide 45 — Text2SQL: i requisiti informativi

**Messaggio**: il SQL esce giusto se nella finestra c'è ciò che un analista nuovo chiederebbe il primo giorno: che cosa c'è, che cosa vuol dire, come si unisce, come si calcola, e qualche esempio. Il data warehouse di Kimball ne dà metà gratis; il transazionale nessuna; il resto è lavoro di chi prepara la KB.

**Layout**: titolo in alto; le sei righe a sinistra (~45%, classe `tight`); visual al centro-destra (~50%); nota in basso.

**Testo**:
- Titolo: *Text2SQL: i requisiti informativi*
- I sei requisiti:
  1. **Lo schema, con le descrizioni**: *tabelle e colonne, e per ciascuna una riga in italiano: `giorni_ritardo: giorni di calendario fra consegna e data prevista, 0 se in anticipo`. I nomi da soli non bastano, e i nomi tecnici sono peggio di niente.*
  2. **Il grano**: *"una riga di `fatto_spedizioni` è una spedizione". Una frase, e il fanout della slide 19 perde metà delle occasioni.*
  3. **Le join note**: *quali tabelle si uniscono, su quali chiavi: la stella lo dice da sola; un transazionale a duecento tabelle no.*
  4. **Le metriche, definite**: *"ordini in ritardo = spedizioni con `giorni_ritardo > 0`"; "ritardo medio = media di `giorni_ritardo` sulle sole spedizioni in ritardo". Senza, ogni domanda inventa la sua regola: le tre verità della slide 14, generate dal modello.*
  5. **I valori di esempio**: *`corriere` contiene `SpedFast`, `Corriere Nord`, `PostaPro`, non `SPEDFAST S.R.L.`; `regione` è il nome, non la sigla. È il modo più economico per evitare un `WHERE` che non trova nulla.*
  6. **Le query di esempio**: *dieci domande frequenti con il SQL giusto: il modello copia la forma, e la forma è quasi tutto.*
- Nota in basso: *Uno star schema con i nomi di business dà 1, 2 e 3 quasi gratis; 4, 5 e 6 li deve scrivere qualcuno. Sono la stessa cosa che serve a un collega nuovo, messa per iscritto una volta: nella sezione 7 si chiama semantic layer, e ha un posto dove stare.*

**Visual**: `slide45-requisiti.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la finestra a strati del 27 con lo strato `system prompt` aperto in sei fasce, una per requisito, ciascuna con il peso in token a lato: `schema + descrizioni ~1.500` · `grano ~30` · `join ~200` · `metriche ~300` · `valori di esempio ~200` · `query di esempio ~1.200`; in fondo il totale `~3.400 token, in cache`.
>
> **A destra**, due colonne di spunte, una per forma: `star schema (sez. 3)` con i requisiti 1, 2, 3 in ✓ e 4, 5, 6 in ✗; `transazionale (sez. 2)` con sei ✗.
>
> **Elemento focale**: le sei fasce nel system prompt, e le tre ✗ dello star schema che qualcuno deve colmare.

## Slide 46 — Text2SQL: dove sbaglia

**Messaggio**: il SQL scritto dal modello sbaglia in pochi modi noti, e quasi tutti producono un numero plausibile invece di un errore. Sono gli stessi errori di un analista frettoloso, e si prevengono nello stesso modo: con i requisiti della slide precedente e con un risultato che non entri in finestra a peso morto.

**Layout**: titolo in alto; i quattro modi a sinistra (~45%); a destra (~50%) il riquadro-payload con le quattro mini-tracce; nota in basso.

**Testo**:
- Titolo: *Text2SQL: dove sbaglia*
- I quattro modi:
  1. **La tabella o la colonna sbagliata**: *il modo più frequente: fra `spedizioni`, `fatto_spedizioni` e `spedizioni_v2` sceglie quella con il nome più simile alla domanda, o inventa una colonna che sembra dovesse esserci (`data_ritardo`). Rimedio: descrizioni, e meno tabelle esposte.*
  2. **La join sbagliata, e il fanout**: *la slide 19, scritta dal modello: unisce due fatti prima di aggregare e l'importo esce nove volte più grande. Nessun errore, un numero. Rimedio: il grano dichiarato, le join note, e un tool che sappia dire di no.*
  3. **L'ambiguità della domanda**: *"ordini in ritardo": rispetto alla data prevista o a quella promessa al cliente? Festivi inclusi? Il modello sceglie, e non dice di aver scelto. Rimedio: le metriche definite; e un modello che, se la definizione manca, chiede invece di scegliere.*
  4. **Il risultato grande**: *"dammi le spedizioni in ritardo" restituisce 187 righe; "tutte le spedizioni" 12.480. Iniettarle in finestra è il carico della slide 18 del 27. Rimedio: l'adattatore salva su file e restituisce le prime righe e il conteggio; il modello cerca nel file se serve.*
- Riquadro-payload (HTML, idioma del 26/27; quattro mini-tracce, ognuna con un `✗` a lato):
  ```
  [assistant] → esegui_sql("SELECT … FROM spedizioni_v2 …")                     ✗ tabella sbagliata
  [tool]      187 righe                                                           (sembra giusto)

  [assistant] → esegui_sql("… FROM fatto_spedizioni s JOIN fatto_reclami r …")   ✗ fanout
  [tool]      SpedFast 1.660.000 €                                                (sembra giusto)

  [assistant] → esegui_sql("… WHERE giorni_ritardo > 0")                          ✗ ritardo secondo chi?
  [tool]      187                                                                 (sembra giusto)

  [assistant] → esegui_sql("SELECT * FROM fatto_spedizioni")                      ✗ 12.480 righe
  [tool]      salvato in risultato.csv (12.480 righe): prime 5 righe … · usa grep o duckdb
  ```
- Nota in basso: *La differenza fra un buon Text2SQL e uno cattivo non è il modello: è quanto di questi quattro errori la KB rende impossibili prima ancora che la query venga scritta. Un semantic layer trasforma i primi tre da "numero sbagliato" a "errore esplicito": sezione 7.*

**Visual**: il riquadro-payload in HTML; nessun SVG.

## Slide 47 — Naive RAG: un colpo solo

> Ripresa della slide 48 del 27 (RAG in due stadi) e delle slide 44–45 del 26 (context rot, tool a scalini). Eyebrow *dall'incontro 27*.

**Messaggio**: la RAG nella sua forma base fa un colpo solo: la domanda diventa una query, tornano i primi k chunk, entrano in finestra, il modello risponde. Due stadi che si misurano separatamente, e un costo che il 26 conosce: i chunk sono risultati di tool, e riempiono la finestra a scalini.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Naive RAG: un colpo solo*
- Punti:
  1. **Il colpo**: *la domanda del cliente, così com'è, va all'indice della sezione 4 (hybrid, magari con reranking); tornano i primi cinque chunk; l'harness li appende alla finestra come `tool_result`; il modello scrive la risposta citando i chunk. Retrieve once, generate once: nessuna decisione del modello, nessun secondo tentativo.*
  2. **Due stadi, due misure**: *il 27 (slide 48): il retrieval ha trovato i chunk giusti, e in cima? La sintesi li ha usati bene, senza aggiungere? Si misurano separatamente perché si correggono in posti diversi: il primo nella KB (chunking, indice, ranking), il secondo nel prompt.*
  3. **Il peso in finestra**: *cinque chunk da cinquecento token sono 2.500 token per domanda, a ogni domanda, per tutta la sessione. È il context rot del 26 (slide 44–45) con l'acceleratore: la RAG è il tool che riempie la finestra più in fretta di tutti, e i chunk vecchi sono i primi da potare (il 27, slide 35).*
- Nota in basso: *Per una parte grande dei casi basta: una domanda, una clausola, una risposta. Fallisce quando la domanda non è la query giusta, quando la risposta sta in due documenti, o quando non sta in nessun chunk: le prossime tre slide.*

**Visual**: `slide47-naive-rag.svg`.

**Prompt per schema SVG**:
> Pipeline orizzontale a un colpo: `domanda` → `indice (sez. 4)` → `5 chunk` → la **finestra a strati del 27** con i cinque chunk in teal appesi allo strato `messaggi`, visibilmente alti → `risposta`. Sotto la pipeline, due graffe: `stadio 1: retrieval — ha trovato i chunk giusti, in cima?` con la leva `KB`, e `stadio 2: sintesi — li ha usati bene?` con la leva `Prompt` (le leve del 27, slide 40). In un angolo, in miniatura, il grafico a scalini della slide 45 del 26 con l'etichetta *cinque chunk a domanda*.
>
> **Elemento focale**: i cinque blocchi teal dentro la finestra.

## Slide 48 — Il modo agentico: iterare, e incrociare le fonti

> Risposta agentica agli errori delle Slide 46 e 47, su due assi. Due tracce affiancate: l'incrocio di fonti a sinistra, l'iterazione pura (solo bash, poi il data warehouse) a destra.

**Messaggio**: gli errori di Text2SQL e naive RAG nascono da un colpo solo su una fonte sola. Con la search e il SQL come tool nel loop del 27, il modello può iterare (l'errore rientra e si corregge) e incrociare le fonti (il data warehouse per i numeri, i documenti per le regole, il grafo per i collegamenti) dentro lo stesso turno.

**Layout**: titolo in alto; i due assi in alto come due colonne (~25% dell'altezza); sotto, i due punti a sinistra (~30%) e i due riquadri-payload affiancati a destra (~65%, classe `micro`); nessuna nota in basso.

**Testo**:
- Titolo: *Il modo agentico: iterare, e incrociare le fonti*
- I due assi:
  - **Da un colpo solo a iterativo**: *la query SQL fallisce o torna vuota: l'errore rientra come testo (il 27, slide 16) e il modello la riscrive con la tabella giusta. Il chunk taglia la clausola: apre il documento intero e ci cerca dentro con `grep` (salva e cerca). La domanda è ambigua: chiede, invece di scegliere. Ogni tentativo è un giro del 3° loop, e ogni giro corregge uno degli errori della slide 46 e 47.*
  - **Da una fonte sola a più fonti**: *"che cosa spetta a Rossi per il ritardo?" non sta in nessuna fonte: i giorni di ritardo sono nel data warehouse, la penale nel contratto, il buono nella policy, il collegamento fra l'ordine e il corriere nel grafo. Il modello chiama tre tool nello stesso turno e compone; nessuno dei tre, da solo, avrebbe risposto.*
- Punti:
  1. **Il prezzo, e la regola**: *più giri, più latenza, più token in finestra; e un modello che cerca male cerca male tre volte. Per questo il primo colpo deve essere buono (i requisiti della slide 45, il retrieval della sezione 4) e il loop serve per ciò che il primo colpo non chiude. Non un altro indice: lo stesso indice, con il loop davanti.*
  2. **A volte basta grep**: *in generale si è visto che una ricerca agentica con un tool come bash, che usa `glob` per elencare e `grep` per cercare, a volte batte indici vettoriali complessi: il modello sa che cosa sta cercando, guarda l'elenco dei file, cerca la parola, legge solo le righe che contano, e riprova se sbaglia. Nessun indice da costruire e da tenere aggiornato. Chi costruisce Claude Code ha provato gli indici vettoriali sul codice e li ha tolti per questo. Vale dove le parole sono esatte e l'archivio è ordinato; dove non lo sono, serve l'indice, ma il loop davanti serve lo stesso.*
- Riquadro-payload **sinistro — «tre fonti, un turno»** (HTML, idioma del 26/27; a lato le marcature *incrociare* sulle tre fonti diverse e *iterare* sul `grep` dopo il chunk tagliato):
  ```
  [user]      Il cliente Rossi chiede cosa gli spetta per il ritardo dell'ordine 4471.
  [assistant] → cerca_ordine("4471")
  [tool]      {corriere: "SpedFast", prevista: "08-14", consegna: "08-19"}   → 5 giorni
  [assistant] → cerca_documenti("penale ritardo", filtri={tipo: "contratto", corriere: "SpedFast"})
  [tool]      3 chunk · il migliore: contratto_SpedFast_2026.pdf, art. 7 (taglia a metà)
  [assistant] → bash("grep -n -A4 'penale' contratti/SpedFast_2026.txt")
  [tool]      art. 7: "…oltre il terzo giorno lavorativo… penale pari al 2% del valore…"
  [assistant] → cerca_documenti("rimborso cliente ritardo corriere", filtri={tipo: "policy"})
  [tool]      policy_rimborsi_2026.md: "…il cliente ha diritto a un buono del 10%…"
  [assistant] Per l'ordine 4471 (5 giorni di ritardo, SpedFast): al cliente spetta un buono
              del 10% (policy rimborsi 2026); ad Acme una penale del 2% da SpedFast (art. 7).
  ```
  Conto a lato: `4 tool call · 3 fonti · 1 turno · ~3.000 token di risultati`.
- Riquadro-payload **destro — «solo bash, poi il data warehouse: la ricerca agentica virtuosa»** (HTML):
  ```
  [user]      Che cosa prevede il contratto con SpedFast se consegnano in ritardo?
  [assistant] → bash("ls contratti/")
  [tool]      CorriereNord_2025.txt  PostaPro_2024.txt  SpedFast_2023.txt  SpedFast_2026.txt
  [assistant] → bash("grep -il 'ritard\|penal\|oltre i termini' contratti/SpedFast_2026.txt")
  [tool]      contratti/SpedFast_2026.txt
  [assistant] → bash("grep -n -B2 -A4 -i 'penal' contratti/SpedFast_2026.txt")
  [tool]      84: Art. 7 – Ritardi. Per consegne effettuate oltre il terzo giorno
              85: lavorativo successivo alla data concordata, il Vettore riconoscerà
              86: una penale pari al 2% del valore della spedizione …
  [assistant] → bash("grep -n -i 'lavorativ' contratti/SpedFast_2026.txt | head -3")
  [tool]      12: …per "giorno lavorativo" si intende dal lunedì al venerdì, festivi esclusi.
  [assistant] → esegui_sql("SELECT COUNT(*) AS n, SUM(importo)*0.02 AS penale_stimata
                FROM fatto_spedizioni s JOIN dim_corriere c USING (id_corriere)
                WHERE c.nome = 'SpedFast' AND s.giorni_lavorativi_ritardo > 3
                AND s.id_data BETWEEN 20260801 AND 20260831")
  [tool]      n: 97 · penale_stimata: 3.640,00
  [assistant] Il contratto SpedFast 2026 (art. 7) prevede una penale del 2% del valore
              della spedizione oltre il terzo giorno lavorativo (lun–ven, festivi esclusi).
              Ad agosto le spedizioni SpedFast oltre la soglia sono 97: penale stimata
              3.640 €. Ho usato la versione 2026 del contratto, non quella 2023.
  ```
  A lato della query: *ha usato `giorni_lavorativi_ritardo`, non `giorni_ritardo`: la definizione l'ha presa dal contratto e l'ha cercata nello schema*. Conto a lato: `5 tool call · 2 fonti · nessun indice · ~800 token di risultati · ha scelto la versione giusta e ha risolto "lavorativo" da solo`.

**Visual**: i due riquadri-payload in HTML; nessun SVG. In Fase 3 verificare a schermo che due tracce di questa lunghezza stiano affiancate a `micro`; se sforano, la traccia sinistra si accorcia alle prime sei righe.

## Slide 49 — Il limite: sintetizzare oltre il chunk

**Messaggio**: c'è una classe di domande che nessuna search risolve, agentica o no: quelle la cui risposta non sta in nessun chunk, perché è una sintesi su tutto l'archivio. Trovare pezzi non è vedere tendenze; per quelle serve un'altra struttura.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il limite: sintetizzare oltre il chunk*
- Punti:
  1. **La domanda che non ha un chunk**: *"di che cosa si lamentano di più i clienti, e con quali corrieri?" Quattromila reclami. Nessun reclamo contiene la risposta: la risposta è una distribuzione sui quattromila. L'indice restituisce i cinque più simili alla domanda, cioè cinque reclami qualsiasi.*
  2. **Perché il loop non basta**: *il modello può cercare "ritardo", poi "danneggiato", poi "mancante", e contare. Ma non sa che cosa cercare prima di aver letto tutto, e leggere tutto non sta in finestra (il 26: il contesto è finito, e degrada prima). Iterare aiuta a trovare; non aiuta a vedere l'insieme.*
  3. **Che cosa servirebbe**: *una struttura costruita prima, una volta, che abbia già letto tutto e tenuto il riassunto: le entità di cui si parla, come si legano, e un sommario per ogni gruppo. Cioè un grafo estratto dal testo, con i suoi riassunti. È GraphRAG, prossime due slide.*
- Nota in basso: *Se i reclami fossero nel data warehouse, con una colonna `motivo`, la domanda sarebbe un `GROUP BY` (slide 10). Il problema è che il motivo sta nel testo: GraphRAG è, in fondo, il modo di costruire quella colonna a partire dal testo, una volta per tutte.*

**Visual**: `slide49-oltre-il-chunk.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la domanda e l'indice che restituisce cinque chunk di reclami sparsi (`#88 ritardo` · `#412 pacco danneggiato` · `#903 ritardo` · `#1201 mancante` · `#77 ritardo`), con l'etichetta *cinque su quattromila: non è una risposta*.
>
> **A destra**, sbiadito e tratteggiato, un istogramma `motivo × corriere` (tre gruppi di barre, `ritardi` · `danni` · `mancanti`, per `SpedFast` · `Corriere Nord` · `PostaPro`), con l'etichetta *la risposta: nessun chunk la contiene*.
>
> Fra i due, una freccia barrata con l'etichetta *la search non ci arriva*.
>
> **Elemento focale**: l'istogramma tratteggiato.

## Slide 50 — GraphRAG: il lexical graph

> Slide a **sei tempi** (fragment), con il dispositivo delle Slide 10 e 39: punti a sinistra, la traccia dell'agente al centro che cresce riga per riga, il lexical graph a destra che si costruisce (tempi 1–2) e poi si colora (tempi 3–6).

**Messaggio**: il primo passo di GraphRAG è dare al testo la struttura che non ha: documenti spezzati in chunk collegati fra loro, e dentro i chunk le entità e le relazioni che un modello estrae, una per una. Il testo diventa un grafo che si può percorrere, e la search atterra su un chunk e poi cammina.

**Layout**: titolo in alto; i tre punti a sinistra (~28%), che si accendono con i tempi 1, 2 e 3; al centro (~32%) il riquadro-payload, in cui le righe compaiono un tempo alla volta (`fragment` sugli stessi indici degli SVG); a destra (~40%) il lexical graph; nota in basso.

**Testo**:
- Titolo: *GraphRAG: il lexical graph*
- Punti:
  1. **Il lexical graph**: *ogni documento è un nodo; ogni chunk è un nodo, collegato al documento (`PART_OF`) e al chunk successivo (`NEXT`). È il chunking della sezione 4 scritto come grafo: si sa da dove viene un chunk e che cosa c'è prima e dopo. Solo con questo, il "chunk che taglia la clausola a metà" si risolve seguendo `NEXT`.*
  2. **Le entità estratte**: *un modello legge ogni chunk e scrive le cose di cui parla e come si legano: `SpedFast` –`ha_penale`→ `2%`; `reclamo #88` –`riguarda`→ `ritardo`; `ritardo` –`di`→ `SpedFast`. Ogni entità è un nodo collegato ai chunk in cui compare (`HAS_ENTITY`). È l'estrazione della slide 29, fatta una volta per tutte e scritta come archi.*
  3. **Come si cerca**: *la search vettoriale trova il chunk d'ingresso; da lì si percorre: le entità del chunk, gli altri chunk delle stesse entità, i vicini a un passo. "Quali reclami citano SpedFast e un ritardo?" diventa un pattern (sezione 5) su un grafo che prima non esisteva.*
- Riquadro-payload (HTML, idioma del 26/27; le righe compaiono ai tempi 3–6):
  ```
  [user]      Quali reclami citano SpedFast per un ritardo, e cosa prevede il contratto?
  [assistant] → cerca_grafo("reclami SpedFast ritardo")                          (tempo 3)
  [tool]      chunk d'ingresso: reclamo #88, chunk 2 (score 0,84)
  [assistant] → percorri_grafo("(c:Chunk {id:'88-2'})-[:HAS_ENTITY]->(e)")       (tempo 4)
  [tool]      SpedFast · ritardo · Rossi
  [assistant] → percorri_grafo("(:Entity {nome:'SpedFast'})<-[:HAS_ENTITY]-(k:Chunk)")  (tempo 5)
  [tool]      6 chunk: reclamo #88, #903, #77 · contratto_SpedFast_2026 (art. 7) · policy_rimborsi
  [assistant] → bash("grep -n -A3 'penale' contratti/SpedFast_2026.txt")         (tempo 6)
  [tool]      art. 7: …penale pari al 2%…
  [assistant] Tre reclami citano SpedFast per ritardi (#88, #903, #77); il contratto 2026,
              art. 7, prevede una penale del 2%.
  ```
- Nota in basso: *Il termine è di Neo4j, e il grafo è quello delle cose (sezione 5): `SpedFast`, `#88`, non `Corriere`. Chi decide quali tipi di entità estrarre e con quali nomi sta già scrivendo un'ontologia, anche se non lo sa: sezione 7.*

**Visual**: il riquadro-payload in HTML + `slide50-lexical-graph-{1..6}.svg` (`.visual.stack` + fragment, stesso viewBox).

**Prompt per schema SVG**:
> La figura ha due metà: **a sinistra** la pila di documenti (`contratto_SpedFast_2026`, `reclamo #88`, `reclamo #903`, `policy_rimborsi`) spezzata in chunk (rettangoli), con archi `PART_OF` verso il documento e `NEXT` fra chunk consecutivi; **al centro** un blocco `modello: estrai entità e relazioni`; **a destra** i nodi entità (`SpedFast` · `penale 2%` · `ritardo` · `reclamo #88` · `Rossi` · `buono 10%`) collegati fra loro da archi etichettati (`ha_penale`, `riguarda`, `di`, `apre`) e collegati indietro ai chunk con linee sottili `HAS_ENTITY`. Sei tempi:
> 1. Solo la metà sinistra: documenti, chunk, `PART_OF`, `NEXT`. Il resto assente.
> 2. Compare il blocco del modello con una freccia da ogni chunk, e la metà destra: entità, archi fra entità, linee `HAS_ENTITY`. Tutto acceso in modo uniforme.
> 3. Tutto si attenua; si accende il **chunk d'ingresso** (`reclamo #88, chunk 2`) con l'etichetta *search: 0,84*.
> 4. Si accendono le tre linee `HAS_ENTITY` dal chunk d'ingresso e le entità `SpedFast` · `ritardo` · `Rossi`.
> 5. Da `SpedFast` si accendono le linee `HAS_ENTITY` verso gli altri chunk e i chunk stessi: `#903`, `#77`, il chunk `art. 7` del contratto, il chunk della policy. Etichetta: *tre documenti, un passo*.
> 6. Il percorso completo evidenziato dal chunk d'ingresso fino al chunk `art. 7` del contratto, con l'etichetta *tre documenti, un percorso*; il chunk del contratto in evidenza.
>
> **Elemento focale**: ai tempi 1–2 le linee `HAS_ENTITY` che uniscono testo ed entità; dal tempo 3, la parte del grafo appena accesa, con la stessa tinta della riga di traccia comparsa.

## Slide 51 — GraphRAG: community detection

**Messaggio**: per le domande globali della slide 49 non basta percorrere: il grafo delle entità si divide in comunità, un modello scrive un riassunto per ogni comunità, e la domanda si risponde sui riassunti, non sui chunk. L'archivio è stato letto tutto, una volta, prima della domanda.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *GraphRAG: community detection*
- Punti:
  1. **Le comunità**: *nel grafo delle entità, i nodi che si citano molto fra loro formano gruppi: `SpedFast · ritardo · penale · Lombardia` da una parte, `PostaPro · pacco danneggiato · reso` dall'altra. Un algoritmo (Leiden) li trova da solo, a più livelli: comunità piccole dentro comunità grandi. Nessuno le ha disegnate.*
  2. **I riassunti**: *per ogni comunità, a ogni livello, un modello scrive un rapporto: chi c'è, di che cosa si parla, quanti chunk. Migliaia di chiamate al modello, una volta, all'indicizzazione: è il costo di GraphRAG, e non è piccolo (ore, milioni di token).*
  3. **La domanda globale**: *"di che cosa si lamentano di più i clienti?" va a tutti i rapporti del livello scelto: ognuno produce una risposta parziale (map), poi una chiamata le fonde (reduce). La risposta è una sintesi su tutto l'archivio, e in finestra sono entrati riassunti, non quattromila reclami.*
- Nota in basso: *Microsoft, 2024: su domande di sintesi GraphRAG batte la naive RAG per completezza e varietà, giudicate da un modello; su domande puntuali la naive RAG resta più diretta, e costa cento volte meno. Non è un'alternativa alla search: è la struttura per la classe di domande che la search non può vedere.*

**Visual**: `slide51-community.svg`.

**Prompt per schema SVG**:
> **A sinistra**, il grafo delle entità della Slide 50, allargato a una ventina di nodi, con i nodi raggruppati in tre aree colorate e contornate: `comunità A: SpedFast, ritardi, penale, Lombardia` · `comunità B: PostaPro, danni, resi` · `comunità C: Corriere Nord, resi, buoni`; un contorno più grande racchiude B e C con l'etichetta `livello 1`.
>
> **Al centro**, da ogni comunità una freccia verso un blocco `modello: scrivi il rapporto`, e da lì tre fogli `rapporto A` · `rapporto B` · `rapporto C`, ciascuno con tre righe di sintesi (es. `A: SpedFast · 61% dei reclami sui ritardi · penale 2% · Lombardia`).
>
> **A destra**, la domanda `di che cosa si lamentano di più i clienti?` che entra in tutti e tre i rapporti (etichetta `map`), tre risposte parziali, e un blocco `reduce` che le fonde nell'istogramma `motivo × corriere` della Slide 49, ora pieno.
>
> **Elemento focale**: i tre rapporti, e l'istogramma che si riempie.

## Slide 52 — La pagella dei pattern, e la cerniera

**Messaggio**: i pattern agentici non cambiano la pagella della forma che leggono: la ereditano. Un tool ottimo su una KB tenuta male risponde male con sicurezza. Ciò che manca a tutti e tre è la stessa cosa: il significato condiviso, scritto una volta e letto da tutti.

**Layout**: come le pagelle precedenti: la pagella a sinistra (~45%) con voti e perché, regola del punto di vista sotto; a destra (~50%) la mini-mappa dello spettro con la fascia dei pattern spuntata e la banda dell'ontologia che si accende; blocco nero centrato in basso. Nelle celle "ereditato", in piccolo, i tre voti delle forme sotto (tabella · documento · grafo).

**Testo**:
- Titolo: *La pagella dei pattern, e la cerniera*
- Pagella (HTML, `.pagella`), letta per pattern, con il voto ereditato dalla forma sotto:
  1. **Ricercabile in modo progressivo**: **✓** — *è il requisito che i pattern migliorano davvero: il SQL scende dal totale al dettaglio, la search agentica riformula e apre, il grafo percorre. A patto che la forma sotto lo permetta: sullo schema normalizzato della slide 11 nessun pattern salva il modello.*
  2. **Non ridondante**: **ereditato** (✓ · ✗ · ✓) — *Text2SQL su dieci pipeline per report sceglie una delle dieci; la search su tre versioni del contratto ne cita una; GraphRAG estrae tre nodi `SpedFast` se il testo lo scrive in tre modi. Il pattern non toglie copie: le trova tutte.*
  3. **Veritiera**: **ereditato, con un'aggravante** (~ · ✗ · ~) — *il modello risponde con la stessa sicurezza su un dato buono e su uno cattivo, e la slide 46 lo mostra: l'errore è un numero plausibile. Il pattern non aggiunge verità; toglie l'esitazione che una persona avrebbe avuto.*
  4. **Compounding**: **~** — *il lexical graph e le comunità sono conoscenza nuova estratta dal testo, e si accumula. Ma senza nomi condivisi (`SpedFast` del data warehouse e `SpedFast` del grafo sono la stessa cosa?) ogni pattern accumula per sé.*
- Regola sotto la pagella: *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Blocco nero centrato (la cerniera): *Tre pattern, e a tutti manca la stessa cosa: che cosa vuol dire "ritardo", che cosa è un "corriere", che `SpedFast` della tabella e `SpedFast` del contratto sono uno. Il significato, scritto una volta, letto da persone, pipeline e agenti. Sezione 7.*

**Visual**: la pagella in HTML + la mini-mappa dello spettro (`minimap` della Slide 7 con la fascia `pattern agentici` spuntata e la banda `Ontologia` come elemento focale).
