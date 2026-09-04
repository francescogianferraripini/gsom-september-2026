# Slide realizzate — Incontro 26

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation/presentation.html`, figure usate.
Per commentare, scrivi sotto la riga della slide.

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
- **04 · Il ruolo dell'harness** — `#slide-4` — `slide4-ruolo-harness.svg`
	- ✅ FATTO — *Figura* riprogettata: i blocchi intorno all'LLM sono raggruppati in 3 categorie distinte da colori
		- **Context management** (teal `#1ab197` su `#d1efea`): Context Initialization · Context Optimization (compaction, pruning, etc.) · Memory management · Skill management
		- **Agentic loop management** (lightblue `#4da0d7` su `#dbecf7`): blocco unico, con l'anello del loop che racchiude l'LLM
		- **Environment management** (giallo `#ffbe0b` su `#fff2ce`): Tool Calling execution and response management · Execution Sandbox · Skill execution management
		- Rimosso il blocco titolo "Harness — l'esoscheletro (simbolico)". viewBox ora `0 0 1000 714`.

## Separatore di sezione — «L'LLM: cos'è e come genera»
`#div-sec2`

- **05 · Che cos'è un modello linguistico** — `#slide-5` — `slide5-modello-linguistico.svg`
	- ✅ FATTO — Nota → "Prevedere bene significa comprimere bene." (rimosso ": non è una metafora, è un teorema. Lo ritroveremo.")
- **06 · La generazione: un token alla volta** — `#slide-6` — `slide6-generazione-autoregressiva.svg`
	- ✅ FATTO — Didascalia: aggiunto in coda "Da questo punto di vista il modello è stateless e ragiona solo in termini di parola successiva."
- **07 · Il golfista** — `#slide-7` — `slide7-golfista.svg`
	- ✅ FATTO — *Figura* i colpi ora riflettono i colpi tipici: gittate decrescenti 390 / 270 / 170 / 80 (atterraggi a x = 560, 830, 1000, 1080) e apici decrescenti in modo monotono (y = 42, 162, 267, 362). L'etichetta `colpo 4` è sfalsata più in basso con linea di richiamo, per non collidere con `colpo 3`.
	- ⚠️ La stessa scena è duplicata dentro `slide31-rlhf.svg`: aggiornata anche lì (archi, palline, etichette e le 4 linee di mira verso la buca).
- **~~08~~ · Il 1° loop: la generazione** — *(numerazione precedente; slide rimossa)* — *nessuna figura*
	- ✅ FATTO — SLIDE RIMOSSA. (Conteggio aggiornato dopo il secondo giro di fix: il deck sta ora a **59** slide — 57 iniziali, meno la 08 e la 24, più le quattro nuove 14b / 15b / 17b / 23b.)
	- ⚠️ Gli `id` e i numeri in footnote delle slide successive **non** sono stati rinumerati: `#slide-8` resta `#slide-8` e la sua footnote resta `09`. Rimane quindi un buco sul numero 08. Rinumerare avrebbe invalidato tutte le ancore citate in questo file e nelle spec (e il deck già usa etichette non sequenziali tipo `10b`, `11b`, `20b`). Se preferisci la numerazione contigua, va fatta come passo a sé su tutto il deck.
