# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 3 — Perché funziona**
**Obiettivo di apprendimento**: il partecipante si costruisce un modello mentale dell'interno dell'LLM — embeddings come "spazio delle idee", prodotto scalare come sovrapposizione, fully connected e attention, context / complessità quadratica / KV cache, conoscenza intrinseca nei pesi, MoE.
**Messaggio chiave (takeaway)**: Nello spazio degli embedding il significato è geometria: vicinanza è affinità, direzioni sono relazioni. (Il "compressore lossy" ha una slide dedicata, ma non è il takeaway della sezione.)
**Budget**: ~40 min — la sezione più lunga dell'incontro.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec3.html` | Separatore — Sezione 3: Perché funziona |
| `slides/slide10-parola-vettore.html` | Slide 10 — La base di tutto: a ogni parola il suo vettore |
| `slides/slide11-vettori-prodotto-scalare.html` | Slide 11 — Vettori e prodotto scalare |
| `slides/slide12-scala-del-calcolo.html` | Slide 12 — La scala del calcolo: vettori e matrici |
| `slides/slide13-embeddings.html` | Slide 13 — Embeddings: lo spazio delle idee |
| `slides/slide14-tokenizzazione.html` | Slide 14 — La tokenizzazione |
| `slides/slide15-architettura.html` | Slide 15 — L'architettura, in un colpo d'occhio |
| `slides/slide16-fanout.html` | Slide 16 — Fanout: il matching concettuale |
| `slides/slide17-compressione.html` | Slide 17 — Compressione: la sovrapposizione |
| `slides/slide18-attention-qk.html` | Slide 18 — Attention: domande e chiavi (Q e K) |
| `slides/slide19-softmax.html` | Slide 19 — Softmax: il budget di ascolto |
| `slides/slide20-attention-v.html` | Slide 20 — V: la consegna |
| `slides/slide21-positional-encoding.html` | Slide 21 — Positional encoding: l'ordine conta |
| `slides/slide22-reverse-embedding.html` | Slide 22 — Reverse embedding: tornare ai token |
| `slides/slide23-costo-contesto.html` | Slide 23 — Il contesto ha un costo |
| `slides/slide24-conoscenza-nei-pesi.html` | Slide 24 — La conoscenza è nei pesi |
| `slides/slide25-compressore-lossy.html` | Slide 25 — L'LLM come compressore lossy |
| `slides/slide26-moe.html` | Slide 26 — MoE: non tutti i pesi lavorano sempre |

> **Logica dell'ordine**: 10–13 i mattoni (parola→vettore, prodotto scalare, la scala del calcolo, spazio delle idee) → 14 la tokenizzazione corregge "parola" in "token" → 15 la mappa dell'architettura → 16–22 zoom sui blocchi della mappa (fanout, compressione, attention in tre tempi Q·K / softmax / V, positional encoding, reverse embedding) → 23 il costo del contesto → 24–25 la conoscenza e la sua natura compressa (fronte 2) → 26 MoE.
>
> **Filo rosso della sezione — le operazioni di manipolazione degli embeddings**: l'LLM come manipolatore di embeddings (punchline Slide 13) si articola in operazioni nominate slide per slide: **spostamento** (Slide 13, direzioni come relazioni), **matching/fanout** (Slide 16), **compressione/sovrapposizione** (Slide 17), e l'attention come manipolazione guidata dal contesto (Slide 18–20: match Q·K, budget softmax, consegna dei value); anche la posizione è uno spostamento (Slide 21).

---

## Slide 10 — La base di tutto: a ogni parola il suo vettore

**Layout**: titolo in alto; visual al centro (~55%); le due frasi di testo sotto il visual; nota in basso.

**Testo**:
- Titolo: *La base di tutto: a ogni parola il suo vettore*
- Frasi:
  1. *Per far entrare il linguaggio in una macchina che calcola, la mossa fondativa è: a ogni parola, una lista di numeri.*
  2. *Quell'associazione non la scrive nessuno a mano: viene appresa.*
