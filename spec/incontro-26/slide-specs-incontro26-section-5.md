# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 5 — Lo scenario, più o meno completo**
**Obiettivo di apprendimento**: il partecipante rilegge il loop conversazionale alla luce del **context rot** (la pila della Slide 42 non solo costa: degrada il modello), conosce multimodality e reasoning, inquadra gli elementi economici (raccogliendo il seme GPU della Slide 16) e la scelta open vs closed, e inquadra la scelta open vs closed.
**Nota di chiusura**: il deck **non ha più** né la slide «La formula, riletta» né la slide di chiusura verso l'incontro 27; finisce sulla fotografia del mercato. Il passaggio all'incontro 27 si fa a voce.
**Messaggio chiave (takeaway)**: Più contesto non è meglio: oltre una soglia il modello degrada. Da questo limite — e dal "chi esegue?" — nasce il bisogno dell'harness.
**Budget**: ~30 min, 16 slide. I contenuti "bonus" (multimodality, reasoning) NON sono sacrificabili.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec5.html` | Separatore — Sezione 5: Lo scenario, più o meno completo |
| `slides/slide23-costo-contesto.html` | Slide 40 — Il contesto ha un costo *(da Sez. 3)* |
| `slides/slide23b-api-stateless.html` | Slide 41 — L'API è stateless *(da Sez. 3)* |
| `slides/slide34-stateless.html` | Slide 42 — Il modello è stateless *(da Sez. 4)* |
| `slides/slide35-figlio-dei-dati.html` | Slide 43 — Il modello è figlio dei suoi training set *(da Sez. 4)* |
| `slides/slide36-context-rot.html` | Slide 44 — Context rot |
| `slides/slide36b-tool-context-rot.html` | Slide 45 — I tool accelerano il context rot |
| `slides/slide37-multimodality.html` | Slide 46 — Multimodality |
| `slides/slide38-reasoning.html` | Slide 47 — Reasoning |
| `slides/slide39-costi-training-inferenza.html` | Slide 48 — I costi: training, inferenza, distillazione |
| `slides/slide40-prezzo-per-token.html` | Slide 49 — Il prezzo per token |
| `slides/slide41-valore-traiettorie.html` | Slide 50 — Il valore delle traiettorie |
| `slides/slide42-closed-openweights-opensource.html` | Slide 51 — Closed, open weights, open source |
| `slides/slide43-tradeoff-closed-open.html` | Slide 52 — Quando closed, quando open |
| `slides/slide44-fine-tuning.html` | Slide 53 — Fine-tuning: riprendere la discesa |
| `slides/slide45-lora.html` | Slide 54 — LoRA: la correzione a basso rango |
| `slides/slide46-pareto.html` | Slide 55 — La fotografia del mercato: il Pareto qualità/costo |
| ~~`slides/slide47-chiusura.html`~~ | *Slide 47 (numerazione precedente) — rimossa* |

---

> **Nota di provenienza**: le Slide 40 e 41 arrivavano dalla Sezione 3 (erano il costo del
> contesto e l'API stateless), le Slide 42 e 43 dalla Sezione 4. Sono state spostate qui
> quando la sezione è diventata «Lo scenario, più o meno completo»: il filo non è più
> *come funziona* o *come si addestra*, ma *che cosa comporta nell'uso reale*.

## Slide 40 — Il contesto ha un costo

**Layout**: titolo in alto; i tre punti di testo a sinistra (~30%); visual a due pannelli al centro-destra (~65%); nota in basso.

**Testo**:
- Titolo: *Il contesto ha un costo*
- Punti:
  1. **Il costo è quadratico**: *ogni nuovo token fa Q·K con tutti i precedenti: raddoppi il contesto, quadruplichi il lavoro.*
  2. **Prefill**: *il costo iniziale di "leggere" il prompt: calcolare K e V di ogni token, a ogni strato.*
  3. **KV cache**: *di ogni token già visto si salvano K e V, per ogni strato e per ogni testa. Dei token precedenti non si rifà più nulla: né le proiezioni W^K e W^V, né — soprattutto — il passaggio dai fully connected layer, la parte più costosa. Ogni giro del 1° loop paga solo il token nuovo.*
- Nota in basso: *Funziona perché la masked attention rende il passato immutabile: K, V e fully connected dei token precedenti non cambiano mai. Le Q del passato, invece, non si salvano affatto — non servono più: servivano solo a produrre l'output di quel token, che non può più cambiare.*

> **Precisione sulle Q** (verificata, vale la pena tenerla): è corretto dire che la cache evita, per i token precedenti, sia le proiezioni `W^K`/`W^V` sia l'intero passaggio dai fully connected layer — ed è quest'ultimo la voce di costo più grossa, perché il FFN è la maggior parte dei parametri di un blocco. **Non** è invece corretto dire che la cache evita `W^Q` dei token precedenti: quelle Q non vengono "risparmiate", semplicemente **non servono più**. La query di un token serve solo a calcolare l'output *di quel token*, che con la masked attention non può più cambiare. In prefill vengono calcolate e buttate (è quello che dice il pannello sinistro della figura); in decoding non vengono calcolate affatto. Per il token nuovo, invece, si paga tutto una volta: `W^Q`, `W^K`, `W^V` e il FFN.

**Visual**: due griglie a confronto, **token sulle colonne e strati sulle righe** — è la stessa struttura della torre (Slide 20), con `strato 1` in basso e `strato N` in alto.

**Prompt per schema SVG**:
> Due pannelli affiancati, stessa griglia. **Colonne** = i token del contesto (`Il`, `gatto`, `è`, `sul`, `tavolo`, `e`) più una colonna finale marcata `token nuovo`; le etichette sono ruotate di 90° e allineate in basso. **Righe** = gli strati, **dal basso**: `strato 1`, `strato 2`, `⋯`, `strato N`. Le corsie verticali attraversano la griglia, come nella torre.
>
> **Ogni cella è la chiave e il valore di quel token a quello strato**: due barrette sovrapposte, grafite (`k`) e lightblue (`v`) — gli stessi oggetti della griglia dell'attention. In fondo alla slide, una legenda minima lo dichiara.
>
> **Pannello sinistro — `senza KV cache`**: ogni cella ha un anello burgundy: è tutta da ricalcolare. Annotazioni: *K e V: ricalcolate a ogni giro*, *fully connected: rifatti*, *Q del passato: calcolate e buttate*. Sotto: `costo del token n-esimo ≈ n²`.
>
> **Pannello destro — `con KV cache`**: le colonne del passato sono dentro un'area grigia etichettata `K, V in cache`, con le celle smorzate; **solo la colonna del token nuovo ha l'anello**. Una freccia dalla cache alla colonna nuova, etichettata *riusate, non ricalcolate*. Sotto: `costo del token n-esimo ≈ n`.
>
> **In fondo**: *la masked attention rende il passato immutabile → si può salvare*.
>
> **Elemento focale**: il contrasto fra le aree accese — tutta la griglia a sinistra, una colonna sola a destra.

---

## Slide 41 — L'API è stateless: cosa significa davvero

> Slide **ripresa dal deck MBA** (`gsom-april-2026`, `slide18-api-stateless.html`). Sta subito dopo la 40 perché è lo stesso costo, visto dall'altro lato: la 40 lo guarda dentro il modello (prefill, KV cache), la 41 lo guarda dalla conversazione e dalla bolletta. Prepara la Slide 42 della sezione 4, che riprende lo stateless dal lato del modello.

**Layout**: titolo in alto; due punti di testo e una nota a sinistra (~40%); il grafico delle curve a destra (~57%); blocco nero in fondo.

**Testo**:
- Titolo: *L'API è stateless: cosa significa davvero*
- Punti:
  1. **L'API non conserva stato tra chiamate** — *a ogni nuovo turno il contesto completo — system prompt, storico, nuovo input — viene inviato da capo al modello.*
  2. **Il contesto cresce con la conversazione** — *e con lui cresce il costo di ogni singolo turno: non paghi la domanda, paghi tutto quello che è stato detto finora.*
- Nota: *Senza KV cache il costo per turno crescerebbe quadraticamente. È il trucco della slide precedente, visto dal lato della bolletta: il provider riusa il lavoro già fatto e processa solo i token nuovi.*
- Blocco nero in fondo: *Il costo di un turno e la qualità della risposta dipendono dalla dimensione cumulativa del contesto, non dalla singola domanda.*

**Visual**: `slide23b-curve-costo.svg` — tre curve di costo per turno, adattate da `slide18-cost-curves.svg` del deck di aprile alla palette e ai font di questo deck.

**Prompt per schema SVG**:
> Piano cartesiano pulito. **Asse X**: `numero di turno`. **Asse Y**: `costo del singolo turno`. Tre curve che partono dall'origine:
>   1. `costo teorico del provider` — *senza KV cache: quadratico* — teal tratteggiata, la più ripida;
>   2. `costo in fattura per l'utente` — *lineare: paghi tutto il contesto* — grigia, pendenza media;
>   3. `costo reale del provider` — *con KV cache: lineare, e più basso* — burgundy piena, la più piatta.
>
> Legenda dentro l'area di plot, in alto a sinistra, dove non ci sono curve. All'estrema destra, una parentesi tratteggiata fra la curva teorica e quella reale, etichettata *il risparmio della cache*.
>
> **Elemento focale**: la forbice che si apre fra la curva tratteggiata e quella burgundy — è tutto il valore della KV cache, e si legge senza numeri.

