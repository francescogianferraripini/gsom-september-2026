# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 4 — Il dato non strutturato: da analisi a search**
**Obiettivo di apprendimento**: il partecipante sa dove sta il non strutturato e che cosa gli manca (schema, ETL, proprietario, ciclo di vita), sa perché un fatto dentro un testo non si interroga ma si cerca, conosce i due modi di cercare (per parole, BM25; per significato, chunk embedding e indice vettoriale) con i loro punti ciechi e i loro rimedi, sa estendere l'embedding del 26 dal token al chunk, e sa che il problema vero non è trovare ma ordinare (hybrid, segnali di rilevanza, reranking a due stadi).
**Messaggio chiave (takeaway)**: Trovare è facile; decidere che cosa conta è il lavoro. E il testo resta senza relazioni esplicite.
**Budget**: ~20 min, 9 slide + separatore. Ripartizione: dove sta e che cosa cambia 3, i due modi di cercare 3, ordinare 2, pagella 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec4.html` | Separatore — Sezione 4: Il dato non strutturato |
| `slides/slide28-dove-sta.html` | Slide 28 — Dove sta il non strutturato |
| `slides/slide29-fatto-nel-testo.html` | Slide 29 — Il fatto dentro il testo |
| `slides/slide30-analisi-search.html` | Slide 30 — Da problema di analisi a problema di search |
| `slides/slide31-bm25.html` | Slide 31 — Cercare per parole: BM25 |
| `slides/slide32-chunk-embedding.html` | Slide 32 — Dal token al chunk: l'embedding di un passaggio |
| `slides/slide33-indice-vettoriale.html` | Slide 33 — Cercare per significato: l'indice vettoriale |
| `slides/slide34-relevance.html` | Slide 34 — Trovare è facile, ordinare è difficile |
| `slides/slide35-reranking.html` | Slide 35 — Reranking: il secondo passaggio |
| `slides/slide36-pagella-non-strutturato.html` | Slide 36 — La pagella del non strutturato, e la cerniera |

---

> **Filo della sezione (la traiettoria, concordata in intervista).** Dove sta il non strutturato e che cosa gli manca (28); che cosa cambia nel fatto: da deciso prima a estratto ogni volta, con il rischio dell'informazione spuria (29); che cosa cambia nell'operazione: non si somma, si trova, l'unità è il chunk, lo strumento un indice (30); il primo modo di cercare, per parole, BM25: efficace, efficiente, con limiti in buona parte risolvibili (31); il ponte dal 26, dal token al chunk (32); il secondo modo, per significato, chunking e indice vettoriale, cieco a codici e nomi (33); il vero problema, ordinare: hybrid, segnali oltre la somiglianza, PageRank (34); il secondo passaggio, cross-encoder e ColBERT (35); pagella e cerniera verso i grafi (36). In una riga: *dal documento al fatto non si passa interrogando ma cercando; cercare ha due modi, ognuno cieco a qualcosa; trovare è facile, ordinare è il lavoro; e alla fine il testo resta senza relazioni esplicite.* La mini-mappa dei separatori accende la colonna del documento.
>
> **Il termine "chunk"** è introdotto nella Slide 32 e usato da lì in avanti come unità della search; il modello si chiama sempre *modello di chunk embedding*.
>
> **"GraphRank"** del brief è letto come il ranking basato sui link fra documenti (PageRank e derivati), nella Slide 34. Il ranking sul grafo delle entità è GraphRAG, sezione 6.
>
> **Ripresa dal 26** (Slide 32): le slide 13 (prodotto scalare) e 16 (spazio delle idee), **estese dal token embedding al chunk embedding**, simile ma non identico: un modello addestrato a mettere vicini un chunk e la domanda a cui risponde; un vettore per chunk, non per token; la ricerca come prodotto scalare contro milioni di vettori. Eyebrow *dall'incontro 26*.
>
> **Esempio Acme in questa sezione**: i contratti con i corrieri (SpedFast art. 7: "penale pari al 2% oltre il terzo giorno lavorativo"; Corriere Nord: "indennizzo per consegna oltre i termini"), le policy rimborsi e resi, i reclami, le procedure del servizio clienti; i file `contratto_SpedFast_v2.docx`, `contratto_SpedFast_v3_FINALE.docx`, `contratto_SpedFast_v3_FINALE (1).docx`; la domanda "che cosa prevede il contratto con SpedFast per i ritardi?"; il cieco dell'indice vettoriale su `4471` / `4417`.

---

## Slide 28 — Dove sta il non strutturato

**Messaggio**: la maggior parte della conoscenza aziendale non sta in un database: sta in documenti, sparsi su condivisioni e caselle di posta, senza schema, senza ETL, senza proprietario, senza ciclo di vita. Prima ancora di cercare, il non strutturato parte con due requisiti in rosso.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 4 · IL DATO NON STRUTTURATO: DA ANALISI A SEARCH*
- Titolo: *Dove sta il non strutturato*
- Punti:
  1. **Che cos'è, e dove sta**: *contratti, procedure, offerte, verbali, presentazioni, mail, chat, pagine di wiki. In Word, PDF, PowerPoint; su SharePoint, Drive, Teams, e nelle caselle di posta di chi li ha scritti. Per volume e per valore è la parte più grande della conoscenza di un'azienda.*
  2. **Che cosa non ha**: *uno schema deciso prima; un ETL che lo porti da qualche parte; un proprietario dichiarato; un ciclo di vita: nessuno sa se `contratto_SpedFast_v3_FINALE.docx` è quello in vigore, o se la policy rimborsi del 2024 è stata sostituita. Le versioni si moltiplicano per copia, mai per sostituzione.*
  3. **Che cosa vuol dire per l'agente**: *è la conoscenza che gli serve di più (che cosa prevede il contratto? come si gestisce un reclamo?) ed è quella tenuta peggio. Il transazionale aveva le chiavi, il warehouse aveva l'ETL e un responsabile; qui non c'è nulla fra il documento e chi lo legge.*
- Nota in basso: *Prima di cercare, la pagella è già segnata: non ridondante ✗ (le copie), veritiera ✗ (nessuno sa quale versione vale). La search, che vediamo adesso, risolve "ricercabile"; gli altri due li risolve solo la governance dei documenti, e la sezione 7.*

**Visual**: `slide28-dove-sta.svg`.

**Prompt per schema SVG**:
> Una mappa di contenitori affiancati: `SharePoint / Drive` (cartelle annidate con dentro tre file: `contratto_SpedFast_v2.docx`, `contratto_SpedFast_v3_FINALE.docx`, `contratto_SpedFast_v3_FINALE (1).docx`), `posta` (buste con allegati), `Teams / chat` (bolle di conversazione), `wiki` (pagine), `PDF scansionati`. Accanto a ogni contenitore, quattro etichette barrate: `schema` · `ETL` · `owner` · `versione valida`.
>
> A destra, la pagella in miniatura con le righe *non ridondante* e *veritiera* già in ✗ e le altre due vuote.
>
> **Elemento focale**: i tre file `contratto_SpedFast…` e la pagella parzialmente segnata.

## Slide 29 — Il fatto dentro il testo

**Messaggio**: nel dato strutturato il fatto è deciso prima di scrivere e sta in una cella; nel testo il fatto va estratto ogni volta che serve, e ogni estrazione può sbagliare. Da elemento informativo strutturato ex ante a informazione da ricostruire, con il rischio che sia spuria.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il fatto dentro il testo*
- Punti:
  1. **Nel warehouse**: *`giorni_ritardo = 5` è un fatto già deciso: qualcuno ha scelto la colonna, il tipo, la regola di calcolo, prima di scrivere. Chi legge non interpreta: trova.*
  2. **Nel contratto**: *"Per consegne effettuate oltre il terzo giorno lavorativo successivo alla data concordata, il Vettore riconoscerà una penale pari al 2% del valore della spedizione." Il fatto (penale 2%, soglia 3 giorni lavorativi) c'è, ma sta in una frase: chi legge deve trovarla, capirla, e decidere che "giorno lavorativo" è la stessa cosa del "giorno di ritardo" del warehouse. Forse no.*
  3. **Informazione spuria**: *ogni estrazione è un'interpretazione, e può essere sbagliata: la frase giusta letta male, la frase di un contratto vecchio, una bozza mai firmata. Il warehouse sbaglia in pochi modi noti (il grano); il testo sbaglia in modi che non si vedono.*
- Nota in basso: *È la piramide della slide 3 al contrario: il testo è informazione con dentro i fatti, e il lavoro è tirarli fuori. Il data management del non strutturato è questo: da documento a fatto, ogni volta, o una volta per tutte (sezione 7).*

**Visual**: `slide29-fatto-nel-testo.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la cella: la tabella `fatto_spedizioni` con la cella `giorni_ritardo = 5` evidenziata, etichetta *deciso prima: trovi*.
>
> **A destra**, un blocco di testo del contratto (un paragrafo di sei o sette righe) con la frase della penale evidenziata al suo interno; da essa tre frecce di estrazione verso tre riquadri: `penale: 2%` · `soglia: 3 giorni lavorativi` · `base: valore spedizione`. Sul secondo riquadro un `?` e l'etichetta *lavorativi ≠ di ritardo?*. Etichetta generale sul lato destro: *estratto ogni volta: interpreti*.
>
> **Elemento focale**: la frase evidenziata e il `?`.

