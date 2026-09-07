# Slide realizzate — Incontro 26

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation-26/presentation.html`, figure usate.
Per commentare, scrivi sotto la riga della slide.

> **Come si numerano le slide nuove** (regola del docente, 7 set 2026): una slide inserita prende **il numero di quella che la precede, più `b`** — dopo la 35 viene la **35b**, dopo la 36 la **36b**. Così non si rinumera nient'altro. È nata dopo tre rinumerazioni globali in due giorni: ognuna tocca centinaia di riferimenti in deck, spec e in questo file, e ogni volta lascia indietro i numeri nudi dentro elenchi e intervalli. Se servisse una terza slide dopo la stessa, si continua con `c`.

---


## Copertina — «Agentic AI: da LLM ad agenti»  
`#cover`


## Separatore di sezione — «Cosa è un agente?»  
`#div-sec1`

- **01 · Cosa è un agente? Le aspettative** — `#slide-1` — *nessuna figura*
	- ✅ FATTO — "Ci aspettiamo che porti a termine un task — non che risponda a una domanda" deve essere un blocco evidenziato e centrato nero, come in altre slide
		- Ora usa `class="nota dark center"`: fondo nero, testo bianco centrato. Aggiunta la regola CSS `.nota.dark.center` (niente bordo a sinistra, 15pt, 600).
- **02 · Lo spazio delle soluzioni** — `#slide-2` — `slide2-spazio-soluzioni.svg`
	- ✅ FATTO — *Figura*. Ragionamento diventa Ragionamento matematico e ha lo stesso ampiezza di contesto di coding e gli stessi colori. Rimpiazza Conversazione Stateful con Ragionamento strategico aziendale
		- `Ragionamento matematico` spostato a cx=1105 (stessa X di Coding) cy=170, con lo stesso trattamento focale di Coding (cerchio #ecd3de r=22 + #a1245a r=12, etichetta burgundy 700/24). `Conversazione stateful` → `Ragionamento strategico aziendale`, stessa posizione e stesso trattamento attenuato.
	- ✅ FATTO — *Testo*
		- Didascalia → "La *jagged frontier*: non tutti i task sono uguali."
		- Nota → "La frontiera si sposta costantemente. La verificabilità deterministica del risultato è l'elemento determinante per poter addestrare gli LLM ad abilitare correttamente gli agenti."
- **03 · Un agente è un sistema composto** — `#slide-3` — `slide3-formula-agent.svg`
	- ✅ FATTO — Nota → "LLM e Harness sono il sistema operativo. Il resto è come se fosse il software che, a parità di infrastruttura, organizza il lavoro a seconda dell'obiettivo."
	- ✅ FATTO — **poi rifatta: la rilettura a tre livelli CPU / sistema operativo / software** — vedi il blocco in fondo al file. La nota di sopra non è più quella in slide.
## Separatore di sezione — «L'LLM: cos'è e come genera»
`#div-sec2`

- **04 · Che cos'è un modello linguistico** — `#slide-4` — `slide5-modello-linguistico.svg`
	- ✅ FATTO — Nota → "Prevedere bene significa comprimere bene." (rimosso ": non è una metafora, è un teorema. Lo ritroveremo.")
- **05 · La generazione: un token alla volta** — `#slide-5` — `slide6-generazione-autoregressiva.svg`
	- ✅ FATTO — Didascalia: aggiunto in coda "Da questo punto di vista il modello è stateless e ragiona solo in termini di parola successiva."
- **06 · Il golfista** — `#slide-6` — `slide7-golfista.svg`
	- ✅ FATTO — *Figura* i colpi ora riflettono i colpi tipici: gittate decrescenti 390 / 270 / 170 / 80 (atterraggi a x = 560, 830, 1000, 1080) e apici decrescenti in modo monotono (y = 42, 162, 267, 362). L'etichetta `colpo 4` è sfalsata più in basso con linea di richiamo, per non collidere con `colpo 3`.
	- ⚠️ La stessa scena è duplicata dentro `slide31-rlhf.svg`: aggiornata anche lì (archi, palline, etichette e le 4 linee di mira verso la buca).
- **~~08~~ · Il 1° loop: la generazione** — *(numerazione precedente; slide rimossa)* — *nessuna figura*
	- ✅ FATTO — SLIDE RIMOSSA. (Conteggio aggiornato dopo il secondo giro di fix: il deck sta ora a **59** slide — 57 iniziali, meno la 08 e la 24, più le quattro nuove 14b / 15b / 17b / 23b.)
	- ⚠️ Gli `id` e i numeri in footnote delle slide successive **non** sono stati rinumerati: `#slide-7` resta `#slide-7` e la sua footnote resta `09`. Rimane quindi un buco sul numero 08. Rinumerare avrebbe invalidato tutte le ancore citate in questo file e nelle spec (e il deck già usa etichette non sequenziali tipo `10b`, `11b`, `20b`). Se preferisci la numerazione contigua, va fatta come passo a sé su tutto il deck.
- **07 · Il 2° loop: la conversazione** — `#slide-7` — `slide9-comparazione-loop.svg`
	- ✅ FATTO — Ora è una slide di comparazione a due metà dentro un unico SVG a piena larghezza (viewBox `0 0 1140 356`, rapporto allineato allo slot per non scalare i testi).
		- **A sinistra** — «IL 1° LOOP — LA GENERAZIONE»: la pila della frase sul gatto ricopiata da `#slide-5` (stessi colori, stesso badge STOP), con graffa "il contesto cresce di un token per volta".
		- **A destra** — «IL 2° LOOP — LA CONVERSAZIONE»: tre turni, ognuno col payload completo rispedito all'API; le righe dei turni passati sono sbiadite, la risposta appena generata è una pill burgundy. Graffa "la storia cresce di un turno per volta". Adattato dagli SVG `slide12-conversation-step{1,2,3}.svg` del deck `gsom-april-2026` (recuperati dal repo locale invece che dall'URL).
		- Rimossi dalla slide lo pseudocodice e il diagramma dei due anelli annidati; la nota-seme sul 3° loop resta.
	- ⚠️ `slide9-secondo-loop.svg` (i due anelli annidati) non è più referenziato da nessuna slide. Non l'ho cancellato: dimmi se vuoi rimuoverlo.
	- ✅ FATTO — «aggiungi il blocco con il system prompt»
		- `[system] Sei un assistente utile.` è ora la **prima riga dentro ciascuno dei tre riquadri**, non una nota a parte: è quello che significa «rispedita per intero», e ora figura e didascalia dicono la stessa cosa. La didascalia mette in grassetto *system prompt in testa*.
	- ✅ FATTO — cliffhanger rimosso (come da tua indicazione)
		- La nota era: *«Il 3° loop non si aggiungerà in coda: si infilerà in mezzo. Lo vedremo nascere oggi, e lo apriremo al prossimo incontro.»* Ora è: *«Dentro un turno, però, non c'è per forza una sola generazione del modello. È la prossima slide.»* — passaggio diretto alla 9.



- **08 · Il 3° loop: la tool call** — `#slide-8` — `slide9b-tool-call.svg` — **NUOVA**
	- ✅ FATTO — «aggiungi una slide qui. Il terzo loop, il tool call. Prendi l'svg a destra di `#slide-7` e affiancalo ad un altro svg che fa vedere un esempio di conversazione con tool call nel flow. metti in una zona del system prompt la dichiarazione del tool (ne mettiamo uno solo per semplicità).»
		- **Metà sinistra**: è, identica, la metà destra della 8 — i tre turni, un giro di generazione ciascuno. Intestazione «SENZA TOOL». La citazione letterale è voluta: chi guarda riconosce la figura di due minuti prima e vede solo che cosa cambia.
		- **Metà destra**: «CON UNA TOOL CALL», due riquadri `giro 1` e `giro 2` **dentro un solo turno** dell'utente (una graffa a lato lo dichiara). Il `[system]` porta su una seconda riga indentata la dichiarazione del tool: `Tool: cerca_ordine(id_ordine) — stato di un ordine`. Un tool solo, come chiesto.
		- Il flusso: `giro 1` finisce con la richiesta del modello — `→ cerca_ordine("4471")` — e lì il modello si ferma; `giro 2` ha in più la riga `[tool]` col risultato e la risposta finale.
		- La riga `[tool]` è in **teal con fondo tinta**, colore diverso da quello del modello: non l'ha generata lui, l'ha appesa qualcun altro. È il punto della slide, e si legge dal colore prima che dal testo. Sotto, i tre passi del giro (① chiede e si ferma · ② qualcun altro esegue e appende · ③ riparte).
		- ⚠️ **Da risolvere, come d'accordo**: la **slide 38** («Nasce il 3° loop», sezione 4) copre ancora gli stessi punti meccanici — *la tool call è testo*, *i tool vanno dichiarati*, *il giro* — ed è ora in buona parte un doppione della 9. Va rifocalizzata sul solo lato RL (da dove viene la capacità) oppure rimossa. Annotato anche nella spec della sezione 2.

