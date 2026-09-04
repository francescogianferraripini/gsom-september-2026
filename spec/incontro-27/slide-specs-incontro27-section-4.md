# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 4 — Context management: la finestra che cresce**
**Obiettivo di apprendimento**: il partecipante sa leggere l'anatomia della finestra a un giro qualsiasi (prefisso, storia, risultati), sa spiegare perché il prefisso non si tocca e perché ogni definizione in più si paga anche se non usata, conosce le tre tecniche di governo del contesto (pruning, compaction, offload), sa che cosa sopravvive fra una sessione e l'altra e in che forma, e sa che la memoria è esposta al modello come un tool.
**Messaggio chiave (takeaway)**: Il contesto è una risorsa scarsa che l'harness amministra: decide cosa entra, cosa esce, cosa si riassume e cosa finisce su un file. Quando finisce su un file, è diventato memoria.
**Budget**: ~25 min, 11 slide + separatore. Ripartizione: skill vs MCP 2, anatomia 1, costo 2, degrado 1, tecniche 2, memory 3.
**Nota di perimetro**: la slide-ponte al 28 ("memoria di un agente e KB di un'organizzazione sono lo stesso problema a scale diverse", con i quattro requisiti) è stata **tolta** in intervista: il ponte al 28 resta nella chiusura (sezione 7).
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec4.html` | Separatore — Sezione 4: Context management |
| `slides/slide29-costo-fisso-richiesta.html` | Slide 29 — Costo fisso e costo a richiesta |
| `slides/slide30-quando-conviene.html` | Slide 30 — Quando conviene cosa |
| `slides/slide31-finestra-giri.html` | Slide 31 — La finestra a ogni giro: tre parti, tre velocità |
| `slides/slide32-prefix-caching.html` | Slide 32 — Il prefisso non si tocca: prefix caching |
| `slides/slide33-cache-regole.html` | Slide 33 — Che cosa rompe la cache |
| `slides/slide34-context-rot.html` | Slide 34 — Non basta che ci stia: il context rot |
| `slides/slide35-pruning-compaction.html` | Slide 35 — Pruning e compaction: togliere e riassumere |
| `slides/slide36-offload.html` | Slide 36 — Offload su file: spostare, non perdere |
| `slides/slide37-memoria-agente.html` | Slide 37 — La memoria: ciò che l'agente salva da solo |
| `slides/slide38-memoria-tool.html` | Slide 38 — La memoria è un tool |
| `slides/slide39-tre-domande.html` | Slide 39 — Le tre domande della memoria |

---

> **Filo della sezione.** Si apre con il conto delle skill contro MCP (il "costo nascosto" con cui si è chiusa la sezione 3), che introduce l'idea di prefisso; poi l'anatomia della finestra; poi i due problemi, costo e degrado; poi le tre tecniche; l'offload su file è la cerniera verso Memory. La mappa in miniatura si accende su `Skill progressive disclosure (runtime)` (29–30), `Context Optimization` (31–36), `Memory management` (37–39).
>
> **Perimetro della memoria (deciso in intervista)**: la memoria è **ciò che l'agente decide di salvare da solo**. I file di istruzioni (`AGENTS.md`, `CLAUDE.md`) non sono memoria: sono espliciti, li scrive una persona, e l'harness li appende sempre al system prompt (Slide 9). Non si usa il termine "deflazionistico".
>
> **Riprese dal 26**: la pila che cresce (slide 42 → Slide 31, **ridisegnata dall'alto** per coerenza con la sezione 2), KV cache e curve di costo (40 e 41 → Slide 32), context rot e tool a scalini (44 e 45 → Slide 34, riusate tali e quali).
>
> **Fatti verificati (set 2026)**: i token letti dalla cache costano circa 0,1× il prezzo base (sconto ~90%; 0,025× su alcuni modelli); la prima scrittura costa 1,25× (cache a 5 minuti) o 2× (a un'ora); massimo 4 checkpoint per chiamata; l'ordine di resa è tools → system → messages. Il pruning dei risultati dei tool, nell'API di Anthropic e in Claude Code, sostituisce i risultati vecchi con un segnaposto (non un riassunto), tenendo intatti gli ultimi.
>
> ⚠️ **Da dire a voce** (non sanato in slide, per scelta): la Slide 21 dice che il sandbox è effimero, la Slide 36 mostra file che sopravvivono alla sessione. L'harness porta i file fuori dal sandbox, in uno spazio persistente suo.
>
> I numeri di token nelle figure sono ordini di grandezza coerenti con la Slide 13 (prefisso ~4.000) e la Slide 25; vanno dichiarati come tali.

---

## Slide 29 — Costo fisso e costo a richiesta

**Messaggio**: cinquanta tool MCP costano a ogni giro, letti o no; venti skill costano due righe ciascuna, più un corpo quando serve. Su venti giri la differenza è di un ordine di grandezza, e non è solo denaro: è ciò che il modello deve leggere prima di scegliere.

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%): la tabella-figura; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 4 · CONTEXT MANAGEMENT*
- Titolo: *Costo fisso e costo a richiesta*
- Punti:
  1. **Il tool paga sempre**: *una definizione sta nel prefisso e rientra a ogni giro, che il tool venga chiamato o no. Cinquanta tool: novemila token letti venti volte in una sessione da venti giri.*
  2. **La skill paga quando serve**: *nel prefisso ci sono due righe per skill; il corpo entra una volta, solo per quella scelta, e da lì resta nella storia come un messaggio qualsiasi. Venti skill: ottocento token a giro, più trecento una tantum.*
- Nota in basso: *La cache abbatte il prezzo del prefisso, non la sua lunghezza: il modello lo rilegge comunque, e sceglie fra cinquanta nomi invece che fra venti descrizioni. È il conto della confusione decisionale della Slide 13.*

**Visual**: `slide29-costo-fisso-richiesta.svg`.

**Prompt per schema SVG**:
> Una tabella-figura a due righe e quattro colonne, con barre proporzionali dentro le celle.
>
> Intestazioni di colonna: `giro 1` · `giro 5` · `giro 20` · `totale letto in 20 giri`.
>
> **Riga «50 tool MCP nel prefisso»**: barre tutte uguali, alte, con `~9.000` in ogni giro; totale `~180.000 token`. Sotto la riga, in piccolo: *ogni giro rilegge tutte le definizioni*.
>
> **Riga «20 skill: indice + un corpo»**: barre basse e uguali con `~800` al giro 1 e al giro 5; al giro 20 una barra appena più alta `~1.100` (l'indice più il corpo di una skill caricata); totale `~19.000 token`. Sotto: *l'indice ogni giro; il corpo una volta, e solo quello scelto*.
>
> A destra dei totali, il rapporto in evidenza: `~10×`.
>
> Una riga di piede sotto la tabella: *con la cache il prezzo cambia, il numero di token letti no*.
>
> **Elemento focale**: il contrasto di altezza fra le due righe di barre, e il `~10×`.

## Slide 30 — Quando conviene cosa

**Messaggio**: tool, skill e script non sono alternative in gara: rispondono a esigenze diverse. La regola è "chi deve poter essere chiamato in qualsiasi momento" contro "chi serve in pochi task ed è lungo da spiegare".

**Layout**: titolo in alto; tabella comparativa a tre righe nella metà superiore (~55%); i due punti sotto; nota in basso. Nessuna figura: la tabella è il visual, come la slide 52 del 26.

**Testo**:
- Titolo: *Quando conviene cosa*
- Tabella:

| | Dove sta | Quando conviene | Che cosa costa |
|---|---|---|---|
| **Tool** (nativo o MCP) | nel prefisso, sempre | azioni brevi che il modello deve poter chiamare in qualsiasi momento: cercare, creare, inviare | una definizione a giro, letta o no |
| **Skill** | indice nel prefisso, corpo a richiesta | procedure lunghe che servono in pochi task: come si fa una cosa, con soglie e regole | due righe a giro; il corpo una volta |
| **Script nella skill** | nel sandbox, fuori dalla finestra | la parte meccanica di una procedura: chiamare un'API, aggregare, formattare | zero token per i passaggi intermedi |

- Punti:
  1. **La domanda da farsi**: *"il modello deve poterlo chiamare in qualsiasi momento?" Se sì, è un tool. Se serve in un caso su cento ed è lungo da spiegare, è una skill. Se è meccanico e sempre uguale, è uno script.*
  2. **La terza via, per i tool**: *quando i tool sono davvero tanti, alcune API permettono di caricarne le definizioni a richiesta: nel prefisso resta un tool di ricerca, e il modello cerca il tool che gli serve. È la progressive disclosure applicata ai tool.*
- Nota in basso: *Nessuna di queste scelte è del modello: è chi progetta l'agente che decide che cosa sta nel prefisso e che cosa no. È la seconda leva di miglioramento, dopo il prompt: torna nella sezione 5.*

**Visual**: nessuno. La tabella è la struttura.

> Note del relatore: il punto 2 è il caricamento differito delle definizioni (nell'API di Anthropic: tool search con `defer_loading`; esempio ufficiale da 55.000 a 8.700 token).

## Slide 31 — La finestra a ogni giro: tre parti, tre velocità

> Ripresa della slide 42 del 26 (la pila che cresce), **ridisegnata dall'alto**: lì gli strati stabili stavano in fondo, qui il prefisso sta in cima come in tutta la sezione 2.

**Messaggio**: a ogni giro la finestra ha tre parti che crescono a velocità diverse: il prefisso non cresce, la storia cresce di un turno per volta, i risultati dei tool crescono più in fretta di tutto.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~30%, classe `tight`); visual al centro-destra (~65%): tre fotogrammi; nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *La finestra a ogni giro: tre parti, tre velocità*
- Punti:
  1. **Il prefisso**: *system prompt, tool, indice delle skill: identico a ogni giro. È la parte che si mette in cache.*
  2. **La storia**: *domande, risposte, richieste di tool: cresce di qualche riga per turno. È la conversazione.*
  3. **I risultati dei tool**: *ogni `tool_result` resta lì per tutta la sessione, e uno solo può pesare quanto tutta la storia. È la parte che cresce più in fretta, e quella su cui si interviene per prima.*
- Nota in basso: *Nel 26: "il modello rilegge tutta la pila da capo, a ogni chiamata". Ora la pila ha un nome per ogni strato, e un responsabile: l'harness decide che cosa ci resta dentro.*

**Visual**: `slide31-finestra-giri.svg` — ripresa di `slide34-stateless.svg` del 26, ridisegnata dall'alto.

**Prompt per schema SVG**:
> Tre fotogrammi affiancati della stessa finestra a strati (quella della sezione 2), a **`giro 1`**, **`giro 5`**, **`giro 20`**, di altezza crescente: il terzo è molto più alto del primo. Si legge dall'alto.
>
> In ogni fotogramma, tre zone colorate in modo distinguibile, con una graffa a destra e l'etichetta: **`prefisso`** (in cima, stessa altezza nei tre fotogrammi: `~4.000`), **`storia`** (in mezzo, cresce poco: `~300` · `~1.500` · `~5.000`), **`risultati dei tool`** (in fondo, cresce molto: `~800` · `~9.000` · `~40.000`). Dentro la zona dei risultati, i blocchi `[tool]` in teal di altezze diverse, uno visibilmente enorme nel terzo fotogramma (etichetta: *un export mai ripulito*).
>
> Sotto ciascun fotogramma il totale: `~5.100` · `~14.500` · `~49.000`. Sotto tutto, la freccia del tempo con l'etichetta del 26: `ogni chiamata rilegge tutta la pila da capo`.
>
> **Elemento focale**: la zona dei risultati dei tool nel terzo fotogramma, e il prefisso che resta identico nei tre.

## Slide 32 — Il prefisso non si tocca: prefix caching

> Ripresa delle slide 40 e 41 del 26 (KV cache, curve di costo), rilette sulla finestra a strati.

**Messaggio**: la KV cache del 26 diventa un servizio dell'API: se il prefisso è identico a quello della chiamata precedente, il provider non lo ricalcola e lo fa pagare una frazione. Ma vale solo per un prefisso esatto, e solo per il prezzo: i token restano lì.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *Il prefisso non si tocca: prefix caching*
- Punti:
  1. **La stessa cache, vista dall'API**: *nel 26: di ogni token già visto si salvano K e V, e non si rifà nulla. Il provider conserva quel calcolo fra una chiamata e l'altra: se le prime N migliaia di token sono identiche a prima, riparte da lì.*
  2. **Solo un prefisso esatto**: *è un confronto byte per byte dall'inizio: cambia una virgola nel system prompt e tutto ciò che segue si ricalcola. Per questo il prefisso sta in cima e non si tocca mai.*
  3. **Sconto, non cancellazione**: *i token in cache costano circa un decimo (sconto del 90%, e su alcuni modelli di più); la prima scrittura costa un po' più del normale, e conviene già dalla seconda chiamata. Ma sono ancora nella finestra: il modello li rilegge, e i cinquanta tool MCP inutilizzati pesano sulla scelta come prima.*
- Nota in basso: *Le curve del 26 avevano tre linee: teorica, in fattura, reale. La cache sposta quella in fattura verso quella reale, e vale solo se l'harness non tocca il prefisso.*

**Visual**: `slide32-prefix-caching.svg` — il pannello `con KV cache` della slide 40 del 26, riletto sulla finestra a strati.

**Prompt per schema SVG**:
> **A sinistra**, due finestre a strati affiancate, `chiamata n` e `chiamata n+1`, lette dall'alto: il prefisso identico in entrambe (stesso contenuto, stessa altezza), racchiuso in un'area grigia etichettata `in cache: K, V già calcolati` con una freccia dalla prima alla seconda etichettata `riusati, non ricalcolati`; sotto il prefisso, la storia e i risultati, diversi fra le due (nella seconda una riga in più, con l'anello burgundy del 26: *solo questo si calcola*).
>
> **A destra**, la stessa coppia ma con una differenza minuscola nel prefisso della seconda chiamata (una riga del system prompt evidenziata: `data: 4 set 2026 10:41`): l'area grigia della cache sparisce e tutta la finestra ha l'anello burgundy. Etichetta: *una riga diversa in cima: tutto da ricalcolare*.
>
> Sotto, un piede a due voci: `prezzo dei token in cache: ~10% del prezzo pieno (sconto ~90%)` · `token letti dal modello: 100%`.
>
> **Elemento focale**: il contrasto fra la coppia di sinistra (cache che regge) e quella di destra (cache persa per una riga).

> Note del relatore: numeri esatti per l'API di Anthropic: lettura 0,1× (0,025× su Claude Fable 5.1), scrittura 1,25× a 5 minuti e 2× a un'ora; pareggio dalla seconda chiamata con la cache a 5 minuti.

## Slide 33 — Che cosa rompe la cache

**Messaggio**: la cache regge solo se l'harness costruisce la finestra nello stesso ordine, byte per byte, a ogni chiamata. Gli errori che la rompono sono pochi, e sempre gli stessi.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); a destra (~55%) la finestra a strati con le regole di posizionamento; nota in basso.

**Testo**:
- Titolo: *Che cosa rompe la cache*
- Punti:
  1. **L'ordine è fisso**: *l'API rende la finestra sempre nello stesso ordine: prima i tool, poi il system prompt, poi i messaggi. Il confronto parte dall'inizio: ciò che sta in alto deve essere identico, ciò che cambia va in fondo.*
  2. **I checkpoint**: *le bandierine `cache_control` della Slide 10 dicono al provider "fin qui salva". Al massimo quattro per chiamata; la si mette in fondo alla parte condivisa, non in fondo a tutto, altrimenti si scrive una cache che nessuno rileggerà.*
  3. **I tre errori classici**: *una data o un'ora nel system prompt (cambia a ogni chiamata); la lista dei tool in ordine diverso (per esempio perché un server MCP la restituisce così); un prefisso troppo corto per essere salvato (sotto le poche centinaia o migliaia di token, dipende dal modello).*
- Nota in basso: *Come si verifica: la risposta dell'API riporta quanti token sono stati letti dalla cache. Se è zero per due chiamate identiche di fila, qualcosa nel prefisso cambia senza che nessuno se ne accorga. È il primo numero da guardare in produzione: torna nella sezione 5.*

**Visual**: `slide33-cache-regole.svg`.

**Prompt per schema SVG**:
> La finestra a strati della sezione 2, letta dall'alto, con a sinistra una scala verticale che va da `stabile` (in alto) a `cambia ogni volta` (in basso). Gli strati: `tool` · `system prompt` · `indice delle skill` · `storia` · `ultimo messaggio`. Due bandierine `cache_control` disegnate sul bordo destro: una dopo `indice delle skill` (etichetta: *fin qui, condiviso da tutte le sessioni*) e una dopo la penultima riga della storia (etichetta: *fin qui, condiviso dai giri di questa sessione*).
>
> A destra, tre piccole vignette-errore, ognuna con un `✗`: (1) una riga `data: 4 set 2026 10:41` dentro il system prompt, con la scritta *cambia a ogni chiamata*; (2) due liste di tool affiancate con lo stesso contenuto in ordine diverso, *stessi tool, ordine diverso: prefisso diverso*; (3) un prefisso di tre righe soltanto, *troppo corto per essere salvato*.
>
> **Elemento focale**: le due bandierine, e la scala stabile/variabile che spiega dove vanno.

## Slide 34 — Non basta che ci stia: il context rot

> Ripresa delle slide 44 e 45 del 26, affiancate, con gli SVG del 26 **riusati tali e quali**. È l'unica slide della lezione che riusa due SVG del 26 senza modifiche.

**Messaggio**: anche quando la finestra è lontana dal limite tecnico, un contesto lungo peggiora le risposte; e i risultati dei tool lo allungano molto più in fretta della conversazione. La cache risolve il prezzo, non questo.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): i due grafici del 26 affiancati in un contenitore a due colonne; nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *Non basta che ci stia: il context rot*
- Punti:
  1. **Il fatto, dal 26**: *oltre una certa lunghezza il modello trova peggio ciò che gli serve, anche se c'è: il budget di attenzione si diluisce. E la soglia arriva molto prima del limite tecnico della finestra.*
  2. **Chi la riempie**: *non la conversazione, che cresce piano: i risultati dei tool, a scalini. Nella Slide 31, al giro 20, erano quattro quinti della finestra.*
  3. **Che cosa non risolve la cache**: *lo sconto vale sul prezzo. Il modello legge tutto lo stesso, e il degrado dipende da quanto legge, non da quanto paga.*
- Nota in basso: *Nel 26 le regole erano per chi usa un chatbot: nuova chat, non riempire. Qui le regole sono per l'harness, che deve decidere da solo che cosa togliere. Sono le prossime due slide.*

**Visual**: `slide36-context-rot.svg` e `slide36b-tool-context-rot.svg` del 26, affiancati; nessun SVG nuovo. Se lo spazio non regge due figure affiancate, resta la seconda (i tool a scalini) e la prima va nel primo punto come richiamo verbale.

## Slide 35 — Pruning e compaction: togliere e riassumere

**Messaggio**: due tecniche per togliere dalla finestra ciò che non serve più: cancellare i risultati vecchi dei tool, o riassumere la storia in un blocco più corto. Entrambe perdono qualcosa; l'harness decide quando e quanto.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): prima e dopo; nota in basso.

**Testo**:
- Titolo: *Pruning e compaction: togliere e riassumere*
- Punti:
  1. **Pruning**: *i risultati dei tool sono i primi a diventare inutili: ciò che contava, il modello l'ha già scritto nella propria risposta. L'harness sostituisce i più vecchi con una riga ("risultato rimosso: 9.000 token"), tenendo intatti gli ultimi. Alcuni harness, invece della riga, mettono un breve riassunto del risultato: costa una chiamata in più, serve quando il modello non l'aveva ancora sfruttato.*
  2. **Compaction**: *quando anche la storia è lunga, l'harness chiede al modello di riassumere tutto ciò che è successo finora (decisioni prese, cose ancora aperte, file toccati) e sostituisce la storia con quel riassunto. La sessione continua da lì.*
  3. **Che cosa si perde**: *il pruning perde dettagli che forse servivano; la compaction perde sfumature e a volte un vincolo detto a metà conversazione. Per questo si fa a soglie (a una certa frazione della finestra) e mai sul prefisso, che deve restare identico per la cache.*
- Nota in basso: *Alcune API offrono entrambe come servizio: l'harness dichiara una strategia e il provider cancella o riassume prima di chiamare il modello. Il principio non cambia: qualcuno, fuori dal modello, decide che cosa il modello vedrà.*

**Visual**: `slide35-pruning-compaction.svg`.

**Prompt per schema SVG**:
> Tre finestre a strati affiancate, lette dall'alto, stessa larghezza: **`prima`**, **`dopo il pruning`**, **`dopo la compaction`**.
>
> **Prima**: prefisso; storia con turni e richieste; tre blocchi `[tool]` in teal di cui uno enorme (`export, 9.000 token`); altezza totale grande.
>
> **Dopo il pruning**: identica, ma due blocchi `[tool]` sono ridotti a righe sottili grigie con la scritta `risultato rimosso · 9.000 token`, e uno a un blocchetto `riassunto: 3 righe`; le pill delle richieste restano; l'ultimo risultato è intatto. Altezza molto minore. Etichetta: *le richieste restano; i contenuti vecchi diventano un segnaposto, o un riassunto breve*.
>
> **Dopo la compaction**: prefisso identico; al posto della storia un unico blocco `riassunto della sessione` (dentro, tre righe: *deciso: …* · *aperto: …* · *file toccati: …*); poi solo gli ultimi due messaggi. Altezza minima. Etichetta: *la storia diventa un riassunto*.
>
> Il prefisso ha la stessa altezza e lo stesso colore in tutte e tre, con la scritta `non si tocca`. Sotto i tre fotogrammi, le altezze in token: `~49.000` · `~14.000` · `~6.000`.
>
> **Elemento focale**: il prefisso invariato nelle tre finestre, e il calo di altezza da sinistra a destra.

> Note del relatore: nell'API di Anthropic esistono come servizio il context editing (cancella i risultati vecchi dei tool con un segnaposto, tenendo gli ultimi N) e la compaction server-side; Claude Code fa lo stesso in locale.

## Slide 36 — Offload su file: spostare, non perdere

**Messaggio**: la terza tecnica non cancella e non riassume: sposta. Ciò che è grande va su un file, in finestra resta il puntatore, e il modello ci torna quando vuole. Ed è il punto in cui il contesto smette di essere solo contesto.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); blocco nero centrato in fondo (la cerniera verso Memory).

**Testo**:
- Titolo: *Offload su file: spostare, non perdere*
- Punti:
  1. **Il pattern**: *un risultato grande, un documento letto, un piano di lavoro: l'harness (o il modello stesso, con bash) lo scrive su un file nel sandbox e in finestra lascia una riga: nome, dimensione, come cercarci dentro. È la Slide 18, promossa a regola generale.*
  2. **Niente si perde**: *a differenza di pruning e compaction, il contenuto esiste ancora: il modello lo riapre con `grep`, `head`, o rileggendolo per intero se serve. La finestra resta corta, l'informazione resta intera.*
  3. **Anche ciò che il modello produce**: *non solo risultati in ingresso: appunti, decisioni, la lista di cose fatte e da fare. Un agente che lavora a lungo scrive per sé stesso, perché sa che la finestra non basterà.*
- Blocco nero centrato: *Un file scritto in questa sessione e letto nella prossima non è più contesto. È memoria.*

**Visual**: `slide36-offload.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la finestra a strati, letta dall'alto, corta: prefisso, storia, e al posto dei blocchi `[tool]` grandi tre righe sottili: `ordini_08.json · 12.480 righe · grep`, `contratto.md · 40 pagine · head`, `piano.md · scritto dal modello`. Etichetta: *in finestra: i puntatori*.
>
> **A destra**, il filesystem del sandbox: tre file disegnati come documenti, con le dimensioni reali (`~90.000 token`, `~30.000 token`, `~400 token`). Frecce bidirezionali fra ogni riga della finestra e il suo file: verso destra `scrive`, verso sinistra `rilegge quando serve` (con una pill piccola `→ bash("grep …")`).
>
> **In basso**, una linea del tempo con due sessioni: `sessione di oggi` e `sessione di domani`, separate da un taglio. I file stanno **sotto entrambe**, attraversano il taglio; la finestra no: quella di domani riparte vuota. Etichetta sul taglio: *la finestra muore, i file restano*.
>
> **Elemento focale**: i file che attraversano il taglio fra le due sessioni.

