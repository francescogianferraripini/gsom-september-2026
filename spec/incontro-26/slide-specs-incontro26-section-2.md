# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 2 — L'LLM: cos'è e come genera**
**Obiettivo di apprendimento**: il partecipante capisce che un LLM è una distribuzione di probabilità sul prossimo token e che genera in modo autoregressivo — un token alla volta — rileggendo tutto il contesto (il 1° loop, fino al token di stop); e vede i tre loop, con la meccanica del 2° e del 3°.
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
| `slides/slide9-secondo-loop.html` | Slide 8 — Il 2° loop: la conversazione (comparazione col 1°) |
| `slides/slide9b-tool-call.html` | Slide 9 — Il 3° loop: la tool call |
| `slides/slide9c-secondo-addestramento.html` | Slide 10 — Perché serve un secondo addestramento |
| `slides/slide9d-golfista-mira.html` | Slide 11 — Il colpo non basta: serve la mira |

> **Nota di filo rosso (i tre loop, numerazione storica — non per annidamento):**
> 1° = generazione (fino a STOP), 2° = conversazione (turno dopo turno), 3° = task/agentico (N giri di tool call dentro un turno). Annidamento: conversazione ⊃ task ⊃ generazione — il 3° non si aggiunge in coda, si infila in mezzo.
>
> **Cambio rispetto alla versione precedente**: i tre loop si aprono ora **tutti e tre qui**, nella Sezione 2 — la Slide 9 mostra la meccanica della tool call e nomina il 3° loop. Prima il 3° era tenuto per la Sezione 4 (Slide 39, lato RL) con un cliffhanger sulla Slide 8; quel cliffhanger è stato rimosso.
>
> ⚠️ **Questione aperta**: la Sezione 2 anticipa ora due slide della Sezione 4.
> - La **Slide 39** («Nasce il 3° loop») copre gli stessi punti meccanici della 9 — *la tool call è testo*, *i tool vanno dichiarati*, *il giro*.
> - La **Slide 37** («RLHF: arriva la mira») usa la stessa vignetta della 10 e dice la stessa cosa — che la mira arriva con un addestramento successivo.
>
> In entrambi i casi quello che resta **solo** alla Sezione 4 è il *come*: le preferenze umane e il reward model (31), l'RL sulle traiettorie (32), e la chiusa sull'harness (33). È lì che vanno rifocalizzate. Decisione rimandata.

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
- Nota in basso (seme, fronte 1 della compressione): *Prevedere bene significa comprimere bene.*

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
- Didascalia (sotto il diagramma): *Il modello non pianifica una risposta. Produce un token alla volta. Ogni nuovo token viene appeso al contesto e il contesto completo viene rivalutato per produrre il successivo. Da questo punto di vista il modello è stateless e ragiona solo in termini di parola successiva.*

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
> Le gittate devono riflettere i **colpi tipici del golf**: il colpo 1 è il drive, nettamente il più lungo, poi 2, 3 e 4 progressivamente più corti fino a un chip. Anche l'altezza degli archi decresce insieme alla gittata (arco 1 il più alto, arco 4 il più basso e teso).
>
> **All'estrema destra**: la buca con la bandierina, resa volutamente in secondo piano (sbiadita/marginale), con etichetta *la buca? per ora, nessuna mira*. Nessuna linea collega i colpi alla buca.
>
> **Elementi focali**: la catena degli archi (ogni arco che nasce dal punto d'atterraggio del precedente) e, per contrasto, la buca ignorata. Il significato sta nella tensione tra i due: bravura nel singolo colpo, nessun obiettivo finale.

## Slide 8 (numerazione precedente) — Il 1° loop: la generazione — **RIMOSSA**

> Slide tagliata: lo pseudocodice del loop di generazione era ridondante col riquadro laterale della Slide 6, e la comparazione della Slide 8 dà al 1° loop tutto lo spazio che gli serve. Gli `id` e i numeri in footnote delle slide successive non sono stati rinumerati: resta un buco sul numero 08.

---

## Slide 8 — Il 2° loop: la conversazione

> **Slide di comparazione.** Il punto non è più solo "esiste un secondo loop": è che i due loop sono **lo stesso meccanismo a due scale**. A sinistra si aggiunge un token al contesto, a destra si aggiunge un turno alla storia — e in entrambi i casi si rilegge tutto da capo.

**Layout**: titolo in alto; un unico visual a piena larghezza diviso in due metà da un filo verticale (~70% della slide); didascalia sotto; nota-seme in basso.

**Testo**:
- Titolo: *Il 2° loop: la conversazione*
- Didascalia: *Stesso meccanismo, due scale. A sinistra il 1° loop: dentro un turno, ogni token generato viene appeso al contesto. A destra il 2° loop: ogni turno viene appeso alla storia — e la storia, **system prompt in testa**, viene rispedita per intero a ogni chiamata. Un chatbot è questi due loop annidati: i primi erano esattamente questo.*
- Nota in basso (passaggio alla 9): *Dentro un turno, però, non c'è per forza una sola generazione del modello. È la prossima slide.*

**Visual**: comparazione affiancata generazione / conversazione, in un solo SVG (`slide9-comparazione-loop.svg`).

**Prompt per schema SVG**:
> Un unico diagramma orizzontale diviso in due metà da un filo verticale sottile. Ogni metà ha la propria intestazione e la propria sotto-intestazione, che è il perno della comparazione.
>
> **Metà sinistra — «IL 1° LOOP — LA GENERAZIONE»**, sotto-intestazione *l'unità che si aggiunge è il token*.
> È la pila della Slide 6 **ricopiata**, stessa frase e stessi colori: otto righe, ognuna un contesto a un certo istante, composta da un rettangolo chiaro (il context) e un rettangolo accento (il token appena generato). Ultima riga con badge `STOP`. Graffa verticale a lato: *il contesto cresce di un token per volta*. Piede: *ogni riga è una passata completa del modello: stessi pesi, contesto più lungo*.
>
> **Metà destra — «IL 2° LOOP — LA CONVERSAZIONE»**, sotto-intestazione *l'unità che si aggiunge è il turno*.
> Tre riquadri impilati, etichettati `turno 1`, `turno 2`, `turno 3`, di altezza crescente: ognuno contiene **l'intero payload rispedito all'API a quel turno**, riga per riga, con i tag di ruolo `[system]` / `[user]` / `[assistant]` in stile "codice". Il **`[system]` sta in testa a ogni riquadro**, non solo al primo: è lui a rendere visibile che *tutto* viene rispedito, system prompt compreso. Le righe ereditate dai turni precedenti sono sbiadite; la riga `[assistant]` appena generata è un blocco pieno nel colore accento, esattamente come il token generato a sinistra. Graffa verticale a lato: *la storia cresce di un turno per volta*.
>
> **Elemento focale**: la rima visiva fra le due metà — a sinistra cresce di un token, a destra di un turno, ma la meccanica (appendi, rileggi tutto) è la stessa. La crescita in altezza dei tre riquadri di destra deve essere evidente a colpo d'occhio: è lei a dire che la storia viene rispedita per intero ogni volta.
>
> Riferimento di partenza: gli SVG `slide12-conversation-step{1,2,3}.svg` del deck `gsom-april-2026` (chat UI a sinistra / payload API a destra), qui ricondotti alla forma "pila che cresce" per rimare con la Slide 6.



## Slide 9 — Il 3° loop: la tool call

> Comparazione, come la Slide 8, e costruita per **citazione**: la metà sinistra è, identica, la metà destra della Slide 8. Chi guarda riconosce la figura di due minuti prima e vede solo che cosa cambia.

**Layout**: titolo in alto; un unico visual a piena larghezza diviso in due metà da un filo verticale (~70% della slide); didascalia sotto; nota in basso.

**Testo**:
- Titolo: *Il 3° loop: la tool call*
- Didascalia: *A sinistra la conversazione di prima: a ogni turno dell'utente, una sola risposta del modello. A destra la stessa identica meccanica — stesso payload, rispedito per intero — con una differenza: il **tool è dichiarato nel system prompt**, e il modello può chiederlo. Quando lo chiede si ferma; il risultato rientra nel contesto come una riga in più; il modello riparte. **Due generazioni dentro un solo turno**: è il 3° loop, e si infila fra gli altri due.*
- Nota in basso: *La riga `[tool]` non l'ha scritta il modello: lui ha solo chiesto, e si è fermato. A eseguire e ad appendere il risultato è stato qualcun altro.*

**Visual**: `slide9b-tool-call.svg`, generato da `presentation/svg-src/gen_sez2.py`.

**Prompt per schema SVG**:
> Stessa impaginazione della Slide 8: due metà, filo verticale al centro, ogni metà con intestazione e sotto-intestazione.
>
> **Metà sinistra — «SENZA TOOL»**, sotto-intestazione *un giro di generazione per turno*: è **la metà destra della Slide 8, invariata** — tre riquadri `turno 1/2/3`, ognuno col payload completo, `[system]` in testa, storia sbiadita e risposta appena generata come pill accesa.
>
> **Metà destra — «CON UNA TOOL CALL»**, sotto-intestazione *due giri dentro un solo turno*: due riquadri `giro 1` e `giro 2`, che stanno **dentro un unico turno dell'utente** (una graffa a lato lo dichiara). Il `[system]` porta ora, su una seconda riga indentata, la **dichiarazione del tool** — uno solo, per semplicità: `Tool: cerca_ordine(id_ordine) — stato di un ordine`.
>   - `giro 1`: system + dichiarazione, la domanda dell'utente, e la richiesta del modello come pill — `→ cerca_ordine("4471")`. Il modello si ferma qui.
>   - `giro 2`: tutto il precedente sbiadito, più la riga **`[tool]`** col risultato, e la risposta finale come pill.
>
> La riga `[tool]` va in un colore **diverso da quello del modello** (teal, con fondo tinta): non l'ha generata il modello, l'ha appesa qualcun altro. È il punto della slide, e deve leggersi dal colore prima che dal testo.
>
> **Sotto i due riquadri**, i tre passi del giro: *① il modello chiede un tool, e si ferma. ② qualcun altro esegue e appende il risultato al contesto. ③ il modello riparte — e il turno non è ancora finito.*
>
> **Elemento focale**: il fatto che a destra ci siano **due** riquadri dove a sinistra ce n'era uno per turno. Il resto della macchina è identico.


## Slide 10 — Perché serve un secondo addestramento

> Ripresa dal deck MBA (`gsom-april-2026`, `slide14-secondo-addestramento.html`). Introduce la mira con **un esempio concreto**, prima che la Slide 11 la generalizzi con la metafora del golfista: prima il fatto, poi la figura.

**Layout**: titolo in alto; visual a tutta larghezza al centro; blocco nero centrato in fondo. Nessuna didascalia.

**Testo**:
- Titolo: *Perché serve un secondo addestramento*
- Blocco nero centrato (classe `.nota.dark.center`, la stessa della Slide 1): *Da «cosa è probabile» a «cosa serve rispondere».*

**Visual**: `slide9c-secondo-addestramento.svg`, generato da `presentation/svg-src/gen_sez2.py`.

**Prompt per schema SVG**:
> **In cima, uno solo per tutti e due**: il prompt dell'utente in un riquadro chiaro, in monospaziato — `Come posso aumentare le vendite?` — con l'etichetta `LO STESSO PROMPT`. Da lì due frecce scendono, una a sinistra grigia e una a destra burgundy, verso le due colonne. Un filo verticale tratteggiato separa le colonne.
>
> **Colonna sinistra — «MODELLO BASE»**, sotto-intestazione *solo pretraining*: riquadro grigio, testo **monospaziato e sbiadito** — il modello continua la frase con altre domande (*«E quante persone lavorano nella tua azienda? Il settore è B2B o B2C?…»*). Sotto, in piccolo: *Continua la frase come farebbe un testo del web: altre domande, non una risposta.*
>
> **Colonna destra — «DOPO IL SECONDO ADDESTRAMENTO»**, sotto-intestazione *stesso modello, un addestramento in più*: riquadro bianco **col bordo burgundy**, testo in Poppins e a piena opacità — la risposta strutturata a tre leve. Sotto: *Riconosce una domanda e risponde: utile, strutturata, orientata all'azione.*
>
> **Elemento focale**: il contrasto **tipografico** prima ancora che di contenuto — monospaziato sbiadito contro testo pieno. Si vede che è la stessa macchina, con un obiettivo diverso.

> **Nota di riuso**: le due risposte sono **le stesse della Slide 37** (RLHF), dove tornano come la coppia che gli umani confrontano. Stesso esempio, due letture: qui è il prima e il dopo, là è il come. Se cambia una, va cambiata l'altra.

## Slide 11 — Il colpo non basta: serve la mira

> Chiude la Sezione 2 e fa da cerniera verso la Sezione 4. Riprende **la stessa vignetta della Slide 7**, con una cosa in più: la mira. È un richiamo visivo, quindi la figura deve leggersi come *la stessa* — stessa inquadratura, stessa scala a schermo, stessi archi.

**Layout**: titolo in alto; visual a tutta larghezza al centro; didascalia sotto. **Nessuna nota**: la Slide 7 non ce l'ha, e ogni riga in più rimpicciolisce la figura rompendo il richiamo (vedi *Nota sulla scala*).

**Testo**:
- Titolo: *Il colpo non basta: serve la mira*
- Didascalia: *Il pretraining insegna **il colpo**: prevedere il token successivo dato il contesto precedente, nient'altro. Ma un turno di conversazione, o un giro di tool call, ha una meta: serve un addestramento **dopo** il pretraining, che non ottimizzi più il prossimo token sul solo contesto precedente, ma **il percorso autoregressivo lungo l'intera traiettoria**.*

**Visual**: `slide9c-golfista-mira.svg` — la scena della Slide 7 con in più il gruppo `mira` e la buca in primo piano, presi pari pari dalla Slide 37.

**Prompt per schema SVG**:
> Identica alla Slide 7 — stesso viewBox `0 0 1300 500`, stesso terreno, stessi quattro archi decrescenti, stessi punti di atterraggio, stesso golfista — con due aggiunte, entrambe copiate dalla Slide 37:
>   - il gruppo **`mira`**: quattro linee tratteggiate burgundy che partono da ciascun punto di atterraggio e convergono tutte sulla bandierina;
>   - la **buca in primo piano** (non più sbiadita): asta nera, bandierina in tinta burgundy, il punto di mira marcato.
>
> Al posto dell'annotazione *«la buca? / per ora, nessuna mira»* della Slide 7, **nello stesso angolo**, si legge che cosa è cambiato: *«ora ogni colpo mira alla buca / e a essere ottimizzato è il percorso, non il singolo colpo»*.
>
> **Elemento focale**: il fascio di tratteggi che converge sulla bandierina — nella Slide 7 quello spazio era vuoto.

> **Nota sulla scala (verificata a schermo)**: perché il richiamo funzioni, la vignetta deve rendersi **della stessa dimensione** della Slide 7. Il viewBox è 2.6 di rapporto contro uno slot da ~3.0, quindi la figura è vincolata in **altezza**: ogni riga di testo sotto le ruba larghezza in proporzione 1:2.6. La Slide 7 ha una didascalia di 2 righe e rende la vignetta a **1026px**; con 4 righe di didascalia a 12.5pt scendeva a 860px (−16%, e si vedeva). La didascalia della 10 è quindi a **11.5pt**: quattro righe che occupano quanto due, e la vignetta torna a **1013px**. Se aggiungi testo qui, ricontrolla questa misura.

<!-- I blocchi slide successivi verranno aggiunti qui durante l'intervista (Fase 2). -->