- Nota in basso: *Perché proprio dei numeri? Perché sui numeri si può calcolare — è la prossima slide.*

**Visual**: tre parole che diventano tre vettori — la tabella di associazione parola → lista di numeri.

**Prompt per schema SVG**:
> Diagramma semplice a due colonne collegate da frecce.
>
> **Colonna sinistra**: tre parole in riquadri: `gatto`, `cane`, `Parigi`.
>
> **Colonna destra**: per ciascuna parola, una freccia che porta a una colonnina di numeri stilizzata: `gatto → [0.8, −1.3, 2.1, …]`, `cane → [0.7, −1.1, 1.9, …]`, `Parigi → [−2.4, 0.6, −0.3, …]`. I vettori di `gatto` e `cane` hanno numeri visibilmente simili tra loro; quello di `Parigi` visibilmente diverso (senza commentarlo: è un seme per la slide sullo spazio delle idee).
>
> Sotto le colonne, un'etichetta: *associazione appresa durante l'addestramento, non scritta a mano*.
>
> **Elemento focale**: la freccia di associazione parola → vettore — è la mossa fondativa che la slide insegna. La somiglianza numerica tra `gatto` e `cane` è un dettaglio deliberato ma non evidenziato.

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

**Visual**: i tre gradini della scala, impilati: dal prodotto scalare singolo, alla moltiplicazione vettore-matrice come batteria di allineamenti, alla matrice-matrice come ripetizione su più vettori.

**Prompt per schema SVG**:
> Diagramma a tre livelli impilati verticalmente, ognuno un gradino della stessa scala.
>
> **Livello 1 — `vettore · vettore = numero`**: due colonnine-vettore affiancate, il simbolo `·`, e in uscita un singolo numero in un riquadro con etichetta `allineamento`.
>
> **Livello 2 — `vettore × matrice = vettore`**: una colonnina-vettore in ingresso; una matrice disegnata esplicitamente come 4 colonnine-vettore affiancate e raggruppate (etichetta: `una matrice = una batteria di vettori`); in uscita una colonnina-vettore di 4 celle, dove ogni cella è collegata con una linea sottile alla colonna corrispondente della matrice (etichetta: `ogni cella = l'allineamento con un vettore della batteria`).
>
> **Livello 3 — `matrice × matrice = matrice`**: più colonnine-vettore in ingresso raggruppate in una matrice (etichetta: `molti vettori insieme — es. tutti i token della frase`), la stessa matrice-batteria del livello 2, e in uscita una griglia (etichetta: `stessa operazione, ripetuta per ogni vettore`).
>
> **Elemento focale**: il livello 2 — la matrice come batteria di vettori e le linee cella-per-colonna che mostrano che moltiplicare per una matrice significa interrogare una batteria di rilevatori. I livelli 1 e 3 fanno da gradini di ingresso e uscita.

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

**Visual**: due frasi tokenizzate a confronto — una tutta di parole comuni (un token ciascuna), una con una parola rara spezzata in frammenti; ogni token con il suo id numerico di vocabolario.