> Note del relatore: il sandbox è effimero (Slide 21): dire a voce che l'harness porta i file fuori dal sandbox, in uno spazio persistente suo, e che è a quello spazio che il tool di memoria (Slide 38) accede.

## Slide 37 — La memoria: ciò che l'agente salva da solo

**Messaggio**: fra una sessione e l'altra sopravvive solo ciò che qualcuno ha scritto. La memoria è la parte che scrive l'agente, di propria iniziativa, mentre lavora; e nella pratica di oggi è quasi sempre una cartella di file di testo, non un database vettoriale.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *La memoria: ciò che l'agente salva da solo*
- Punti:
  1. **Il confine**: *Context management è tutto ciò che succede dentro una sessione. Memory è ciò che sopravvive fra una sessione e l'altra: la finestra muore, il sandbox muore, il modello non ricorda nulla (nel 26: stateless). Resta solo ciò che è stato scritto.*
  2. **Non le istruzioni**: *`AGENTS.md` e simili li scrive una persona e li porta l'harness, sempre (Slide 9). La memoria è l'altra cosa: ciò che l'agente decide di annotare mentre lavora: un fatto sull'utente, una scelta presa e il perché, una cosa imparata a proprie spese, lo stato di un lavoro a metà, e le tracce delle sessioni passate.*
  3. **Quasi sempre un file**: *file piccoli, nomi parlanti, una cartella che l'harness conosce, e `grep`. "Memoria" evoca embedding e ricerca semantica; nella pratica attuale è l'eccezione: un indice quando i file sono troppi, un tool di ricerca sulla memoria, non la memoria.*
