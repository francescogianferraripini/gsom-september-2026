# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 1 — Tutto ciò che non è il modello**
**Obiettivo di apprendimento**: il partecipante sa dire perché un LLM da solo non è un agente, sa leggere la mappa dell'harness (le tre zone, la fascia di observability, i tre anelli) e sa che cosa fa un giro del loop agentico.
**Messaggio chiave (takeaway)**: Il modello sa volere. L'harness è tutto ciò che serve perché quella volontà diventi un task completato.
**Budget**: ~13 min, 6 slide + separatore. Copertina fuori sezione.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec1.html` | Separatore — Sezione 1: Tutto ciò che non è il modello |
| `slides/slide1-ieri-oggi.html` | Slide 1 — Ieri il modello, oggi chi esegue |
| `slides/slide2-aspettative-requisiti.html` | Slide 2 — Dalle aspettative ai requisiti |
| `slides/slide3-formula-harness.html` | Slide 3 — La formula: oggi il sistema operativo |
| `slides/slide4-mappa-harness.html` | Slide 4 — La mappa dell'harness |
| `slides/slide5-tre-anelli.html` | Slide 5 — I tre anelli: dove si infila il loop agentico |
| `slides/slide6-harness-minimo.html` | Slide 6 — L'harness più semplice possibile |

---

> **Impianto della lezione (decisioni prese in intervista, 4 set 2026 — valgono per tutte le sezioni):**
>
> **Le sette sezioni seguono la mappa dell'harness** (la slide 4 del 26, estesa nella Slide 4 di questa lezione): 1 Apertura e anello · 2 Context Initialization · 3 Environment management · 4 Context management a runtime · 5 Observability · 6 Orchestrazione · 7 L'offerta di harness. Budget: 6 / 8 / 14 / 11 / 11 / 7 / 6 = **63 slide**, ±2 per sezione. Ogni separatore ripropone la mappa in miniatura con la zona corrente accesa (mini-mappa "sei qui", come le `minimap-*` della sezione 3 del 26).
>
> **La mappa estesa**: tre zone del 26 (`Context management` teal, `Agentic loop management` lightblue, `Environment management` giallo) attorno all'`LLM`, con: i **tre anelli concentrici** al posto dell'anello singolo; `Context Initialization` aperta in tre sottoblocchi (`System prompt: ruolo e regole` · `Dichiarazione dei tool: nativi e via MCP` · `Skill initialization: indice nome + descrizione`); `Skill management` rinominato **`Skill progressive disclosure (runtime)`**; una **fascia trasversale `Observability`** sotto le tre zone, con quattro sottoblocchi `Tracing · Logging · Metrics · Eval`. MCP non è un blocco: le sue definizioni entrano in Context Initialization, le sue chiamate in Tool Calling execution. Nessun numero di sezione dentro la figura.
>
> **Riprese dal 26**: sempre **citazione letterale della figura** (stesso SVG o sua evoluzione con gli stessi elementi nella stessa posizione) e la slide dice solo che cosa cambia oggi; mai una rispiegazione. Eyebrow *dall'incontro 26*. Undici figure candidate: 1 (post-it), 3 (formula), 4 (esoscheletro), 39 (anelli), 9 (i due giri con la riga `[tool]`), 42 (la pila che cresce), 40 (KV cache), 41 (curve di costo), 44 (context rot), 45 (tool a scalini), 38 (traiettorie premiate), 50 (valore delle traiettorie).
>
> **La formula come avanzamento del corso**: il diagramma della slide 3 del 26 (`Agent = LLM + Harness + System Prompt + Tools + KB + Skills`, sei blocchi fermi, tre graffe *la CPU / il sistema operativo / il software installato* — applicate sul 26 il 4 set 2026) si riaccende progressivamente: 26 chiusura `LLM`; 27 apertura `Harness`; 27 chiusura anche `System Prompt`, `Tools`, `Skills`; 28 `KB`.
>
> **Metafore del 26**: nessuna riportata di default; le propone il docente quando servono.
>
> **Idioma dei pezzi veri**: payload, messaggi e tracce reali ma corti (solo i campi che insegnano qualcosa, mai un JSON intero), nell'idioma dei riquadri con tag `[system] / [user] / [assistant] / [tool]` fissato nella sezione 2 del 26 (righe ereditate sbiadite, pill burgundy per ciò che il modello genera adesso, `[tool]` in teal perché non l'ha scritta il modello). Lo pseudocodice compare **una sola volta**, nella Slide 6. Monospaziato solo per ciò che è token/codice.
>
> **SVG**: markup diretto (a mano o via `svg-generator`), niente generatori Python di default; se per una famiglia di figure un generatore avesse senso, si chiede al docente.
>
> **Chiusura (sezione 7)**: formula riletta con tutto acceso tranne `KB` + cliffhanger sul 28.

---

## Slide 1 — Ieri il modello, oggi chi esegue

**Messaggio**: il 26 ha spiegato che cosa il modello sa fare e come impara a *volere* un tool; oggi si guarda tutto il resto, cioè chi trasforma quella volontà in un task completato.

**Layout**: titolo in alto; tre righe di ripresa al centro-sinistra, allineate come un elenco che si conclude; sotto, staccata, la riga sull'attesa e la domanda in burgundy; il blocco nero centrato in basso (classe `.nota.dark.center`, quella delle slide 1 e 10 del 26). Nessuna figura.

**Testo**:
- Eyebrow: *SEZIONE 1 · TUTTO CIÒ CHE NON È IL MODELLO*
- Titolo: *Ieri il modello, oggi chi esegue*
- Le tre righe di ripresa:
  1. **Cosa sa**: *conoscenza compressa nei pesi, ferma al cut-off.*
  2. **Come genera**: *un token alla volta, rileggendo tutto il contesto, stateless.*
  3. **Come impara a volere un tool**: *RL sulle traiettorie: la tool call è testo, e il modello si ferma ad aspettare.*
- La riga sull'attesa (staccata): *Il modello è una funzione dietro un endpoint: si aspetta di essere chiamato, e di esserlo di nuovo con il risultato. Ma finché un processo non lo chiama, non gira e non fa nulla.*
- La domanda (in burgundy): **Chi lo chiama, chi esegue, chi lo richiama?**
- Blocco nero centrato: *Il modello sa volere. Non sa eseguire. Oggi: tutto ciò che sta intorno.*

**Visual**: nessuno. La sequenza "tre righe chiuse, una riga aperta" è la struttura visiva; gli anelli tornano nella Slide 5.

## Slide 2 — Dalle aspettative ai requisiti

> Ripresa della slide 1 del 26 (i post-it). Slide a **due tempi** (fragment reveal.js): prima i post-it sparsi come nel 26, al click si riordinano nelle tre colonne e compaiono le intestazioni.

**Messaggio**: le aspettative del 26 non erano desideri: sono requisiti, e ognuno esiste nell'harness sotto forma di un pezzo preciso.

**Layout**: titolo in alto; tre colonne che occupano il corpo, ognuna con in testa il requisito e sotto i post-it del 26 che vi si riconducono (stesso stile post-it del 26, ora allineati); in fondo a ogni colonna, in burgundy, il pezzo di harness che risponde; due post-it fuori colonna, sbiaditi; nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *Dalle aspettative ai requisiti*
- Colonna 1 — **Autonomia**: *"Che faccia da solo, senza che io lo guidi passo passo"* · *"Che usi i miei strumenti: mail, file, gestionali"* · *"Che sostituisca una persona"* → **il loop e i tool**
- Colonna 2 — **Affidabilità**: *"Che non sbagli mai"* · *"Che si accorga quando sbaglia, e ci riprovi"* → **errori come feedback, sandbox**
- Colonna 3 — **Verificabilità**: *"Che sappia spiegarmi cosa ha fatto e perché"* → **observability: tracce, eval**
- Fuori colonna, sbiaditi: *"Un chatbot, ma più intelligente"* · *"Che risponda a qualsiasi domanda"* (le ipotesi naïf: il 26 le ha già superate)
- Nota in basso: *Sono le ragioni per cui esistono loop, sandbox e logging. Non funzioni "in più": è l'harness che rende un modello un agente.*

**Visual**: nessuno. Le tre colonne di post-it sono la struttura, in HTML come nel 26.

## Slide 3 — La formula: oggi il sistema operativo

> Ripresa della slide 3 del 26. Stessa figura, stesso viewBox: cambia solo lo stato dei blocchi. È il secondo dei quattro stati della formula lungo il corso (vedi *Impianto*).

**Messaggio**: il 26 ha aperto il primo termine; oggi si apre il secondo, il sistema operativo, e tutto ciò che il modello "vuole" passa da lì.

**Layout**: titolo in alto; diagramma protagonista al centro (~65%); nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *La formula: oggi il sistema operativo*
- Formula (nel visual): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Nota in basso: *L'LLM è la CPU: calcola, non decide che cosa gira. L'harness è il sistema operativo: chiama la CPU, le mette davanti la memoria, esegue l'I/O. Oggi apriamo il sistema operativo, e con lui tre pezzi del software installato.*

**Visual**: `slide3-formula-harness.svg` — `slide3-formula-agent.svg` del 26 con la sola opacità dei blocchi cambiata.

**Prompt per schema SVG**:
> La figura è quella della slide 3 dell'incontro 26, ripresa senza spostare nulla: blocco `Agent`, segno `=`, sei blocchi in fila separati da `+`, ognuno con la glossa sotto, e le tre graffe *la CPU* / *il sistema operativo* / *il software installato*.
>
> Cambia solo lo stato dei blocchi: `LLM` attenuato con un piccolo segno di spunta e l'etichetta *incontro 26*; `Harness` pieno, in evidenza, unico elemento focale; `System Prompt`, `Tools`, `Skills` con riempimento in tinta leggera e l'etichetta condivisa *oggi*; `KB` attenuato con l'etichetta *incontro 28*.
>
> **Elemento focale**: il blocco `Harness`. La lettura da lontano deve essere: uno fatto, uno acceso, tre in arrivo, uno che aspetta.

## Slide 4 — La mappa dell'harness

> Ripresa della slide 4 del 26, **estesa**: è la figura madre della lezione. Ogni separatore di sezione la ripropone in miniatura con la zona corrente accesa.

**Messaggio**: l'harness ha una struttura, ed è l'indice della lezione: tre zone attorno all'anello, una fascia sotto, e i problemi si presentano in quest'ordine.

**Layout**: titolo in alto; la figura occupa quasi tutta la slide (~80%), come la torre della slide 20 del 26; didascalia in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *La mappa dell'harness*
- Didascalia: *La figura dell'incontro 26, con ciò che oggi si aggiunge: i tre anelli del loop, gli strati dell'inizializzazione, la fascia di observability. L'ordine delle sezioni segue l'ordine in cui i problemi si presentano: prima si prepara la finestra, poi si esegue, poi la finestra cresce, poi si guarda che cosa è successo.*

**Visual**: `slide4-mappa-harness.svg` — evoluzione di `slide4-ruolo-harness.svg` del 26 (viewBox `0 0 1000 714`, da allargare in basso per la fascia).

**Prompt per schema SVG**:
> Riprende l'esoscheletro della slide 4 dell'incontro 26 senza spostare le zone esistenti: al centro il blocco `LLM` (*la CPU*), intorno le tre zone contigue che formano la cornice, ognuna con la propria intestazione.
>
> **`Agentic loop management`**: al posto dell'anello singolo, **tre anelli concentrici** attorno all'`LLM`, etichettati dall'interno: `1° loop · generazione (fino a STOP)`, `3° loop · task (giro dopo giro di tool call)`, `2° loop · conversazione (turno dopo turno)`. L'ordine degli anelli è l'annidamento, non la numerazione: il 3° sta in mezzo, ed è questo che la figura deve far vedere.
>
> **`Context management`**, con `Context Initialization` che si apre in tre sottoblocchi impilati: `System prompt: ruolo e regole` · `Dichiarazione dei tool: nativi e via MCP` · `Skill initialization: indice nome + descrizione`; poi `Context Optimization (compaction, pruning, offload)` · `Memory management` · `Skill progressive disclosure (runtime)`.
>
> **`Environment management`**, invariata: `Tool Calling execution and response management` · `Execution Sandbox` · `Skill execution management`.
>
> **Sotto le tre zone**, una **fascia orizzontale** a tutta larghezza, `Observability`, con quattro sottoblocchi affiancati: `Tracing` · `Logging` · `Metrics` · `Eval`. È trasversale: tocca tutte e tre le zone e non appartiene a nessuna.
>
> Nessun numero di sezione dentro la figura.
>
> **Elemento focale**: i tre anelli. Il secondo elemento è la fascia nuova in basso. I nomi delle zone e dei sottoblocchi sono etichette esatte, da non parafrasare.

## Slide 5 — I tre anelli: dove si infila il loop agentico

> Ripresa della slide 39 del 26 (i tre anelli). Non è un doppione della Slide 4: là gli anelli stanno nel contesto della mappa, qui si spiegano.

**Messaggio**: il 3° loop non si aggiunge in coda, si infila in mezzo: dentro un turno di conversazione, N giri di tool call, ognuno con dentro una generazione.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *I tre anelli: dove si infila il loop agentico*
- Punti:
  1. **1° loop, la generazione**: *un token alla volta, fino a STOP. Lo fa il modello; la sua unica volontà è il prossimo token.*
  2. **2° loop, la conversazione**: *turno dopo turno, la storia rispedita per intero. Lo fa un chatbot: al modello non serve altro che essere richiamato.*
  3. **3° loop, il task**: *dentro un solo turno, N giri: il modello chiede un tool e si ferma, qualcuno esegue, il risultato rientra, il modello riparte. Fino a task completato.*
- Nota in basso: *I numeri sono storici, l'annidamento no: conversazione ⊃ task ⊃ generazione. Il 3° è nato per ultimo ma sta in mezzo. E "qualcuno" adesso ha un nome: l'harness.*

**Visual**: `slide5-tre-anelli.svg` — lo zoom sull'anello della mappa: gli stessi tre anelli della slide 39 del 26, con l'etichetta `chi? → prossimo incontro` sostituita da `l'harness`.

