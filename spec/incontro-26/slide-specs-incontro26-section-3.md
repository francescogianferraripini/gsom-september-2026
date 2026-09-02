# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 3 — Perché funziona**
**Obiettivo di apprendimento**: il partecipante si costruisce un modello mentale dell'interno dell'LLM — embeddings come "spazio delle idee", prodotto scalare come sovrapposizione, fully connected e attention, context / complessità quadratica / KV cache, conoscenza intrinseca nei pesi, MoE.
**Messaggio chiave (takeaway)**: Nello spazio degli embedding il significato è geometria: vicinanza è affinità, direzioni sono relazioni. (Il "compressore lossy" ha una slide dedicata, ma non è il takeaway della sezione.)
**Budget**: ~40 min — la sezione più lunga dell'incontro.
**Stato**: bozza — impianto visivo rifatto per tutte le slide 10–22 (vedi *Alfabeto visivo* più sotto)

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec3.html` | Separatore — Sezione 3: Perché funziona |
| `slides/slide10-parola-vettore.html` | Slide 10 — La base di tutto: a ogni parola il suo vettore |
| `slides/slide11-vettori-prodotto-scalare.html` | Slide 11 — Vettori e prodotto scalare |
| `slides/slide12-scala-del-calcolo.html` | Slide 12 — La scala del calcolo: vettori e matrici |
| `slides/slide13-embeddings.html` | Slide 13 — Embeddings: lo spazio delle idee |
| `slides/slide14-tokenizzazione.html` | Slide 14 — La tokenizzazione |
| `slides/slide15-architettura.html` | Slide 15 — L'architettura, in un colpo d'occhio (in tre tempi) |
| `slides/slide16-fanout.html` | Slide 16 — Fanout: il matching concettuale |
| `slides/slide17-compressione.html` | Slide 17 — Compressione: la sovrapposizione |
| `slides/slide18-attention-qk.html` | Slide 18 — Attention: domande e chiavi (Q e K) |
| `slides/slide19-softmax.html` | Slide 19 — Softmax: il budget di ascolto |
| `slides/slide20-attention-v.html` | Slide 20 — V: la consegna |
| `slides/slide20b-contesto.html` | Slide 20b — Lo stesso token, due contesti |
| `slides/slide21-positional-encoding.html` | Slide 21 — Positional encoding: l'ordine conta |
| `slides/slide22-reverse-embedding.html` | Slide 22 — Reverse embedding: tornare ai token |
| `slides/slide23-costo-contesto.html` | Slide 23 — Il contesto ha un costo |
| `slides/slide24-conoscenza-nei-pesi.html` | Slide 24 — La conoscenza è nei pesi |
| `slides/slide25-compressore-lossy.html` | Slide 25 — L'LLM come compressore lossy |
| `slides/slide26-conseguenze-compressione.html` | Slide 26 — Conseguenze della compressione |
| `slides/slide27-moe.html` | Slide 27 — MoE: non tutti i pesi lavorano sempre |

> **Logica dell'ordine**: 10–13 i mattoni (parola→vettore, prodotto scalare, la scala del calcolo, spazio delle idee) → 14 la tokenizzazione corregge "parola" in "token" → 15 la mappa dell'architettura → 16–22 zoom sui blocchi della mappa (fanout, compressione, attention in tre tempi Q·K / softmax / V, la prova del contesto in 20b, positional encoding, reverse embedding) → 23 il costo del contesto → 24–26 la conoscenza, la sua natura compressa e le conseguenze pratiche (fronte 2) → 27 MoE.
>
> **Filo rosso della sezione — le operazioni di manipolazione degli embeddings**: l'LLM come manipolatore di embeddings (punchline Slide 13) si articola in operazioni nominate slide per slide: **spostamento** (Slide 13, direzioni come relazioni), **matching/fanout** (Slide 16), **compressione/sovrapposizione** (Slide 17), e l'attention come manipolazione guidata dal contesto (Slide 18–20b: match Q·K, budget softmax, consegna dei value, e la prova che il contesto sposta il significato); anche la posizione è uno spostamento (Slide 21).
>
> **Alfabeto visivo della sezione** — fissato nella Slide 15. Ogni disegno di questa sezione deve rispettarlo, altrimenti il pubblico ricostruisce il modello mentale da capo a ogni slide.
>
> | elemento | forma | colore |
> |---|---|---|
> | embedding / residual stream | riga di **4 celle** | teal `#1ab197` |
> | q — la domanda | riga di **3 celle** | burgundy `#a1245a` |
> | k — la chiave | riga di **3 celle** | grafite `#161719` |
> | v — il contenuto | riga di **3 celle** | lightblue `#4da0d7` |
> | matrice di proiezione W | griglia **4×3** (4 in ingresso, 3 in uscita) | il colore del vettore che produce |
> | corsia | linea verticale continua | grigio; burgundy per il token attivo |
> | token | tessera con testo monospaziato | — |
>
> La griglia 4×3 non è decorativa: è letteralmente `vettore 4 × matrice 4×3 = vettore 3`, cioè il livello 2 della Slide 12. Chi ha visto quella slide riconosce l'operazione senza rispiegazioni.
>
> **Direzione di lettura: dal basso verso l'alto**, in *tutti* i diagrammi della sezione — l'input entra in fondo, il risultato esce in cima. Vale per la torre (15), per la griglia dell'attention (18–20b) e per la mini-mappa.
>
> **Stato dell'allineamento**: rispettano l'alfabeto tutte le slide da **10 a 22**. Le Slide 10, 12 e 14 lo *insegnano* (il vettore a 4 celle, la griglia 4×3, la tessera-token); dalla 15 in poi lo *usano*. Restano fuori le Slide **23–27**, disegnate prima della revisione: la 23 in particolare guadagnerebbe molto, perché la sua griglia token × strati è già la torre.
>
> **Mini-mappa "sei qui"**: le slide 16–22 portano, in fondo alla colonna di testo, la torre della Slide 15 ridotta a silhouette grigia con **un solo elemento in burgundy** — la parte trattata da quella slide. Varianti: `minimap-fc` (16), `minimap-somma` (17), `minimap-attn` (18, 19, 20, 20b), `minimap-pos` (21), `minimap-testa` (22). Esiste anche `minimap-corsie`, pronta per la Slide 23 ma non ancora cablata.