- Nota in basso: *È lo stesso schema del sandbox: il modello non ha uno stato, l'harness glielo mette davanti. Il file è la forma più semplice di stato che sopravvive.*

**Visual**: `slide37-memoria-agente.svg`.

**Prompt per schema SVG**:
> **In alto**, tre sessioni affiancate sulla linea del tempo (`lunedì`, `martedì`, `giovedì`), ognuna con la propria finestra a strati che nasce vuota e muore alla fine (un taglio dopo ciascuna).
>
> **In basso**, sotto tutte e tre, un'unica cartella persistente `memoria/` con dentro: `note/utente.md` (*preferenze, contesto*), `note/scelte.md` (*decisioni e perché*), `scratch/stato-lavoro.md` (*a che punto ero*), `sessioni/` (*le conversazioni passate*).
>
> Le frecce `scrive` partono **dal modello** di ogni sessione (una pill burgundy `→ memoria_scrivi(…)`), non dall'harness. **Nessuna freccia di lettura al giro zero**: la memoria si legge quando serve (una piccola nota: *si legge cercando → Slide 38*).
>
> In un angolo, separato dalla cartella e con l'etichetta *non è memoria*, il file `AGENTS.md` con una freccia che entra nel system prompt della finestra: *istruzioni esplicite, le porta l'harness*.
>
> In un altro angolo, sbiadito e tratteggiato, un cilindro `database vettoriale` con l'etichetta *un indice, quando i file sono troppi*, collegato alla cartella da una freccia sottile.
>
> **Elemento focale**: la cartella sotto tutte le sessioni, e le frecce `scrive` che partono dal modello.