## Slide 30 — Da problema di analisi a problema di search

**Messaggio**: senza una cella non si somma: si trova. Il problema cambia natura: l'unità non è più la riga ma il passaggio, la domanda non è più "quanto" ma "dove sta scritto", lo strumento non è più una query ma un indice.

**Layout**: titolo in alto; la tabella di confronto nella metà superiore (~40%); sotto, i due punti a sinistra (~55%) e la mini-figura a destra (~40%); nota in basso.

**Testo**:
- Titolo: *Da problema di analisi a problema di search*
- Tabella di confronto (HTML, `.tbl`, due colonne *analisi* | *search*):

| | **Analisi** | **Search** |
|---|---|---|
| **L'unità** | la riga di un fatto, con il suo grano | il passaggio: un paragrafo, una clausola, una pagina |
| **La domanda** | quanto, per chi, quando: si calcola | dove sta scritto: si trova, poi si legge |
| **Lo strumento** | una query su tabelle con uno schema | un indice su testi senza schema, e un punteggio |
| **La risposta** | un numero, esatto o sbagliato | una lista ordinata di candidati, e nessuna garanzia che il primo sia quello giusto |

- Punti:
  1. **I documenti di Acme**: *i contratti con i corrieri (SpedFast, Corriere Nord, PostaPro), le policy sui rimborsi e sui resi, i reclami dei clienti, le procedure del servizio clienti. Qualche migliaio di pagine.*
  2. **La domanda tipo**: *"che cosa prevede il contratto con SpedFast per i ritardi?" Nessuna tabella la contiene. Un indice deve restituire il passaggio giusto fra migliaia, e in cima.*