---

## Slide 10 — La base di tutto: a ogni parola il suo vettore

**Layout**: titolo in alto; visual al centro (~55%); le due frasi di testo sotto il visual; nota in basso.

**Testo**:
- Titolo: *La base di tutto: a ogni parola il suo vettore*
- Frasi:
  1. *Per far entrare il linguaggio in una macchina che calcola, la mossa fondativa è: a ogni parola, una lista di numeri.*
  2. *Quell'associazione non la scrive nessuno a mano: viene appresa.*
- Nota in basso: *Perché proprio dei numeri? Perché sui numeri si può calcolare — è la prossima slide.*

**Visual**: tre colonne, ognuna dal basso verso l'alto — la tessera-token in fondo, il vettore sopra. È la coppia di righe che sta alla base della torre (Slide 15).

**Prompt per schema SVG**:
> Tre colonne affiancate: `gatto`, `cane`, `Parigi`. In ciascuna, dal basso: la **tessera-token** (testo monospaziato), una freccia verso l'alto, e il **vettore: quattro celle teal con i numeri dentro**. È l'unica slide della sezione in cui le celle portano i numeri — serve a dire "una lista di numeri"; da qui in poi le celle restano colorate e mute.
>
> `gatto` `[0.8, −1.3, 2.1, 0.4]` e `cane` `[0.7, −1.1, 1.9, 0.5]` hanno numeri visibilmente simili; `Parigi` `[−2.4, 0.6, −0.3, 1.8]` visibilmente diverso. Non commentarlo: è un seme per la Slide 13.
>
> Etichette di riga a sinistra: `vettore / l'embedding` e `parola`. In fondo, una riga sola: *quattro celle nel disegno, migliaia di numeri nella realtà — e l'associazione è appresa durante l'addestramento, non scritta a mano*.
>
> **Elemento focale**: la freccia parola → vettore.

---

## Slide 11 — Vettori e prodotto scalare

**Layout**: titolo in alto; definizioni a sinistra (~35%); visual a tre pannelli al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Vettori e prodotto scalare*
- Definizioni (a sinistra):
  1. **Vettore**: *una lista di numeri — ovvero una direzione nello spazio.*
  2. **Prodotto scalare**: *misura quanto due vettori si sovrappongono: è un rilevatore di affinità.*
- Nota in basso: *Tutto ciò che segue — embeddings, attention, fully connected — è questa operazione, ripetuta miliardi di volte.*

**Visual**: la doppia natura del vettore (lista di numeri ↔ freccia) e tre pannelli con coppie di frecce che mostrano i tre casi del prodotto scalare: affini / estranei / opposti.