**Prompt per schema SVG**:
> Tre anelli concentrici, identici per posizione ed etichette a quelli della slide 39 dell'incontro 26 (esterno conversazione, mezzo task, interno generazione, con i passi scritti lungo ciascun anello).
>
> L'unica differenza: sul passo `qualcuno la esegue` della corona di mezzo, dove prima pendeva l'etichetta `chi? → prossimo incontro`, ora pende `l'harness`, ed è l'elemento focale. Accanto, in piccolo: *risposto*.
>
> **Elemento focale**: l'etichetta `l'harness` che chiude la domanda lasciata aperta.

## Slide 6 — L'harness più semplice possibile

**Messaggio**: questo è il minimo che un harness deve fare per essere minimamente utile: chiamare, leggere, decidere, e richiamare. Tutto il resto della lezione è ciò che questo minimo nasconde.

**Layout**: titolo in alto; visual a tutta larghezza al centro (~65%): il flusso a decisione a sinistra (~70% della figura), il riquadro di pseudocodice a destra (~30%); didascalia sotto; blocco nero centrato in fondo.

**Testo**:
- Titolo: *L'harness più semplice possibile*
- Didascalia: *Un processo che chiama il modello, legge la risposta e decide: se è testo, il turno è finito; se è una tool call, esegue, appende il risultato e richiama. È l'unica volta in cui vediamo codice: da qui in poi vedremo solo che cosa entra ed esce dalla finestra.*
- Blocco nero centrato: *Questo è il minimo. Senza, il modello aspetta per sempre.*

**Visual**: `slide6-harness-minimo.svg` — flusso a decisione più pseudocodice.

**Prompt per schema SVG**:
> **A sinistra, il flusso**, dall'alto verso il basso, in cinque nodi collegati da frecce:
> 1. `chiama il modello` (con accanto, in piccolo: *tutta la finestra, ogni volta*)
> 2. `leggi la risposta`
> 3. un **nodo di decisione** a rombo: `è una tool call?`
> 4. ramo **no**, verso destra e in basso: `è testo: il turno è finito` (nodo terminale)
> 5. ramo **sì**, verso il basso: `esegui il tool` → `appendi il risultato alla finestra` → una freccia di ritorno che risale fino al nodo 1, etichettata `giro successivo`.
>
> **A destra, il riquadro di pseudocodice**, in monospaziato:
> ```
> while not done:
>     risposta = modello(finestra)
>     if risposta.vuole_un_tool:
>         finestra += esegui(risposta)
>     else: done = True
> ```
> Etichetta sotto il riquadro: *lo stesso flusso, in cinque righe*.
>
> **Elemento focale**: il rombo di decisione e la freccia di ritorno. Il resto dell'harness (chi prepara la finestra, chi esegue, chi decide quando la finestra è troppo piena) è tutto nascosto in tre parole di questo flusso: `finestra`, `esegui`, `done`.

> Nota: il flusso legge lo `stop_reason` della risposta (la Slide 10, in sezione 2, lo chiamerà per nome); qui si dice "è una tool call?" e basta.
