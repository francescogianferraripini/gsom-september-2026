# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 1 — La conoscenza**
**Obiettivo di apprendimento**: il partecipante sa dire che cosa un agente trova dietro i tool, sa leggere la piramide dati → informazione → conoscenza → intelligenza e che cosa si aggiunge a ogni gradino, sa elencare i quattro requisiti di una conoscenza utile (e sa che sono quattro modi di dire "di qualità"), distingue know-what e know-how, e sa leggere lo spettro strutturato ↔ non strutturato come indice della lezione.
**Messaggio chiave (takeaway)**: La conoscenza c'è quasi sempre. Il problema è la forma in cui sta.
**Budget**: ~15 min, 7 slide + separatore. Copertina fuori sezione.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec1.html` | Separatore — Sezione 1: La conoscenza |
| `slides/slide1-ieri-oggi.html` | Slide 1 — Ieri chi esegue, oggi che cosa sa |
| `slides/slide2-formula-kb.html` | Slide 2 — La formula: oggi la KB |
| `slides/slide3-piramide.html` | Slide 3 — Dalla piramide: dati, informazione, conoscenza, intelligenza |
| `slides/slide4-requisiti.html` | Slide 4 — I quattro requisiti di una conoscenza utile |
| `slides/slide5-nome-della-rosa.html` | Slide 5 — Non è un problema dell'AI |
| `slides/slide6-know-what-know-how.html` | Slide 6 — Know-what e know-how |
| `slides/slide7-spettro.html` | Slide 7 — Lo spettro: dal dato strutturato al non strutturato |

---

> **Impianto della lezione (decisioni prese in intervista, 7–8 set 2026 — valgono per tutte le sezioni):**
>
> **Titolo di copertina**: *Agentic AI: dietro i tool, la conoscenza* (in rima con il 27, *Agentic AI: dentro l'harness*).
>
> **Sette sezioni, lungo lo spettro**: 1 La conoscenza · 2 Il dato strutturato, 1/2: dove nasce (relazionale e transazionale) · 3 Il dato strutturato, 2/2: dove si interroga (l'analitico) · 4 Il dato non strutturato: da analisi a search · 5 In mezzo allo spettro: i grafi · 6 Pattern agentici di accesso al dato · 7 Superare i limiti, e il know-how. Budget definitivo (8 set 2026): 7 / 6 / 14 / 9 / 6 / 10 / 8 = **60 slide**, più copertina e sette separatori; ~140 min come il 27. (La slide "Da Excel al data warehouse" è passata dalla sezione 2 alla 3; la sezione 4 ha guadagnato la slide "Dove sta il non strutturato".)
>
> **La 3 è un approfondimento della 2**, ed è dichiarato nei titoli (1/2 · 2/2) e in una slide-cerniera in chiusura della 2: il transazionale è dove il dato nasce e l'agente lo raggiunge attraverso i tool (il 27: dietro `cerca_ordine` c'è un DB transazionale, ma l'agente parla con l'API); l'analitico è dove il dato si interroga, ed è lì che l'agente entra da solo (Text2SQL funziona su uno star schema con nomi di business e metriche definite, non su duecento tabelle normalizzate). La struttura dell'analitico deriva sempre dal transazionale, soprattutto sul grano: la 2 è la premessa obbligata della 3.
>
> **La figura madre è la formula con `KB` esploso verso l'alto nello spettro** (Slide 7): i sei blocchi restano alle coordinate del 26 (contratto scritto nella spec del 26: nient'altro si muove); sopra `KB` si apre una callout con tre fasce (oggetti: tabella · grafo · documento; accesso: si interroga · si percorre · si cerca; pattern agentici: Text2SQL · GraphRAG · RAG/agentic search) e, sopra le fasce, la banda dell'ontologia. Nella Slide 2 la callout c'è già, con i tre blocchi in grigio e senza etichette; nella Slide 7 si accende. Ogni separatore delle sezioni 2–7 la ripropone in miniatura con la zona corrente accesa (2–3 la tabella, 4 il documento, 5 il grafo, 6 la fascia dei pattern, 7 la banda dell'ontologia). Gli estremi dello spettro si chiamano `strutturato` e `non strutturato`: le parole "dato" e "informazione" non si usano per gli estremi, perché la piramide (Slide 3) dà loro un altro significato.
>
> **Il grafo ha due ruoli**, e la lezione li tiene separati: (a) un modo di tenere i dati, il knowledge graph di istanze (Rossi, 4471, SpedFast), che sta **in mezzo** allo spettro ed è la sezione 5; (b) l'ontologia, un grafo di classi e relazioni che non contiene i dati ma ne documenta e arricchisce la semantica, per il dato strutturato come per il non strutturato: è la sezione 7 e nella figura madre sta **sopra** lo spettro, come strato che lo attraversa tutto. Stesso disegno, due livelli: uno parla delle cose, l'altro dei tipi di cose. **Tesi della sezione 5** (perché il grafo sta in mezzo): la struttura non va decisa tutta prima, si crea e si evolve nel tempo, un tipo di nodo o di relazione alla volta; ma ciò che c'è si percorre e si interpreta in modo deterministico e rigoroso, come una tabella.
>
> **La pagella dei requisiti** (Slide 4) è il dispositivo ricorrente: un componente HTML (`.pagella`) a quattro righe — *ricercabile in modo progressivo · non ridondante · veritiera · compounding* — con tre valori (✓ · ~ · ✗), nella stessa posizione in slide, che torna alla fine di ogni blocco: transazionale (sez. 2), analitico Kimball (sez. 3), search sul non strutturato (sez. 4), grafi (sez. 5), pattern agentici (sez. 6), ontologie e data as a product (sez. 7). La pagella della sezione 7 è la prima con quattro spunte. Equivalente della pipeline in miniatura della sezione 5 del 27. I quattro requisiti sono **quattro modi di dire "di qualità"**: il terzo è la qualità del dato in senso stretto, gli altri tre non si misurano sul singolo fatto ma contano altrettanto.
>
> **L'esempio che attraversa la lezione: Acme**, che cresce dal 26 e dal 27 (l'assistente clienti, `cerca_ordine`, l'ordine 4471, i corrieri SpedFast / Corriere Nord / PostaPro, `ordini_08.json`, la domanda della slide 20 del 27 "quanti ordini di agosto sono in ritardo, e per quale corriere?"). Sez. 2: il DB transazionale degli ordini (`ordini`, `clienti`, `prodotti`, `spedizioni`), quello che sta dietro `cerca_ordine`. Sez. 3: il DWH vendite, con il fatto `spedizioni` (o `righe ordine`) e le dimensioni cliente, prodotto, corriere, tempo. Sez. 4: i documenti: contratti con i corrieri, reclami, policy rimborsi. Sez. 5: il grafo cliente – ordine – spedizione – corriere – contratto – penale. Sez. 6: la stessa domanda della slide 20 del 27 rifatta via Text2SQL; "che cosa prevede il contratto con SpedFast sui ritardi?" via RAG; le due insieme (ritardi di SpedFast + penali del contratto) come caso che chiede grafo o agentic search.
>
> **Riprese dal 26 e dal 27**: stessa regola del 27 — citazione letterale della figura (stesso SVG o sua evoluzione con gli stessi elementi nella stessa posizione), eyebrow *dall'incontro 26* / *dall'incontro 27*, la slide dice solo che cosa cambia oggi, mai una rispiegazione. Le riprese decise: (1) formula, 26 slide 3 → Slide 2 (quarto stato) e chiusura; (2) i quattro requisiti, 27 slide 63 → Slide 4; (3) embeddings e prodotto scalare, 26 slide 13 e 16 → semantic search in sez. 4, **estendendo da token embedding a sentence/passage embedding** (simile ma non identico: un modello addestrato apposta a mettere vicine frasi che si rispondono, un vettore per chunk e non per token, la ricerca come prodotto scalare contro milioni di vettori); (4) tool ≠ API e "salva e cerca", 27 slide 18 → Text2SQL e RAG come tool, sez. 6; (5) RAG in due stadi, 27 slide 48 → sez. 6; (6) bash universale con lo script su `ordini_08.json`, 27 slide 20 → DuckDB nel sandbox, sez. 3 o 6; (7) context rot e tool a scalini, 26 slide 44–45 → "dieci chunk nella finestra", sez. 6; (8) la skill `rimborsi-acme` e "know-how, non know-what", 27 slide 26 → Slide 6 e sez. 7; (9) **in sospeso**: le tre domande della memoria più "chi la ripulisce", 27 slide 39 → memoria dell'agente e KB come stesso problema a scale diverse (era la slide-ponte tolta dal 27): entra solo se la formulazione è pulita.
>
> **Codice**: SQL, DDL e Cypher **sì, ma in riquadri corti** (3–6 righe) nell'idioma dei riquadri monospaziati del 26/27, mai a piena slide, sempre con la lettura in italiano a fianco: un `CREATE TABLE` breve per tabelle, tipi, PK e FK (sez. 2) e uno per fatto e dimensione (sez. 3), da saltare a voce se il tempo stringe; una `SELECT … JOIN … GROUP BY` sul transazionale (sez. 2); la query star schema con il fanout sbagliato accanto a quella corretta con subquery (sez. 3); una `MATCH` Cypher contro la stessa domanda in SQL con tre self-join (sez. 5); il SQL generato dal Text2SQL, giusto e sbagliato (sez. 6).
>
> **Storia**: una slide sola, in sez. 1, con *Il nome della rosa* (Slide 5) e l'immagine originale della pianta del labirinto. Dewey, Hoover, Bush, Otlet escono dalle slide; Eulero e Berners-Lee restano in sez. 5 come una riga di apertura. La ricerca verificata sta in `docs/ricerche-28/research-storia-classificazione.md` (per le note del relatore).
>
> **Know-how (sez. 7)**: una slide-placeholder sola (Slide 59), con la ripresa di "know-how, non know-what" dal 27 e lo spazio per una demo dal vivo sul repo Quantyca, se c'è tempo. Niente frontmatter inventati, niente ontologie-per-governance in slide. Seconda demo possibile nella Slide 56: l'ontologia di Quantyca e il suo semantic linking alle tabelle.
>
> **Nessun modello è un silver bullet** (deciso nella sezione 5, Slide 41): il data warehouse per somme e metriche, il documentale ben organizzato per testi e clausole, il grafo per relazioni e percorsi; ciò che converge è il significato (sezione 7), non la forma.
>
> **Chiusura (sez. 7)**: una slide sola, la formula con i sei blocchi accesi, `Harness` esploso nella mappa in miniatura del 27 (tre zone, anelli, fascia di observability) e `KB` esploso nello spettro. Nessun blocco nero, nessun cliffhanger.
>
> **Piramide (Slide 3)**: viene dal deck Quantyca *Information Architecture — Podcast Knowledge Management* (21 maggio 2025; 15 slide, 5 nascoste): piramide DATI → INFORMAZIONE → CONOSCENZA → INTELLIGENZA, a sinistra *contesto · semantica · azioni*, a destra *+ metadati · + relazioni · + algoritmi*, esempio meteo (`31 32 33 …` → tabella Milano luglio 2024 → knowledge graph Food Corp/Weather → bot); tesi "il Data Management non si limita alla gestione dei puri dati; salire di livello rende i dati riutilizzabili". Qui l'esempio è rifatto su Acme; il meteo si cita a voce come origine. Nella slide il gradino della conoscenza è **solo l'ontologia**.
>
> **SVG**: markup diretto (a mano o via `svg-generator`), niente generatori Python di default. Deck e SVG non si producono in questa fase.

---

## Slide 1 — Ieri chi esegue, oggi che cosa sa

> Ripresa della slide 63 del 27 (*Dietro i tool, la conoscenza*). Stessa struttura della slide 1 del 27: tre righe di ripresa, una riga staccata, la domanda in burgundy, il blocco nero. Il titolo è in rima con la slide 1 del 27 (*Ieri il modello, oggi chi esegue*): la serie dei tre incontri si legge dai soli titoli.

**Messaggio**: il 26 ha aperto il modello, il 27 l'harness; la domanda lasciata aperta è che cosa l'agente trova quando chiama un tool. Oggi si apre quella porta.

**Layout**: titolo in alto; tre righe di ripresa al centro-sinistra, allineate come un elenco che si conclude; sotto, staccata, la riga sui sistemi e la domanda in burgundy; il blocco nero centrato in basso (classe `.nota.dark.center`). Nessuna figura. Eyebrow *dall'incontro 27*.

**Testo**:
- Eyebrow: *SEZIONE 1 · LA CONOSCENZA*
- Titolo: *Ieri chi esegue, oggi che cosa sa*
- Le tre righe di ripresa:
  1. **Il 26, il modello**: *sa volere, non sa eseguire. Ciò che sa è compresso nei pesi, fermo al cut-off.*
  2. **Il 27, l'harness**: *prepara la finestra, esegue i tool, governa il contesto, osserva le tracce.*
  3. **La domanda lasciata aperta**: *quando l'agente chiama `cerca_ordine`, o `cerca_documenti`, che cosa trova dall'altra parte?*
- Riga staccata: *Quasi tutto ciò che l'agente deve sapere non sta nei suoi pesi e non lo scrive lui: sta nei sistemi dell'organizzazione. Dati, documenti, procedure, in forme diverse, fatte per lettori diversi.*
- Domanda (in burgundy): **In che forma sta, e chi ce l'ha messa?**
- Blocco nero centrato: *L'agente legge tutto ciò che trova. Oggi: che cosa trova, e come dev'essere fatto perché gli serva.*

**Visual**: nessuno. La sequenza "tre righe chiuse, una domanda aperta" è la struttura visiva, come nella slide 1 del 27.

## Slide 2 — La formula: oggi la KB

> Ripresa della slide 3 del 26 (e della 62 del 27). Quarto stato della formula lungo il corso: 26 `LLM`; 27 `Harness`, poi `System Prompt`, `Tools`, `Skills`; 28 `KB`. Stessa figura, stesso viewBox per la fila dei blocchi; il canvas cresce solo verso l'alto.

**Messaggio**: cinque termini aperti in due incontri; oggi si apre l'ultimo, e il modo in cui si apre è un'espansione, non una spunta: la KB non è un blocco, è uno spettro.

**Layout**: titolo in alto; diagramma protagonista al centro (~70%); nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *La formula: oggi la KB*
- Formula (nel visual): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Nota in basso: *L'LLM è la CPU, l'harness il sistema operativo, il resto il software installato. Del software abbiamo aperto tre programmi su quattro. Il quarto è quello che gli altri tre consultano: senza, `cerca_ordine` non ha nulla da cercare e la skill `rimborsi-acme` non ha nulla da verificare.*

**Visual**: `slide2-formula-kb.svg` — la figura del 26 alle stesse coordinate, con lo stato dei blocchi cambiato e la callout sopra `KB`.

**Prompt per schema SVG**:
> La figura è quella della slide 3 dell'incontro 26, ripresa senza spostare nulla: blocco `Agent`, segno `=`, sei blocchi in fila separati da `+`, ognuno con la glossa sotto, e le tre graffe *la CPU* / *il sistema operativo* / *il software installato*.
>
> Stato dei blocchi: `LLM` attenuato con un piccolo segno di spunta e l'etichetta *incontro 26*; `Harness`, `System Prompt`, `Tools`, `Skills` attenuati con la spunta e l'etichetta condivisa *incontro 27*; `KB` pieno, in evidenza, unico blocco acceso.
>
> **Sopra `KB`** si apre una callout (un riquadro collegato al blocco da un breve raccordo, come un fumetto che esce dal blocco), larga quanto la fila dei sei blocchi. Dentro, **tre blocchi in fila, in grigio, attenuati, senza etichette**: sono la sagoma dello spettro (strutturato · grafo · non strutturato) che la Slide 7 accenderà. Nessun testo nella callout. Il canvas cresce solo verso l'alto per far posto alla callout; la geometria dei blocchi e delle graffe non cambia.
>
> **Elemento focale**: il blocco `KB` acceso e la callout che ne esce. La lettura da lontano deve essere: cinque fatti, uno acceso, e l'acceso si apre.

## Slide 3 — Dalla piramide: dati, informazione, conoscenza, intelligenza

> Dal deck Quantyca *Information Architecture — Podcast Knowledge Management* (2025), con l'esempio rifatto su Acme. Slide a **quattro tempi** (fragment reveal.js, pattern `.visual.stack` come la torre della slide 19 del 26): a ogni tempo si accende un livello e appare il suo esempio.

**Messaggio**: gli stessi numeri diventano informazione, conoscenza e infine azione aggiungendo ogni volta una cosa precisa: contesto, semantica, azioni. Un agente vive in cima: i tre gradini sotto vanno costruiti, e sono la lezione.

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~35%), uno per tempo, che si accendono con il livello corrispondente; visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Dalla piramide: dati, informazione, conoscenza, intelligenza*
- Punti (uno per tempo):
  1. **Dati**: *numeri e stringhe senza contesto: `3 5 2 0 4 1 3`. Veri, e inutilizzabili.*
  2. **+ contesto → informazione**: *gli stessi numeri con intestazioni, unità e chiavi: giorni di ritardo, per corriere, per settimana. È la tabella: sezioni 2 e 3.*
  3. **+ semantica → conoscenza**: *le relazioni esplicite fra i tipi di cose: il corriere consegna la spedizione, il contratto vincola il corriere, il ritardo attiva la penale. È l'ontologia: il grafo che spiega tabelle e documenti. Sezione 7.*
  4. **+ azioni → intelligenza**: *qualcuno che usa la conoscenza per agire: l'agente, con i suoi tool e i suoi pattern di accesso. Sezione 6.*
- Nota in basso: *Gestire i dati non basta: ogni gradino in più rende ciò che sotto c'è già riutilizzabile, da una persona e da un agente. Dalla presentazione Quantyca "Information Architecture", 2025.*

**Visual**: `slide3-piramide-{1..4}.svg` — la piramide in quattro tempi, stesso viewBox.

**Prompt per schema SVG**:
> **A sinistra della figura, la piramide** a quattro livelli, dal basso: `DATI` (base larga) · `INFORMAZIONE` · `CONOSCENZA` · `INTELLIGENZA` (apice). Sul fianco sinistro della piramide tre frecce piegate che salgono da un livello al successivo, ciascuna con l'etichetta di ciò che si aggiunge: `contesto` (dati → informazione) · `semantica` (informazione → conoscenza) · `azioni` (conoscenza → intelligenza). Sul fianco destro, in corrispondenza degli stessi tre passaggi, un piccolo cerchio con `+` e l'etichetta di ciò che lo implementa: `+ metadati` · `+ relazioni` · `+ algoritmi`.
>
> **A destra della piramide, l'esempio Acme**, un elemento allineato a ogni livello, che compare al tempo corrispondente:
> 1. accanto a `DATI`: una striscia di sette celle con i soli numeri `3 · 5 · 2 · 0 · 4 · 1 · 3`;
> 2. accanto a `INFORMAZIONE`: una tabella con intestazione `Ritardi di consegna` e colonne `giorni di ritardo · corriere · settimana · regione`, con cinque righe (gli stessi numeri della striscia, con `SpedFast`, `Corriere Nord`, `PostaPro`, settimane `35`–`36`, regioni `Lombardia`, `Lazio`, `Veneto`);
> 3. accanto a `CONOSCENZA`: un grafo di **classi** (ellissi) con relazioni etichettate: `Cliente –ordina→ Ordine`, `Ordine –spedito con→ Spedizione`, `Spedizione –consegnata da→ Corriere`, `Contratto –vincola→ Corriere`, `Spedizione –ha→ Ritardo`, `Ritardo –attiva→ Penale`, `Penale –prevista da→ Contratto`. Nessuna istanza: sono i tipi di cose. Etichetta sotto il grafo: *l'ontologia*;
> 4. accanto a `INTELLIGENZA`: la pill dell'agente (l'idioma del 26 per ciò che il modello genera) con dentro `→ "quanti ordini in ritardo, per corriere, e che cosa prevede il contratto?"` e, in piccolo, l'icona di una persona accanto all'agente.
>
> **Quattro tempi**: al tempo 1 solo `DATI` e la striscia sono pieni, il resto in sagoma attenuata; a ogni tempo si accende il livello successivo con la sua freccia, il suo `+` e il suo esempio; al tempo 4 tutto è acceso.
>
> **Elemento focale**: a ogni tempo, il livello che si accende e la freccia che lo raggiunge. Al tempo 4, la pill dell'agente in cima e i tre gradini pieni sotto di lei.

## Slide 4 — I quattro requisiti di una conoscenza utile

> Ripresa della riga in burgundy della slide 63 del 27 (i quattro requisiti, anticipati). Qui nasce la **pagella**, il dispositivo ricorrente della lezione.

**Messaggio**: una conoscenza serve, a una persona come a un agente, se ha quattro proprietà, e sono quattro modi di dire "di qualità"; sono i criteri con cui giudicheremo ogni modo di tenere i dati, da qui alla fine.

**Layout**: titolo in alto; sottotitolo sotto il titolo; le quattro righe a sinistra (~60%); a destra (~35%) la pagella in HTML, vuota; nessuna nota in basso. Eyebrow *dall'incontro 27*.

**Testo**:
- Titolo: *I quattro requisiti di una conoscenza utile*
- Sottotitolo: *Quattro modi di dire "di qualità". Il terzo è quello che si intende di solito; gli altri tre non si misurano sul singolo fatto, ma contano altrettanto.*
- Le quattro righe:
  1. **Ricercabile in modo progressivo**: *qualità dell'accesso: si arriva a ciò che serve per passi, dal generale al particolare, senza leggere tutto. L'agente ha una finestra limitata: trova il contratto SpedFast, poi la clausola sui ritardi, poi la penale, non l'archivio intero.*
  2. **Non ridondante**: *qualità della struttura: un fatto sta in un posto solo. Se il ritardo di una spedizione è calcolato in tre report con tre regole, un agente ne trova tre valori diversi e non sa quale sia vero.*
  3. **Veritiera**: *la qualità del dato in senso stretto: accurata, completa, aggiornata, con un responsabile. Un listino del 2024 senza data è una risposta sbagliata pronta per essere data.*
  4. **Compounding**: *qualità nel tempo: ogni aggiunta rende più utile ciò che c'era già, perché si aggancia a ciò che esiste invece di rifarlo. Il contrario: un'altra pipeline, un altro report, un'altra copia.*
- Pagella (HTML, classe `.pagella`): quattro righe con l'etichetta breve — *ricercabile in modo progressivo* · *non ridondante* · *veritiera* · *compounding* — e una casella vuota ciascuna. Legenda in piccolo sotto: `✓ sì · ~ in parte · ✗ no`.

**Visual**: nessun SVG. La pagella in HTML è il componente che torna alla fine di ogni blocco (sez. 2, 3, 4, 5, 6, 7) con le caselle riempite; qui è vuota.

## Slide 5 — Non è un problema dell'AI

> L'unica slide storica della lezione. La ricerca di supporto (Dewey, Hoover, Bush, Otlet, Eulero, Berners-Lee) sta in `docs/ricerche-28/research-storia-classificazione.md`, per le note del relatore.

**Messaggio**: organizzare la conoscenza perché si trovi è un problema vecchio di secoli; l'AI non l'ha creato, l'ha reso evidente, perché un agente legge tutto e fallisce dove una persona si arrangiava.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~45%); a destra (~50%) l'immagine della pianta del labirinto, con la didascalia sotto; nessuna nota in basso.

**Testo**:
- Titolo: *Non è un problema dell'AI*
- Punti:
  1. **La biblioteca dell'abbazia**: *tutto il sapere del mondo c'è, in una torre. Ma è un labirinto, e la mappa è nella testa del bibliotecario: i libri si trovano solo chiedendo a lui, e lui decide che cosa si può leggere.*
  2. **Che cosa manca**: *non i libri. Manca un ordine che chiunque possa percorrere: la conoscenza c'è, ma non è ricercabile, e muore con chi la custodisce.*
  3. **L'AI l'ha reso evidente**: *finché a cercare era una persona, si arrangiava: chiedeva al collega, sapeva quale report era quello buono. Un agente non ha il collega: legge ciò che trova, tutto, e con lo stesso peso. Ogni disordine che una persona aggirava diventa una risposta sbagliata.*
- Didascalia dell'immagine: *La pianta del labirinto, dall'edizione Bompiani del 1980. Ogni stanza porta una lettera; lette in fila, le lettere compongono il nome della regione da cui vengono i libri (HIBERNIA, YSPANIA, LEONES…): dentro il labirinto c'è già l'abbozzo di un'organizzazione, per provenienza. Non basta, ma è un inizio.*

**Visual**: l'immagine originale della pianta del labirinto della biblioteca de *Il nome della rosa* (Umberto Eco, Bompiani 1980); nessun SVG. **Da reperire in fase di deck**: prima di scaricarla, indicare al docente fonte, nome file e dimensione; in slide va con attribuzione (autore, edizione), salvata in `assets/images/uploads/`.

## Slide 6 — Know-what e know-how

> Ripresa del punto 3 della slide 26 del 27 (*Know-how, non know-what*), che rimandava a oggi.

**Messaggio**: nella formula ci sono due termini per la conoscenza, e non è un caso: la KB dice come stanno le cose, la skill dice come si fa. Oggi quasi tutto il tempo va al primo; il secondo chiude la lezione.

**Layout**: titolo in alto; due colonne che occupano il corpo (~60%), con a lato di ciascuna, sbiadito, il blocco della formula corrispondente (`KB`, `Skills`); una riga sotto le colonne; nota in basso. Eyebrow *dall'incontro 27*.

**Testo**:
- Titolo: *Know-what e know-how*
- Colonna 1 — **Know-what: la KB**: *ciò che l'organizzazione sa: quanti ordini, quali clienti, che cosa dice il contratto con SpedFast. Sta in tabelle, documenti, grafi; l'agente lo raggiunge con i tool. È ricercabile: la domanda è in che forma.*
- Colonna 2 — **Know-how: le skill**: *ciò che l'organizzazione sa fare: come si gestisce un rimborso, come si scrive il report della settimana. Sta in procedure scritte da chi il lavoro lo sa fare; l'agente lo carica a richiesta (il 27: `rimborsi-acme`). È eseguibile: la domanda è chi lo scrive.*
- Riga sotto le colonne: *La skill del 27 chiamava `cerca_ordine` e `crea_rimborso`: il know-how usa il know-what. Senza il primo, il secondo non ha su che cosa lavorare.*
- Nota in basso: *Oggi: sezioni 2–6 sul know-what, la 7 sul know-how e su ciò che li lega.*

**Visual**: nessuno. Le due colonne sono la struttura; i due blocchi della formula a lato sono HTML (o ritagli dell'SVG della Slide 2), non una figura nuova.

## Slide 7 — Lo spettro: dal dato strutturato al non strutturato

> La **figura madre** della lezione: la callout grigia della Slide 2 si accende. I separatori delle sezioni 2–7 la riprendono in miniatura con la zona corrente accesa.

**Messaggio**: il know-what sta su uno spettro, dal dato strutturato al non strutturato, con i grafi in mezzo; a ogni punto dello spettro corrisponde un modo di accedere e un pattern agentico; sopra tutto, l'ontologia. È l'indice della lezione.

**Layout**: titolo in alto; la figura occupa quasi tutta la slide (~80%), come la mappa dell'harness nella slide 4 del 27; didascalia in basso.

**Testo**:
- Titolo: *Lo spettro: dal dato strutturato al non strutturato*
- Didascalia: *A un capo il dato strutturato: la struttura è decisa prima di scrivere, e il fatto sta in una cella; si interroga. All'altro il dato non strutturato: la struttura non c'è, e il fatto va estratto dal testo; si cerca. In mezzo il grafo, e sta in mezzo per una ragione precisa: la struttura non va decisa tutta prima, si crea e si evolve nel tempo, un tipo di nodo o di relazione alla volta; ma ciò che c'è si percorre e si interpreta in modo deterministico e rigoroso, come una tabella. Sopra tutto, l'ontologia: non tiene i dati, ne spiega il significato, da un capo all'altro.*

**Visual**: `slide7-spettro.svg` — la formula della Slide 2 con la callout accesa.

**Prompt per schema SVG**:
> **Nella metà inferiore**, la formula della Slide 2 (stessa geometria della slide 3 del 26): tutti i blocchi attenuati tranne `KB`, acceso. Da `KB` esce verso l'alto la stessa callout della Slide 2, ora piena.
>
> **Dentro la callout, tre fasce orizzontali**, allineate su tre colonne:
> - fascia **oggetti** (in alto): tre blocchi in fila, `Dato strutturato: la tabella` · `Grafo: le relazioni` · `Dato non strutturato: il documento`; sotto i tre blocchi, una freccia bidirezionale a tutta larghezza con agli estremi le sole parole `strutturato` (a sinistra) e `non strutturato` (a destra);
> - fascia **accesso** (in mezzo): sotto ciascun blocco il verbo, `si interroga (query)` · `si percorre (traversal)` · `si cerca (search)`;
> - fascia **pattern agentici** (in basso): sotto ciascun verbo il pattern, `Text2SQL` · `GraphRAG` · `RAG · agentic search`.
>
> **Sopra le tre fasce**, dentro la callout, una banda sottile a tutta larghezza etichettata `Ontologia: il significato, da un capo all'altro`, disegnata come un piccolo grafo di classi steso in orizzontale (poche ellissi collegate da archi etichettati, es. `Corriere –consegna→ Spedizione`), che tocca tutte e tre le colonne e non appartiene a nessuna.
>
> Le parole "dato" e "informazione" non compaiono come etichette degli estremi. Nessun numero di sezione dentro la figura.
>
> **Elemento focale**: la fascia degli oggetti con la freccia `strutturato ↔ non strutturato`. Secondo elemento: la banda dell'ontologia sopra, che attraversa tutto.

> **Mini-mappe dei separatori** (`minimap-secN.svg`, da fare in fase di deck): silhouette di questa figura con la zona corrente accesa: sez. 2 e 3 la colonna della tabella (la 3 con uno zoom sul blocco), sez. 4 la colonna del documento, sez. 5 la colonna del grafo, sez. 6 la fascia dei pattern agentici, sez. 7 la banda dell'ontologia.