**Prompt per schema SVG**:
> Diagramma in due parti.
>
> **Parte sinistra — la doppia natura**: una lista di numeri `[0.8, −1.3, 2.1, …]` e, accanto, una freccia disegnata nel piano, collegate da un segno di equivalenza con etichetta *stessa cosa, vista in due modi*.
>
> **Parte destra — tre pannelli affiancati**, ognuno con due frecce che partono dalla stessa origine:
>   1. frecce quasi parallele (~20° tra loro) — etichetta: `affini` — sotto: `prodotto scalare: alto`;
>   2. frecce perpendicolari (90°) — etichetta: `estranei` — sotto: `prodotto scalare: ≈ 0`;
>   3. frecce opposte (~180°) — etichetta: `opposti` — sotto: `prodotto scalare: negativo`.
>
> **Elemento focale**: il contrasto tra i tre pannelli — è la progressione alto / zero / negativo a portare il messaggio (il prodotto scalare come misura di sovrapposizione). Nel primo pannello, evidenziare visivamente la zona di sovrapposizione tra le due frecce (es. l'angolo stretto tra esse).

## Slide 12 — La scala del calcolo: vettori e matrici

**Layout**: titolo in alto; visual a tre livelli impilati al centro (~70%); nota in basso.

**Testo**:
- Titolo: *La scala del calcolo: vettori e matrici*
- Tre gradini (uno per livello del visual):
  1. **vettore · vettore = un numero**: *l'allineamento tra i due.*
  2. **vettore × matrice = un vettore**: *la matrice è una batteria di vettori; il risultato è la lista degli allineamenti con ciascuno di essi — una batteria di rilevatori interrogata in un colpo solo.*
  3. **matrice × matrice = una matrice**: *la stessa operazione, ripetuta per molti vettori insieme.*
- Nota in basso: *È tutto qui il calcolo di un LLM — ed è per questo che le GPU, fatte per moltiplicare matrici, sono il suo motore naturale.*

**Visual**: tre gradini impilati **dal basso verso l'alto**, ognuno un'equazione. È la slide che insegna la griglia 4×3, quindi la forma dev'essere identica a quella che comparirà in W^Q, W^K e W^V.

**Prompt per schema SVG**:
> Tre livelli, dal basso: a sinistra il disegno, a destra la spiegazione in due righe. Tutto in teal (vettori) e grigio (matrici): **i colori di ruolo non esistono ancora**, arrivano alla Slide 18.
>
> **Livello 1 (in basso) — `vettore · vettore = numero`**: due vettori da 4 celle, il simbolo `·`, e in uscita un riquadro con `0,83`.
>
> **Livello 2 (al centro, il gradino focale) — `vettore × matrice = vettore`**: un vettore da **4 celle**, il `×`, una **matrice 4 righe × 3 colonne**, l'`=`, e in uscita un vettore da **3 celle**. Tre curve sottili collegano ogni cella in uscita alla colonna corrispondente della matrice, passando **sotto** la matrice. Sotto: *3 colonne = 3 rilevatori, lunghi 4 come il vettore in ingresso*. A destra: *Moltiplicare per una matrice significa interrogare una batteria di rilevatori, tutti insieme* e *è la stessa forma delle matrici Q, K e V dell'attention*.
>
> **Livello 3 (in alto) — `matrice × matrice = matrice`**: tre vettori da 4 celle impilati, la stessa matrice 4×3, tre vettori da 3 celle in uscita.
>
> **Elemento focale**: il livello 2. È il gradino da cui dipende la leggibilità di tutta la griglia dell'attention.

---

## Slide 13 — Embeddings: lo spazio delle idee

**Layout**: titolo in alto; definizione sotto il titolo; grande visual al centro (~65%); nota-punchline in basso.

**Testo**:
- Titolo: *Embeddings: lo spazio delle idee*
- Definizione: *Un embedding è il vettore che rappresenta un token in uno spazio a migliaia di dimensioni.*
- Due proprietà (accanto o dentro il visual):
  1. **La vicinanza è affinità**: *concetti simili stanno vicini.*
  2. **Le direzioni sono relazioni**: *king − man + woman ≈ queen.*
- Nota in basso (punchline): *Un LLM, in fondo, è un manipolatore di embeddings.*

**Visual**: proiezione 2D dello spazio degli embedding con cluster di concetti affini e frecce parallele che mostrano che una relazione ("capitale di") è una direzione.

**Prompt per schema SVG**:
> Proiezione bidimensionale di uno spazio di embedding: un piano punteggiato con parole posizionate come punti etichettati.
>
> **Due evidenze da mostrare, in due zone del piano:**
>
> 1. **La vicinanza è affinità** — due cluster ben distinti: un cluster di animali (`gatto`, `cane`, `tigre`) e, lontano, un cluster di nazioni (`Francia`, `Italia`, `Germania`); poco distante da quest'ultimo, il cluster delle capitali (`Parigi`, `Roma`, `Berlino`).
> 2. **Le direzioni sono relazioni** — tre frecce, tutte visibilmente parallele e della stessa lunghezza: `Francia → Parigi`, `Italia → Roma`, `Germania → Berlino`, con etichetta condivisa *stessa direzione = "capitale di"*. In un angolo, il parallelogramma classico: `king`, `queen`, `man`, `woman`, con le frecce `man → woman` e `king → queen` parallele, ed etichetta `king − man + woman ≈ queen`.
>
> **Elemento focale**: il parallelismo delle frecce — è quello a dimostrare che una relazione semantica è una direzione geometrica. I cluster fanno da supporto. Etichetta d'ambiente in un angolo del piano: *proiezione 2D di uno spazio a migliaia di dimensioni*.

## Slide 14 — La tokenizzazione

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *La tokenizzazione*
- Punti:
  1. **L'unità non è la parola: è il token** — *frammenti di testo da un vocabolario fisso, ~100.000 voci.*
  2. **Le parole comuni sono un token intero; quelle rare vengono spezzate.**
- Nota in basso: *È per questo che a un modello riesce difficile contare le lettere di una parola: le lettere, lui, non le ha mai viste. D'ora in poi diremo: token.*

**Visual**: due scene impilate, ognuna dal basso verso l'alto — il testo grezzo in fondo, le tessere-token sopra.

**Prompt per schema SVG**:
> **In cima**, una fascia larga: il **vocabolario**, una griglia di celle con tre evidenziate, etichetta *vocabolario fisso: ~100.000 token — le tessere sono prese da qui*, e una freccia che scende verso le tessere. È un riferimento, non un passo del flusso.
>
> **Scena superiore — parola rara**: dal basso il testo `elettroencefalogramma`, una freccia in su, e tre tessere burgundy `elettro` · `encefal` · `ogramma`. **L'id del vocabolario sta dentro la tessera**, sotto al testo: una tessera è un oggetto solo.
>
> **Scena inferiore — parole comuni**: dal basso `Il gatto è sul tavolo`, una freccia, e cinque tessere neutre con i loro id.
>
> **Elemento focale**: il contrasto fra le due scene. Le tessere burgundy sono spezzate, quelle neutre no.

---

## Slide 15 — L'architettura, in un colpo d'occhio

**Layout**: titolo in alto; il diagramma occupa quasi tutta la slide (~80%), **sviluppo verticale dal basso verso l'alto**; didascalia e note in basso. La slide si apre in **tre tempi** (fragment reveal.js: tre SVG sovrapposti con lo stesso viewBox e lo stesso contorno, così nulla si sposta fra un tempo e l'altro).

**Testo**:
- Titolo: *L'architettura, in un colpo d'occhio*
- Didascalia: *Dal testo alla distribuzione sul prossimo token. Ogni pezzo di questo percorso è una delle prossime slide.*
- Note in basso (piccole):
  - *Il canale centrale scorre: ogni sottoblocco non sostituisce l'embedding, gli somma il suo contributo.*
  - *Dopo la distribuzione, il sampling sceglie il token effettivo.*
  - *Semplificato: omesse le normalizzazioni e le teste dell'attention (Slide 18).*

**Visual**: la torre — il transformer decoder-only disegnato in verticale, con una corsia per token che sale attraverso i blocchi.

**File**: `slide15a-scatola-nera.svg`, `slide15b-torre.svg`, `slide15c-torre-aperta.svg` (viewBox condiviso 1160×420).

**Prompt per schema SVG** — tre tempi, stessa inquadratura:

> **Impianto comune a tutti e tre**: colonna di etichette a sinistra (~140px, stile "label gutter"); al centro la torre, larga a bande; a destra la testa del modello (vettore finale → matrice di reverse embedding → softmax → distribuzione a barre) e, sotto, una legenda compatta dell'alfabeto visivo. In basso la frase in tessere-token: una corsia fantasma `⋯` (*il contesto precedente*) e poi `Il`, `gatto`, `è`; la corsia di `è` è burgundy — è l'ultimo token, l'unico che produce il prossimo.
>
> **Tempo 1 — la scatola nera**: al posto della torre, un unico blocco nero etichettato `LLM`, con sottotitolo *una funzione: testo → distribuzione sul prossimo token* e il richiamo *è quello che abbiamo definito finora*. Dalle tessere-token salgono frecce nel blocco; dal blocco esce la distribuzione, nella stessa posizione che avrà nei tempi successivi.
>
> **Tempo 2 — la torre chiusa**: il blocco nero si apre in quattro bande impilate dentro un contenitore tratteggiato etichettato `IL BLOCCO, RIPETUTO ×N — ~100 nei modelli grandi`: `BLOCCO 1` (banda alta, chiusa, con dentro *tutti i blocchi sono uguali: cambiano solo i pesi*), `BLOCCO 2`, `⋯`, `BLOCCO N`. Le corsie restano visibili anche sopra le bande: non si interrompono mai. Sopra le tessere compaiono le due righe di vettori: `embedding` (4 celle teal) e `+ posizione` (4 celle gialle), unite da un nodo `+`.
>
> **Tempo 3 — il blocco aperto**: `BLOCCO 1` — e solo lui — si apre e mostra due sottoblocchi, **con la stessa impronta della banda chiusa del tempo 2, così nulla si muove**:
>   - `masked self-attention`: una banda che **attraversa e collega** le corsie, con una linea orizzontale e frecce che vanno **solo verso destra** (etichetta nel gutter: *qui le corsie si parlano — e solo verso destra*);
>   - `fully connected`: **quattro riquadri separati**, uno per corsia, che non si toccano (etichetta: *ogni corsia per conto suo*);
>   - un nodo `+` su ogni corsia dopo ciascun sottoblocco, e due skip connection tratteggiate sulla corsia attiva che aggirano i sottoblocchi sulla destra.
>
> **Elementi focali**: (1) il contrasto attention-vs-fully-connected — è l'unica figura del deck che lo mostra, e risolve metà delle domande in aula; (2) la profondità, che si **vede** invece di essere scritta; (3) la mascheratura, gratis, dalle frecce che vanno in una direzione sola; (4) il fatto che solo l'ultima corsia esce in cima verso la testa.

## Slide 16 — Fanout: il matching concettuale

**Layout**: titolo in alto; tre bullet a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Fanout: il matching concettuale*
- Bullet:
  1. **Un rilevatore per concetto**: *ogni riga della matrice è un pattern memorizzato; il prodotto scalare misura quanto l'embedding in transito gli somiglia.*
  2. **Tutti in parallelo (fanout)**: *migliaia di rilevatori scattano insieme, a ogni token, a ogni strato — lo spazio si espande.*
  3. **La non linearità è un gate**: *passa solo ciò che è davvero affine; tutto il resto viene azzerato.*
- Nota in basso: *È il rilevatore di affinità della Slide 11, moltiplicato per migliaia: da un rilevatore a una batteria di rilevatori.*

**Visual**: il fanout dal basso verso l'alto — l'embedding interroga in parallelo una batteria di rilevatori, le attivazioni salgono come barre, il gate le filtra.

**Prompt per schema SVG**:
> Dal basso: il **vettore in transito** (4 celle teal) da cui parte un ventaglio di frecce verso sei colonne.
>
> **La batteria**: sei **vettori-colonna** grigi (4 celle impilate ciascuno) — è la matrice della Slide 12, disegnata come batteria di rilevatori. Etichetta: *un rilevatore per concetto, migliaia a ogni token*.
>
> **Le attivazioni**: sopra ogni colonna una **barra verticale** alta quanto l'attivazione, burgundy piena se forte, tinta se debole. Accanto a ogni barra, il nome del concetto **ruotato di 90°**: `animale domestico`, `arriva un luogo`, `frase al presente` (forti), `contesto giuridico`, `linguaggio matematico` (mute), `… e altre migliaia`.
>
> **Il gate**: una barra nera orizzontale che taglia tutta la larghezza. Le tre attivazioni forti la attraversano con una freccia burgundy; le deboli si fermano dentro la barra con uno `0` cerchiato. **Nessun testo dentro la barra**: le etichette stanno nel gutter a sinistra (`non linearità / il gate`) e in cima.
>
> **Elemento focale**: il contrasto fra le tre frecce che passano e gli zeri che restano.

---

## Slide 17 — Compressione: la sovrapposizione

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Compressione: la sovrapposizione*
- Punti:
  1. **Compressione**: *i concetti sopravvissuti al gate vengono ri-sommati in un unico vettore: più significati coesistono, sovrapposti, nello stesso embedding.*
  2. **La somma è uno spostamento**: *sommare quel contributo all'embedding originale — è il nodo `+` della skip connection — lo sposta nello spazio delle idee: il significato si muove, si arricchisce.*
- Nota in basso: *La stessa geometria della Slide 13: le relazioni sono direzioni. Il blocco calcola la direzione in cui muovere il significato.*

**Visual**: la somma dal basso verso l'alto, e in cima il punto che si sposta nello spazio delle idee.

**Prompt per schema SVG**:
> **In basso**, le **attivazioni sopravvissute al gate**: tre barre burgundy, disegnate esattamente come nella Slide 16 — la continuità visiva è il punto — con i nomi dei concetti sotto.
>
> Le tre convergono verso l'alto nel **contributo del blocco**: un vettore da 4 celle teal (*una direzione nello spazio delle idee*).
>
> Sopra, un nodo `+` con, in ingresso da sinistra, l'**embedding originale** (4 celle teal, etichetta *skip connection*). In uscita l'**embedding spostato**: 4 celle teal con bordo burgundy — è un embedding, ma non più quello di prima. Da lì una linea tratteggiata sale verso lo spazio delle idee.
>
> **In cima**, un piano punteggiato: due nuvole (`ANIMALI DOMESTICI`, `LUOGHI DELLA CASA`), il punto `«gatto» in ingresso` e una freccia burgundy che lo porta a `«gatto» dopo il blocco`, etichettata *= il contributo del blocco*.
>
> **Elemento focale**: la freccia nel piano è la stessa cosa del vettore-contributo disegnato sotto. Vanno lette come un oggetto solo.