## Slide 38 — La memoria è un tool

**Messaggio**: la memoria non è un meccanismo nascosto: l'harness la espone al modello come un tool, con le sole operazioni permesse. Il caso più comune è un tool che cerca nelle conversazioni passate.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); a destra (~55%) la definizione del tool nell'idioma dei riquadri e, sotto, un riquadro-payload con un giro; nota in basso.

**Testo**:
- Titolo: *La memoria è un tool*
- Punti:
  1. **Dichiarata al giro zero, come gli altri**: *nella lista dei tool c'è anche la memoria, con le operazioni che l'harness ha deciso di permettere: cercare, leggere, scrivere. Non per forza tutte: un agente può poter leggere senza poter scrivere.*
  2. **Il caso più comune: cercare nel passato**: *un tool che cerca nelle conversazioni e nelle note delle sessioni precedenti e restituisce i passaggi che corrispondono. Dietro, molto spesso, è `grep` su una cartella di file: nomi parlanti, testo semplice, operatori Unix. Basta quasi sempre.*
  3. **Stesso contratto, stesso giro**: *il modello chiede, l'harness esegue, il risultato rientra come `tool_result`. La memoria non "si accende": si legge quando serve, e pesa nella finestra come qualsiasi altro risultato.*
- Riquadro-definizione (HTML, testo esatto):
  ```
  name:        memoria_cerca
  description: Cerca nelle note e nelle conversazioni delle sessioni
               precedenti. Usalo quando l'utente si riferisce a qualcosa
               di già discusso, o prima di rifare un lavoro già fatto.
  input_schema:
    query: string — parole o frase da cercare

  name:        memoria_scrivi
  description: Salva una nota breve da ritrovare nelle prossime sessioni.
  input_schema:
    testo: string
  ```