**Prompt per schema SVG**:
> Diagramma a due righe di esempio, ognuna mostra un testo che viene spezzato in tessere-token.
>
> **Riga 1**: il testo `Il gatto è sul tavolo` spezzato in 5 tessere adiacenti: `Il` · `gatto` · `è` · `sul` · `tavolo`. Sotto ogni tessera, il suo id numerico di vocabolario (numeri plausibili a 4-5 cifre, es. `243`, `28741`, `1105`, `3387`, `9152`). Etichetta a lato: *parole comuni: un token ciascuna*.
>
> **Riga 2**: la parola `elettroencefalogramma` spezzata in 3 tessere: `elettro` · `encefal` · `ogramma`, ognuna con il suo id. Etichetta a lato: *parola rara: spezzata in frammenti*.
>
> **In basso**: un riquadro-vocabolario stilizzato con etichetta `vocabolario fisso: ~100.000 token`, da cui una freccia risale verso le tessere (i token vengono da lì).
>
> **Elemento focale**: la spezzatura della parola rara della riga 2 — il contrasto con la riga 1 è il messaggio (l'unità è il token, non la parola). Testi delle tessere e id numerici sono di natura token/codice.

## Slide 15 — L'architettura, in un colpo d'occhio

**Layout**: titolo in alto; il diagramma occupa quasi tutta la slide (~80%), sviluppo orizzontale da sinistra a destra; didascalia e note di semplificazione in basso.

**Testo**:
- Titolo: *L'architettura, in un colpo d'occhio*
- Didascalia: *Dal testo alla distribuzione sul prossimo token. Ogni pezzo di questo percorso è una delle prossime slide.*
- Note in basso (piccole):
  - *Il blocco attention + fully connected è ripetuto N volte (nei modelli grandi, ~100).*
  - *Dopo la distribuzione, il sampling sceglie il token effettivo.*
  - *Diagramma semplificato: omesse le normalizzazioni.*

**Visual**: pipeline orizzontale completa del transformer (decoder-only): tokenizer → embedding + positional encoding → blocco [masked multi-head attention + fully connected, con skip connection attorno a ciascun sottoblocco] → matrice dei logits → softmax → distribuzione in uscita (la stessa della Slide 5).

**Prompt per schema SVG**:
> Pipeline orizzontale, da sinistra a destra, dell'architettura di un LLM (decoder-only). Le tappe:
>
> 1. **Input**: il testo `Il gatto è` in un riquadro.
> 2. **Tokenizer**: blocco che spezza il testo in token; in uscita i token come tessere separate (`Il`, `gatto`, `è`).
> 3. **Embedding + positional encoding**: blocco etichettato `Embedding`, con un innesto dal basso etichettato `+ positional encoding`; in uscita, le tessere diventano vettori (colonnine di numeri stilizzate).
> 4. **Il blocco transformer** (il cuore, racchiuso in un contenitore con etichetta `blocco — ripetuto ×N`): due sottoblocchi in sequenza:
>    - `Masked multi-head attention`: al suo interno si vedono più corsie parallele (es. 4) etichettate `teste`, che poi riconvergono;
>    - `Fully connected`;
>    - attorno a **ciascuno** dei due sottoblocchi, una skip connection: una freccia che aggira il sottoblocco e si ricongiunge dopo con un nodo `+`. Le due skip devono leggersi come "l'informazione scorre in un canale centrale e ogni sottoblocco aggiunge il suo contributo".
> 5. **Matrice dei logits**: blocco etichettato `matrice di reverse embedding → logits`.
> 6. **Softmax**: blocco etichettato `softmax`.
> 7. **Uscita**: un mini grafico a barre — la distribuzione sul prossimo token. Le barre più alte portano parole plausibili come completamento di `Il gatto è`: `sul` (~30%), `un` (~22%), `morbido` (~15%), `nero` (~12%), `stanco` (~8%); a seguire qualche barra minore senza etichetta. È la stessa distribuzione già vista quando si è definito il modello linguistico.
>
> **Elementi focali**: il contenitore del blocco ripetuto ×N (il cuore del modello) e la distribuzione finale in uscita — il percorso deve leggersi come "testo entra, distribuzione esce". Le etichette dei token e delle barre sono di natura "token/codice".

## Slide 16 — Fanout: il matching concettuale

**Layout**: titolo in alto; tre bullet a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Fanout: il matching concettuale*
- Bullet:
  1. **Un rilevatore per concetto**: *ogni riga della matrice è un pattern memorizzato; il prodotto scalare misura quanto l'embedding in transito gli somiglia.*
  2. **Tutti in parallelo (fanout)**: *migliaia di rilevatori scattano insieme, a ogni token, a ogni strato — lo spazio si espande.*
  3. **La non linearità è un gate**: *passa solo ciò che è davvero affine; tutto il resto viene azzerato.*
- Nota in basso: *È il rilevatore di affinità della Slide 11, moltiplicato per migliaia: da un rilevatore a una batteria di rilevatori.*

**Visual**: l'embedding in transito confrontato con una batteria di rilevatori concettuali (alcuni scattano, altri restano muti), seguita dal gate della non linearità che lascia passare solo le attivazioni forti.

**Prompt per schema SVG**:
> Diagramma orizzontale in tre stadi: un embedding confrontato in parallelo con una batteria di rilevatori concettuali, poi filtrato da un gate.
>
> **Stadio 1 — a sinistra**: un vettore (colonnina di numeri stilizzata) etichettato `l'embedding in transito`.
>
> **Stadio 2 — al centro, il fanout**: una pila verticale di 6 righe-rilevatore. Ogni riga contiene: un piccolo vettore-pattern, il simbolo `·` (prodotto scalare), e una barretta orizzontale che mostra l'attivazione risultante. Le righe, con etichetta ed esito:
>   1. `animale domestico` — attivazione alta (scattato);
>   2. `sta per arrivare un luogo` — attivazione alta (scattato);
>   3. `frase al presente` — attivazione media;
>   4. `contesto giuridico` — attivazione ≈ 0 (muto);
>   5. `linguaggio matematico` — attivazione ≈ 0 (muto);
>   6. `… e decine di migliaia di altri` (riga di elisione).
> L'embedding di sinistra è collegato con una freccia a ciascuna riga (stesso input per tutti i rilevatori). Una graffa verticale abbraccia la pila, con etichetta `fanout: lo spazio si espande`.
>
> **Stadio 3 — a destra, il gate**: una barriera verticale etichettata `non linearità: il gate`. Solo le frecce dei rilevatori con attivazione alta/media la attraversano e proseguono; le altre si fermano sulla barriera (troncate, con simbolo di azzeramento). In uscita, i soli concetti sopravvissuti: `animale domestico`, `sta per arrivare un luogo`, `frase al presente`.
>
> **Elementi focali**: il contrasto tra rilevatori scattati e muti (il matching concettuale) e la barriera del gate con le frecce troncate (il filtro). Gli esempi sono coerenti con il contesto ricorrente `Il gatto è sul…`.

## Slide 17 — Compressione: la sovrapposizione

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Compressione: la sovrapposizione*
- Punti:
  1. **Compressione**: *i concetti sopravvissuti al gate vengono ri-sommati in un unico vettore: più significati coesistono, sovrapposti, nello stesso embedding.*
  2. **La somma è uno spostamento**: *sommare quel contributo all'embedding originale — è il nodo `+` della skip connection — lo sposta nello spazio delle idee: il significato si muove, si arricchisce.*
- Nota in basso: *La stessa geometria della Slide 13: le relazioni sono direzioni. Il blocco calcola la direzione in cui muovere il significato.*

**Visual**: i vettori dei concetti sopravvissuti che si sommano in un unico contributo, il quale — aggiunto all'embedding originale — sposta il punto nello spazio delle idee.

**Prompt per schema SVG**:
> Diagramma orizzontale in due stadi.
>
> **Stadio 1 — a sinistra, la somma**: tre piccole frecce-vettore etichettate con i concetti sopravvissuti al gate (`animale domestico`, `sta per arrivare un luogo`, `frase al presente`) che convergono su un nodo `+`, da cui esce un unico vettore etichettato `contributo del blocco`. Sotto il nodo, una seconda freccia entra nel `+`: è l'`embedding originale` che arriva dalla skip connection (etichetta: `skip connection`).
>
> **Stadio 2 — a destra, lo spostamento**: un piano che rappresenta lo spazio delle idee (stesso ambiente visivo della proiezione 2D degli embeddings). Un punto etichettato `"gatto" (in ingresso)` e una freccia di spostamento che lo porta a una nuova posizione etichettata `"gatto" (dopo il blocco)`, più vicina a una piccola nuvola di punti di contesto (`animali domestici`, `luoghi della casa`). La freccia di spostamento è la traduzione geometrica del `contributo del blocco` dello stadio 1 (le due frecce devono essere visivamente la stessa freccia, richiamata).
>
> **Elemento focale**: la freccia di spostamento nel piano — il punto che si muove è il messaggio della slide (la somma manipola il significato). Il nodo `+` con l'ingresso della skip connection è il secondo elemento in risalto.

## Slide 18 — Attention: domande e chiavi (Q e K)

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); box metafora e nota multi-head in basso.