---

## Slide 18 — Attention: domande e chiavi (Q e K)

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%, classe `micro`: è la slide più piena della sezione); la griglia al centro-destra (~60%); il box metafora affiancato alla mini-mappa, e la nota multi-head in basso.

**Testo**:
- Titolo: *Attention: domande e chiavi*
- Punti:
  1. **Ogni token emette una domanda (Q)**: *"cosa sto cercando?" — e una chiave (K): "cosa offro a chi cerca?"*
  2. **L'affinità è ancora un prodotto scalare**: *Q·K misura quanto la chiave di un token risponde alla domanda di un altro.*
  3. **Tre proiezioni semantiche apprese**: *tre matrici, applicate all'embedding di ogni token, lo proiettano in tre vesti. Q e K sono ottimizzate — testa per testa — per trovare il token giusto nel contesto precedente. Ciò su cui fai match non è ciò che ricevi.*
- Box metafora: *Come in biblioteca: porti una richiesta al banco (Q), il match si fa sulle etichette dei dorsi (K). Il contenuto del libro (V) è un'altra cosa — e arriva dopo.*
- Nota in basso (multi-head): *Ogni testa fa una domanda diversa — sintassi, riferimenti, tono: più ricerche in parallelo.*

**La griglia dell'attention (condivisa da 18, 19, 20 e 20b)**: un'unica tabella, ferma per quattro slide. **Colonne** = i cinque token della frase `Il portiere diede un calcio`; **righe** = i passi del calcolo, impilati **dal basso verso l'alto**:

`token` · `embedding` · **`× W^Q`** · `q` · **`× W^K`** · `k` · `q · k` · `softmax` · **`× W^V`** · `v` · `v × peso` · `somma`

Le righe non ancora raggiunte restano disegnate ma **spente**: si vede che manca qualcosa. Le tre matrici stanno nei varchi fra le righe, disegnate come griglie 4×3, e da ognuna parte una linea orizzontale con una freccia per colonna — *è la stessa matrice per tutta la frase*. Una linea di alimentazione verticale sale dalla riga `embedding` e tocca tutte e tre le matrici: **le tre proiezioni partono tutte dall'embedding**, non l'una dall'altra.

La riga `q` è popolata **solo nella colonna `calcio`**: K e V esistono per ogni token, Q solo per quello che sta cercando. È già, disegnata, la nota della Slide 23 (*«Q del passato: calcolate e buttate»*).

**Numeri, unici per tutte e quattro le slide** — `calcio` guarda anche sé stesso, quindi i punteggi sono cinque e le percentuali sono una softmax vera sui punteggi:

| | `Il` | `portiere` | `diede` | `un` | `calcio` |
|---|---|---|---|---|---|
| `q · k` | 0.1 | 3.1 | 1.4 | 0.2 | 1.9 |
| `softmax` | 3% | 63% | 12% | 3% | 19% |

**Visual (stadio 1 di 3)**: `slide18-griglia-qk.svg`. Accende `token`, `embedding`, `× W^Q`, `q`, `× W^K`, `k`, `q · k`. Restano spente `softmax`, `v`, `v × peso`, `somma`. In cima, un callout scuro: *«Il match si fa su q · k. Ma ciò su cui fai match non è ciò che ricevi: manca ancora una riga.»*

**Elemento focale**: le due righe `q` e `k` con le rispettive matrici — è qui che il terzo bullet ("tre proiezioni della stessa cosa") smette di essere solo testo e diventa disegno.

## Slide 19 — Softmax: il budget di ascolto

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); la griglia al centro-destra (~60%); mini-mappa in fondo alla colonna di testo; nota in basso.

**Testo**:
- Titolo: *Softmax: il budget di ascolto*
- Punti:
  1. **Da punteggi a percentuali**: *la softmax trasforma le affinità grezze in pesi che sommano a 1 — un budget di ascolto da distribuire.*
  2. **Esagera le differenze**: *chi è più affine prende quasi tutto il budget: è un "max morbido".*
- Nota in basso: *La stessa macchina la ritroveremo all'uscita del modello, quando i punteggi diventeranno la distribuzione sul prossimo token.*

**Visual (stadio 2 di 3)**: `slide19-griglia-softmax.svg`. La stessa griglia della Slide 18, con in più la riga `softmax` accesa. Ogni cella porta la percentuale e, in fondo, una barretta sottile proporzionale — il confronto si legge senza che la barra passi sotto al numero. In cima, il callout: *«Le stesse affinità, ora come budget. I divari si allargano: 3.1 contro 1.9 diventa 63% contro 19%.»*

**Elemento focale**: il passaggio fra due righe adiacenti della stessa tabella — `q · k` sopra, `softmax` sotto — che è il modo più diretto di mostrare cosa fa la softmax: normalizza e amplifica.

## Slide 20 — V: la consegna

**Layout**: titolo in alto; i due punti di testo a sinistra (~30%); la griglia al centro-destra (~65%); mini-mappa in fondo alla colonna di testo; nota in basso.

**Testo**:
- Titolo: *V: la consegna*
- Punti:
  1. **Il terzo volto del token: il value**: *la proiezione V è ottimizzata per estrarre la semantica di quel token in quel contesto — ciò che consegna, se ascoltato, per arricchire il token in arrivo. Il libro, non l'etichetta.*
  2. **La somma pesata è lo spostamento**: *i value, pesati dal budget di ascolto, si sommano all'embedding: il significato si muove verso l'interpretazione giusta.*
- Nota in basso: *È la manipolazione della Slide 17 — ma qui guidata dal contesto: sono gli altri token a decidere la direzione.*