- **08 · Il 2° loop: la conversazione** — `#slide-8` — `slide9-comparazione-loop.svg`
	- ✅ FATTO — Ora è una slide di comparazione a due metà dentro un unico SVG a piena larghezza (viewBox `0 0 1140 356`, rapporto allineato allo slot per non scalare i testi).
		- **A sinistra** — «IL 1° LOOP — LA GENERAZIONE»: la pila della frase sul gatto ricopiata da `#slide-6` (stessi colori, stesso badge STOP), con graffa "il contesto cresce di un token per volta".
		- **A destra** — «IL 2° LOOP — LA CONVERSAZIONE»: tre turni, ognuno col payload completo rispedito all'API; le righe dei turni passati sono sbiadite, la risposta appena generata è una pill burgundy. Graffa "la storia cresce di un turno per volta". Adattato dagli SVG `slide12-conversation-step{1,2,3}.svg` del deck `gsom-april-2026` (recuperati dal repo locale invece che dall'URL).
		- Rimossi dalla slide lo pseudocodice e il diagramma dei due anelli annidati; la nota-seme sul 3° loop resta.
	- ⚠️ `slide9-secondo-loop.svg` (i due anelli annidati) non è più referenziato da nessuna slide. Non l'ho cancellato: dimmi se vuoi rimuoverlo.
	- ✅ FATTO — «aggiungi il blocco con il system prompt»
		- `[system] Sei un assistente utile.` è ora la **prima riga dentro ciascuno dei tre riquadri**, non una nota a parte: è quello che significa «rispedita per intero», e ora figura e didascalia dicono la stessa cosa. La didascalia mette in grassetto *system prompt in testa*.
	- ✅ FATTO — cliffhanger rimosso (come da tua indicazione)
		- La nota era: *«Il 3° loop non si aggiungerà in coda: si infilerà in mezzo. Lo vedremo nascere oggi, e lo apriremo al prossimo incontro.»* Ora è: *«Dentro un turno, però, non c'è per forza una sola generazione del modello. È la prossima slide.»* — passaggio diretto alla 9.



- **09 · Il 3° loop: la tool call** — `#slide-9` — `slide9b-tool-call.svg` — **NUOVA**
	- ✅ FATTO — «aggiungi una slide qui. Il terzo loop, il tool call. Prendi l'svg a destra di `#slide-8` e affiancalo ad un altro svg che fa vedere un esempio di conversazione con tool call nel flow. metti in una zona del system prompt la dichiarazione del tool (ne mettiamo uno solo per semplicità).»
		- **Metà sinistra**: è, identica, la metà destra della 8 — i tre turni, un giro di generazione ciascuno. Intestazione «SENZA TOOL». La citazione letterale è voluta: chi guarda riconosce la figura di due minuti prima e vede solo che cosa cambia.
		- **Metà destra**: «CON UNA TOOL CALL», due riquadri `giro 1` e `giro 2` **dentro un solo turno** dell'utente (una graffa a lato lo dichiara). Il `[system]` porta su una seconda riga indentata la dichiarazione del tool: `Tool: cerca_ordine(id_ordine) — stato di un ordine`. Un tool solo, come chiesto.
		- Il flusso: `giro 1` finisce con la richiesta del modello — `→ cerca_ordine("4471")` — e lì il modello si ferma; `giro 2` ha in più la riga `[tool]` col risultato e la risposta finale.
		- La riga `[tool]` è in **teal con fondo tinta**, colore diverso da quello del modello: non l'ha generata lui, l'ha appesa qualcun altro. È il punto della slide, e si legge dal colore prima che dal testo. Sotto, i tre passi del giro (① chiede e si ferma · ② qualcun altro esegue e appende · ③ riparte).
		- ⚠️ **Da risolvere, come d'accordo**: la **slide 39** («Nasce il 3° loop», sezione 4) copre ancora gli stessi punti meccanici — *la tool call è testo*, *i tool vanno dichiarati*, *il giro* — ed è ora in buona parte un doppione della 9. Va rifocalizzata sul solo lato RL (da dove viene la capacità) oppure rimossa. Annotato anche nella spec della sezione 2.

- **10 · Perché serve un secondo addestramento** — `#slide-10` — `slide9c-secondo-addestramento.svg` — **NUOVA**
	- ✅ FATTO — «per introdurre la mira, riporta qui la slide …/slide-secondo-addestramento adattandola»
		- Ripresa dal repo locale (`slide14-secondo-addestramento.html` + `slide14-rlhf-comparison.svg`) e **riportata alla palette e ai font di questo deck**: quella di aprile era in Arial su fondi grigi. Lo stesso prompt — *«Come posso aumentare le vendite?»* — dato a due modelli: a sinistra il modello base continua il testo con altre domande (monospaziato, sbiadito, come un testo del web), a destra risponde (Poppins, bordo burgundy).
		- Chiusa col blocco nero centrato: *«Da «cosa è probabile» a «cosa serve rispondere».»* — riusa la classe `.nota.dark.center` introdotta per la slide 1.
	- ⚠️ **Il golfista è slittato a `#slide-11`** (file `slide9d-golfista-mira.svg`), perché questa si inserisce prima. Aggiornati id, footnote e i commenti di sincronizzazione nei tre file del golfista.