**Testo**:
- Titolo: *Attention: domande e chiavi*
- Punti:
  1. **Ogni token emette una domanda (Q)**: *"cosa sto cercando?" — e una chiave (K): "cosa offro a chi cerca?"*
  2. **L'affinità è ancora un prodotto scalare**: *Q·K misura quanto la chiave di un token risponde alla domanda di un altro.*
  3. **Tre proiezioni semantiche apprese**: *tre matrici, applicate all'embedding di ogni token, lo proiettano in tre vesti. Q e K sono ottimizzate — testa per testa — per trovare il token giusto nel contesto precedente. Ciò su cui fai match non è ciò che ricevi.*
- Box metafora: *Come in biblioteca: porti una richiesta al banco (Q), il match si fa sulle etichette dei dorsi (K). Il contenuto del libro (V) è un'altra cosa — e arriva dopo.*
- Nota in basso (multi-head): *Ogni testa fa una domanda diversa — sintassi, riferimenti, tono: più ricerche in parallelo.*

**Visual**: la frase del portiere: il token `calcio` emette la sua domanda (Q), gli altri token espongono le loro chiavi (K), e i prodotti scalari Q·K accendono indicatori di affinità diversi.

**Prompt per schema SVG**:
> Diagramma su una frase di token: `Il portiere diede un calcio e …`.
>
> **Il token `calcio`** è marcato ed emette verso l'alto un fumetto-domanda etichettato `Q — cerco: chi compie l'azione, in che ambito` .
>
> **Gli altri token** espongono ciascuno una piccola targhetta-chiave `K`: `portiere → "persona, sport"`, `diede → "azione, passato"`, `un → "articolo"`, `Il → "articolo"`.
>
> **Tra il fumetto Q e ogni targhetta K**: una linea con il simbolo `·` (prodotto scalare) e un indicatore di affinità: `portiere` alto, `diede` medio, `un` e `Il` ≈ 0.
>
> **Elementi focali**: il match tra la domanda di `calcio` e la chiave di `portiere` (l'affinità più alta) e la separazione visiva domanda/chiave — due oggetti diversi emessi da ogni token. La frase è di natura token/codice.

## Slide 19 — Softmax: il budget di ascolto

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Softmax: il budget di ascolto*
- Punti:
  1. **Da punteggi a percentuali**: *la softmax trasforma le affinità grezze in pesi che sommano a 1 — un budget di ascolto da distribuire.*
  2. **Esagera le differenze**: *chi è più affine prende quasi tutto il budget: è un "max morbido".*
- Nota in basso: *La stessa macchina la ritroveremo all'uscita del modello, quando i punteggi diventeranno la distribuzione sul prossimo token.*

**Visual**: prima/dopo — i punteggi grezzi di affinità della slide precedente che passano nella softmax e diventano percentuali che sommano al 100%, con le differenze amplificate.

**Prompt per schema SVG**:
> Diagramma prima/dopo in due pannelli collegati da un blocco centrale `softmax`.
>
> **Pannello sinistro — punteggi grezzi**: barre orizzontali con i punteggi di affinità Q·K della frase del portiere: `portiere: 3.1`, `diede: 1.4`, `un: 0.2`, `Il: 0.1`. Etichetta: *affinità grezze — scala arbitraria*.
>
> **Blocco centrale**: `softmax`, con una freccia che entra e una che esce.
>
> **Pannello destro — budget di ascolto**: le stesse voci come percentuali: `portiere: 78%`, `diede: 17%`, `un: 3%`, `Il: 2%`, impilate in un'unica barra verticale che totalizza `100%` (etichetta: *il budget somma sempre a 100*).
>
> **Elementi focali**: il contrasto tra i due pannelli — a sinistra i divari sono moderati, a destra `portiere` domina — e l'etichetta del totale 100%. Sono i due effetti che la slide insegna: normalizzare e amplificare.

## Slide 20 — V: la consegna

**Layout**: titolo in alto; i due punti di testo a sinistra (~30%); visual al centro-destra (~65%); nota in basso.

**Testo**:
- Titolo: *V: la consegna*
- Punti:
  1. **Il terzo volto del token: il value**: *la proiezione V è ottimizzata per estrarre la semantica di quel token in quel contesto — ciò che consegna, se ascoltato, per arricchire il token in arrivo. Il libro, non l'etichetta.*
  2. **La somma pesata è lo spostamento**: *i value, pesati dal budget di ascolto, si sommano all'embedding: il significato si muove verso l'interpretazione giusta.*
- Nota in basso: *È la manipolazione della Slide 17 — ma qui guidata dal contesto: sono gli altri token a decidere la direzione.*

**Visual**: i pacchi-value che fluiscono verso `calcio` con dimensioni proporzionali al budget di ascolto, e — accanto — lo spazio delle idee in cui lo stesso token, in due frasi diverse, si sposta in direzioni opposte.

**Prompt per schema SVG**:
> Diagramma in due parti affiancate.
>
> **Parte sinistra — la consegna**, due mini-scene impilate:
>   1. Frase `Il portiere diede un calcio e …`: dai token partono pacchi-value verso `calcio`, con dimensione proporzionale al peso: pacco grande da `portiere (78%)`, piccolo da `diede (17%)`, trascurabili dagli altri. I pacchi convergono in un nodo `+` che entra in `calcio`.
>   2. Frase `Per le mie ossa ho preso il calcio e …`: pacco grande da `ossa`, medio da `preso`, che convergono allo stesso modo su `calcio`.
>
> **Parte destra — lo spazio delle idee** (stesso ambiente visivo delle slide precedenti): un unico punto `calcio (ambiguo)` da cui partono due frecce di spostamento divergenti: una verso una nuvola `sport` (punti: `pallone`, `rigore`, `partita`) etichettata `frase 1`; una verso una nuvola `minerali / salute` (punti: `ferro`, `vitamina D`, `ossa`) etichettata `frase 2`.
>
> **Elementi focali**: la dimensione dei pacchi (il budget di ascolto che pesa la consegna) e le due frecce divergenti dallo stesso punto — lo stesso token, spostato in direzioni opposte dal contesto. Le frasi sono di natura token/codice.

## Slide 21 — Positional encoding: l'ordine conta

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Positional encoding: l'ordine conta*
- Punti:
  1. **L'attention è cieca all'ordine**: *nel match Q·K nulla dice chi viene prima: "il gatto morde il cane" e "il cane morde il gatto" sarebbero lo stesso sacchetto di embedding.*
  2. **La correzione**: *a ogni embedding si somma un vettore che codifica la sua posizione nella sequenza.*
  3. **Ancora uno spostamento**: *anche la posizione è una direzione nello spazio delle idee: "gatto, secondo token della frase" è il punto `gatto`, spostato un po'.*
- Nota in basso: *È l'innesto "+ positional encoding" già visto nella mappa dell'architettura (Slide 15).*

**Visual**: le due frasi-gemelle che senza posizione collassano nello stesso insieme di embedding, e che con la somma dei vettori di posizione tornano distinguibili.

**Prompt per schema SVG**:
> Diagramma a due scene sovrapposte (sopra/sotto), stesso impianto.
>
> **Scena superiore — `senza posizione`**: due frasi come sequenze di tessere-token, una accanto all'altra: `il gatto morde il cane` e `il cane morde il gatto`. Da entrambe partono frecce verso UN UNICO insieme non ordinato di 5 colonnine-embedding (un "sacchetto": le stesse 5 colonnine, disposte alla rinfusa). Etichetta: `stesso sacchetto: per l'attention sono indistinguibili`.
>
> **Scena inferiore — `con positional encoding`**: le stesse due frasi, ma ogni tessera-token passa per un nodo `+` dove si somma un piccolo vettore di posizione (`pos 1` … `pos 5`). Ora le frecce portano a DUE insiemi distinti di embedding, visivamente diversi tra loro. Etichetta: `due frasi diverse: l'ordine è entrato nei vettori`.
>
> **Elementi focali**: il sacchetto unico della scena superiore (il problema) e i nodi `+` con i vettori di posizione della scena inferiore (la soluzione). Le frasi sono di natura token/codice.