- **09 · Perché serve un secondo addestramento** — `#slide-9` — `slide9c-secondo-addestramento.svg` — **NUOVA**
	- ✅ FATTO — «per introdurre la mira, riporta qui la slide …/slide-secondo-addestramento adattandola»
		- Ripresa dal repo locale (`slide14-secondo-addestramento.html` + `slide14-rlhf-comparison.svg`) e **riportata alla palette e ai font di questo deck**: quella di aprile era in Arial su fondi grigi. Lo stesso prompt — *«Come posso aumentare le vendite?»* — dato a due modelli: a sinistra il modello base continua il testo con altre domande (monospaziato, sbiadito, come un testo del web), a destra risponde (Poppins, bordo burgundy).
		- Chiusa col blocco nero centrato: *«Da «cosa è probabile» a «cosa serve rispondere».»* — riusa la classe `.nota.dark.center` introdotta per la slide 1.
	- ⚠️ **Il golfista è slittato a `#slide-10`** (file `slide9d-golfista-mira.svg`), perché questa si inserisce prima. Aggiornati id, footnote e i commenti di sincronizzazione nei tre file del golfista.


- **09 · Il colpo non basta: serve la mira** — `#slide-9` — `slide9c-golfista-mira.svg` — **NUOVA**
	- ✅ FATTO — «porta in una nuova slide qui una copia del golfista di slide 36, spiegando che per fare il secondo ed il terzo loop è necessario un training successivo al pretraining con cui aggiungere la mira, ottimizzando non il prossimo token solo sul contesto precedente, ma sul percorso sequenziale autoregressivo lungo la traiettoria»
		- La vignetta è **la stessa della slide 6** — stesso viewBox, stessi archi, stesso golfista — con in più il gruppo `mira` e la buca in primo piano, presi pari pari dalla 37. Al posto di *«la buca? / per ora, nessuna mira»*, **nello stesso angolo**, ora si legge *«ora ogni colpo mira alla buca / e a essere ottimizzato è il percorso, non il singolo colpo»*.
		- Didascalia col tuo testo: il pretraining insegna il colpo (prossimo token sul contesto precedente, nient'altro); un turno di conversazione o un giro di tool call hanno una meta; serve un addestramento **dopo** il pretraining che ottimizzi il percorso autoregressivo lungo l'intera traiettoria.
		- ⚠️ **Un dettaglio che ho dovuto misurare.** Perché il richiamo funzioni la vignetta deve rendersi *della stessa dimensione* della slide 6. Il viewBox è 2.6 di rapporto in uno slot da ~3.0, quindi è vincolata in **altezza**: ogni riga di testo sotto le ruba larghezza in proporzione 1:2.6. Con la mia prima stesura (didascalia di 4 righe a 12.5pt + una nota) la vignetta scendeva a **757px** contro i **1026px** della slide 6 — un −26% che si vedeva, e leggeva come un disegno diverso. Ho tolto la nota (il rimando alla sezione 4 è passato nelle note del relatore, come fa la slide 6 col suo) e portato la didascalia a 11.5pt: ora è a **1013px**. Se ci aggiungi testo, ricontrolla questa misura.
	- ⚠️ **La scena del golfista è ora in TRE file**: `slide7-golfista.svg` (senza mira), `slide9c-golfista-mira.svg` e il gruppo `scena-golfista` dentro `slide31-rlhf.svg`. Ho aggiornato i commenti di sincronizzazione in tutti e tre: se cambiano terreno, atterraggi, archi o buca, vanno cambiati ovunque. Era già due; ora è tre, ed è il punto più fragile del deck.
	- ⚠️ **Si aggiunge alla questione aperta della 39**: ora la sezione 2 anticipa **due** slide della sezione 4 — la **33** (meccanica della tool call, doppione della 9) e la **31** (stessa vignetta, stesso messaggio «la mira arriva dopo»). Quello che resta solo alla sezione 4 è il *come*: preferenze umane e reward model (31), RL sulle traiettorie (32), la chiusa sull'harness (33). È lì che vanno rifocalizzate.

## Separatore di sezione — «Perché funziona»  
`#div-sec3`

- **11 · La base di tutto: a ogni parola il suo vettore** — `#slide-11` — `slide10-parola-vettore.svg`
- **12 · Che cos'è un vettore** — `#slide-12` — `slide10b-che-cos-e-un-vettore.svg`
- **13 · Vettori e prodotto scalare** — `#slide-13` — `slide11-vettori-prodotto-scalare.svg`
- **14 · La somma: spostarsi nello spazio** — `#slide-14` — `slide11b-somma-vettori.svg`
- **15 · La scala del calcolo: vettori e matrici** — `#slide-15` — `slide12-scala-del-calcolo.svg`
- **16 · Embeddings: lo spazio delle idee** — `#slide-16` — `slide13-embeddings.svg`
- **17 · La tokenizzazione e l'embedding lookup** — `#slide-17` — `slide14-tokenizzazione.svg`
	- ✅ FATTO — Figura: mettere tra le parole e i blocchi con la parola e l'id (ad esempio tra "Il" ed "Il 243") la grande matrice monoriga di lookup degli encoding
		- Aggiunta una **fascia sottile** fra il testo grezzo e le tessere: strip grigio alto 30, 7 celle larghe quanto il contenuto (voce in mono + id sotto), `⋯` ai due estremi **e nei vuoti fra le celle** — così si legge come il troncone di una tabella da centomila voci, e le tre celle della parola rara risultano *sparse*, non contigue. Le frecce ora sono due per token: testo grezzo → cella → tessera, grigie per i comuni e burgundy per i tre della parola rara.
		- Id riusati esattamente quelli già nel generatore: `243`, `28741`, `1274`, `553`, `11621`, `45093`, `30818`. Etichetta di gutter `encoding` / *~100.000 voci*. viewBox `0 0 784 368` (era 700×322).
		- Rimossa la vecchia etichetta in alto a destra *"id da un vocabolario fisso di ~100.000 voci"*: era diventata un doppione di quella della fascia, e il bullet della slide lo dice già.
		- ✅ **RISOLTO, e alla radice.** Il problema era: fascia e tessera portavano lo stesso contenuto (`Il` + `243`) una sopra l'altra e si leggevano come la stessa cosa scritta due volte. La mia proposta era togliere l'id dalla tessera, contro una decisione esplicita della spec. Hai deciso meglio tu: **via le tessere**. Ora la frase compare una volta come testo grezzo e una volta come voci del vocabolario, e non c'è più niente di ripetuto.

	- ✅ FATTO — «vorrei rendere evidente che la lookup è una one hot encoding sulla matriciona degli embedding»
	- ✅ FATTO — «sostituisci le tessere senza fascia grigia con la grafica appena creata (matrice embedding e onehot)»
	- ✅ FATTO — «cambia il titolo in La tokenizzazione e l'embedding lookup» — la slide ora dichiara i due passaggi che disegna, non più solo il primo.
		- **Una precisazione, che ha deciso dove mettere la cosa.** Nella figura ci sono due lookup diverse: *testo → id* (la fascia grigia) è il tokenizer, string matching, e lì il one-hot non c'entra; *id → vettore* è quella che è letteralmente `one-hot × E`, ed era l'unico passaggio della figura senza spiegazione. Le due bande nuove spiegano **quella**.
		- **La figura è ora una pipeline sola, cinque bande, un solo asse orizzontale** — le stesse sette x per tutte. Dal basso: testo grezzo → fascia di encoding (testo + id) → **one-hot** (un quadratino per voce, tutti vuoti tranne quello di `gatto` con dentro `1`) → **matrice degli embedding** (una colonna di 4 celle per voce, `⋯` nei vuoti, tutte spente tranne quella di `gatto`) → vettori. Un `×` nel margine sinistro, fra le due bande nuove, dice l'operazione.
		- **L'allineamento fa il lavoro della didascalia**: l'`1` sta esattamente sopra la cella `gatto` della fascia e sotto la colonna che pesca. Il one-hot non è un oggetto nuovo da imparare — è la fascia con una cella accesa.
		- **Il filo di `gatto` è acceso in teal per tutta l'altezza**: voce → uno → colonna → vettore. Gli altri sei restano neutri e saltano il one-hot: il meccanismo si insegna una volta sola, perché sette one-hot sovrapposti non sarebbero un vettore.
		- Aggiunto un terzo bullet alla slide: «**L'id è un numero di riga** — cercare la riga 28741 nella matrice degli embedding *è* moltiplicare per quella matrice un vettore one-hot».
		- ⚠️ **Che cosa si è perso togliendo le tessere**: le tre tessere burgundy **contigue** sotto un'unica parola, che erano l'elemento focale della slide e dicevano a colpo d'occhio «questa parola è stata spezzata». Le celle della fascia non lo fanno: sono sparse, non contigue. **Ho compensato** con una sottolineatura burgundy sotto la parola rara nel testo grezzo, etichettata *una parola, tre token* — meno vivace, ma nel posto giusto, cioè sul testo che viene tagliato. Se non ti basta, dimmelo: si può rimettere il contrasto in un altro modo.
		- ⚠️ **Deroga all'alfabeto, dichiarata**: qui l'embedding è una **colonna** di 4 celle e non una riga, perché l'asse orizzontale è il vocabolario e va tenuto allineato per tutte le bande. È la stessa deroga della Slide 29 (vocabolario in uscita, una colonna per token) — e quel parallelo torna utile in aula: è la stessa matrice, vista dai due lati.
		- ⚠️ **Semplificazione ereditata**: la fascia mostra sette voci in ordine di frase, non di id (243, 28741, 1274, …), quindi non è davvero una fetta contigua del vocabolario. Era già così prima, ma per il one-hot pesa un po' di più, perché la posizione dell'uno *è* un indice. Per il pubblico non cambia nulla; se vuoi essere rigoroso va ordinata per id.
		- Nella nota nera «dentro la **tessera** le lettere spariscono» è diventato «dentro il **token**»: la tessera non c'è più.
		- **Misure**: viewBox da `784×368` a `784×416`. La figura resta vincolata in **larghezza** — rende 706,9px in uno slot alto 468,8 e ne usa 375,1, quindi **94px di margine**, molto più comodo di prima. Oltre `784×520` diventerebbe vincolata in altezza e tutto rimpicciolirebbe insieme.
		- Toccato `gen_a.py`, non l'SVG: `regen.py` lo riscriverebbe. Lanciato dopo la modifica tocca **solo** `slide14-tokenizzazione.svg` — cioè generatori e SVG erano allineati, che è il test di consistenza del repo.
		- ⚠️ La spec portava una *Nota di revisione* di segno opposto: una versione precedente aveva un grande rettangolo-vocabolario **in cima**, tolto perché era «l'elemento più grande e il meno informativo». La fascia nuova è lo stesso oggetto in forma diversa (sottile, dentro il flusso invece che sopra) e quel difetto non lo ha; nota aggiunta anche nella spec.
		- ⚠️ Il gutter dell'etichetta ha allargato il viewBox dell'11%: a schermo tutto rimpicciolisce di altrettanto, e gli id dentro le tessere scendono a ~8.6px CSS su slide da 1280. Leggibili in proiezione, ma è il testo più piccolo della sezione.

- **18 · Cosa serve, per prevedere la parola successiva** — `#slide-18` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «Qui vorrei fare una slide nuova di introduzione all'architettura, solo testo riportato verbatim»
		- Testo riportato **verbatim**, spezzato solo per il layout: frase di apertura in evidenza, i tre punti come bullet (il nome del meccanismo — attention / fully connected layers / blocchi con skip connection — in burgundy in coda a ciascuno), e le due frasi finali come due blocchi grigi affiancati, etichettati *il vincolo del calcolo* e *il vincolo del dataset*.
		- Titolo scelto da me (non era nel fix): **«Cosa serve, per prevedere la parola successiva»**. Cambialo se preferisci.
		- Questa slide diventa il **riferimento** che la 21 e la 24 richiamano: se ne cambi il testo, va cambiato anche il richiamo là.

- **19 · L'architettura, in un colpo d'occhio** — `#slide-19` — `slide15a-scatola-nera.svg`, `slide15b-torre.svg`, `slide15c-torre-aperta.svg`
	- *(non toccata)*

- **20 · Il fully connected: fanout, gate, compressione** — `#slide-20` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «Qui inserire una slide di introduzione al fully connected layer, facendo vedere che è la combinazione di una parte di fanout, non linearità, compressione. ricorda la finalità dalla slide introduttiva della sezione»
		- Apre richiamando **alla lettera** la seconda capacità della 19 («conoscenza fattuale su tutti i domini dello scibile»), poi i tre stadi come tre colonne numerate — Fanout / Non linearità / Compressione — ognuna col rimando alla slide che la apre (16, 16, 17).
		- Solo testo, nessuna figura: le due slide dopo disegnano gli stessi tre stadi per esteso, anticiparli li brucerebbe.
	- ✅ **Qui è finita la ex slide «La conoscenza è nei pesi»** — vedi sotto.

- **21 · Fanout: il matching concettuale** — `#slide-21` — `minimap-fc.svg`, `slide16-fanout.svg`
	- ✅ FATTO — Figura: rendi graficamente evidente il passaggio dalla relu
		- La ReLU è ora disegnata **come funzione**, in un riquadro-inset nel gutter all'altezza della barra del gate: spezzata piatta sotto zero e diagonale a 45° sopra, assi `in`/`out`, zero marcato, e due punti campione — uno pieno sul ramo diagonale (passa), uno vuoto sul ramo piatto (azzerato). L'etichetta del gutter diventa `non linearità · ReLU`.
		- Scelta di progetto: la spezzata **non** è dentro la barra con le colonne appoggiate sopra, perché la batteria è ordinata per concetto e l'asse x di una ReLU è il valore in ingresso. Farle coincidere richiederebbe di riordinare le colonne per attivazione crescente, cambio più grosso di quanto chiesto e che romperebbe la continuità con le barre della 23.
	- ✅ FATTO — *Testo* allineato: il terzo bullet ora dice «**La non linearità è un gate: la ReLU** — sotto zero azzera, sopra zero lascia passare invariato».

- **22 · Compressione: la sovrapposizione** — `#slide-22` — `minimap-somma.svg`, `slide17-compressione.svg`
	- ✅ FATTO — Figura: rimuovi lo spazio delle idee e la skip connection. il ruolo di questa slide è far capire che i tanti rilevatori semantici scattati dopo la non linearità vengono compressi in un vettore di dimensione 4
		- Via il piano punteggiato con le due nuvole, via il punto che si sposta, via il nodo `+` e l'embedding originale in ingresso. Resta il solo collo di bottiglia: **sette** barre burgundy (le prime tre con gli stessi nomi delle sopravvissute della Slide 21, per continuità) che convergono in **un unico vettore da 4 celle**, con l'annotazione *molti rilevatori accesi → quattro celle*.
		- viewBox da 700×440 a **700×322**: con la scena in cima rimossa il disegno si è accorciato di un terzo.
		- Ho anche **levato dalla figura** il titolo *Da migliaia a quattro* e la frase sulla sovrapposizione: erano già i due bullet dell'HTML, e a schermo si leggevano due volte.
	- ✅ FATTO — *Testo* rifatto: i due bullet ora sono «**Da migliaia a quattro**» e «**La sovrapposizione**»; la nota rimanda il nodo `+` alla Slide 19, dove è disegnato al posto suo.

- **23 · L'attention: a che cosa serve** — `#slide-23` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «qui aggiungi una introduzione alla attention, solo testo, ricordando la finalità del blocco dall'introduzione generale»
		- Apre richiamando **alla lettera** la prima capacità della 19, poi il punto che conta («è l'unico posto in cui le corsie si parlano»), poi i tre passi come tre colonne numerate — Q·K / softmax / V — col rimando a 18, 19, 20.

- **24 · Attention: domande e chiavi** — `#slide-24` — `minimap-attn.svg`, `slide18-griglia-qk.svg`
	- ✅ FATTO — Figura: sposterei le piccole matrici Wk e Wq sul lato destro, ed è l'embedding più a destra, sopra calcio, ad essere collegato a Wq. non penso ci sia necessità di freccia che collega Wq a Wk
		- Le tre matrici 4×3 sono ora impilate **sul lato destro**, fuori dalle colonne dei token: `× W^V` in alto, poi `× W^K`, `× W^Q` in basso, con l'etichetta *tre proiezioni dello stesso embedding*. `W^Q` è alimentata dalla sola colonna `calcio`, la più a destra. Il collegamento `W^Q`→`W^K` è stato rimosso.
		- viewBox della griglia da 700×440 a **756×440** (allargata in larghezza, dove c'era margine, non in altezza).
		- ⚠️ L'agente è stato **fermato durante la sua verifica finale**, quindi il controllo l'ho rifatto io: verificato a schermo su 18, 20 e sul secondo tempo della 27, viewBox coerenti fra tutte e cinque le uscite, nessuno sforo in tutto il deck. Le 19 e 20b hanno ereditato lo spostamento (griglia condivisa) ma **non le ho guardate una per una**.

- **25 · Softmax: il budget di ascolto** — `#slide-25` — `minimap-attn.svg`, `slide19-griglia-softmax.svg`
	- *(non toccata direttamente: erediterà lo spostamento delle matrici dalla 25)*

- **26 · V: il contenuto del libro** — `#slide-26` — `minimap-attn.svg`, `slide20-griglia-v.svg`, `slide20-multihead.svg`
	- ✅ FATTO — Titolo: applicare il contenuto del libro
		- «V: la consegna» → **«V: il contenuto del libro»**, che riprende alla lettera la metafora della biblioteca fissata nella Slide 24 (Q = la richiesta al banco, K = l'etichetta sul dorso, V = il contenuto del libro).
	- ✅ FATTO — secondo visual al click che fa vedere le tante heads, col testo che compare contestualmente
		- HTML: la slide ora è a due tempi (`.visual.stack` + `fragment`), e il secondo SVG si sovrappone al primo con lo stesso viewBox, così al click nulla si sposta. Il testo — «Tanti blocchi attention sono applicati in parallelo, per modellare relazioni diverse e estrarre semantiche differenti dal contesto precedente» — è legato allo **stesso** `data-fragment-index`, quindi compare insieme al visual e non un click dopo.
		- `slide20-multihead.svg` creato, stesso viewBox 756×440 della griglia base: `testa 1` in primo piano è la griglia completa, dietro `testa 2 · sintassi`, `testa 3 · riferimenti`, `testa 4 · tono` sfalsate in profondità, più `⋯`. Verificato a schermo: al click la sovrapposizione registra, niente si sposta, e la caption compare insieme al visual.

- **27 · Lo stesso token, due contesti** — `#slide-27` — `minimap-attn.svg`, `slide20b-contesto-frase1.svg`, `slide20b-contesto-frase2.svg`
	- *(non toccata direttamente: erediterà lo spostamento delle matrici dalla 25)*
- **28 · Positional encoding: l'ordine conta** — `#slide-28` — `minimap-pos.svg`, `slide21-positional-encoding.svg`
- **29 · Reverse embedding: tornare ai token** — `#slide-29` — `minimap-testa.svg`, `slide22-reverse-embedding.svg`
	- ✅ FATTO — Figura: la matrice con i vari vettori "sul", "un", "morbido", "nero", "stanco", "parigi" etc la farei in orizzontale, così è sempre un riga per colonna, con il valore dei logits che è in cima ad ogni vettore verticale che compone la matrice rettangolare
		- Vocabolario trasposto: ogni token è una **colonna** di 4 celle, il **logit in cima**, il nome sotto. Le colonne sono **contigue**, così compongono davvero una matrice rettangolare; dopo l'ultima, una colonna tratteggiata con `⋯` e `~100.000` dice che continua. Le note sono passate nel gutter di sinistra, come nel resto della sezione. viewBox da 700×430 a **700×444**.
		- ⚠️ **Deroga all'alfabeto, dichiarata**: qui le celle sono **42×20, non quadrate** come altrove. È il prezzo per avere insieme le tre cose che hai chiesto — colonne contigue, logit orizzontale in cima, nome del token orizzontale e leggibile sotto: `morbido` in monospaziato non sta sotto una colonna quadrata abbastanza bassa da starci in quattro righe. Le alternative erano ruotare le etichette (numeri ruotati, poco leggibili) o distanziare le colonne (e allora non è più una matrice). Annotata nel codice e nella spec.


- 

- **~~24~~ · La conoscenza è nei pesi** — *(numerazione precedente; slide rimossa)* — `slide24-conoscenza-nei-pesi.svg`
	- ✅ FATTO — «Rimuovere la slide, se ci sono degli elementi da riportare nella slide introduttiva sul fully connected layer proponimelo»
		- **Slide rimossa.** Ecco la proposta, già applicata — dimmi se la cambio:
		- **Riportati nella 21**: i due bullet **«Ciò che è scritto»** e **«Ciò che emerge»**. Parlano esattamente di cosa contengono i pesi del fully connected (embedding e colonne delle matrici, e le regolarità geometriche fra loro): nella slide di introduzione al blocco sono al posto giusto.
		- **Ricostruito nella 31**: la nota della 24 portava il ponte verso il compressore lossy («niente archivio consultabile → ed è per questo che il recupero può sbagliare»). Senza la 24 la 31 restava senza attacco, quindi quel ponte è diventato il **primo bullet della 31**: «**Niente archivio consultabile** — nessuna riga di database da andare a leggere: la conoscenza è nei vettori appresi, e va ricostruita ogni volta. È per questo che il recupero può sbagliare».
		- **NON riportato**: il confronto disegnato `UN DATABASE` / `UN LLM`. Era una figura a sé e la 21 è di solo testo. Se ti dispiace perderlo, l'alternativa è tenere la 24 come slide di sola figura, senza bullet.
		- ⚠️ `slide24-conoscenza-nei-pesi.svg` e la funzione `slide24()` in `gen_c.py` restano nel repo ma non sono più referenziati: dimmi se li rimuovo.

- **30 · L'LLM come compressore lossy** — `#slide-30` — `slide25-compressore-lossy.svg`
- **31 · Conseguenze della compressione** — `#slide-31` — *nessuna figura*
- **32 · MoE: non tutti i pesi lavorano sempre** — `#slide-32` — `minimap-fc.svg`, `slide27-moe.svg`

## Separatore di sezione — «Come viene addestrato»  
`#div-sec4`

- **33 · Le tre fasi** — `#slide-33` — `slide28-tre-fasi.svg`
- **34 · Pretraining: indovinare il prossimo token** — `#slide-34` — `slide29-pretraining.svg`, `slide29-scala-dati.svg`
- **35 · Gradient descent: sbaglia, misura, correggi** — `#slide-35` — `slide30-gradient-descent.svg`

- **35b · Nasce il 1° loop** — `#slide-35b` — `slide33-primo-loop.svg` — **NUOVA**
	- ✅ FATTO — «metti qui una slide come la slide-38, in cui è evidenziato in magenta solo il 1° loop, quello interno»
		- È **la stessa figura della 38**, non una nuova: stessa geometria, cambia solo quale anello è acceso. Qui il nucleo — cerchio burgundy su tinta, etichetta `1° LOOP` burgundy, frecce interne burgundy; corona di mezzo e anello esterno restano neutri.
		- Il testo chiude il pretraining: la capacità che lascia è una sola, e ripetuta *è* la generazione (Slide 5); ottimizza il colpo, non il percorso — il golfista senza mira della Slide 6; con questo soltanto il modello continua un testo, non risponde a un turno e non esegue niente.
		- Ho usato il **burgundy** del deck (`#a1245a`) e non un magenta a sé: è il colore focale di tutta la lezione, e questa figura lo usa già per l'anello acceso nella 38. Se volevi proprio un magenta diverso, dimmelo.
- **36 · RLHF: arriva la mira** — `#slide-36` — `slide31-rlhf.svg`
	- ✅ FATTO — «in questo visual, fai vedere una domanda e due esempi reali di risposta»
		- I riquadri A/B erano segnaposto (tre righe grigie) a 15px dentro un SVG largo 1550, che in slide diventavano **~6.8px**: sotto il minimo leggibile del deck. Per starci con del testo vero serviva spazio, e l'hai deciso tu: **via il golfista dalla 37**.
		- Ora il meccanismo occupa tutta la larghezza. A sinistra la domanda — *«Come posso aumentare le vendite?»* — e le due risposte per esteso, A col bordo burgundy e il segno di scelta; a destra la catena *preferenze → reward model → reward → modello*; sotto, il callout invariato. Il testo delle risposte rende ora a **12.5px** in slide, contro i 6.8 di prima.
		- **Le due risposte sono le stesse della 10**, di proposito: là erano il prima e il dopo dell'addestramento, qui sono la coppia che gli umani confrontano. Stesso esempio, due letture — il primo bullet della 37 ora lo dichiara.
		- Layout della slide da `tv-35` a `tv-30`, perché la figura è diventata orizzontale.
		- ⚠️ Il golfista è così sceso da tre copie a **due**: `slide7-golfista.svg` (senza mira) e `slide9d-golfista-mira.svg` (con). La 37 non lo disegna più.
	- ✅ FATTO — «Riporta qui in piccolo nella figura, nel blocco Modello, le 3 matricine con embedding, fully connected ed qkv presenti anche in slide 34»
		- Le tre matrici 3×3 sono **ricopiate** dalla TAPPA 4 della Slide 34, non ridisegnate: stesse etichette (`embedding` · `Q K V` · `rilevatori`, i nomi che usa la 35 — «rilevatori» è il fully connected), stesso schema di celle gialle, stesse proporzioni. È una citazione: chi guarda deve riconoscere l'oggetto del pretraining e vedere che l'unica cosa a cambiare è **da dove arriva il punteggio**.
		- Il blocco `modello` è diventato **nero**, come quello della 35. Non è un vezzo: le celle sono `#f6f6f6` su `#ffbe0b`, e il giallo su fondo bianco non tiene il contrasto. Nero, la figura combacia con quella della 35 anche di colore.
		- **Non ho riportato la linea gialla di distribuzione** con le tre frecce che nella 35 salgono dentro le matrici: il blocco è alto 130 e non c'è lo spazio. La freccia burgundy `reward` che arriva da sopra fa già quel lavoro — ed è anzi il punto, perché lì il punteggio veniva dalla cross-entropy e qui dal reward model.
		- ⚠️ **Ora le matrici sono in due file**: `slide29-pretraining.svg` (tappa 4) e `slide31-rlhf.svg`. Se cambiano di là, vanno cambiate anche qui — commento di sincronizzazione aggiunto in tutti e due.
	- ⚠️ **Trovato e corretto un difetto preesistente nella stessa figura**: la riga *«stesso metodo: gradient descent —»* era lunga 33 caratteri a 14px partendo da x=910, e finiva a 1141 dentro un viewBox largo 1100. Veniva **tagliata a schermo**. Stesse parole, ora su tre righe a 12.5.

- **36b · Nasce il 2° loop** — `#slide-36b` — `slide33-secondo-loop.svg` — **NUOVA**
	- ✅ FATTO — «qui una slide come la 38, con evidenziato il loop esterno, conversazionale»
		- Acceso l'anello esterno: i tre riquadri (`l'utente scrive`, `il modello lavora`, `la risposta si accoda alla storia`) su tinta con bordo burgundy, e la pill `2° LOOP — CONVERSAZIONE` piena. Nucleo e corona di mezzo neutri.
		- Il testo chiude l'RLHF: non aggiunge parole, aggiunge **la forma del turno**; a ogni giro si rispedisce tutto (Slide 39); e manca ancora l'anello di mezzo — il modello sa parlare, non sa agire.
		- **Il vuoto in mezzo è il punto**, e l'ho detto nella nota: fra «il modello lavora» e «la risposta si accoda» non c'è ancora niente. È lo spazio che la 38 riempie.
		- ⚠️ **Ora sono tre varianti della stessa figura** — `slide33-primo-loop.svg`, `slide33-secondo-loop.svg`, `slide33-terzo-loop.svg`. La geometria deve restare identica in tutte e tre, altrimenti l'effetto «si accende un pezzo alla volta» salta: le ho generate insieme dallo stesso codice e ho messo la nota di sincronizzazione in testa a ciascuna. La 38 non è cambiata a vedersi (solo il markup si è riformattato).
		- **Una simmetria che ora si vede**: tre fasi di addestramento, tre anelli, in quest'ordine — pretraining → interno, RLHF → esterno, RL agentico → mezzo. Sezione 4 da 6 a **8 slide** (budget ~20 → ~24 min).
- **37 · RL agentico: traiettorie** — `#slide-37` — `slide32-rl-agentico.svg`
	- ✅ FATTO — «rendi più chiaro il GRPO: reward su completamento di task verificabili, su più tentativi dello stesso task, nello svilupparsi di n chiamate a sistemi esterni; un training simile alla 36 con aggiornamento matricine simile, ma con reward su tutta la traiettoria agentica»
		- Le tre corsie e la freccia di reward c'erano già. Mancava il resto, e il GRPO era **detto, non mostrato**: una graffa con la scritta «i tentativi si confrontano tra loro».
		- **Il task è ora dichiarato verificabile**, e con lui la fonte del punteggio: *il foglio ha il prezzo giusto? sì / no — lo dice un controllo, non un umano*. È la differenza con la 36, dove il punteggio arriva dal reward model, e ora si legge dalla figura.
		- **Esiti e punteggi in colonna**, allineati fra le tre corsie: `r = 0`, `r = 1`, `r = 0`. L'allineamento è il punto — i tre punteggi devono confrontarsi a colpo d'occhio, perché è esattamente quello che fa il GRPO.
		- **Il pannello fa il conto vero**: `media dei tentativi (1 + 0 + 0) / 3 = 0,33`, `vantaggio = r − media`, `+0,67 −0,33 −0,33`. È il *relative* di Group Relative: il critico è la media del gruppo, non un secondo modello addestrato.
		- **Il giro si chiude sulle matrici**: freccia `gradiente` nel blocco `modello` nero con le tre matricine, ricopiate dalla TAPPA 4 della 34 e dal blocco modello della 36. Le tre slide dicono ora lo stesso meccanismo e cambiano solo il punteggio — cross-entropy, reward model, controllo deterministico su una traiettoria intera.
		- Etichetta sotto le corsie: *ogni tentativo è una traiettoria: n chiamate a sistemi esterni, una dopo l'altra*.
		- ⚠️ **Ho dovuto anche fare spazio.** Con `tv-35` e la nota in basso la figura era vincolata in altezza e rendeva a **662px**, coi testi a 9,6px: aggiungerci controllo, gruppo e matrici l'avrebbe resa illeggibile. Layout portato a `tv-30`, nota HTML rimossa (il suo contenuto è finito nel quarto bullet) e viewBox ridisegnato a `1120×560`. Ora è vincolata in **larghezza** e rende a **763,9px**, scala 0,68. Se riaggiungi testo attorno, torna vincolata in altezza.
		- ⚠️ **Le tre matricine sono ora in tre file**: `slide29-pretraining.svg` (tappa 4), `slide31-rlhf.svg` e `slide32-rl-agentico.svg`. Se cambiano in uno, vanno cambiate in tutti.

- **38 · Nasce il 3° loop** — `#slide-38` — `slide33-terzo-loop.svg`


## Separatore di sezione — «Lo scenario, più o meno completo»

	- ✅ FATTO — titolo cambiato. Il separatore ora dice «Lo scenario, / più o meno completo» e il sottotitolo elenca anche il costo del contesto. Gli eyebrow di tutte le slide della sezione sono passati a `SEZIONE 5 · LO SCENARIO, PIÙ O MENO COMPLETO`.
	- ✅ FATTO — **spostate qui 23, 23b, 34 e 35**, in quest'ordine, prima della 44 *(tutti numeri della numerazione di allora)*. Eyebrow e footnote aggiornati a «Sezione 5».
		- ⚠️ **La numerazione ora è fuori ordine e si vede**: dopo «33 / Sezione 4» il pubblico legge «23 / Sezione 5», poi 23b, 34, 35, 36… Non ho rinumerato perché toccherebbe tutte le ancore citate in questo file e nelle spec. Ma con la 08 e la 24 rimosse, sei slide nuove aggiunte e ora quattro spostate, **una passata di rinumerazione globale è diventata la cosa giusta da fare**: dimmi quando e la faccio in un colpo solo, aggiornando anche fix e spec.
		- ⚠️ La 40 si porta dietro la mini-mappa «sei qui» della torre (`minimap-corsie.svg`), che è un dispositivo della sezione 3. In sezione 5 non è sbagliata — rimanda comunque all'architettura — ma è l'unica slide della sezione ad averla.
`#div-sec5`

- **39 · L'API: come si parla al modello** — `#slide-39` — `slide23c-api-formato.svg` — **NUOVA**
	- ✅ FATTO — «aggiungi qui una slide, in cui introduciamo un concetto che vedremo anche dopo, ovvero quello delle api con cui chiamiamo il modello. Parliamo delle api originali di openai, che erano stateless, e facciamo vedere un esempio di 2 successive call con quel formato.»
		- Due colonne, `CHIAMATA 1` e `CHIAMATA 2 — SUBITO DOPO`, ognuna con endpoint (`POST /v1/chat/completions`), riquadro `richiesta` col JSON e riquadro `risposta · 200 OK`.
		- **Riusa l'idioma dei payload della sezione 2** (slide 7 e 9), qui però sul formato vero: grigio attenuato = messaggio già spedito, nero = il turno nuovo, burgundy = ciò che il modello ha appena generato. Chi ha visto i tre riquadri della slide 7 riconosce la stessa cosa scritta come la scrive la macchina — la didascalia lo dichiara.
		- **Il punto è la differenza di altezza**: cinque righe contro sette. I due riquadri `risposta` invece partono alla stessa y, così le due righe `usage` si confrontano a colpo d'occhio: `prompt_tokens` 24 → 71. Fascia in chiusura: *«Nessun identificatore di sessione, da nessuna parte.»*
		- Nelle note del relatore: la primissima API (2020) era ancora più semplice — un solo campo `prompt`, una stringa; `messages` e i ruoli arrivano nel 2023. Le API recenti offrono anche uno stato lato server, ma **opzionale**: il modello mentale che conta resta questo.
		- ⚠️ **Niente testo sopra la figura.** Con una `.defn` in testa la figura scendeva a **935px** e il monospaziato a 9.85px CSS; togliendola rende **1:1 (1140×380) e il mono a 12px**. Tutto il testo è finito nella didascalia sotto. Se ci aggiungi una riga, ricontrolla questa misura.
		- ⚠️ **Ordine da valutare.** L'ho messa **prima** della 41 («Il contesto ha un costo»), come dice il tuo marcatore. Ma la 42 è «L'API è stateless: cosa significa davvero», quindi la sequenza è API → KV cache → API stateless. Se preferisci tenere insieme le due slide sull'API, basta scambiarla con la 41.
		- ⚠️ **Si sovrappone di proposito con l'incontro 27**, che alla sua slide 3a mostra la stessa cosa con l'API di Anthropic. La divisione ora è: qui il formato di OpenAI per dire *stateless*, là la richiesta **con i tool** (`tools`, blocchi della risposta, `stop_reason`). La spec del 27 diceva «il 26 non ha mai mostrato la struttura dell'API»: non è più vero, l'ho riscritta.

- **40 · Il contesto ha un costo** — `#slide-40` — `minimap-corsie.svg`, `slide23-costo-contesto.svg`
	- ✅ FATTO — «esplicita che salvando nella KV cache i valori, per ogni testa e blocco, delle attivazioni K e V si evita tutto il passaggio dai fully connected layer (molto costoso) e la moltiplicazione di Wq, Wk e Wv di tutti i token precedenti. se non è corretto dimmelo.»
		- **È corretto, tranne un punto: le Wq.** La cache non "evita" le Q dei token precedenti — quelle Q semplicemente **non servono più**. La query di un token serve solo a calcolare l'output *di quel token*, che con la masked attention non può più cambiare: in prefill vengono calcolate e buttate (è già quello che dice il pannello sinistro della figura), in decoding non vengono calcolate affatto. Tutto il resto sì: la cache evita, per i token già visti, le proiezioni W^K e W^V **e** l'intero passaggio dai fully connected layer — ed è quest'ultimo la voce di costo più grossa, perché il FFN è la maggior parte dei parametri di un blocco. Per il token nuovo si paga tutto una volta: W^Q, W^K, W^V e FFN.
		- Testo in slide riscritto con questa distinzione; la precisione completa è finita anche nella spec, come nota.
		- ⚠️ La slide sforava di parecchio con il testo in più: colonna portata a `pts micro` e nota a `nota small`. Verificato: nessuno sforo.
	- ✅ spostata dalla sezione precedente
- **41 · L'API è stateless: cosa significa davvero** — `#slide-41` — `slide23b-curve-costo.svg` — **NUOVA**
	- ✅ FATTO — «Qui aggiungi la slide presa da qui: …/gsom-april-2026/lezione-mba/presentation.html#/slide-api-stateless»
		- Ripresa dal repo locale `gsom-april-2026` (`slide18-api-stateless.html`) invece che dall'URL. Le tre curve di costo sono state **riadattate** alla palette e ai font di questo deck in `slide23b-curve-costo.svg`: quella di aprile aveva fondo `#f2f2f2` e font sans-serif generici.
		- ⚠️ Sovrapposizione da valutare: la **slide 42** («Il modello è stateless: il contesto è tutto», sezione 4) dice una cosa vicina, dal lato del modello. Qui l'ho impostata come "lo stesso costo visto dalla conversazione e dalla bolletta" e l'ho dichiarato nelle note del relatore, ma se vuoi le si può fondere.
	- ✅ spostata dalla sezione precedente

- **42 · Il modello è stateless: il contesto è tutto** — `#slide-42` — `slide34-stateless.svg`
	- ✅ spostata dalla sezione precedente
	- ✅ FATTO — «metti anche l'asse verticale (context size) e la legenda sulla linea tratteggiata rossa»
		- **Asse** nel margine sinistro: linea con freccia verso l'alto, etichetta ruotata *dimensione del contesto*, una tacca burgundy all'altezza della cima di ciascuna delle quattro foto e una guida tratteggiata che la porta fino alla foto. Sotto, in piccolo, *scala indicativa*: le altezze non sono conteggi di token veri e non volevo far credere il contrario.
		- **Legenda** nello spazio vuoto in alto a sinistra: un campione della tratteggiata burgundy e il testo *«la linea tratteggiata segue la cima della pila: ogni foto è più alta della precedente, e non torna mai giù»*, con un richiamo tratteggiato che punta al primo scalino.
		- Il disegno esistente non l'ho toccato: è traslato di 56 a destra per fare posto all'asse. viewBox da `1120×700` a `1176×700`.
		- ⚠️ **Ma qui c'è un problema più grosso, che l'asse ha solo reso evidente.** Questa figura rende a **540px su un viewBox di 1176**: scala **0,459**, la più piccola del deck. I suoi testi da 15px arrivano a schermo a **6,9px** — sotto il minimo leggibile — e la legenda nuova a 6,2px. Non è colpa dell'asse: era già così.
			- La causa è il riquadro **Memento** in cima: 96px più margine, che tolgono altezza alla figura in una slide dove la figura è già vincolata in altezza (rapporto 1,68 in uno slot da 2,38).
			- ✅ **Curato, come hai detto**: il testo di Memento è passato nelle **note del relatore** — è un racconto che si fa a voce, non si legge. La figura è salita da 540 a **721px**, scala da 0,459 a **0,613**: i testi da 6,9 a **9,2px**, in linea col resto del deck.
			- ⚠️ **Regola per questa slide**: qualunque cosa si rimetta sopra la figura le toglie altezza, e qui l'altezza è il vincolo (rapporto 1,68 in uno slot da 1,78). Prima di riaggiungere un blocco in apertura, rimisurare.
- **43 · Il modello è figlio dei suoi training set** — `#slide-43` — *nessuna figura*
	- ✅ spostata dalla sezione precedente

- **44 · Context rot** — `#slide-44` — `slide36-context-rot.svg`
- **45 · I tool accelerano il context rot** — `#slide-45` — `slide36b-tool-context-rot.svg` — **NUOVA**
	- ✅ FATTO — «aggiungi qui la slide …/slide-context-rot»
		- Ripresa dal repo locale (`slide27-context-rot.html`). Il grafico è stato **rifatto** invece che copiato: quello di aprile importava Poppins da Google Fonts (qui il font è già in locale) e usava grigi generici. Ora sono due pannelli — *conversazione pura*, crescita lineare in teal, e *con i tool*, a scalini in burgundy — con la stessa scala, così il confronto si legge.
		- Tenuti i tre consigli pratici (esporre solo i tool necessari · dimensionare i tool result · meglio tool specifici che generici) e la nota sul perché i tool servono comunque.
		- La chiusa di aprile rimandava ai sub-agent: qui è tolta, perché i sub-agent sono materia dell'incontro 27. L'ho annotato nelle note del relatore.
- **46 · Multimodality** — `#slide-46` — `slide37-multimodality.svg`
- **47 · Reasoning** — `#slide-47` — `slide38-reasoning.svg`
	- ✅ FATTO — «sostituisci il visual con un esempio di conversazione con e senza reasoning»
		- Due colonne sulla stessa domanda: *«Un prodotto costa 80€. Applico −25%, poi +25%. Quanto costa?»*. A sinistra risponde subito **80€** — e sbaglia; a destra genera prima il blocco `[thinking]` (−25% → 60, +25% → 75, il secondo % si applica a 60) e poi risponde **75€**.
		- L'esempio è scelto perché la risposta intuitiva è anche quella sbagliata: si vede *a che cosa serve* il ragionamento, non solo che c'è.
		- Il blocco `[thinking]` è tratteggiato e grigio, con una graffa burgundy a lato: *token che paghi e non vedi*. Riusa l'idioma dei payload della sezione 2 (riquadri con tag di ruolo, burgundy per ciò che il modello genera adesso), così le due sezioni si parlano.
- **48 · I costi: training, inferenza, distillazione** — `#slide-48` — `slide39-costi.svg`
- **49 · Il prezzo per token** — `#slide-49` — `slide40-prezzo-per-token.svg`
- **50 · Il valore delle traiettorie** — `#slide-50` — *nessuna figura*
- **51 · Closed, open weights, open source** — `#slide-51` — *nessuna figura*
- **52 · Quando closed, quando open** — `#slide-52` — *nessuna figura*
- **53 · Fine-tuning: riprendere la discesa** — `#slide-53` — `slide44-fine-tuning.svg`
- **54 · LoRA: la correzione a basso rango** — `#slide-54` — `slide45-lora.svg`
- **55 · La fotografia del mercato** — `#slide-55` — *nessuna figura*
	- ✅ FATTO — «Immagine: fare screenshot ed includere da https://arena.ai/leaderboard/text/pareto»
		- Lo screenshot è in `presentation/assets/images/uploads/arena-pareto-2026-09-02.png` (2700×1348, cablato nella slide al posto del placeholder `.asset-ph`).
		- **Il banner cookie**: col tuo via libera l'ho gestito scegliendo l'opzione conservativa — *Manage Cookies*, tutte e quattro le categorie opzionali (Functionality, Advertising, Analytics, Social Media) portate su **off**, poi *Save Preferences*. Erano tutte attive di default.
		- **Come l'ho prodotto**: lo strumento di screenshot del browser restituisce un'immagine in conversazione, non un file. Non c'erano né puppeteer né librerie WebSocket, e non ho voluto installare un Chromium solo per questo; ho scritto un **client CDP minimale in Python puro** (solo `socket` + `base64`) per pilotare Chrome headless: chiude il banner con la stessa scelta conservativa, poi cattura. Lo script sta nella scratchpad, non nel repo: è servito una volta.
		- **Due accorgimenti sulla resa.** (1) Il sito è in tema scuro; ho emulato `prefers-color-scheme: light` via CDP e la pagina passa a fondo quasi bianco — così lo screenshot non stona in un deck tutto chiaro. (2) Al primo tentativo il ritaglio tagliava via l'asse dei prezzi, che è metà del senso del grafico; e con viewport 1700×1250 la card veniva 2308×1348 (rapporto 1.7), che nello slot largo e basso della slide si sarebbe resa a ~660px con le etichette illeggibili. Ho ricatturato con viewport **2400×980**, così la card stessa diventa panoramica: ora è 2700×1348 e in slide rende a **781px**.
		- **Attribuzione in slide**: fonte e data (2 settembre 2026, 7.999.020 voti, 400 modelli) sono nella didascalia, insieme al promemoria che va rifatto a ridosso della lezione.

- **56 · La formula, riletta** — `#slide-56` — `slide56-formula-avanzamento.svg` — **NUOVA**
	- ✅ FATTO — vedi il blocco in fondo al file.

- **57 · Il ruolo dell'harness** — `#slide-57` — `slide4-ruolo-harness.svg`
	- ✅ FATTO — *Figura* riprogettata: i blocchi intorno all'LLM sono raggruppati in 3 categorie distinte da colori
		- **Context management** (teal `#1ab197` su `#d1efea`): Context Initialization · Context Optimization (compaction, pruning, etc.) · Memory management · Skill management
		- **Agentic loop management** (lightblue `#4da0d7` su `#dbecf7`): blocco unico, con l'anello del loop che racchiude l'LLM
		- **Environment management** (giallo `#ffbe0b` su `#fff2ce`): Tool Calling execution and response management · Execution Sandbox · Skill execution management
		- Rimosso il blocco titolo "Harness — l'esoscheletro (simbolico)". viewBox ora `0 0 1000 714`.
	- ✅ FATTO — «metti questa come ultima slide, introduce il prossimo incontro»
		- La mappa dell'harness è ora la **Slide 57**, dopo «La formula, riletta». Eyebrow `VERSO IL PROSSIMO INCONTRO`, footnote `57 / Verso il 27`: non appartiene più a nessuna sezione, ed è giusto così — non introduce l'agente, apre il 27.
		- **La Sezione 1 perdeva il suo ponte**: la nota del relatore «oggi apriamo il primo termine della formula» stava su questa slide. Spostata sulla Slide 3, che ora chiude la sezione.
		- Nelle note della nuova ultima slide: la formula prima dice che dei sei termini se n'è aperto uno, questa apre il secondo e si ferma lì; la mappa torna in apertura del 27, estesa, ed è la figura madre di quella lezione.
		- Sezione 1 da 4 a **3 slide** (budget ~15 → ~12 min); il blocco della spec è passato dal file della Sezione 1 a quello della Sezione 5, sotto un cappello *Chiusura — fuori sezione*.
		- ⚠️ **Ha rinumerato 53 slide**: la 4 è andata alla 57 e tutte le altre sono scalate di uno (5→4 … 57→56). Vedi la nota in fondo al file.


---

## Nota — rinumerazione globale

Fatta: le slide ora sono **01…55** nell'ordine del deck, senza buchi e senza numeri fuori sequenza. Toccava riparare tre cose insieme — i buchi lasciati dalle slide rimosse (08, 24, 47), le quattro slide spostate in Sezione 5 (che facevano leggere «23 / Sezione 5» dopo «33 / Sezione 4») e le sei slide nuove con la lettera (9b, 9c, 14b…).

**Che cosa è stato riscritto**: 115 `id`, 55 footnote, 296 riferimenti in prosa («Slide N») e 54 voci di elenco in questo file, più le scorciatoie in italiano («la 33», «nella 25») e gli intervalli («16–22») nelle spec.

**Due insidie, per memoria:**

1. **Le slide rimosse.** 8, 24 e 47 non hanno un nuovo numero, ma quei numeri **esistono di nuovo** con altro contenuto: la nuova 24 è «L'attention: a che cosa serve». I riferimenti storici sono stati messi al riparo prima del remap e riscritti **per titolo** — «la ex slide *La conoscenza è nei pesi*» — o marcati *(numerazione precedente)*. Non citarle mai più per numero.
2. **Il doppio remap sugli intervalli.** Un passaggio mappava «Slide 18–20b» sul primo numero e un secondo passaggio lo rimappava di nuovo, producendo «Slide 31–28». Corretti a mano cinque punti, fra cui due che **non erano numeri di slide**: un budget («~22–25 min») e una stima («~6–12 mesi»), finiti nel remap per sbaglio. Se serve rifare una rinumerazione, gli intervalli vanno trattati in un passaggio solo.

**I nomi dei file SVG non sono stati rinumerati** — `slide14-tokenizzazione.svg` resta tale anche se ora è la Slide 17. 48 slide su 55 hanno cambiato numero: legare i nomi dei file alla posizione significherebbe rinominarne cinquanta a ogni riordino, e trascinarsi dietro i nomi delle funzioni nei generatori. Il nome del file identifica **il contenuto** (`tokenizzazione`), non la posizione; la tabella *file → slide* in cima a ogni spec è la traduzione autorevole. Se preferisci allinearli, si fa — ma è una scelta da prendere sapendo che si ripete a ogni riordino.

## Nota — spec riallineate alle slide

Oltre ai numeri, le spec avevano contenuti fermi a prima:

- **Sezione 2**: mancava del tutto il blocco della Slide 9 («Perché serve un secondo addestramento») — quando l'avevo inserita avevo aggiornato solo la tabella. E il golfista era rimasto numerato 10 invece di 11. Corretti entrambi.
- **Sezione 3**: le Slide 40 e 41 (costo del contesto, API stateless) sono uscite, spostate in Sezione 5.
- **Sezione 4**: uscite le Slide 42 e 43; budget da 8 a 6 slide; riscritto il blocco della 37 (RLHF) per la figura rifatta; tolto il riuso del golfista, che ora si disegna solo nella Slide 10.
- **Sezione 5**: rinominata «Lo scenario, più o meno completo»; accolte le quattro slide in arrivo con una nota di provenienza; aggiunto il blocco della Slide 45 (tool e context rot); riscritti i blocchi 47 (reasoning) e 55 (Pareto, con le due accortezze per rifare lo screenshot); dichiarato che il deck non ha più né la formula riletta né la chiusura.

**Controllo finale**: 55 slide nel deck, 55 blocchi nelle spec, nessuna in eccesso, nessuna nella sezione sbagliata, nessuna ancora `#slide-N` rotta. *(Aggiornamento: con la slide di chiusura il deck è passato a **56**; il controllo è stato rifatto e regge — 56 slide nel deck, 56 blocchi nelle spec.)*

---

## Nota — seconda rinumerazione (6 set 2026)

L'inserimento della Slide 39 ha spostato di uno tutte le slide da 40 in su: il deck passa da 56 a **57**, numerate 1…57 senza buchi. Rimappati in un passaggio solo e **in ordine decrescente** — l'errore dell'altra volta era un secondo passaggio che rimappava numeri già cambiati — 17 `id`, 17 `.sid`, 17 footnote e i riferimenti in prosa in deck, spec e in questo file.

**Che cosa è rimasto fermo, di proposito:**

- **I nomi dei file.** `slide23-costo-contesto.svg` resta tale anche se ora è la Slide 40: il nome dice il contenuto, non la posizione. Vale anche per la nuova figura, `slide23c-api-formato.svg`, che sta accanto alle sue sorelle `23` e `23b` invece di chiamarsi `slide40-`.
- **«Slide 47 (numerazione precedente)»**, il blocco della vecchia chiusura rimossa: quel 47 appartiene a una numerazione che non c'è più. Protetto con un sentinella prima del remap.
- **I numeri che non sono slide**: conteggi («da 55 a 56 slide»), minuti, percentuali. Per questo il remap ha girato solo dentro pattern espliciti — `id="slide-N"`, `#slide-N`, `footnote">N /`, `Slide N` — e mai su un numero nudo. Le scorciatoie in minuscolo («la slide 42», «la 44») e le voci di elenco sono state corrette a mano, una per una.

**Anche il 27 ne risente**: le sue spec citavano dieci volte le slide del 26 con numero ≥ 40 (KV cache, curve di costo, context rot, la pila che cresce, la tabella closed/open, il valore delle traiettorie). Aggiornate. Il **deck** del 27 e `fix-incontro-27.md` non sono stati toccati: citano solo slide del 26 sotto la 40.

---

## Nota — terza rinumerazione (7 set 2026)

Lo spostamento della slide 4 in fondo ha scalato di uno tutte le slide da 5 in su: **4 → 57, e 5…57 → 4…56**. Il deck resta a 57 slide, numerate 1…57 senza buchi.

Passaggio **ascendente** questa volta (5→4, poi 6→5, …): ogni passo produce un numero più piccolo di quelli che restano da trattare, quindi nessun numero viene rimappato due volte. Rimappati `id`, `.sid`, footnote, `Slide N` e `slide N` in deck, spec e in questo file; più **26 riferimenti nelle spec del 27** e cinque nel suo deck e nel suo file di fix, che citano le slide del 26 per numero.

**Gli intervalli restano il punto fragile.** Un remap che gira su `Slide N` prende il primo numero di «Slide 25–28» e lascia il secondo: nascono intervalli come «24–28», sbagliati e credibili. Riscritti a mano tutti quelli trovati.

**Trovato per strada un debito più vecchio.** Tre righe di orientamento nella spec della Sezione 3 — *Logica dell'ordine*, *Filo rosso della sezione*, *Direzione di lettura* — erano ferme alla numerazione di **due riordini fa**: parlavano di «14 la tokenizzazione», «15b l'introduzione al fully connected», «la torre (15)». Sono fatte di numeri nudi dentro elenchi, che nessun remap prende. Riscritte coi numeri di oggi. Stessa cosa per due note del relatore: la slide-mappa delle tre fasi («richiamata alle slide 34, 31 e 32» → 34, 36 e 37) e quella dell'architettura («attention (slide 23-20b), fully connected (15b-17)» → 23–27 e 20–22).

**Morale, per la prossima volta**: i numeri di slide dentro elenchi e intervalli o si scrivono in una forma che un remap sappia riconoscere, o non si scrivono. Ogni riordino li lascia indietro, e restano sbagliati finché qualcuno non li rilegge uno per uno.

---


## Fix chiuso — slide 56: la formula come barra di avanzamento del corso

- **56 · La formula, riletta** — `#slide-56` — `slide56-formula-avanzamento.svg` — **NUOVA, in fondo al deck**
	- ✅ FATTO — «Riprendere il diagramma-formula della slide 03 come barra di avanzamento del corso: nel 26 si accende solo il blocco `LLM`, gli altri cinque restano sbiaditi.»
		- La figura **non è ridisegnata**: `Agent`, il segno `=`, i cinque `+`, i sei blocchi e le tre graffe sono le coordinate della slide 3 **copiate**, non ricalcolate. Cambia l'opacità e basta: `<g id="accesi">` (solo `LLM`, fondo `#ecd3de` e bordo burgundy, con la sua graffa *la CPU*) contro `<g id="spenti">` a `opacity="0.3"` (gli altri cinque blocchi e le loro due graffe). I `+` scendono a `0.4`; `Agent` e `=` restano pieni, perché sono l'intestazione della formula e non un termine da accendere.
		- **Sintesi di giornata** sotto il blocco acceso, allineata al suo bordo sinistro: barra verticale burgundy, occhiello *QUELLO CHE ABBIAMO APERTO OGGI*, e le due righe *manipolatore di embeddings · stateless* / *addestrato in tre fasi a volere i tool*.
		- **Legenda** in basso a destra: campione del colore acceso + *acceso = visto in questo incontro*. Nessun cliffhanger in slide, come deciso; in didascalia solo *«Dei sei termini della formula, oggi ne abbiamo aperto uno.»* Il resto è nelle note del relatore.
		- **Contratto scritto dentro il file** (commento in testa) per gli incontri 27 e 28: si parte da questo SVG, si sposta un blocco da `spenti` ad `accesi`, si riscrive la sola sintesi, e nient'altro si muove.
	- ⚠️ **Una deroga, dichiarata: il viewBox non è identico.** Il fix chiedeva «stesso viewBox e stessa posizione dei blocchi». La posizione dei blocchi è identica al pixel; il canvas invece è **1302×428** contro i 1302×334 della slide 3, perché la sintesi di giornata sotto `LLM` non ci stava (sotto la graffa restavano 22px). Allargare in basso non tocca l'origine né la geometria, quindi il vincolo che conta — *i blocchi non si muovono fra un incontro e l'altro* — regge; ed è **questo** il canvas che il 27 e il 28 devono riusare.
		- **Verificato a schermo che l'effetto non si rompe**: entrambe le figure sono vincolate in larghezza e rendono a **1140px CSS** — slide 3 e slide 56 disegnano i blocchi esattamente alla stessa scala, che è la condizione perché il richiamo funzioni. Se un domani si aggiunge testo alla 57, questa misura va ricontrollata (è lo stesso inciampo della slide 10).
	- ⚠️ Il deck passa da 55 a **56 slide**. Aggiornati: tabella file → slide e blocco della slide nella spec della sezione 5, budget della sezione (16 → 17 slide) e la nota di chiusura, che diceva il contrario («il deck non ha più né la formula riletta né la chiusura»). Il vecchio blocco della *Slide 47 (numerazione precedente)* resta nella spec come traccia storica, ma ora descrive **solo il cliffhanger**, che è l'unica cosa davvero rimossa: la formula riletta è tornata, non più tipografica ma come diagramma.

## Fix chiuso — slide 03: CPU, sistema operativo, software

- **03 · Un agente è un sistema composto** — `#slide-3` — `slide3-formula-agent.svg`
	- ✅ FATTO — Le graffe passano da due a **tre**: *la CPU* sotto il solo `LLM`, *il sistema operativo* sotto il solo `Harness`, *il software installato* sotto i quattro termini restanti. La terza graffa è invariata; le due nuove sono la stessa forma su un blocco solo.
	- ✅ FATTO — Nota in basso → *«L'LLM è la CPU, l'harness il sistema operativo. Il resto è il software che, a parità di macchina, organizza il lavoro a seconda dell'obiettivo.»*
	- I sei blocchi **non si sono spostati di un pixel**, come richiesto: è la condizione perché la figura resti sovrapponibile alla 57 e alle versioni degli incontri 27 e 28.
	- ⚠️ **Un dettaglio di misura.** Le etichette *la CPU* e *il sistema operativo* stanno sotto due blocchi adiacenti larghi 150: a 24pt si sarebbero quasi toccate. Portate a **21**, lo stacco è netto (verificato a schermo). Se una delle due etichette si allunga, il corpo va ricontrollato.
	- Aggiornato il blocco della Slide 3 nella spec della sezione 1: layout, nota, descrizione del visual e prompt SVG (tre graffe), più il perché della metafora a tre livelli — il 27 apre con «oggi apriamo il sistema operativo», e quella frase regge solo se il sistema operativo è l'harness da solo.

---

## Controllo

- **59 slide** nel deck (`<section id="slide-…">`), **59 blocchi** nelle spec.
- Numerazione: 1…57 più **35b** e **36b**, inserite col suffisso senza rinumerare nient'altro.
- **`id`, footnote e `.sid` coerenti** su tutte e 59.
- **Nessuno sforo di testo** in tutto il deck: controllate `section`, `.content`, `.col-text`, `.cols` e `.tv` di tutte e 65 le sezioni (59 slide + copertina + 5 separatori) — zero.
- **Sezioni**: 1 = 1–3 · 2 = 4–10 · 3 = 11–32 · 4 = 33–38 (con 35b e 36b) · 5 = 39–56 · chiusura fuori sezione = 57.
- Le tre slide-anello (35b, 36b, 38) condividono geometria identica.
- Slide 3 e slide 56 rendono la formula a **1140px CSS** entrambe.
- Slide 17 (tokenizzazione): viewBox `784×416`, vincolata in larghezza, 94px di margine.
- Slide 37 (RL agentico): viewBox `1120×560`, vincolata in larghezza, rende a **763,9px**.
- Slide 39 (API): la figura rende **1:1**, 1140×380, monospaziato a 12px CSS.
- `regen.py` idempotente: generatori e SVG della Sezione 3 sono allineati.