---

## Slide 42 — Il modello è stateless: il contesto è tutto

**Layout**: titolo in alto; blocco analogia in apertura; i due punti di testo a sinistra (~30%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Il modello è stateless: il contesto è tutto*
- Blocco analogia (apertura, in prosa): *Il protagonista di Memento: amnesia anterograda — ricorda la vita prima dell'incidente, ma ogni nuovo ricordo svanisce in minuti. Sopravvive scrivendo tutto su Polaroid e tatuaggi: ciò che gli serve sapere deve essere fisicamente davanti ai suoi occhi, ora. Un LLM funziona così: il training è la "vita prima" — enorme, ma congelata. Tutto il resto esiste solo se è nel contesto, in questo istante.*
- Punti:
  1. **Nessuna memoria interna**: *a ogni chiamata il modello rilegge tutto da capo. L'unica sua memoria è il contesto che gli passi — la KV cache è un risparmio di calcolo, non un ricordo.*
  2. **E il contesto si accumula**: *turni di conversazione, dichiarazioni dei tool, tool call, risultati: ogni giro dei tre loop appende qualcosa. Può crescere moltissimo.*
- Nota in basso: *E abbiamo visto che il contesto costa — e vedremo tra poco che, oltre a costare, a un certo punto inizia a far male.*

**Visual**: la finestra di contesto fotografata a istanti successivi — una pila che cresce di giro in giro: system prompt e tool dichiarati, domanda, tool call, risultato, risposta, nuovo turno… — con l'altezza che aumenta vistosamente.

**Prompt per schema SVG**:
> Sequenza di 4 "fotografie" della finestra di contesto, affiancate da sinistra a destra, a istanti successivi della stessa sessione. Ogni fotografia è una pila verticale di strati etichettati; la pila cresce vistosamente da una fotografia all'altra (l'ultima è molto più alta della prima).
>
> **Foto 1 — `giro 0`**: strati `system prompt` e `tool dichiarati`, poi `domanda dell'utente`.
> **Foto 2 — `dopo la 1ª tool call`**: stessi strati, più `tool call: cerca()` e `risultato (lungo)` — lo strato risultato è visibilmente spesso.
> **Foto 3 — `fine del 1° turno`**: si aggiungono `tool call: leggi()`, `risultato`, `risposta del modello`.
> **Foto 4 — `3° turno di conversazione`**: la pila è alta, con molti strati compressi e in cima `nuova domanda dell'utente`; etichetta a lato: `…e ogni giro appende ancora`.
>
> **Sotto la sequenza**: una freccia orizzontale del tempo con etichetta `ogni chiamata rilegge TUTTA la pila da capo`.
>
> **Elementi focali**: la crescita dell'altezza tra la foto 1 e la foto 4 (il contesto si accumula) e la freccia "rilegge tutta la pila da capo" (la statelessness). Gli strati stabili in fondo (`system prompt`, `tool dichiarati`) devono restare riconoscibili e identici in tutte le foto.