- Nota in basso: *Il numero si controlla ricalcolandolo; il passaggio si controlla leggendolo. È per questo che nella search il problema non è trovare qualcosa, ma trovare quello giusto e metterlo per primo: slide 34.*

**Visual**: la tabella in HTML + `slide30-analisi-search.svg` (mini-figura).

**Prompt per schema SVG**:
> Due vignette affiancate, piccole. **A sinistra**: una tabella stilizzata con una freccia verso un numero grande, `121`. **A destra**: una pila di documenti con una freccia verso una lista di cinque passaggi numerati, il primo evidenziato, gli altri sfumati, e un `?` accanto alla lista con l'etichetta *è quello giusto?*.
>
> **Elemento focale**: il contrasto fra il numero unico e la lista con il `?`. ViewBox ritagliato: la figura sta in una colonna da ~40%.

## Slide 31 — Cercare per parole: BM25

**Messaggio**: il primo modo di cercare conta le parole, ed è estremamente efficace ed efficiente: nessun modello, un indice che si costruisce in minuti e risponde in millisecondi, preciso su termini, codici e nomi. I suoi limiti sono noti e in buona parte risolvibili.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~45%); a destra (~50%) il riquadro con la domanda e i tre passaggi; nessuna nota in basso.

**Testo**:
- Titolo: *Cercare per parole: BM25*
- Punti:
  1. **Tre ingredienti**: *quante volte il passaggio contiene la parola (frequenza del termine); in quanti passaggi dell'archivio quella parola compare (più è rara, più pesa: "penale" vale, "il" no); quanto è lungo il passaggio (un termine in dieci righe vale più dello stesso in cento). BM25 è la formula che li combina, ed è lo standard da trent'anni.*
  2. **Efficace ed efficiente**: *nomi, codici, sigle, numeri: "SpedFast", "art. 7", "4471": se la parola c'è, la trova, e la trova in cima. Nessun modello, nessun addestramento, nessuna GPU: un indice invertito, parola → passaggi, che si costruisce in minuti su milioni di documenti e risponde in millisecondi. È il motore dentro Elasticsearch, e per una parte enorme delle ricerche reali basta da solo.*
  3. **I limiti, e i rimedi**: *cerca lettere, non significato: "ritardo" non trova "consegna oltre i termini". Ma molto si sistema senza un modello: elenchi di sinonimi ("penale, indennizzo, risarcimento"), riduzione delle parole alla radice (ritardo, ritardi, ritardata), espansione con i termini del dominio. Resta cieco alle parafrasi che nessuno ha previsto: è lì che serve il significato, prossima slide.*
