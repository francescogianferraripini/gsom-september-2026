# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 2 — L'LLM: cos'è e come genera**
**Obiettivo di apprendimento**: il partecipante capisce che un LLM è una distribuzione di probabilità sul prossimo token e che genera in modo autoregressivo — un token alla volta — rileggendo tutto il contesto (il 1° loop, fino al token di stop).
**Messaggio chiave (takeaway)**: Il modello non pianifica una risposta: produce un token alla volta, e ogni token appena generato rientra nel contesto per produrre il successivo.
**Budget**: ~20 min.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec2.html` | Separatore — Sezione 2: L'LLM: cos'è e come genera |
| `slides/slide5-modello-linguistico.html` | Slide 5 — Che cos'è un modello linguistico |
| `slides/slide6-generazione-autoregressiva.html` | Slide 6 — La generazione: un token alla volta |
| `slides/slide7-golfista.html` | Slide 7 — Il golfista |
| `slides/slide8-primo-loop.html` | Slide 8 — Il 1° loop: la generazione |
| `slides/slide9-secondo-loop.html` | Slide 9 — Il 2° loop: la conversazione |

> **Nota di filo rosso (i tre loop, numerazione storica — non per annidamento):**
> 1° = generazione (fino a STOP), 2° = conversazione (turno dopo turno), 3° = task/agentico (N giri di tool call dentro un turno). Il 3° *nasce* in questo incontro (sez. 4, RL agentico, lato modello) e viene aperto nell'incontro 27 (lato harness), col colpo di scena dell'annidamento: non si aggiunge in coda, si infila in mezzo — conversazione ⊃ task ⊃ generazione.

> **Nota di filo rosso (compressione, due fronti distinti — non confonderli):**
> 1. **Il modello come compressore di messaggi**: prevedere bene il prossimo token = codificare il testo con meno bit (Shannon, cross-entropy). Seminato in Slide 5, raccolto in sezione 4 (cross-entropy loss).
> 2. **La conoscenza compressa nei pesi**: i fatti del training set sono compressi con perdita dentro il modello. Raccolto in sezione 3 ("LLM come compressore lossy", knowledge nei pesi).

---

## Slide 5 — Che cos'è un modello linguistico

**Layout**: titolo in alto; definizione centrale subito sotto; visual al centro (~50% della slide); box narrativo "1951" a sinistra del visual; nota-seme in basso.

**Testo**:
- Titolo: *Che cos'è un modello linguistico*
- Definizione centrale: *Un modello linguistico assegna una probabilità al prossimo token, dato il contesto che lo precede.*
- Box narrativo (a lato): *1951 — Claude Shannon stima l'entropia dell'inglese con un gioco: mostrare un testo troncato a una persona e chiederle di indovinare la lettera successiva. Un LLM è la macchina che gioca a quel gioco — meglio di chiunque.*
- Nota in basso (seme, fronte 1 della compressione): *Prevedere bene significa comprimere bene: non è una metafora, è un teorema. Lo ritroveremo.*

**Visual**: due contesti diversi che entrano nello stesso modello e producono due distribuzioni dalla forma opposta — appuntita (bassa entropia) vs piatta (alta entropia).

**Prompt per schema SVG**:
> Diagramma orizzontale a 2 righe parallele, entrambe convergenti su un unico blocco centrale `LLM`.
>
> **A sinistra**, due rettangoli di contesto impilati:
>   1. `La capitale della Francia è …`
>   2. `Il gatto è …`
> Ogni rettangolo ha una freccia verso il blocco centrale `LLM`.
>
> **A destra del blocco**, due frecce in uscita, ognuna verso un mini grafico a barre (la distribuzione sul prossimo token):
>   1. per il primo contesto: barra dominante `Parigi` (~97%), barre residue minuscole `una` (~2%), `sede` (~1%) — etichetta sotto: *bassa entropia: il seguito è quasi obbligato*;
>   2. per il secondo contesto: barre confrontabili `sul` (~28%), `un` (~22%), `morbido` (~15%), `nero` (~12%), `…` (~23%) — etichetta sotto: *alta entropia: molti seguiti plausibili*.
>
> **Elementi focali**: il blocco centrale `LLM` e il contrasto di forma tra le due distribuzioni (una appuntita, una piatta) — è il contrasto a portare il messaggio: la distribuzione misura quanto è prevedibile il seguito. I testi dei contesti e i token delle barre sono di natura "token/codice".

## Slide 6 — La generazione: un token alla volta

**Layout**: titolo in alto, grande visual narrativo al centro (~70% della slide), didascalia sotto.

**Testo**:
- Titolo: *La generazione: un token alla volta*
- Didascalia (sotto il diagramma): *Il modello non pianifica una risposta. Produce un token alla volta. Ogni nuovo token viene appeso al contesto e il contesto completo viene rivalutato per produrre il successivo.*

**Visual**: sequenza narrativa che mostra il contesto che cresce token dopo token, con freccia laterale che chiarisce che ogni riga è una chiamata indipendente al modello. Ogni riga è divisa in due zone: il context (sfondo scuro) e il token appena generato (sfondo accento). Una legenda in alto spiega i due colori. L'esempio prosegue deliberatamente il contesto "Il gatto è…" della Slide 5.

**Prompt per schema SVG**:
> Visual narrativo verticale che mostra l'evoluzione del contesto token dopo token.
>
> **Legenda in alto**: due riquadri con etichetta — "context (input al modello)" e "token generato (output)" — che devono leggersi come due zone di natura opposta.
>
> **Colonna centrale** — una pila verticale di 7-8 righe, ognuna è un "contesto" a un certo istante. Ogni riga è composta da due rettangoli adiacenti: uno per il context, uno per il token appena generato.
>
> Sequenza delle righe (dall'alto verso il basso):
>   1. `Il`  →  2. `Il gatto`  →  3. `Il gatto è`  →  ...  →  8. `Il gatto è sul tavolo e dorme.` (ultimo token "." con simbolo di STOP).
>
> **A destra della pila** — diagramma del loop a 4 passi: ① contesto → ② LLM → ③ token → ④ freccia tratteggiata che torna a ① ("appeso al contesto"). Footer: "↻ si ripete fino al token di STOP".
>
> **A sinistra** — graffa verticale che abbraccia le righe: "il contesto cresce di un token per volta".
>
> Elementi focali (da mettere in risalto): l'ultimo token di ogni riga, il diagramma del loop a destra e il badge STOP. Il testo delle righe è di natura "token/codice".

---

## Slide 7 — Il golfista

**Layout**: titolo in alto, visual a tutta larghezza al centro (~70% della slide), didascalia sotto.

**Testo**:
- Titolo: *Il golfista*
- Didascalia: *Come un golfista bravissimo a colpire la pallina: ogni colpo parte da dove è atterrata l'ultima, informato dalla storia di tutti i colpi precedenti. Ma alla buca, per ora, non mira nessuno.*

**Visual**: vignetta orizzontale del golfista con la catena di colpi ad arco — ogni traiettoria parte dal punto di atterraggio della precedente — e la buca sulla destra, sbiadita, ignorata. **Nota di riuso**: in sezione 4 (RL) la stessa immagine verrà ripresa aggiungendo la mira alla buca; il diagramma deve quindi poter evolvere.

**Prompt per schema SVG**:
> Vignetta orizzontale su un campo da golf stilizzato (una linea di terreno).
>
> **A sinistra**: una figura stilizzata di golfista nell'atto di colpire.
>
> **Da sinistra verso destra**: una catena di 4 traiettorie ad arco. Ogni arco parte esattamente dal punto in cui è atterrata la pallina dell'arco precedente (i punti di atterraggio sono marcati con una pallina ed etichettati `colpo 1`, `colpo 2`, `colpo 3`, `colpo 4`). La catena comunica: ogni colpo è determinato da dove ti ha portato la storia dei colpi precedenti.
>
> **All'estrema destra**: la buca con la bandierina, resa volutamente in secondo piano (sbiadita/marginale), con etichetta *la buca? per ora, nessuna mira*. Nessuna linea collega i colpi alla buca.
>
> **Elementi focali**: la catena degli archi (ogni arco che nasce dal punto d'atterraggio del precedente) e, per contrasto, la buca ignorata. Il significato sta nella tensione tra i due: bravura nel singolo colpo, nessun obiettivo finale.

## Slide 8 — Il 1° loop: la generazione

**Layout**: titolo in alto, pseudocodice grande al centro, nota-seme in basso.

**Testo**:
- Titolo: *Il 1° loop: la generazione*
- Pseudocodice centrale: `finché non esce STOP: leggi il contesto → genera un token → appendilo al contesto`
- Nota in basso (seme): *Lo chiamiamo 1° loop perché ne arriveranno altri due.*

**Visual**: nessuno. Il loop circolare è già disegnato nel riquadro laterale della Slide 6; qui il punto è dargli il nome e la forma di pseudocodice — un altro diagramma sarebbe ridondante.

---

## Slide 9 — Il 2° loop: la conversazione

**Layout**: titolo in alto; pseudocodice annidato a sinistra (~40%); visual dei loop annidati a destra (~50%); nota-seme in basso.

**Testo**:
- Titolo: *Il 2° loop: la conversazione*
- Pseudocodice annidato: `finché la conversazione continua: l'utente scrive → [1° loop: genera token fino a STOP] → la risposta si accoda alla storia`
- Didascalia: *Un chatbot è due loop annidati: dentro ogni turno, il loop di generazione; attorno, la conversazione che accumula contesto. I primi chatbot erano esattamente questo.*
- Nota in basso (seme): *Il 3° loop — quello agentico — non si aggiungerà in coda: si infilerà in mezzo. Lo vedremo nascere oggi, e lo apriremo al prossimo incontro.*

**Visual**: due anelli annidati (conversazione fuori, generazione dentro), con uno spazio tratteggiato vuoto tra i due — il posto riservato al 3° loop.

**Prompt per schema SVG**:
> Diagramma di loop annidati, due anelli concentrici.
>
> **Anello esterno**: etichetta `2° loop — conversazione`, con i passi disposti lungo l'anello: `l'utente scrive` → `il modello risponde` → `la risposta si accoda alla storia` → (torna a) `l'utente scrive`.
>
> **Anello interno** (dentro il passo `il modello risponde`): etichetta `1° loop — generazione`, con i passi: `leggi il contesto` → `genera un token` → `appendi` → (ripeti) fino a badge `STOP`.
>
> **Tra i due anelli**: una corona circolare vuota, delimitata da tratteggio, con etichetta `?` — il posto riservato a un terzo loop che verrà inserito qui.
>
> **Elementi focali**: l'annidamento (l'anello interno deve leggersi chiaramente come contenuto nel passo "il modello risponde" dell'esterno) e la corona tratteggiata vuota col `?`, che è il cliffhanger del diagramma.

<!-- I blocchi slide successivi verranno aggiunti qui durante l'intervista (Fase 2). -->