## Slide 43 — Il modello è figlio dei suoi training set

**Layout**: titolo in alto; i tre punti di testo al centro; box di riflessione in basso (~30% della slide), visivamente distinto.

**Testo**:
- Titolo: *Il modello è figlio dei suoi training set*
- Punti:
  1. **Tutto viene dai dati**: *ciò che il modello sa, come parla, cosa considera ovvio — è la conseguenza di ciò che ha letto, con i bias di chi quei testi li ha scritti.*
  2. **Il cut-off**: *il mondo del modello si ferma alla data di raccolta dei dati: di ciò che accade dopo, nei pesi non c'è nulla.*
  3. **Anche il carattere**: *cosa risponde volentieri, come si comporta — viene anch'esso da un training set: le preferenze umane, stimate dal reward model. Chi fornisce il feedback plasma l'AI: implicazioni etiche, geopolitiche, di business.*
- Frase in evidenza: *Il modello che usi non è "l'AI": è una particolare AI, addestrata con particolari valori da particolari persone.*
- Box di riflessione: *La conoscenza sui modelli fa parte dei training set: un'AI ha letto i paper che descrivono il suo stesso funzionamento interno. L'uomo non sa progettare un cervello — un'AI ha conoscenza di dettaglio del proprio.*

**Visual**: nessuno. È una slide di riflessione: i tre punti e il box finale in evidenza sono essi stessi la struttura visiva; un diagramma diluirebbe il peso della chiusura.

## Slide 44 — Context rot

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); grafico a destra (~55%); nota-cliffhanger in basso.