- Riquadro (HTML): la domanda `penale ritardo SpedFast` in testa, e sotto tre passaggi con il conteggio delle parole e il punteggio:
  1. contratto SpedFast, art. 7 — *"…il Vettore riconoscerà una penale pari al 2%…"* — `SpedFast ×2 · penale ×1 · ritardo ×0` → **alto**
  2. mail del 3 settembre — *"…la spedizione SpedFast è di nuovo in ritardo…"* — `SpedFast ×1 · ritardo ×1` → medio
  3. (sbiadito) contratto Corriere Nord — *"…indennizzo per consegna oltre i termini…"* — `0 parole in comune` → **non trovato**; sotto, in evidenza: *con il sinonimo "indennizzo" nell'elenco → trovato*.

**Visual**: il riquadro in HTML; nessun SVG.

## Slide 32 — Dal token al chunk: l'embedding di un passaggio

> Ripresa delle slide 13 e 16 del 26, eyebrow *dall'incontro 26*. Introduce il termine **chunk**.

**Messaggio**: nel 26 un vettore rappresentava un token, e la vicinanza era affinità. Per cercare serve un vettore per un passaggio intero, un chunk: si ottiene con un modello addestrato apposta, e la ricerca è il prodotto scalare del 26 fatto contro milioni di vettori. Simile, non identico.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Dal token al chunk: l'embedding di un passaggio*
- Punti:
  1. **Nel 26**: *a ogni token il suo vettore, in uno spazio a migliaia di dimensioni; la vicinanza è affinità, il prodotto scalare la misura. Era il primo strato dell'LLM.*
  2. **Che cosa cambia**: *qui serve un vettore per un pezzo di testo: una frase, un paragrafo, una clausola. Quel pezzo si chiama **chunk**, ed è l'unità della search da qui in avanti. Il suo vettore non è la media dei token: è l'uscita di un modello (un piccolo transformer, lo stesso della sezione 3 del 26) addestrato a un compito diverso: mettere vicini un chunk e la domanda a cui risponde, lontani i chunk che non c'entrano. Milioni di coppie domanda–risposta, e il modello impara che "penale per ritardo" e "indennizzo oltre i termini" devono stare vicini.*
  3. **La ricerca**: *la domanda diventa un vettore con lo stesso modello; il punteggio di ogni chunk è il prodotto scalare fra i due (la slide 13 del 26); vince il più alto. Contro milioni di chunk, con un indice fatto apposta, in millisecondi.*