**Visual (stadio 3 di 3)**: `slide20-griglia-v.svg`. La griglia completa: si accendono `× W^V`, `v`, `v × peso` — dove le celle sbiadiscono in proporzione al peso — e `somma`, con le frecce che convergono da tutte le colonne nel nuovo embedding di `calcio` (4 celle teal con bordo burgundy: è un embedding, ma non più quello del vocabolario). In cima, il callout: *«Il contesto ha consegnato. L'embedding di "calcio" non è più quello del vocabolario: è quello di questa frase.»*

**Elementi focali**: la sbiadatura della riga `v × peso` (il budget che pesa la consegna) e la convergenza nella somma. Il callout prepara la Slide 20b.

> **Nota di revisione**: la scena "spazio delle idee con le due frasi divergenti", che in una versione precedente stava in questa slide, è diventata la Slide 20b. Serviva un confronto fra due frasi, e la griglia ne mostra una alla volta.

## Slide 20b — Lo stesso token, due contesti

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); la griglia al centro-destra (~60%); mini-mappa in fondo alla colonna di testo; nota in basso. La slide ha **due fotogrammi** che si scambiano con un fragment reveal.js: due SVG sovrapposti, stesso viewBox e stessa geometria, così cambia solo il contenuto.

**Testo**:
- Titolo: *Lo stesso token, due contesti*
- Punti:
  1. **Stessa macchina, altra frase**: *le tre matrici di proiezione non cambiano: cambia solo ciò che entra.*
  2. **Il budget si sposta da solo**: *nella prima frase «calcio» ascolta «portiere» al 63%; nella seconda ascolta «ossa» e «forti» — 78% in due.*
  3. **Ed è questo a decidere il significato**: *lo stesso token esce dall'attention in due punti diversi dello spazio delle idee.*
- Nota in basso: *Nessuno ha scritto da nessuna parte che «calcio» è ambiguo: l'ambiguità la scioglie il contesto, e lo strumento sono i pesi.*

**Visual**: la griglia completa (tutte le righe accese), due volte.

**File**: `slide20b-contesto-frase1.svg`, `slide20b-contesto-frase2.svg`.

**Prompt per schema SVG**:

> Stessa griglia delle Slide 18–20, con tutte le righe accese. Al posto del callout scuro, in cima una fascia `DOVE FINISCE «CALCIO»`: a sinistra il punto `calcio (dal vocabolario)`, una freccia orizzontale, e a destra **una sola nuvola** con il titolo dell'area semantica e tre parole vicine. La nuvola cambia insieme alla frase: la transizione muove i pesi **e** la destinazione, così si vede che la seconda è conseguenza dei primi.
>
> **Fotogramma 1** — frase `Il portiere diede un calcio`; nuvola `SPORT`: `pallone`, `rigore`, `partita`.
>
> **Fotogramma 2** — frase `ossa forti con il calcio`; nuvola `MINERALI · SALUTE`: `ferro`, `vitamina D`, `latte`.
>
> | | `q · k` più alto | budget |
> |---|---|---|
> | frase 1 | `portiere` 3.1 | portiere **63%**, calcio 19%, diede 12%, Il 3%, un 3% |
> | frase 2 | `ossa` 2.9 | ossa **52%**, forti **26%**, calcio 16%, con 3%, il 3% |
>
> Nella frase 1 un solo token si prende quasi tutto; nella frase 2 il budget si **divide fra due** (78% in due). Il contrasto è deliberato: è più realistico, e dà una frase in più da dire.
>
> `ossa` non compare fra le parole della nuvola della frase 2, perché lì è un token della frase.
>
> **Elemento focale**: il fatto che a cambiare sia **solo la riga dei token**. Tutto il resto della macchina — le tre matrici, la struttura, i passi — è identico: è il contesto, e nient'altro, a spostare il significato.

## Slide 21 — Positional encoding: l'ordine conta

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Positional encoding: l'ordine conta*
- Punti:
  1. **L'attention è cieca all'ordine**: *nel match Q·K nulla dice chi viene prima: "il gatto morde il cane" e "il cane morde il gatto" sarebbero lo stesso sacchetto di embedding.*
  2. **La correzione**: *a ogni embedding si somma un vettore che codifica la sua posizione nella sequenza.*
  3. **Ancora uno spostamento**: *anche la posizione è una direzione nello spazio delle idee: "gatto, secondo token della frase" è il punto `gatto`, spostato un po'.*
- Nota in basso: *È l'innesto "+ positional encoding" già visto nella mappa dell'architettura (Slide 15).*

**Visual**: due scene impilate — in basso il problema (senza posizione), in alto la correzione.

**Prompt per schema SVG**:
> **Scena inferiore — senza posizione**: le due frasi `il gatto morde il cane` e `il cane morde il gatto` come righe di tessere; due frecce che convergono su **un solo sacchetto** tratteggiato contenente cinque vettori teal sparsi e ruotati. Etichetta: *stesso sacchetto: per l'attention sono indistinguibili*.
>
> **Scena superiore — con positional encoding**, due parti:
>   - *a sinistra, il meccanismo su un token solo*, dal basso: tessera `gatto` → 4 celle teal (l'embedding) → nodo `+` giallo → 4 celle **gialle** (il vettore della posizione 2) → 4 celle teal con bordo giallo (*«gatto», secondo token: lo stesso punto, spostato un po'*);
>   - *a destra, i due insiemi ora ordinati*: due riquadri, `FRASE 1 — «il gatto morde il cane»` e `FRASE 2 — «il cane morde il gatto»`, con i vettori **in fila** e una barretta gialla `pos 1 … pos 5` sotto ciascuno. Il vettore di `gatto` è in tinta più intensa: nella frase 1 sta in posizione 2, nella frase 2 in posizione 5. **I due riquadri devono risultare visibilmente diversi** — è tutto il messaggio della slide.
>
> **Elemento focale**: sparso sotto contro ordinato sopra.

---