- **10 · Il colpo non basta: serve la mira** — `#slide-10` — `slide9c-golfista-mira.svg` — **NUOVA**
	- ✅ FATTO — «porta in una nuova slide qui una copia del golfista di slide 37, spiegando che per fare il secondo ed il terzo loop è necessario un training successivo al pretraining con cui aggiungere la mira, ottimizzando non il prossimo token solo sul contesto precedente, ma sul percorso sequenziale autoregressivo lungo la traiettoria»
		- La vignetta è **la stessa della slide 7** — stesso viewBox, stessi archi, stesso golfista — con in più il gruppo `mira` e la buca in primo piano, presi pari pari dalla 37. Al posto di *«la buca? / per ora, nessuna mira»*, **nello stesso angolo**, ora si legge *«ora ogni colpo mira alla buca / e a essere ottimizzato è il percorso, non il singolo colpo»*.
		- Didascalia col tuo testo: il pretraining insegna il colpo (prossimo token sul contesto precedente, nient'altro); un turno di conversazione o un giro di tool call hanno una meta; serve un addestramento **dopo** il pretraining che ottimizzi il percorso autoregressivo lungo l'intera traiettoria.
		- ⚠️ **Un dettaglio che ho dovuto misurare.** Perché il richiamo funzioni la vignetta deve rendersi *della stessa dimensione* della slide 7. Il viewBox è 2.6 di rapporto in uno slot da ~3.0, quindi è vincolata in **altezza**: ogni riga di testo sotto le ruba larghezza in proporzione 1:2.6. Con la mia prima stesura (didascalia di 4 righe a 12.5pt + una nota) la vignetta scendeva a **757px** contro i **1026px** della slide 7 — un −26% che si vedeva, e leggeva come un disegno diverso. Ho tolto la nota (il rimando alla sezione 4 è passato nelle note del relatore, come fa la slide 7 col suo) e portato la didascalia a 11.5pt: ora è a **1013px**. Se ci aggiungi testo, ricontrolla questa misura.
	- ⚠️ **La scena del golfista è ora in TRE file**: `slide7-golfista.svg` (senza mira), `slide9c-golfista-mira.svg` e il gruppo `scena-golfista` dentro `slide31-rlhf.svg`. Ho aggiornato i commenti di sincronizzazione in tutti e tre: se cambiano terreno, atterraggi, archi o buca, vanno cambiati ovunque. Era già due; ora è tre, ed è il punto più fragile del deck.
	- ⚠️ **Si aggiunge alla questione aperta della 39**: ora la sezione 2 anticipa **due** slide della sezione 4 — la **33** (meccanica della tool call, doppione della 9) e la **31** (stessa vignetta, stesso messaggio «la mira arriva dopo»). Quello che resta solo alla sezione 4 è il *come*: preferenze umane e reward model (31), RL sulle traiettorie (32), la chiusa sull'harness (33). È lì che vanno rifocalizzate.

## Separatore di sezione — «Perché funziona»  
`#div-sec3`

- **12 · La base di tutto: a ogni parola il suo vettore** — `#slide-12` — `slide10-parola-vettore.svg`
- **13 · Che cos'è un vettore** — `#slide-13` — `slide10b-che-cos-e-un-vettore.svg`
- **14 · Vettori e prodotto scalare** — `#slide-14` — `slide11-vettori-prodotto-scalare.svg`
- **15 · La somma: spostarsi nello spazio** — `#slide-15` — `slide11b-somma-vettori.svg`
- **16 · La scala del calcolo: vettori e matrici** — `#slide-16` — `slide12-scala-del-calcolo.svg`
- **17 · Embeddings: lo spazio delle idee** — `#slide-17` — `slide13-embeddings.svg`
- **18 · La tokenizzazione** — `#slide-18` — `slide14-tokenizzazione.svg`
	- ✅ FATTO — Figura: mettere tra le parole e i blocchi con la parola e l'id (ad esempio tra "Il" ed "Il 243") la grande matrice monoriga di lookup degli encoding
		- Aggiunta una **fascia sottile** fra il testo grezzo e le tessere: strip grigio alto 30, 7 celle larghe quanto il contenuto (voce in mono + id sotto), `⋯` ai due estremi **e nei vuoti fra le celle** — così si legge come il troncone di una tabella da centomila voci, e le tre celle della parola rara risultano *sparse*, non contigue. Le frecce ora sono due per token: testo grezzo → cella → tessera, grigie per i comuni e burgundy per i tre della parola rara.
		- Id riusati esattamente quelli già nel generatore: `243`, `28741`, `1274`, `553`, `11621`, `45093`, `30818`. Etichetta di gutter `encoding` / *~100.000 voci*. viewBox `0 0 784 368` (era 700×322).
		- Rimossa la vecchia etichetta in alto a destra *"id da un vocabolario fisso di ~100.000 voci"*: era diventata un doppione di quella della fascia, e il bullet della slide lo dice già.
		- ⚠️ **Da guardare: la fascia duplica le tessere.** Strip e tessera portano ora lo stesso contenuto (`Il` + `243`) una sopra l'altra. È strutturalmente giusto — la strip è il vocabolario, la tessera è il token che ne esce — ma a occhio si legge come la stessa cosa scritta due volte. **Proposta**: togliere l'id dalla tessera e lasciarlo solo nella strip, così la strip diventa *il posto da cui viene l'id* e la tessera tiene solo il testo. Non l'ho fatto perché la spec ha una decisione esplicita in senso opposto («l'id sta dentro la tessera: una tessera è un oggetto solo»). Dimmi tu.
		- ⚠️ La spec portava una *Nota di revisione* di segno opposto: una versione precedente aveva un grande rettangolo-vocabolario **in cima**, tolto perché era «l'elemento più grande e il meno informativo». La fascia nuova è lo stesso oggetto in forma diversa (sottile, dentro il flusso invece che sopra) e quel difetto non lo ha; nota aggiunta anche nella spec.
		- ⚠️ Il gutter dell'etichetta ha allargato il viewBox dell'11%: a schermo tutto rimpicciolisce di altrettanto, e gli id dentro le tessere scendono a ~8.6px CSS su slide da 1280. Leggibili in proiezione, ma è il testo più piccolo della sezione.

- **19 · Cosa serve, per prevedere la parola successiva** — `#slide-19` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «Qui vorrei fare una slide nuova di introduzione all'architettura, solo testo riportato verbatim»
		- Testo riportato **verbatim**, spezzato solo per il layout: frase di apertura in evidenza, i tre punti come bullet (il nome del meccanismo — attention / fully connected layers / blocchi con skip connection — in burgundy in coda a ciascuno), e le due frasi finali come due blocchi grigi affiancati, etichettati *il vincolo del calcolo* e *il vincolo del dataset*.
		- Titolo scelto da me (non era nel fix): **«Cosa serve, per prevedere la parola successiva»**. Cambialo se preferisci.
		- Questa slide diventa il **riferimento** che la 21 e la 24 richiamano: se ne cambi il testo, va cambiato anche il richiamo là.

- **20 · L'architettura, in un colpo d'occhio** — `#slide-20` — `slide15a-scatola-nera.svg`, `slide15b-torre.svg`, `slide15c-torre-aperta.svg`
	- *(non toccata)*

- **21 · Il fully connected: fanout, gate, compressione** — `#slide-21` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «Qui inserire una slide di introduzione al fully connected layer, facendo vedere che è la combinazione di una parte di fanout, non linearità, compressione. ricorda la finalità dalla slide introduttiva della sezione»
		- Apre richiamando **alla lettera** la seconda capacità della 19 («conoscenza fattuale su tutti i domini dello scibile»), poi i tre stadi come tre colonne numerate — Fanout / Non linearità / Compressione — ognuna col rimando alla slide che la apre (16, 16, 17).
		- Solo testo, nessuna figura: le due slide dopo disegnano gli stessi tre stadi per esteso, anticiparli li brucerebbe.
	- ✅ **Qui è finita la ex slide «La conoscenza è nei pesi»** — vedi sotto.

- **22 · Fanout: il matching concettuale** — `#slide-22` — `minimap-fc.svg`, `slide16-fanout.svg`
	- ✅ FATTO — Figura: rendi graficamente evidente il passaggio dalla relu
		- La ReLU è ora disegnata **come funzione**, in un riquadro-inset nel gutter all'altezza della barra del gate: spezzata piatta sotto zero e diagonale a 45° sopra, assi `in`/`out`, zero marcato, e due punti campione — uno pieno sul ramo diagonale (passa), uno vuoto sul ramo piatto (azzerato). L'etichetta del gutter diventa `non linearità · ReLU`.
		- Scelta di progetto: la spezzata **non** è dentro la barra con le colonne appoggiate sopra, perché la batteria è ordinata per concetto e l'asse x di una ReLU è il valore in ingresso. Farle coincidere richiederebbe di riordinare le colonne per attivazione crescente, cambio più grosso di quanto chiesto e che romperebbe la continuità con le barre della 23.
	- ✅ FATTO — *Testo* allineato: il terzo bullet ora dice «**La non linearità è un gate: la ReLU** — sotto zero azzera, sopra zero lascia passare invariato».

- **23 · Compressione: la sovrapposizione** — `#slide-23` — `minimap-somma.svg`, `slide17-compressione.svg`
	- ✅ FATTO — Figura: rimuovi lo spazio delle idee e la skip connection. il ruolo di questa slide è far capire che i tanti rilevatori semantici scattati dopo la non linearità vengono compressi in un vettore di dimensione 4
		- Via il piano punteggiato con le due nuvole, via il punto che si sposta, via il nodo `+` e l'embedding originale in ingresso. Resta il solo collo di bottiglia: **sette** barre burgundy (le prime tre con gli stessi nomi delle sopravvissute della Slide 22, per continuità) che convergono in **un unico vettore da 4 celle**, con l'annotazione *molti rilevatori accesi → quattro celle*.
		- viewBox da 700×440 a **700×322**: con la scena in cima rimossa il disegno si è accorciato di un terzo.
		- Ho anche **levato dalla figura** il titolo *Da migliaia a quattro* e la frase sulla sovrapposizione: erano già i due bullet dell'HTML, e a schermo si leggevano due volte.
	- ✅ FATTO — *Testo* rifatto: i due bullet ora sono «**Da migliaia a quattro**» e «**La sovrapposizione**»; la nota rimanda il nodo `+` alla Slide 20, dove è disegnato al posto suo.

- **24 · L'attention: a che cosa serve** — `#slide-24` — *nessuna figura* — **NUOVA**
	- ✅ FATTO — «qui aggiungi una introduzione alla attention, solo testo, ricordando la finalità del blocco dall'introduzione generale»
		- Apre richiamando **alla lettera** la prima capacità della 19, poi il punto che conta («è l'unico posto in cui le corsie si parlano»), poi i tre passi come tre colonne numerate — Q·K / softmax / V — col rimando a 18, 19, 20.

- **25 · Attention: domande e chiavi** — `#slide-25` — `minimap-attn.svg`, `slide18-griglia-qk.svg`
	- ✅ FATTO — Figura: sposterei le piccole matrici Wk e Wq sul lato destro, ed è l'embedding più a destra, sopra calcio, ad essere collegato a Wq. non penso ci sia necessità di freccia che collega Wq a Wk
		- Le tre matrici 4×3 sono ora impilate **sul lato destro**, fuori dalle colonne dei token: `× W^V` in alto, poi `× W^K`, `× W^Q` in basso, con l'etichetta *tre proiezioni dello stesso embedding*. `W^Q` è alimentata dalla sola colonna `calcio`, la più a destra. Il collegamento `W^Q`→`W^K` è stato rimosso.
		- viewBox della griglia da 700×440 a **756×440** (allargata in larghezza, dove c'era margine, non in altezza).
		- ⚠️ L'agente è stato **fermato durante la sua verifica finale**, quindi il controllo l'ho rifatto io: verificato a schermo su 18, 20 e sul secondo tempo della 27, viewBox coerenti fra tutte e cinque le uscite, nessuno sforo in tutto il deck. Le 19 e 20b hanno ereditato lo spostamento (griglia condivisa) ma **non le ho guardate una per una**.

- **26 · Softmax: il budget di ascolto** — `#slide-26` — `minimap-attn.svg`, `slide19-griglia-softmax.svg`
	- *(non toccata direttamente: erediterà lo spostamento delle matrici dalla 25)*

- **27 · V: il contenuto del libro** — `#slide-27` — `minimap-attn.svg`, `slide20-griglia-v.svg`, `slide20-multihead.svg`
	- ✅ FATTO — Titolo: applicare il contenuto del libro
		- «V: la consegna» → **«V: il contenuto del libro»**, che riprende alla lettera la metafora della biblioteca fissata nella Slide 25 (Q = la richiesta al banco, K = l'etichetta sul dorso, V = il contenuto del libro).
	- ✅ FATTO — secondo visual al click che fa vedere le tante heads, col testo che compare contestualmente
		- HTML: la slide ora è a due tempi (`.visual.stack` + `fragment`), e il secondo SVG si sovrappone al primo con lo stesso viewBox, così al click nulla si sposta. Il testo — «Tanti blocchi attention sono applicati in parallelo, per modellare relazioni diverse e estrarre semantiche differenti dal contesto precedente» — è legato allo **stesso** `data-fragment-index`, quindi compare insieme al visual e non un click dopo.
		- `slide20-multihead.svg` creato, stesso viewBox 756×440 della griglia base: `testa 1` in primo piano è la griglia completa, dietro `testa 2 · sintassi`, `testa 3 · riferimenti`, `testa 4 · tono` sfalsate in profondità, più `⋯`. Verificato a schermo: al click la sovrapposizione registra, niente si sposta, e la caption compare insieme al visual.

- **28 · Lo stesso token, due contesti** — `#slide-28` — `minimap-attn.svg`, `slide20b-contesto-frase1.svg`, `slide20b-contesto-frase2.svg`
	- *(non toccata direttamente: erediterà lo spostamento delle matrici dalla 25)*
- **29 · Positional encoding: l'ordine conta** — `#slide-29` — `minimap-pos.svg`, `slide21-positional-encoding.svg`
- **30 · Reverse embedding: tornare ai token** — `#slide-30` — `minimap-testa.svg`, `slide22-reverse-embedding.svg`
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

- **31 · L'LLM come compressore lossy** — `#slide-31` — `slide25-compressore-lossy.svg`
- **32 · Conseguenze della compressione** — `#slide-32` — *nessuna figura*
- **33 · MoE: non tutti i pesi lavorano sempre** — `#slide-33` — `minimap-fc.svg`, `slide27-moe.svg`

## Separatore di sezione — «Come viene addestrato»  
`#div-sec4`

- **34 · Le tre fasi** — `#slide-34` — `slide28-tre-fasi.svg`
- **35 · Pretraining: indovinare il prossimo token** — `#slide-35` — `slide29-pretraining.svg`, `slide29-scala-dati.svg`
- **36 · Gradient descent: sbaglia, misura, correggi** — `#slide-36` — `slide30-gradient-descent.svg`
- **37 · RLHF: arriva la mira** — `#slide-37` — `slide31-rlhf.svg`
	- ✅ FATTO — «in questo visual, fai vedere una domanda e due esempi reali di risposta»
		- I riquadri A/B erano segnaposto (tre righe grigie) a 15px dentro un SVG largo 1550, che in slide diventavano **~6.8px**: sotto il minimo leggibile del deck. Per starci con del testo vero serviva spazio, e l'hai deciso tu: **via il golfista dalla 37**.
		- Ora il meccanismo occupa tutta la larghezza. A sinistra la domanda — *«Come posso aumentare le vendite?»* — e le due risposte per esteso, A col bordo burgundy e il segno di scelta; a destra la catena *preferenze → reward model → reward → modello*; sotto, il callout invariato. Il testo delle risposte rende ora a **12.5px** in slide, contro i 6.8 di prima.
		- **Le due risposte sono le stesse della 10**, di proposito: là erano il prima e il dopo dell'addestramento, qui sono la coppia che gli umani confrontano. Stesso esempio, due letture — il primo bullet della 37 ora lo dichiara.
		- Layout della slide da `tv-35` a `tv-30`, perché la figura è diventata orizzontale.
		- ⚠️ Il golfista è così sceso da tre copie a **due**: `slide7-golfista.svg` (senza mira) e `slide9d-golfista-mira.svg` (con). La 37 non lo disegna più.
- **38 · RL agentico: traiettorie** — `#slide-38` — `slide32-rl-agentico.svg`
- **39 · Nasce il 3° loop** — `#slide-39` — `slide33-terzo-loop.svg`


## Separatore di sezione — «Lo scenario, più o meno completo»
	- ✅ FATTO — titolo cambiato. Il separatore ora dice «Lo scenario, / più o meno completo» e il sottotitolo elenca anche il costo del contesto. Gli eyebrow di tutte le slide della sezione sono passati a `SEZIONE 5 · LO SCENARIO, PIÙ O MENO COMPLETO`.
	- ✅ FATTO — **spostate qui 23, 23b, 34 e 35**, in quest'ordine, prima della 44. Eyebrow e footnote aggiornati a «Sezione 5».
		- ⚠️ **La numerazione ora è fuori ordine e si vede**: dopo «33 / Sezione 4» il pubblico legge «23 / Sezione 5», poi 23b, 34, 35, 36… Non ho rinumerato perché toccherebbe tutte le ancore citate in questo file e nelle spec. Ma con la 08 e la 24 rimosse, sei slide nuove aggiunte e ora quattro spostate, **una passata di rinumerazione globale è diventata la cosa giusta da fare**: dimmi quando e la faccio in un colpo solo, aggiornando anche fix e spec.
		- ⚠️ La 40 si porta dietro la mini-mappa «sei qui» della torre (`minimap-corsie.svg`), che è un dispositivo della sezione 3. In sezione 5 non è sbagliata — rimanda comunque all'architettura — ma è l'unica slide della sezione ad averla.
`#div-sec5`

**23 · Il contesto ha un costo** — `#slide-40` — `minimap-corsie.svg`, `slide23-costo-contesto.svg`
	- ✅ FATTO — «esplicita che salvando nella KV cache i valori, per ogni testa e blocco, delle attivazioni K e V si evita tutto il passaggio dai fully connected layer (molto costoso) e la moltiplicazione di Wq, Wk e Wv di tutti i token precedenti. se non è corretto dimmelo.»
		- **È corretto, tranne un punto: le Wq.** La cache non "evita" le Q dei token precedenti — quelle Q semplicemente **non servono più**. La query di un token serve solo a calcolare l'output *di quel token*, che con la masked attention non può più cambiare: in prefill vengono calcolate e buttate (è già quello che dice il pannello sinistro della figura), in decoding non vengono calcolate affatto. Tutto il resto sì: la cache evita, per i token già visti, le proiezioni W^K e W^V **e** l'intero passaggio dai fully connected layer — ed è quest'ultimo la voce di costo più grossa, perché il FFN è la maggior parte dei parametri di un blocco. Per il token nuovo si paga tutto una volta: W^Q, W^K, W^V e FFN.
		- Testo in slide riscritto con questa distinzione; la precisione completa è finita anche nella spec, come nota.
		- ⚠️ La slide sforava di parecchio con il testo in più: colonna portata a `pts micro` e nota a `nota small`. Verificato: nessuno sforo.
	--> spostare da sezione precedente
- **41 · L'API è stateless: cosa significa davvero** — `#slide-41` — `slide23b-curve-costo.svg` — **NUOVA**
	- ✅ FATTO — «Qui aggiungi la slide presa da qui: …/gsom-april-2026/lezione-mba/presentation.html#/slide-api-stateless»
		- Ripresa dal repo locale `gsom-april-2026` (`slide18-api-stateless.html`) invece che dall'URL. Le tre curve di costo sono state **riadattate** alla palette e ai font di questo deck in `slide23b-curve-costo.svg`: quella di aprile aveva fondo `#f2f2f2` e font sans-serif generici.
		- ⚠️ Sovrapposizione da valutare: la **slide 42** («Il modello è stateless: il contesto è tutto», sezione 4) dice una cosa vicina, dal lato del modello. Qui l'ho impostata come "lo stesso costo visto dalla conversazione e dalla bolletta" e l'ho dichiarato nelle note del relatore, ma se vuoi le si può fondere.
	--> spostare da sezione precedente

- **42 · Il modello è stateless: il contesto è tutto** — `#slide-42` — `slide34-stateless.svg`
	- spostare da sezione precedente
- **43 · Il modello è figlio dei suoi training set** — `#slide-43` — *nessuna figura*
	- spostare da sezione precedente

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


---

## Nota — rinumerazione globale

Fatta: le slide ora sono **01…55** nell'ordine del deck, senza buchi e senza numeri fuori sequenza. Toccava riparare tre cose insieme — i buchi lasciati dalle slide rimosse (08, 24, 47), le quattro slide spostate in Sezione 5 (che facevano leggere «23 / Sezione 5» dopo «33 / Sezione 4») e le sei slide nuove con la lettera (9b, 9c, 14b…).

**Che cosa è stato riscritto**: 115 `id`, 55 footnote, 296 riferimenti in prosa («Slide N») e 54 voci di elenco in questo file, più le scorciatoie in italiano («la 33», «nella 25») e gli intervalli («16–22») nelle spec.

**Due insidie, per memoria:**

1. **Le slide rimosse.** 8, 24 e 47 non hanno un nuovo numero, ma quei numeri **esistono di nuovo** con altro contenuto: la nuova 24 è «L'attention: a che cosa serve». I riferimenti storici sono stati messi al riparo prima del remap e riscritti **per titolo** — «la ex slide *La conoscenza è nei pesi*» — o marcati *(numerazione precedente)*. Non citarle mai più per numero.
2. **Il doppio remap sugli intervalli.** Un passaggio mappava «Slide 18–20b» sul primo numero e un secondo passaggio lo rimappava di nuovo, producendo «Slide 31–28». Corretti a mano cinque punti, fra cui due che **non erano numeri di slide**: un budget («~22–25 min») e una stima («~6–12 mesi»), finiti nel remap per sbaglio. Se serve rifare una rinumerazione, gli intervalli vanno trattati in un passaggio solo.

**I nomi dei file SVG non sono stati rinumerati** — `slide14-tokenizzazione.svg` resta tale anche se ora è la Slide 18. 48 slide su 55 hanno cambiato numero: legare i nomi dei file alla posizione significherebbe rinominarne cinquanta a ogni riordino, e trascinarsi dietro i nomi delle funzioni nei generatori. Il nome del file identifica **il contenuto** (`tokenizzazione`), non la posizione; la tabella *file → slide* in cima a ogni spec è la traduzione autorevole. Se preferisci allinearli, si fa — ma è una scelta da prendere sapendo che si ripete a ogni riordino.

## Nota — spec riallineate alle slide

Oltre ai numeri, le spec avevano contenuti fermi a prima:

- **Sezione 2**: mancava del tutto il blocco della Slide 10 («Perché serve un secondo addestramento») — quando l'avevo inserita avevo aggiornato solo la tabella. E il golfista era rimasto numerato 10 invece di 11. Corretti entrambi.
- **Sezione 3**: le Slide 40 e 41 (costo del contesto, API stateless) sono uscite, spostate in Sezione 5.
- **Sezione 4**: uscite le Slide 42 e 43; budget da 8 a 6 slide; riscritto il blocco della 37 (RLHF) per la figura rifatta; tolto il riuso del golfista, che ora si disegna solo nella Slide 11.
- **Sezione 5**: rinominata «Lo scenario, più o meno completo»; accolte le quattro slide in arrivo con una nota di provenienza; aggiunto il blocco della Slide 45 (tool e context rot); riscritti i blocchi 47 (reasoning) e 55 (Pareto, con le due accortezze per rifare lo screenshot); dichiarato che il deck non ha più né la formula riletta né la chiusura.

**Controllo finale**: 55 slide nel deck, 55 blocchi nelle spec, nessuna in eccesso, nessuna nella sezione sbagliata, nessuna ancora `#slide-N` rotta.