## Slide 22 — Reverse embedding: tornare ai token

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Reverse embedding: tornare ai token*
- Punti:
  1. **L'operazione inversa della prima**: *all'ingresso, da token a vettore; all'uscita, dal vettore finale a una preferenza su ogni token del vocabolario.*
  2. **Ancora prodotti scalari**: *l'embedding finale viene confrontato con il vettore di ogni token del vocabolario: ~100.000 affinità — i logits — che la softmax trasforma nella distribuzione.*
- Nota in basso: *È la distribuzione da cui siamo partiti: il cerchio del "manipolatore di embeddings" si chiude.*

**Visual**: l'embedding finale confrontato con il vocabolario intero, i logits che ne escono e la softmax che li trasforma nella distribuzione sul prossimo token.

**Prompt per schema SVG**:
> Diagramma orizzontale in quattro stadi.
>
> **Stadio 1 — a sinistra**: un vettore (colonnina di numeri stilizzata) etichettato `embedding finale` (con sotto-etichetta: *dopo tutti i blocchi, per il contesto `Il gatto è`*).
>
> **Stadio 2 — il confronto col vocabolario**: una pila verticale che rappresenta il vocabolario (~100.000 righe, mostrate 5-6 con riga di elisione), ogni riga un token con il suo vettore: `sul`, `un`, `morbido`, `nero`, `Parigi`, `… ~100.000 righe`. L'embedding finale è collegato a ogni riga con il simbolo `·` (prodotto scalare).
>
> **Stadio 3 — i logits**: da ogni confronto esce un punteggio grezzo: `sul: 4.2`, `un: 3.6`, `morbido: 2.9`, `nero: 2.6`, `Parigi: −3.1`. Etichetta: `logits — affinità grezze`.
>
> **Stadio 4 — softmax e distribuzione**: un blocco `softmax` (con richiamo: *la stessa macchina del budget di ascolto*) da cui esce il grafico a barre della distribuzione: `sul` (~30%), `un` (~22%), `morbido` (~15%), `nero` (~12%), `stanco` (~8%), barre minori senza etichetta.
>
> **Elementi focali**: la simmetria ingresso/uscita (da token a vettore, da vettore a token) e la distribuzione finale — la stessa già vista nella definizione di modello linguistico e nell'architettura. Il punteggio negativo di `Parigi` mostra che l'affinità può anche escludere. Token e numeri sono di natura token/codice.

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

> **PLACEHOLDER** — da definire in un secondo passaggio. Appunti dall'intervista (non validati):
> raccoglie il fronte 2 della compressione (seminato in Slide 5). Possibile taglio in tre battute: (1) i numeri non tornano — terabyte di testo dentro centinaia di GB di pesi; (2) si perdono i dettagli, restano pattern e geometria; (3) ricostruisce, non recupera — l'allucinazione come comportamento naturale di un compressore lossy. Visual candidato: paragone JPEG.

## Slide 26 — MoE: non tutti i pesi lavorano sempre

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
