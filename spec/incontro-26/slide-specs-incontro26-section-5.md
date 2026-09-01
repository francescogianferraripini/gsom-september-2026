# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 5 — Chiusura: il modello nel mondo**
**Obiettivo di apprendimento**: il partecipante rilegge il loop conversazionale alla luce del **context rot** (la pila della Slide 34 non solo costa: degrada il modello), conosce multimodality e reasoning, inquadra gli elementi economici (raccogliendo il seme GPU della Slide 12) e la scelta open vs closed, e riceve il cliffhanger verso l'harness (incontro 27).
**Messaggio chiave (takeaway)**: Più contesto non è meglio: oltre una soglia il modello degrada. Da questo limite — e dal "chi esegue?" — nasce il bisogno dell'harness.
**Budget**: ~22–25 min, 12 slide. I contenuti "bonus" (multimodality, reasoning) NON sono sacrificabili.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec5.html` | Separatore — Sezione 5: Il modello nel mondo |
| `slides/slide36-context-rot.html` | Slide 36 — Context rot |
| `slides/slide37-multimodality.html` | Slide 37 — Multimodality |
| `slides/slide38-reasoning.html` | Slide 38 — Reasoning |
| `slides/slide39-costi-training-inferenza.html` | Slide 39 — I costi: training, inferenza, distillazione |
| `slides/slide40-prezzo-per-token.html` | Slide 40 — Il prezzo per token |
| `slides/slide41-valore-traiettorie.html` | Slide 41 — Il valore delle traiettorie |
| `slides/slide42-closed-openweights-opensource.html` | Slide 42 — Closed, open weights, open source |
| `slides/slide43-tradeoff-closed-open.html` | Slide 43 — Quando closed, quando open |
| `slides/slide44-fine-tuning.html` | Slide 44 — Fine-tuning: riprendere la discesa |
| `slides/slide45-lora.html` | Slide 45 — LoRA: la correzione a basso rango |
| `slides/slide46-pareto.html` | Slide 46 — La fotografia del mercato: il Pareto qualità/costo |
| `slides/slide47-chiusura.html` | Slide 47 — Chiusura: la formula riletta |

---

## Slide 36 — Context rot

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); grafico a destra (~55%); nota-cliffhanger in basso.

**Testo**:
- Titolo: *Context rot*
- Punti:
  1. **Il fatto**: *con il contesto lungo, la qualità degrada: il modello trova peggio ciò che gli serve, anche se c'è.*
  2. **Perché**: *il budget di attenzione (la softmax della Slide 19) si diluisce su migliaia di token: tutto ascolta un po', niente abbastanza.*
  3. **La conseguenza**: *il contesto è una risorsa scarsa da governare, non un cassetto infinito.*
- Regole pratiche (evidenziate):
  1. *Nuovo compito, nuova chat: "continuare" una conversazione lunga per comodità peggiora, non migliora.*
  2. *Non riempire: seleziona ciò che entra.*
- Nota in basso (cliffhanger): *Governarlo — decidere cosa entra, cosa esce, cosa si riassume — non lo fa il modello. Serve qualcuno fuori: l'harness.*

**Visual**: **asset esterno** — il grafico già disponibile sul degrado delle performance al crescere della lunghezza del contesto (lo stesso citato nel draft dell'incontro 27, "Context Management"). Da inserire come immagine; eventuale rifacimento in stile deck da valutare a valle.

**Prompt per schema SVG**: — (asset esterno; se si deciderà di rifarlo: curva qualità vs lunghezza del contesto con salita, plateau e declino evidente, e il punto di piega come elemento focale, marcato *prima del limite tecnico della finestra*).

## Slide 37 — Multimodality

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

## Slide 38 — Reasoning

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Reasoning*
- Punti:
  1. **Pensare è generare**: *prima di rispondere, il modello genera token di ragionamento: restano nel contesto, ma non sono la risposta.*
  2. **Da dove viene**: *è ancora RL: vengono premiate le traiettorie di pensiero che arrivano alla risposta giusta (Slide 32).*
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

## Slide 39 — I costi: training, inferenza, distillazione

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *I costi: training, inferenza, distillazione*
- Punti:
  1. **Training**: *investimento una tantum, enorme: mesi di cluster di GPU — ordine delle decine di milioni.*
  2. **Un pretraining, molti RL**: *dallo stesso foundational model si addestrano poi più varianti via RL — conversazionale, coding, agentica: il grosso dell'investimento si paga una volta sola.*
  3. **Inferenza**: *centesimi per chiamata, moltiplicati per miliardi di chiamate: è qui che si gioca il margine.*
  4. **Distillazione**: *il ponte: il modello grande e costoso genera gli esempi su cui si addestra un modello piccolo ed economico — qualità simile, costo per token molto più basso.*
- Nota in basso: *Tutto è moltiplicazione di matrici (Slide 12): per questo l'economia dei modelli è, in fondo, economia di GPU.*

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

## Slide 40 — Il prezzo per token

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual-fattura a destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il prezzo per token*
- Punti:
  1. **Input e output hanno prezzi diversi**: *i token di output costano di più (~3–5×): vengono generati uno alla volta; quelli di input si processano in parallelo nel prefill (Slide 23).*
  2. **Il contesto si ripaga a ogni chiamata**: *il modello è stateless (Slide 34): tutta la pila rientra — e si ripaga — a ogni giro.*
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

## Slide 41 — Il valore delle traiettorie

**Layout**: titolo in alto; mini-definizione sotto il titolo; due blocchi asimmetrici al centro (utente piccolo, provider grande); conclusione evidenziata; tre domande in chiusura.

**Testo**:
- Titolo: *Il valore delle traiettorie*
- Mini-definizione (richiamo della Slide 32): *Ogni conversazione è una traiettoria: prompt, risposte, correzioni, approvazioni e rifiuti — una traccia ricca di segnali su cosa funziona.*
- **Blocco 1 — Per l'utente** (piccolo): *un mezzo per risolvere un problema oggi; stateless, dimenticata domani.*
- **Blocco 2 — Per il provider** (grande): *miliardi di traiettorie reali = il carburante del prossimo training; pattern d'uso che nessun test artificiale produce.*
- Conclusione (evidenziata): *Il moat non è il modello — il modello diventa commodity. Il moat sono le traiettorie d'uso reale, che nessuno può replicare.*
- **Tre domande da utente informato**:
  1. *Nel contratto, i miei dati entrano nel prossimo training?*
  2. *Se costruisco un prodotto AI, dove accumulo il mio flywheel di traiettorie?*
  3. *Quando il modello sarà commodity, dove si sarà spostato il valore?*

**Visual**: nessuno. L'asimmetria dei due blocchi (utente piccolo, provider grande) è l'elemento visivo.

## Slide 42 — Closed, open weights, open source

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

## Slide 43 — Quando closed, quando open

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

- Nota moat (in evidenza, aggancio alla Slide 41): *Con closed paghi il token E regali le traiettorie. Con open paghi l'infrastruttura, e le traiettorie restano tue.*
- Take-home (in chiusura): *Closed per sperimentare velocemente, open per scalare volumi, privacy, customization. La scelta è per use case, non ideologica.*

**Visual**: nessuno. La tabella è l'elemento visivo.

## Slide 44 — Fine-tuning: riprendere la discesa

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual a destra (~55%); nota in basso.

**Testo**:
- Titolo: *Fine-tuning: riprendere la discesa*
- Punti:
  1. **L'idea**: *riprendere l'addestramento sui propri dati — stesso metodo di sempre, gradient descent (Slide 30) — per specializzare dominio, tono, formato.*
  2. **Il costo**: *aggiornare tutti i pesi richiede GPU e tempo da training, non da inferenza.*
  3. **Il rischio**: *correggendo tutto, il modello può disimparare il resto (catastrophic forgetting).*
- Nota in basso: *Serve un'alternativa che corregga senza riscrivere. È la prossima slide.*

**Visual**: la valle dell'errore della Slide 30 ripresa: il modello già addestrato riparte dal fondo valle e scende in una valletta laterale più piccola etichettata "i tuoi dati".

**Prompt per schema SVG**:
> Riprende il diagramma della valle dell'errore (stesso ambiente visivo della slide sul gradient descent): la curva ha un fondo valle principale dove sta una pallina etichettata `modello pre-addestrato`.
>
> Da lì, una breve discesa secondaria porta a una valletta laterale, più piccola e leggermente più in basso, etichettata `specializzato sui tuoi dati`; i passetti di discesa sono pochi (etichetta: `pochi passi, dati tuoi`).
>
> Sul percorso, un cartello di avvertimento rivolto all'indietro: `attenzione: muovendo tutti i pesi si può risalire altrove` (il catastrophic forgetting).
>
> **Elemento focale**: la brevità della discesa secondaria rispetto alla discesa originaria — il fine-tuning riparte da un modello già addestrato, non da zero.

## Slide 45 — LoRA: la correzione a basso rango

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~40%); visual a destra (~55%); nota in basso.

**Testo**:
- Titolo: *LoRA: la correzione a basso rango*
- Punti:
  1. **Non toccare W**: *la matrice originale resta congelata; si impara solo una correzione ΔW da sommarle.*
  2. **Il vincolo (low-rank)**: *ΔW è costretta a essere il prodotto di due matrici sottili, A e B: poche direzioni nuove, non una riscrittura — la specializzazione è un piccolo insieme di spostamenti nello spazio delle idee.*
  3. **I numeri**: *r piccolo (8–64) contro dimensioni in migliaia: da d×d parametri a 2·d·r — meno dell'1%.*
  4. **In pratica**: *l'adattatore (A, B) è un file di pochi MB: si monta, si smonta, se ne tengono molti — uno per dominio.*
- Nota in basso: *È questo a rendere davvero interessanti gli open weights (Slide 42): il modello resta condiviso, la specializzazione diventa tua.*

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

## Slide 46 — La fotografia del mercato: il Pareto qualità/costo

**Layout**: titolo in alto; il chart occupa quasi tutta la slide (~80%); didascalia in basso.

**Testo**:
- Titolo: *La fotografia del mercato*
- Didascalia: *Qualità (Arena score) contro prezzo: contano i modelli sulla frontiera — a parità di qualità il meno caro, a parità di prezzo il migliore. La fotografia invecchia in settimane: il punto è saper leggere il grafico, non memorizzarlo.*

**Visual**: **asset esterno** — il chart Pareto qualità/prezzo da `https://arena.ai/leaderboard/text/pareto` (screenshot/export da aggiornare a ridosso della lezione, proprio perché invecchia in fretta).

**Lettura in aula (appunti per il docente, non testo slide)**:
- evidenziare la frontiera di Pareto e il concetto di "dominato" (tutto ciò che sta sotto/destra della frontiera);
- indicare un paio di closed di punta e almeno un open weights competitivo (aggancio Slide 42);
- i punti in basso a destra della frontiera: è lì che lavora la distillazione (aggancio Slide 39).

## Slide 47 — Chiusura: la formula riletta

**Layout**: titolo in alto; la formula grande al centro con la sintesi sotto il termine LLM; nota-cliffhanger in basso.

**Testo**:
- Titolo: *La formula, riletta*
- Formula centrale (tipografica, come alla Slide 3): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Sotto il termine `LLM`, la sintesi di giornata: *manipolatore di embeddings — stateless — addestrato in tre fasi a volere i tool*
- Nota in basso (cliffhanger): *Il modello sa volere. Non sa eseguire. Chi fa parsing, dispatch, sandbox, memoria? Prossimo incontro: dentro l'harness.*

**Visual**: nessuno. La formula tipografica con la sintesi sotto LLM è la struttura; il cliffhanger sta nel testo.