- Nota in basso: *L'LLM del 26 usa i vettori per generare; questo modello li usa per confrontare. Sono parenti (stessa architettura, stesso spazio delle idee), non la stessa cosa: un modello di embedding non scrive, e un LLM non è un buon motore di ricerca.*

**Visual**: `slide32-chunk-embedding.svg`.

**Prompt per schema SVG**:
> **A sinistra**, in miniatura e attenuata, la scena della slide 16 del 26: lo spazio delle idee con alcuni token vicini fra loro (citazione della figura, non una rispiegazione).
>
> **A destra**, la stessa scena a scala di chunk. Tre riquadri di testo etichettati `chunk`: `"penale del 2% oltre il terzo giorno"` · `"indennizzo per consegna oltre i termini"` · `"il carrello è stato svuotato"`. Ognuno ha una freccia verso un blocco `modello di chunk embedding`, e da lì esce un vettore (una freccia in uno spazio a due assi): i primi due vettori vicini, il terzo lontano. Dall'alto, la domanda `"che cosa prevede il contratto per i ritardi?"` entra nello stesso blocco e atterra vicino ai primi due; accanto, i tre punteggi `prodotto scalare: 0,82 · 0,79 · 0,11`.
>
> **Elemento focale**: i due vettori vicini che il modello ha imparato a mettere vicini pur non avendo parole in comune.

## Slide 33 — Cercare per significato: l'indice vettoriale

**Messaggio**: per cercare per significato si spezzano i documenti in chunk, si calcola un vettore per chunk, si mette tutto in un indice che trova i più vicini alla domanda. Trova ciò che le parole non trovano; perde ciò che non ha significato: codici, nomi, numeri.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Cercare per significato: l'indice vettoriale*
- Punti:
  1. **Il chunking**: *ogni documento va spezzato in chunk di qualche centinaio di token, con una sovrapposizione fra l'uno e l'altro perché una frase tagliata a metà non perda senso. Troppo piccoli: il chunk non dice da che contratto viene. Troppo grandi: il vettore diventa una media di tutto e non somiglia a nulla. È la prima decisione, e la più sottovalutata.*
  2. **L'indice**: *un vettore per chunk, milioni di vettori; la ricerca del più vicino esatta costerebbe un prodotto scalare per ciascuno, l'indice la approssima (ANN) e risponde in millisecondi. Lo offrono i database vettoriali dedicati, ma anche Postgres, Elasticsearch, DuckDB.*
  3. **Dove è cieco**: *"4471", "art. 7", "SpedFast": per il modello sono stringhe senza significato, e due codici diversi hanno vettori quasi uguali. Il cliente che chiede dell'ordine 4471 riceve il chunk dell'ordine 4417. È esattamente ciò che BM25 faceva bene.*
- Nota in basso: *Chunking e modello di embedding sono scelte di progetto, non impostazioni: cambiare l'uno o l'altro vuol dire rifare l'indice. Sono la KB della leva "Knowledge Base" del 27 (slide 40), letteralmente.*

**Visual**: `slide33-indice-vettoriale.svg`.

**Prompt per schema SVG**:
> Flusso da sinistra a destra. Un documento `contratto_SpedFast.pdf · 40 pagine` viene tagliato in chunk disegnati come rettangoli che si accavallano leggermente (la sovrapposizione è visibile); ogni chunk ha una freccia verso il blocco `modello di chunk embedding`, e da lì esce un vettore; i vettori entrano in un cilindro `indice vettoriale (ANN)`. Dall'alto, la domanda entra nello stesso blocco e poi nell'indice; dall'indice escono cinque chunk in colonna, ordinati, con il punteggio a fianco.
>
> In un angolo, la vignetta del cieco: `"ordine 4471"` → `chunk: ordine 4417 · 0,91` con un ✗.
>
> **Elemento focale**: i chunk che si accavallano, e la vignetta con il ✗.