## Slide 22 — Reverse embedding: tornare ai token

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Reverse embedding: tornare ai token*
- Punti:
  1. **L'operazione inversa della prima**: *all'ingresso, da token a vettore; all'uscita, dal vettore finale a una preferenza su ogni token del vocabolario.*
  2. **Ancora prodotti scalari**: *l'embedding finale viene confrontato con il vettore di ogni token del vocabolario: ~100.000 affinità — i logits — che la softmax trasforma nella distribuzione.*
- Nota in basso: *È la distribuzione da cui siamo partiti: il cerchio del "manipolatore di embeddings" si chiude.*

**Visual**: la testa del modello, dal basso verso l'alto — è lo stesso percorso che chiude la torre della Slide 15.

**Prompt per schema SVG**:
> Dal basso: l'**embedding finale** (4 celle teal, *dopo tutti i blocchi*), con accanto la nota della simmetria: *all'ingresso da token a vettore. Qui il percorso si inverte: da vettore a token.*
>
> Sopra, il **vocabolario**: un riquadro con una riga per token — nome monospaziato, il suo vettore (4 celle grigie), il simbolo `·` e il **logit**: `sul 4.2`, `un 3.9`, `morbido 3.5`, `nero 3.3`, `stanco 2.8`, `Parigi −3.1`, poi `⋯ ~100.000 righe`. A destra, dentro il riquadro: *ogni riga è un prodotto scalare fra l'embedding finale e il vettore del token* e *Parigi ha logit negativo: l'affinità non seleziona soltanto, esclude*.
>
> Sopra ancora il blocco **`softmax`** (nero, come nella torre), con il richiamo *la stessa macchina del budget di ascolto*.
>
> **In cima**, la distribuzione a barre: `sul` 30%, `un` 22%, `morbido` 15%, `nero` 12%, `stanco` 8%, poi *… e gli altri ~100.000 token*. Sono gli stessi valori della Slide 5 e della Slide 15.
>
> **Elemento focale**: la simmetria ingresso/uscita, e il logit negativo di `Parigi`.

---

## Slide 23 — Il contesto ha un costo

**Layout**: titolo in alto; i tre punti di testo a sinistra (~30%); visual a due pannelli al centro-destra (~65%); nota in basso.

**Testo**:
- Titolo: *Il contesto ha un costo*
- Punti:
  1. **Il costo è quadratico**: *ogni nuovo token fa Q·K con tutti i precedenti: raddoppi il contesto, quadruplichi il lavoro.*
  2. **Prefill**: *il costo iniziale di "leggere" il prompt: calcolare K e V di ogni token, a ogni strato.*
  3. **KV cache**: *chiavi e valori dei token già visti si salvano: ogni giro del 1° loop paga solo il token nuovo.*
- Nota in basso: *Funziona perché la masked attention rende il passato immutabile: i token precedenti non vedono il nuovo, quindi i loro K, V e fully connected non cambiano mai. Il contesto resta comunque una risorsa costosa — lo ritroveremo.*

**Visual**: due pannelli a confronto — generare il token n-esimo senza e con KV cache — con evidenza di ciò che viene ricalcolato in un caso e riusato nell'altro.