- Riquadro-payload (HTML, idioma del 26):
  ```
  [user]      Riprendiamo il report che stavamo preparando.
  [assistant] → memoria_cerca("report")
  [tool]      sessioni/2026-09-01.md: "report vendite settimana 35: totali fatti,
              manca il confronto con SpedFast" · scratch/stato-lavoro.md: "report: bozza in report_35.md"
  [assistant] Ripartiamo dal confronto con SpedFast: la bozza è in report_35.md.
  ```
- Nota in basso: *Ed è così che la memoria si può avvelenare: chi riesce a farci scrivere una riga (Slide 19) la ritrova in ogni sessione futura. Il permesso di scrittura è la decisione più delicata di questa slide.*

**Visual**: i due riquadri HTML; nessun SVG.

## Slide 39 — Le tre domande della memoria

**Messaggio**: progettare la memoria di un agente è rispondere a tre domande: che cosa vale la pena ricordare, chi lo scrive, chi lo legge. Le risposte sbagliate producono una memoria che cresce, si contraddice, e nessuno consulta.

**Layout**: titolo in alto; tre colonne che occupano il corpo (~60%), una per domanda, ognuna con la risposta buona e quella cattiva; nota in basso. Nessuna figura: le tre colonne sono la struttura.

**Testo**:
- Titolo: *Le tre domande della memoria*
- Colonna 1 — **Che cosa vale la pena ricordare?**
  - *Sì*: *ciò che cambia il lavoro futuro: una preferenza dell'utente, una decisione presa e il suo perché, un errore fatto e come evitarlo, lo stato di un lavoro a metà.*
  - *No*: *ciò che è già altrove (nel codice, nei file di istruzioni, nella KB), ciò che vale solo per questa sessione, i risultati grezzi dei tool.*
- Colonna 2 — **Chi lo scrive?**
  - *Sì*: *l'agente, alla fine di un passaggio, con una nota breve e datata; oppure l'utente, quando dice "ricordati che…".*
  - *No*: *tutto in automatico, a ogni giro: la memoria diventa un log, e un log non è memoria.*
- Colonna 3 — **Chi lo legge, e quando?**
  - *Sì*: *il modello, quando cerca (Slide 38); poche note stabili possono entrare al giro zero, ma sono l'eccezione.*
  - *No*: *tutto nel prefisso a ogni sessione: è il costo fisso della Slide 29, applicato alla memoria.*
- Nota in basso: *Tre domande, e una quarta implicita: chi la ripulisce? Una memoria che nessuno pota si riempie di note vecchie, doppie, o false. È lo stesso problema di una base di conoscenza, ed è materia del prossimo incontro.*

**Visual**: nessuno.