## Slide 34 — Trovare è facile, ordinare è difficile

**Messaggio**: con parole e significato insieme si trovano cento candidati in un istante; il lavoro è decidere quali cinque contano. La somiglianza non basta: servono altri segnali, la data, la fonte, e l'autorità che un documento riceve da chi lo cita.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Trovare è facile, ordinare è difficile*
- Punti:
  1. **Hybrid: i due modi insieme**: *BM25 trova i nomi e i codici, l'indice vettoriale trova le parafrasi. Si lanciano entrambi, si fondono le due liste, e si tengono i primi cento. Retrieval largo e a basso costo: qui dentro la risposta c'è quasi sempre.*
  2. **Ma quale dei cento?**: *il primo per somiglianza è spesso una bozza mai firmata, un contratto scaduto, la mail che cita la clausola invece della clausola. La somiglianza dice "parla della stessa cosa", non "è la fonte giusta".*
  3. **I segnali oltre la somiglianza**: *la data (un contratto del 2026 batte uno del 2023); la fonte (la cartella dei contratti firmati batte la posta); e l'autorità: un documento che molti altri citano, linkano, allegano vale di più. È PageRank: i link sono voti, e chi riceve voti da chi ha voti pesa di più. Sul web ha fatto Google; in azienda vale sul grafo di chi cita chi.*
- Nota in basso: *La rilevanza è una somma pesata di segnali, e i pesi si imparano guardando che cosa gli utenti aprono davvero. È il retrieval come tool a sua volta AI del 27 (slide 48): si valuta a parte, con documenti attesi, non a sensazione.*

**Visual**: `slide34-relevance.svg`.

**Prompt per schema SVG**:
> **In alto**, due imbuti affiancati, `BM25` e `vettoriale`, che versano in un contenitore `100 candidati (hybrid)`.
>
> **Sotto**, quattro colonne di segnali che riordinano la lista: `somiglianza` · `data` · `fonte` · `autorità (link)`; in ciascuna, tre barre per tre candidati (`contratto 2026 firmato` · `bozza 2025` · `mail che lo cita`): nella colonna `somiglianza` vince la bozza; sommando le quattro colonne vince il contratto firmato. Accanto ad `autorità`, un mini-grafo di documenti con frecce (*chi cita chi*) in cui il nodo del contratto firmato è il più grande.
>
> **In fondo**, la lista finale `5 scelti`, con il contratto firmato al primo posto.
>
> **Elemento focale**: l'inversione fra la classifica per sola somiglianza e quella finale.

## Slide 35 — Reranking: il secondo passaggio

**Messaggio**: i cento candidati si rileggono con un modello più caro, che confronta domanda e chunk insieme invece di due vettori fatti separatamente; ne escono i cinque migliori. Due stadi: il primo largo ed economico, il secondo stretto e accurato.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Reranking: il secondo passaggio*
- Punti:
  1. **Perché un secondo passaggio**: *l'indice vettoriale confronta due vettori calcolati separatamente, la domanda senza sapere del chunk e il chunk senza sapere della domanda. È ciò che lo rende veloce su milioni, ed è ciò che lo rende approssimativo. Su cento candidati ci si può permettere di più.*
  2. **Il cross-encoder**: *domanda e chunk entrano insieme nello stesso transformer, e l'attention (il 26) li legge l'uno alla luce dell'altro: esce un solo numero, quanto quel chunk risponde a quella domanda. Cento chiamate, non milioni: costa, ma si può.*
  3. **ColBERT: la via di mezzo**: *un vettore per ogni token del chunk, calcolati prima e messi nell'indice; al momento della domanda ogni suo token cerca il token più simile nel chunk, e i punteggi si sommano (interazione tardiva). Quasi l'accuratezza del cross-encoder, quasi la velocità dell'indice: "4471" torna a contare come parola, perché ha il suo vettore.*