**Prompt per schema SVG**:
> Diagramma a due pannelli affiancati, stesso impianto: una griglia con i token del contesto sulle colonne (`Il`, `gatto`, `è`, `sul`, `tavolo`, `e`, e l'ultima colonna marcata `token nuovo`) e gli strati del modello sulle righe (3-4 righe etichettate `strato 1`, `strato 2`, `…`, `strato N`; ogni cella rappresenta i calcoli K, V, FC di quel token a quello strato).
>
> **Pannello sinistro — `senza KV cache`**: TUTTE le celle della griglia sono accese/attive (da ricalcolare). Annotazioni puntate sulle celle del passato: `K e V: ricalcolate`, `fully connected: rifatti`, `Q del passato: calcolate e buttate`. Sotto il pannello: `costo del token n-esimo ≈ n² — ricalcoli tutto il passato, a ogni strato`.
>
> **Pannello destro — `con KV cache`**: solo l'ultima colonna (`token nuovo`) è accesa; tutte le colonne del passato sono rese come archivio salvato (celle quiete, etichettate `K,V in cache`), con una freccia dal blocco-archivio verso l'attention del token nuovo: `riusate, non ricalcolate`. Sotto il pannello: `costo del token n-esimo ≈ n — paghi solo il token nuovo`.
>
> **In basso, tra i due pannelli**: una riga che spiega il perché: `la masked attention rende il passato immutabile → si può salvare`.
>
> **Elemento focale**: il contrasto tra le due aree accese — l'intera griglia a sinistra contro la singola colonna a destra: è la differenza di costo il messaggio della slide. Le etichette dei token sono di natura token/codice.

## Slide 24 — La conoscenza è nei pesi

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual a due pannelli al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *La conoscenza è nei pesi*
- Punti:
  1. **Ciò che è scritto**: *la conoscenza abita nei vettori appresi — gli embedding dei token e le righe delle matrici: i pattern dei rilevatori e i loro contributi.*
  2. **Ciò che emerge**: *le regolarità geometriche tra quei vettori — le direzioni-relazione dello spazio delle idee. Nessuno le ha scritte: si sono formate perché servivano a predire.*
- Nota in basso: *Niente archivio consultabile, niente righe di database. Ed è per questo che il recupero può sbagliare — prossima slide.*

**Visual**: la stessa domanda — "qual è la capitale della Francia?" — risolta in due modi: a sinistra un database che trova la riga; a destra il modello, dove la risposta è distribuita tra rilevatori e geometria.

**Prompt per schema SVG**:
> Diagramma a due pannelli affiancati, stessa domanda in alto al centro: `Qual è la capitale della Francia?`.
>
> **Pannello sinistro — `un database`**: una tabella con righe `paese | capitale` (`Italia | Roma`, `Francia | Parigi`, `Germania | Berlino`); la riga `Francia | Parigi` è selezionata, con etichetta `trova la riga: recupero esatto`.
>
> **Pannello destro — `un LLM`**: nessuna tabella. Due elementi che cooperano:
>   1. un rilevatore (riga di matrice) etichettato `pattern: "capitale della Francia"` che scatta e consegna un contributo-vettore che spinge verso `Parigi`;
>   2. un mini piano dello spazio delle idee con la freccia `Francia → Parigi` parallela a `Italia → Roma` (etichetta: `regolarità emersa, non scritta`).
> Etichetta del pannello: `la risposta è distribuita: vettori scritti + geometria emersa`.
>
> **Elemento focale**: il contrasto tra la riga selezionata del database (recupero) e la natura distribuita del pannello destro (ricostruzione) — è la differenza che prepara la slide sul compressore lossy.

## Slide 25 — L'LLM come compressore lossy

**Layout**: titolo in alto; concetto centrale in evidenza; tre punti sotto; visual a destra (~45%); pull-quote in basso.

**Testo**:
- Titolo: *L'LLM come compressore lossy*
- Concetto centrale (in evidenza): *Per far stare trilioni di token in miliardi di parametri, il modello è costretto ad astrarre: non memorizza, modella.*
- Punti:
  1. **I numeri non tornano**: *non c'è spazio per memorizzare letteralmente il training set.*
  2. **Cosa resta**: *concetti, relazioni, regolarità — la geometria dello spazio delle idee.*
  3. **Il sottoprodotto**: *le capacità emergenti — ragionamento, analogia, transfer tra domini — non sono programmate: sono un effetto collaterale della compressione.*
- Pull-quote in basso: *"ChatGPT è un JPEG sfocato del web"* — Ted Chiang, The New Yorker. E per comprimere così, ha dovuto capire.

**Visual**: l'imbuto di compressione: la materia prima eterogenea che entra, e in uscita qualcosa di qualitativamente diverso — una rete di concetti, non una miniatura.

**Prompt per schema SVG**:
> Diagramma verticale a imbuto.
>
> **Parte superiore — la materia prima**: un'area larga riempita densamente di piccoli pittogrammi eterogenei (documenti, libri, pagine web, snippet di codice — decine di elementi in griglia disordinata). Etichetta: `trilioni di token — web, libri, codice`.
>
> **Al centro — l'imbuto**: una grande forma a imbuto dall'area larga a un'area stretta, con etichetta `compressione per astrazione`.
>
> **Parte inferiore — il modello**: un'area piccola divisa in due sotto-zone:
>   1. a sinistra, una rete di nodi concettuali connessi, con pochi nodi etichettati: `sintassi`, `causa-effetto`, `temporalità`, `oggetti e proprietà`, `analogia`;
>   2. a destra, un piccolo riquadro sfocato/pixelato che suggerisce un'immagine riconoscibile ma non fedele, con etichetta `riconoscibile, non fedele`.
>
> **Punto visivo centrale (elemento focale)**: ciò che sta sotto l'imbuto NON è una versione rimpicciolita di ciò che sta sopra — è qualitativamente diverso. La compressione è concettuale, non letterale.

## Slide 26 — Conseguenze della compressione

**Layout**: titolo in alto; due colonne contrastive al centro; regola pratica in basso come blocco evidenziato.

**Testo**:
- Titolo: *Conseguenze della compressione*
- **Colonna sinistra — Dove è forte**:
  1. *Framing concettuali su qualunque dominio*
  2. *Ragionamento e analogia*
  3. *Trasformazione di testo: traduzione, sintesi, riformattazione*
- **Colonna destra — Dove serve cautela**:
  1. *Fatti puntuali: date, numeri, citazioni letterali*
  2. *Conoscenza post-cutoff*
  3. *Nicchie poco rappresentate nel training*
  4. *Dati proprietari mai visti*
  5. *Calcoli numerici precisi*
- Regola pratica in basso (evidenziata): *Fidati del framing, verifica i fatti. Le allucinazioni non sono un bug morale del modello: sono il comportamento strutturale di un compressore lossy a cui chiedi di ricostruire ciò che non ha memorizzato bene.*

**Visual**: nessuno. Il contrasto tra le due colonne è l'elemento visivo.

## Slide 27 — MoE: non tutti i pesi lavorano sempre

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *MoE: non tutti i pesi lavorano sempre*
- Punti:
  1. **Il perché**: *il fanout è la parte più costosa — ma per un dato token la maggior parte dei rilevatori resta muta. Allora i pesi si spezzano in esperti, e si attivano solo i pochi rilevanti.*
  2. **Il router**: *davanti agli esperti, un piccolo selettore decide a chi mandare ogni token.*
- Nota in basso: *Il risultato: modelli enormi nei parametri totali, ma con un costo per token da modello piccolo. Torneremo sul lato economico.*

**Visual**: il blocco fully connected dell'architettura che si apre in una schiera di esperti con un router davanti: il token attraversa solo i due esperti accesi.

**Prompt per schema SVG**:
> Diagramma orizzontale: un token in transito attraversa un blocco fully connected trasformato in Mixture of Experts.
>
> **A sinistra**: una colonnina-vettore etichettata `embedding in transito`, che entra in un piccolo blocco `router`.
>
> **Al centro**: una schiera verticale di 8 blocchi identici etichettati `esperto 1` … `esperto 8`. Dal router partono frecce verso solo 2 esperti (es. `esperto 3` ed `esperto 6`), che sono accesi/attivi; gli altri 6 sono spenti/quiescenti. Etichetta sul gruppo: `ogni esperto: un fully connected più piccolo`.
>
> **A destra**: i contributi dei 2 esperti attivi convergono in un nodo `+` e proseguono come un unico vettore in uscita.
>
> **Didascalia interna in basso**: `parametri totali: tutti gli esperti — lavoro per token: solo 2`.
>
> **Elemento focale**: il contrasto tra i 2 esperti accesi e i 6 spenti, con il router come arbitro — è il messaggio della slide. Il richiamo visivo al blocco fully connected dell'architettura (Slide 15) deve essere riconoscibile.