**Testo**:
- Titolo: *Context rot*
- Punti:
  1. **Il fatto**: *con il contesto lungo, la qualità degrada: il modello trova peggio ciò che gli serve, anche se c'è.*
  2. **Perché**: *il budget di attenzione (la softmax della Slide 26) si diluisce su migliaia di token: tutto ascolta un po', niente abbastanza.*
  3. **La conseguenza**: *il contesto è una risorsa scarsa da governare, non un cassetto infinito.*
- Regole pratiche (evidenziate):
  1. *Nuovo compito, nuova chat: "continuare" una conversazione lunga per comodità peggiora, non migliora.*
  2. *Non riempire: seleziona ciò che entra.*
- Nota in basso (cliffhanger): *Governarlo — decidere cosa entra, cosa esce, cosa si riassume — non lo fa il modello. Serve qualcuno fuori: l'harness.*

**Visual**: **asset esterno** — il grafico già disponibile sul degrado delle performance al crescere della lunghezza del contesto (lo stesso citato nel draft dell'incontro 27, "Context Management"). Da inserire come immagine; eventuale rifacimento in stile deck da valutare a valle.

**Prompt per schema SVG**: — (asset esterno; se si deciderà di rifarlo: curva qualità vs lunghezza del contesto con salita, plateau e declino evidente, e il punto di piega come elemento focale, marcato *prima del limite tecnico della finestra*).

## Slide 45 — I tool accelerano il context rot

> Ripresa dal deck MBA (`gsom-april-2026`, `slide27-context-rot.html`). Sta subito dopo la 44 perché è lo stesso fenomeno con l'acceleratore: la 44 dice che il contesto degrada, la 45 dice che i tool lo riempiono molto più in fretta.

**Layout**: titolo in alto; i tre consigli pratici a sinistra (~40%); il grafico a due pannelli a destra (~57%); nota in basso.

**Testo**:
- Titolo: *I tool accelerano il context rot*
- Punti:
  1. **Esporre solo i tool necessari** — *ogni definizione paga un costo fisso in contesto, anche se quel tool non viene mai chiamato.*
  2. **Dimensionare i tool result** — *un tool che restituisce 50k token grezzi non è un tool ben progettato: è un carico.*
  3. **Meglio tool specifici che generici** — *un tool che fa una cosa sola viene anche scelto con più precisione.*
- Nota in basso: *I tool sono la risposta al limite più evidente del modello da solo: non sa quello che non sa, e non può agire nel mondo. Ma ogni tool call deposita nel contesto il suo risultato — e lì resta per tutta la sessione.*

**Visual**: `slide36b-tool-context-rot.svg` — due grafici a confronto.

**Prompt per schema SVG**:
> Due pannelli affiancati, **stessa scala su entrambi gli assi**, divisi da un filo verticale. Asse X: *turni della conversazione*; asse Y (una sola etichetta, a sinistra): *token nel contesto*.
>
> **Pannello sinistro — «CONVERSAZIONE PURA»**, sotto-intestazione *cresce solo di quello che vi dite*: una spezzata teal che sale **lineare e piano**. Piede: *crescita lineare, e lenta*.
>
> **Pannello destro — «CON I TOOL»**, sotto-intestazione *ogni risultato resta nel contesto*: una spezzata burgundy **a scalini**, che a ogni tool call fa un salto e riparte più in alto, arrivando molto più su. Piede: *a scalini, e molto più ripida*.
>
> **Elemento focale**: il confronto fra le due pendenze a parità di scala. Il grafico non deve avere numeri sull'asse Y: il punto è la forma, non la quantità.

> **Nota di adattamento**: il grafico di aprile è stato **rifatto**, non copiato. Quello importava Poppins da Google Fonts (qui il font è già in locale) e usava grigi generici fuori palette. La chiusa di aprile rimandava ai sub-agent: qui è tolta, perché i sub-agent sono materia dell'incontro 27.

## Slide 46 — Multimodality

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Multimodality*
- Punti:
  1. **Stessa macchina, ingressi diversi**: *un'immagine viene spezzata in tessere (patch); ogni tessera diventa un embedding, come un token.*
  2. **Lo stesso spazio delle idee**: *la foto di un gatto e la parola "gatto" finiscono vicine: il significato è la posizione, non il mezzo.*
  3. **E oltre**: *vale anche per audio e video.*
- Nota in basso: *Per questo lo stesso modello può leggere un contratto e guardarne la scansione.*

**Visual**: due percorsi che convergono nello stesso spazio delle idee: la parola "gatto" via tokenizer, la foto di un gatto via patch.

**Prompt per schema SVG**:
> Diagramma a due percorsi paralleli che convergono, da sinistra a destra.
>
> **Percorso superiore — il testo**: la parola `gatto` in un riquadro → blocco `tokenizer` → una colonnina-embedding.
>
> **Percorso inferiore — l'immagine**: una foto stilizzata di un gatto (sagoma semplice in un riquadro) → la stessa immagine suddivisa da una griglia 3×3 con etichetta `patch` → una fila di colonnine-embedding (una per patch).
>
> **A destra, la convergenza**: entrambi i percorsi entrano nello stesso piano dello spazio delle idee (stesso ambiente visivo delle slide precedenti): il punto `"gatto" (parola)` e il punto `gatto (immagine)` sono vicinissimi, dentro la stessa piccola nuvola; poco distante, per contrasto, un punto `Parigi`.
>
> **Elemento focale**: la vicinanza dei due punti nel piano — due mezzi diversi, stessa posizione nello spazio del significato. La griglia di patch è il secondo elemento didattico (l'immagine "tokenizzata").

## Slide 47 — Reasoning

> **La figura è stata rifatta**: al posto del confronto astratto fra modello standard e modello di reasoning, ora c'è **un esempio di conversazione con e senza**.
> Due colonne sulla stessa domanda — *«Un prodotto costa 80€. Applico −25%, poi +25%. Quanto costa?»*. A sinistra risponde subito **80€**, e sbaglia; a destra genera prima il blocco `[thinking]` (−25% → 60, +25% → 75, il secondo % si applica a 60) e poi risponde **75€**.
> L'esempio è scelto perché **la risposta intuitiva è anche quella sbagliata**: si vede *a che cosa serve* il ragionamento, non solo che c'è.
> Il blocco `[thinking]` è tratteggiato e grigio, con una graffa burgundy a lato — *token che paghi e non vedi*. Riusa l'idioma dei payload della Sezione 2 (riquadri con tag di ruolo, burgundy per ciò che il modello genera adesso), così le due sezioni si parlano.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Reasoning*
- Punti:
  1. **Pensare è generare**: *prima di rispondere, il modello genera token di ragionamento: restano nel contesto, ma non sono la risposta.*
  2. **Da dove viene**: *è ancora RL: vengono premiate le traiettorie di pensiero che arrivano alla risposta giusta (Slide 38).*
  3. **Il prezzo**: *più qualità = più calcolo alla domanda — i token di pensiero si pagano come gli altri.*
- Nota in basso: *È sempre il 1° loop: semplicemente, lo STOP arriva molto più tardi.*

**Visual**: due corsie a confronto sulla stessa domanda: risposta immediata (e sbagliata) del modello standard vs blocco di token di ragionamento e risposta corretta del modello reasoning.

**Prompt per schema SVG**:
> Diagramma a due corsie orizzontali, stessa domanda in ingresso a entrambe (riquadro a sinistra: `domanda: un problemino logico`).
>
> **Corsia superiore — `modello standard`**: freccia diretta da `domanda` a `risposta` (etichetta `immediata`), con esito `✗`.
>
> **Corsia inferiore — `modello di reasoning`**: da `domanda` parte un lungo blocco tratteggiato etichettato `token di ragionamento: prova, verifica, correggi…` (visivamente molto più lungo della risposta), e solo dopo arriva `risposta`, con esito `✓`. Sotto il blocco tratteggiato, un'etichetta: `occupano contesto e si pagano — ma non sono la risposta`.
>
> **Elementi focali**: il blocco di ragionamento interposto (la novità: il tempo/calcolo speso prima di rispondere) e il contrasto `✗` / `✓` tra le due corsie.

## Slide 48 — I costi: training, inferenza, distillazione

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *I costi: training, inferenza, distillazione*
- Punti:
  1. **Training**: *investimento una tantum, enorme: mesi di cluster di GPU — ordine delle decine di milioni.*
  2. **Un pretraining, molti RL**: *dallo stesso foundational model si addestrano poi più varianti via RL — conversazionale, coding, agentica: il grosso dell'investimento si paga una volta sola.*
  3. **Inferenza**: *centesimi per chiamata, moltiplicati per miliardi di chiamate: è qui che si gioca il margine.*
  4. **Distillazione**: *il ponte: il modello grande e costoso genera gli esempi su cui si addestra un modello piccolo ed economico — qualità simile, costo per token molto più basso.*
- Nota in basso: *Tutto è moltiplicazione di matrici (Slide 16): per questo l'economia dei modelli è, in fondo, economia di GPU.*

**Visual**: le due economie e il ponte: la fabbrica del training (una tantum, con le varianti RL che gemmano dal foundational model), il servizio dell'inferenza (per token), e la distillazione dal modello grande al piccolo.

**Prompt per schema SVG**:
> Diagramma orizzontale in tre zone.
>
> **Zona 1 — `training (una tantum)`**: un cluster di GPU stilizzato (griglia di schedine) con etichetta `mesi di calcolo — decine di milioni` che produce un riquadro `foundational model`. Dal foundational model gemmano, con frecce corte, 3 varianti più piccole etichettate `RL chat`, `RL coding`, `RL agentico` (etichetta del gruppo: `un pretraining, molti RL`).
>
> **Zona 2 — `inferenza (per token, per sempre)`**: una delle varianti serve un flusso di molte piccole richieste in arrivo (frecce numerose), etichetta `centesimi a chiamata × miliardi di chiamate`.
>
> **Zona 3 — `distillazione (il ponte)`**: dal modello grande parte una freccia in evidenza etichettata `genera esempi sintetici` verso un riquadro `modello piccolo`, che serve lo stesso flusso di richieste con etichetta `stesso lavoro, costo per token molto più basso`.
>
> **Elementi focali**: il contrasto tra le due economie (l'investimento unico della zona 1 vs il flusso perpetuo della zona 2) e la freccia di distillazione — il meccanismo che le ricuce.

## Slide 49 — Il prezzo per token

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual-fattura a destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il prezzo per token*
- Punti:
  1. **Input e output hanno prezzi diversi**: *i token di output costano di più (~3–5×): vengono generati uno alla volta; quelli di input si processano in parallelo nel prefill (Slide 40).*
  2. **Il contesto si ripaga a ogni chiamata**: *il modello è stateless (Slide 42): tutta la pila rientra — e si ripaga — a ogni giro.*
  3. **La cache sconta ciò che non cambia**: *il prefisso stabile (system prompt, tool) costa una frazione se riusato: è la KV cache diventata listino.*
- Nota in basso: *Ordine di grandezza oggi: da centesimi a qualche dollaro per milione di token, a seconda del modello. Le cifre invecchiano in fretta: le regole no.*

**Visual**: la "fattura" di una singola chiamata: le voci del contesto e dell'output, ognuna con la sua quantità e il suo prezzo unitario.

**Prompt per schema SVG**:
> Una fattura stilizzata, intestata `una chiamata al modello`, con righe-voce. Ogni riga ha: descrizione, una barra orizzontale proporzionale alla quantità di token, e il prezzo unitario in simboli (`€`, `€€`, `€€€`).
>
> **Le voci, dall'alto:**
>   1. `input — system prompt + tool dichiarati` — barra media, prezzo `€` barrato con sconto evidente, etichetta `in cache: riusato, scontato`;
>   2. `input — storia della conversazione` — barra lunga, prezzo `€`;
>   3. `input — nuova domanda` — barra corta, prezzo `€`;
>   4. `output — token di ragionamento` — barra lunga, prezzo `€€€`;
>   5. `output — risposta` — barra media, prezzo `€€€`.
>
> **In fondo**: la riga `totale`, e una postilla: `alla prossima chiamata, le voci 1–3 si ripagano (+ la risposta appena data)`.
>
> **Elementi focali**: il prezzo maggiorato delle voci di output (generati uno alla volta) e lo sconto-cache sulla voce 1 — le due regole economiche che discendono dalla meccanica vista. La postilla sul ripagarsi è il richiamo alla statelessness.

## Slide 50 — Il valore delle traiettorie

**Layout**: titolo in alto; mini-definizione sotto il titolo; due blocchi asimmetrici al centro (utente piccolo, provider grande); conclusione evidenziata; tre domande in chiusura.

**Testo**:
- Titolo: *Il valore delle traiettorie*
- Mini-definizione (richiamo della Slide 38): *Ogni conversazione è una traiettoria: prompt, risposte, correzioni, approvazioni e rifiuti — una traccia ricca di segnali su cosa funziona.*
- **Blocco 1 — Per l'utente** (piccolo): *un mezzo per risolvere un problema oggi; stateless, dimenticata domani.*
- **Blocco 2 — Per il provider** (grande): *miliardi di traiettorie reali = il carburante del prossimo training; pattern d'uso che nessun test artificiale produce.*
- Conclusione (evidenziata): *Il moat non è il modello — il modello diventa commodity. Il moat sono le traiettorie d'uso reale, che nessuno può replicare.*
- **Tre domande da utente informato**:
  1. *Nel contratto, i miei dati entrano nel prossimo training?*
  2. *Se costruisco un prodotto AI, dove accumulo il mio flywheel di traiettorie?*
  3. *Quando il modello sarà commodity, dove si sarà spostato il valore?*

**Visual**: nessuno. L'asimmetria dei due blocchi (utente piccolo, provider grande) è l'elemento visivo.

## Slide 51 — Closed, open weights, open source

**Layout**: titolo in alto; tre colonne contrastive che occupano il corpo della slide; nota in basso.

**Testo**:
- Titolo: *Closed, open weights, open source*
- Tre colonne:
  - **Closed (API)**:
    1. *paghi a token, zero infrastruttura*
    2. *qualità di frontiera*
    3. *i dati passano dal provider*
    4. *dipendenza dal fornitore*
  - **Open weights**:
    1. *scarichi i pesi: giri dove vuoi, anche on-premise*
    2. *dati in casa; personalizzabile: fine-tuning, distillazione*
    3. *ma dati e ricetta di training restano privati*
    4. *licenze a volte con vincoli; infrastruttura a tuo carico*
  - **Open source (vero)**:
    1. *pesi + dati + codice di training pubblici*
    2. *riproducibile e ispezionabile fino in fondo*
    3. *rari, e tipicamente lontani dalla frontiera*
- Nota in basso: *Quasi tutto ciò che il mercato chiama "open source" è in realtà open weights. La scelta si fa sul caso d'uso — sensibilità dei dati, scala, competenze — non per principio. E la frontiera si muove: guardiamola.*

**Visual**: nessuno. Le tre colonne contrastive sono la struttura visiva; il gradiente di apertura (da closed a open source) si legge nell'ordine delle colonne.

## Slide 52 — Quando closed, quando open

**Layout**: titolo in alto; tabella comparativa nella metà superiore; nota moat sotto la tabella; take-home in chiusura evidenziato.

**Testo**:
- Titolo: *Quando closed, quando open*
- Tabella a 3 colonne:

| Dimensione | Closed | Open |
|---|---|---|
| Qualità di frontiera | In testa oggi | A ~6–12 mesi, ma il gap si chiude |
| Costo a scala | Pay-per-token, lineare con l'uso | Infrastruttura fissa, marginale vicino a zero |
| Privacy / data residency | Dati al provider (salvo piani enterprise) | Totalmente in casa |
| Customization | Fine-tuning limitato, niente pesi | Fine-tuning completo, distillazione, LoRA |
| Effort di adozione | Zero infrastruttura | GPU, MLOps, competenze |
| Geopolitica / compliance | Dipendenza da vendor USA o Cina | Sovranità, compatibilità AI Act |

- Nota moat (in evidenza, aggancio alla Slide 50): *Con closed paghi il token E regali le traiettorie. Con open paghi l'infrastruttura, e le traiettorie restano tue.*
- Take-home (in chiusura): *Closed per sperimentare velocemente, open per scalare volumi, privacy, customization. La scelta è per use case, non ideologica.*

**Visual**: nessuno. La tabella è l'elemento visivo.

## Slide 53 — Fine-tuning: riprendere la discesa

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual a destra (~55%); nota in basso.

**Testo**:
- Titolo: *Fine-tuning: riprendere la discesa*
- Punti:
  1. **L'idea**: *riprendere l'addestramento sui propri dati — stesso metodo di sempre, gradient descent (Slide 36) — per specializzare dominio, tono, formato.*
  2. **Il costo**: *aggiornare tutti i pesi richiede GPU e tempo da training, non da inferenza.*
  3. **Il rischio**: *correggendo tutto, il modello può disimparare il resto (catastrophic forgetting).*
- Nota in basso: *Serve un'alternativa che corregga senza riscrivere. È la prossima slide.*

**Visual**: la valle dell'errore della Slide 36 ripresa: il modello già addestrato riparte dal fondo valle e scende in una valletta laterale più piccola etichettata "i tuoi dati".

**Prompt per schema SVG**:
> Riprende il diagramma della valle dell'errore (stesso ambiente visivo della slide sul gradient descent): la curva ha un fondo valle principale dove sta una pallina etichettata `modello pre-addestrato`.
>
> Da lì, una breve discesa secondaria porta a una valletta laterale, più piccola e leggermente più in basso, etichettata `specializzato sui tuoi dati`; i passetti di discesa sono pochi (etichetta: `pochi passi, dati tuoi`).
>
> Sul percorso, un cartello di avvertimento rivolto all'indietro: `attenzione: muovendo tutti i pesi si può risalire altrove` (il catastrophic forgetting).
>
> **Elemento focale**: la brevità della discesa secondaria rispetto alla discesa originaria — il fine-tuning riparte da un modello già addestrato, non da zero.

## Slide 54 — LoRA: la correzione a basso rango

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~40%); visual a destra (~55%); nota in basso.

**Testo**:
- Titolo: *LoRA: la correzione a basso rango*
- Punti:
  1. **Non toccare W**: *la matrice originale resta congelata; si impara solo una correzione ΔW da sommarle.*
  2. **Il vincolo (low-rank)**: *ΔW è costretta a essere il prodotto di due matrici sottili, A e B: poche direzioni nuove, non una riscrittura — la specializzazione è un piccolo insieme di spostamenti nello spazio delle idee.*
  3. **I numeri**: *r piccolo (8–64) contro dimensioni in migliaia: da d×d parametri a 2·d·r — meno dell'1%.*
  4. **In pratica**: *l'adattatore (A, B) è un file di pochi MB: si monta, si smonta, se ne tengono molti — uno per dominio.*
- Nota in basso: *È questo a rendere davvero interessanti gli open weights (Slide 51): il modello resta condiviso, la specializzazione diventa tua.*

**Visual**: la matrice W congelata e, in parallelo, il ramo LoRA con il collo di bottiglia a r dimensioni; accanto, la pila di adattatori intercambiabili.

**Prompt per schema SVG**:
> Diagramma del ramo LoRA accanto a una matrice congelata.
>
> **Ramo principale**: un vettore in ingresso entra in una grande matrice quadrata `W — congelata` (con un lucchetto), da cui esce verso un nodo `+`. Dimensioni annotate: `d × d` (es. `4096 × 4096 ≈ 17M parametri`).
>
> **Ramo parallelo (LoRA)**: lo stesso vettore in ingresso attraversa una matrice sottile e alta `A` (`d × r`), passa per un collo di bottiglia stretto etichettato `r direzioni nuove (es. r = 16)`, poi una matrice sottile e larga `B` (`r × d`), e arriva allo stesso nodo `+`. Dimensioni annotate: `2·d·r ≈ 131k parametri — meno dell'1%`. Solo questo ramo porta il segno "in addestramento".
>
> **Dal nodo `+`**: il vettore in uscita, etichetta `uscita corretta`.
>
> **A lato**: una pila di 3 coppie `A,B` intercambiabili etichettate `legale`, `medico`, `customer care`, con etichetta `un file piccolo per dominio: si monta e si smonta`.
>
> **Elementi focali**: la sproporzione visiva tra `W` (enorme, col lucchetto) e le strisce `A`/`B` (sottilissime), e il collo di bottiglia `r` — poche direzioni bastano a specializzare. I numeri di dimensione sono di natura token/codice.

## Slide 55 — La fotografia del mercato: il Pareto qualità/costo

> **Il placeholder è stato sostituito dall'immagine vera**: `assets/images/uploads/arena-pareto-2026-09-02.png`, screenshot di `arena.ai/leaderboard/text/pareto` con i dati al **2 settembre 2026** (7.999.020 voti, 400 modelli).
> Due accorgimenti da ripetere quando la si rifà: (1) il sito è in tema scuro — va catturato forzando `prefers-color-scheme: light`, altrimenti stona in un deck tutto chiaro; (2) va catturato con un **viewport largo e basso** (~2400×980), perché la card del grafico è responsive e con un viewport alto esce in rapporto ~1.7, che nello slot della slide si renderebbe a ~660px con le etichette illeggibili. Con 2400×980 esce ~2700×1348 e rende a **781px**.
> Il ritaglio deve includere **entrambi gli assi**: senza l'asse dei prezzi in basso il grafico non dice niente.
> Fonte e data stanno nella didascalia, col promemoria che la fotografia invecchia in settimane.

**Layout**: titolo in alto; il chart occupa quasi tutta la slide (~80%); didascalia in basso.

**Testo**:
- Titolo: *La fotografia del mercato*
- Didascalia: *Qualità (Arena score) contro prezzo: contano i modelli sulla frontiera — a parità di qualità il meno caro, a parità di prezzo il migliore. La fotografia invecchia in settimane: il punto è saper leggere il grafico, non memorizzarlo.*

**Visual**: **asset esterno** — il chart Pareto qualità/prezzo da `https://arena.ai/leaderboard/text/pareto` (screenshot/export da aggiornare a ridosso della lezione, proprio perché invecchia in fretta).

**Lettura in aula (appunti per il docente, non testo slide)**:
- evidenziare la frontiera di Pareto e il concetto di "dominato" (tutto ciò che sta sotto/destra della frontiera);
- indicare un paio di closed di punta e almeno un open weights competitivo (aggancio Slide 51);
- i punti in basso a destra della frontiera: è lì che lavora la distillazione (aggancio Slide 48).

## Slide 47 (numerazione precedente) — Chiusura: la formula riletta — **RIMOSSA**

**Layout**: titolo in alto; la formula grande al centro con la sintesi sotto il termine LLM; nota-cliffhanger in basso.

**Testo**:
- Titolo: *La formula, riletta*
- Formula centrale (tipografica, come alla Slide 3): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Sotto il termine `LLM`, la sintesi di giornata: *manipolatore di embeddings — stateless — addestrato in tre fasi a volere i tool*
- Nota in basso (cliffhanger): *Il modello sa volere. Non sa eseguire. Chi fa parsing, dispatch, sandbox, memoria? Prossimo incontro: dentro l'harness.*

**Visual**: nessuno. La formula tipografica con la sintesi sotto LLM è la struttura; il cliffhanger sta nel testo.