- Nota in basso: *La regola dei due stadi vale ovunque nella search: economico e largo per non perdere nulla, caro e stretto per scegliere bene. Nella sezione 6 il secondo stadio, a volte, è l'LLM stesso.*

**Visual**: `slide35-reranking.svg`.

**Prompt per schema SVG**:
> **In alto**, una pipeline orizzontale a imbuto: `milioni di chunk` → `stadio 1: hybrid (bi-encoder + BM25)` → `100 candidati` → `stadio 2: reranker` → `5 scelti`; le larghezze si stringono da sinistra a destra.
>
> **Sotto lo stadio 2**, due vignette affiancate: **`cross-encoder`**: un blocco transformer in cui `domanda + chunk` entrano insieme da un lato e un solo numero esce dall'altro (`0,94`); **`ColBERT`**: la domanda e il chunk come due file di token, ognuno con il suo piccolo vettore, e linee da ogni token della domanda al token più simile del chunk (fra cui `4471 ↔ 4471`), con un `Σ` in fondo.
>
> **In basso**, una scala di costo per i tre modi: `bi-encoder: 1 prodotto scalare` · `ColBERT: n × m confronti` · `cross-encoder: una chiamata al modello`.
>
> **Elemento focale**: lo stringersi dell'imbuto da milioni a cento a cinque.

## Slide 36 — La pagella del non strutturato, e la cerniera

**Messaggio**: la search rende il testo ricercabile, ma per chunk, non per fatti; gli altri tre requisiti restano dove la slide 28 li aveva trovati. E il testo non ha relazioni esplicite: che il contratto vincoli il corriere lo sa chi legge, non l'indice.

**Layout**: come le Slide 13 e 27: la pagella a sinistra (~45%) con voti e perché, regola del punto di vista sotto; a destra (~50%) la mini-mappa dello spettro con la colonna del documento spuntata e la colonna del grafo che si accende; blocco nero centrato in basso.

**Testo**:
- Titolo: *La pagella del non strutturato, e la cerniera*
- Pagella (HTML, `.pagella`), voti dal punto di vista di chi fa domande:
  1. **Ricercabile in modo progressivo**: **~** — *si trova il chunk, in cima se il ranking è buono; ma non si scende dal generale al particolare: non c'è un "totale per corriere" da cui partire, e per sapere se il chunk è la risposta bisogna leggerlo. Ricercabile, non interrogabile.*
  2. **Non ridondante**: **✗** — *le copie della slide 28: tre versioni del contratto, tutte nell'indice, tutte con lo stesso vettore. La search le trova tutte e tre; quale valga lo deve decidere qualcun altro.*
  3. **Veritiera**: **✗** — *l'indice non sa se un documento è in vigore, firmato, sostituito. Un chunk di una bozza pesa quanto uno del contratto. Senza un ciclo di vita gestito (sezione 7), la search è precisa su fonti di cui non si sa nulla.*
  4. **Compounding**: **✗** — *un documento nuovo non rende più utili i vecchi: si aggiunge all'indice, e basta. Il contratto e il reclamo che parlano della stessa spedizione non si agganciano: la relazione esiste nel mondo, non nell'archivio.*
- Regola sotto la pagella: *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Blocco nero centrato (la cerniera): *Il contratto vincola SpedFast; la spedizione 4471 è di SpedFast; il reclamo di Rossi riguarda la 4471. Tre fatti, in tre posti, che nessun indice collega: le relazioni esistono, ma nessuno le ha scritte. Scriverle, una per una, e percorrerle: sezione 5.*

**Visual**: la pagella in HTML + la mini-mappa dello spettro (`minimap` della Slide 7 con la colonna `documento` spuntata e la colonna `grafo` come elemento focale).
