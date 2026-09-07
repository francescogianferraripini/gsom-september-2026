# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 4 — Come viene addestrato**
**Obiettivo di apprendimento**: il partecipante distingue le tre fasi di addestramento — pretraining (cross-entropy, gradient descent), RLHF (dal completamento alla conversazione), RL agentico (tool calling, traiettorie, GRPO) — e capisce come nasce la "volontà" del modello di chiamare un tool.
**Messaggio chiave (takeaway)**: Tre fasi lo trasformano: da completatore di testo, a conversatore, a modello che *sa volere* i tool — ed è qui che nasce il 3° loop.
**Budget**: ~24 min, 8 slide.
**Riusi narrativi**: il seme di Shannon della Slide 4 (cross-entropy = fronte 1 della compressione).
**Nota di perimetro**: le vecchie Slide 42 e 43 (*Il modello è stateless* e *Il modello è figlio dei suoi training set*) sono passate alla **Sezione 5**. E il golfista non si disegna più qui: la vignetta con la mira è la **Slide 10**, in Sezione 2 — questa sezione spiega da dove quella mira arriva.
**Stato**: bozza

> **Le tre slide-anello.** Le Slide 35b, 36b e 38 sono **la stessa figura** — i tre loop annidati — con un anello acceso in più ogni volta: interno (generazione), esterno (conversazione), mezzo (task). Vanno lette come una progressione: *a ogni fase di addestramento corrisponde un loop che nasce*. La geometria è identica nelle tre varianti (`slide33-primo-loop.svg`, `slide33-secondo-loop.svg`, `slide33-terzo-loop.svg`): se si sposta un elemento, va spostato in tutte e tre, altrimenti l'effetto «si accende un pezzo alla volta» salta. Solo la terza porta il callout col cliffhanger sull'harness.


### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec4.html` | Separatore — Sezione 4: Come viene addestrato |
| `slides/slide28-tre-fasi.html` | Slide 33 — Le tre fasi |
| `slides/slide29-pretraining.html` | Slide 34 — Pretraining: indovinare il prossimo token |
| `slides/slide30-gradient-descent.html` | Slide 35 — Gradient descent: sbaglia, misura, correggi |
| `slides/slide33-primo-loop.html` | Slide 35b — Nasce il 1° loop |
| `slides/slide31-rlhf.html` | Slide 36 — RLHF: arriva la mira |
| `slides/slide33-secondo-loop.html` | Slide 36b — Nasce il 2° loop |
| `slides/slide32-rl-agentico.html` | Slide 37 — RL agentico: traiettorie |
| `slides/slide33-terzo-loop.html` | Slide 38 — Nasce il 3° loop |

---

## Slide 33 — Le tre fasi

**Layout**: titolo e sottotitolo in alto; visual-pipeline al centro (~65%); nota in basso.

**Testo**:
- Titolo: *Le tre fasi*
- Sottotitolo: *Ogni fase produce un modello diverso — e ognuna parte dal modello prodotto dalla precedente.*
- Le tre tappe (dentro il visual):
  1. **Pretraining** → *il completatore: un modello linguistico puro*
  2. **RLHF** → *il conversatore*
  3. **RL agentico** → *il modello che sa usare i tool*

**Visual**: pipeline orizzontale a tre stadi concatenati, ognuno che riceve in ingresso il modello prodotto dallo stadio precedente. Slide-mappa: verrà richiamata alle slide 34, 36 e 37 evidenziando lo stadio corrente.

**Prompt per schema SVG**:
> Pipeline orizzontale a tre stadi-freccia concatenati, da sinistra a destra. La concatenazione è il punto: da ogni stadio esce un modello, e quel modello è l'ingresso dello stadio successivo.
>
> **Stadio 1 — `Pretraining`**: dall'alto entra un flusso etichettato `testo di internet`; in uscita un riquadro-modello etichettato `il completatore (modello linguistico puro)`.
>
> **Stadio 2 — `RLHF`**: riceve in ingresso il riquadro-modello dello stadio 1 (freccia esplicita, etichetta `si parte da qui`); dall'alto entra `preferenze umane`; in uscita un riquadro-modello `il conversatore`.
>
> **Stadio 3 — `RL agentico`**: riceve in ingresso il riquadro-modello dello stadio 2; dall'alto entra `task e tool`; in uscita `il modello che sa usare i tool`.
>
> I tre riquadri-modello in uscita devono essere visivamente lo stesso oggetto che si arricchisce (stessa sagoma, dettaglio crescente): è la stessa rete, trasformata tre volte — mai ricostruita da zero.
>
> **Elementi focali**: le frecce di concatenazione modello→stadio successivo (ognuno si basa sul precedente) e la progressione delle tre etichette di uscita.

## Slide 34 — Pretraining: indovinare il prossimo token

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Pretraining: indovinare il prossimo token*
- Punti:
  1. **Il gioco**: *prendi un testo vero, nascondi il seguito, chiedi al modello il prossimo token.*
  2. **Il punteggio (cross-entropy)**: *quanta probabilità hai dato al token che era davvero lì? Tanta: punteggio buono. Poca: penalità.*
  3. **La correzione (gradient descent)**: *un metodo sistematico e iterativo che, a ogni errore, aggiusta di poco i valori di tutte le matrici che abbiamo visto — embedding, Q, K, V, rilevatori.*
  4. **Cosa si impara davvero**: *il giudizio è sul singolo token successivo, ma ciò che alla fine viene stimata è l'intera distribuzione.*
- Nota in basso: *Minimizzare la cross-entropy è letteralmente comprimere: è il fronte 1 della Slide 4. E tutto questo, ripetuto su 25–50 trilioni di token.*

**Visual**: il ciclo del gioco: testo vero troncato → distribuzione del modello → confronto col token vero → correzione che torna sulle matrici del modello. In basso, una striscia-infografica sulla scala dei dati.

**Visual secondario (striscia in basso, ~20% della slide)** — la scala del pretraining:

**Prompt per infografica SVG (striscia)**:
> Infografica a 5 righe orizzontali compatte. Ogni riga: etichetta a sinistra, barra orizzontale su scala logaritmica comune (da 10^8 a 10^14 parole/token), valore a destra.
>   1. `Un lettore, nell'intera vita` — barra cortissima — `~200 milioni di parole`
>   2. `Wikipedia, tutte le lingue` — `~10 miliardi di parole`
>   3. `Una grande biblioteca universitaria (20M volumi)` — `~1 trilione di parole`
>   4. `Training di un LLM di frontiera` — barra molto lunga, riga in risalto — `~25–50 trilioni di token`
>   5. `Tutto il testo digitale di qualità sul web` — barra massima, resa attenuata — `~50–100 trilioni di token`, etichetta `la frontiera dei dati disponibili`
> **Elementi focali**: la riga 4 (il punto della slide: la scala del training) e, come avvertimento, la riga 5 — ci stiamo avvicinando al limite del testo disponibile.

**Prompt per schema SVG**:
> Diagramma circolare del ciclo di pretraining, in quattro tappe.
>
> **Tappa 1 — il testo vero**: la frase `Il gatto è sul tavolo` con il seguito coperto dopo `Il gatto è` (i token `sul tavolo` oscurati, etichetta `nascosto`).
>
> **Tappa 2 — la previsione**: il blocco `modello` produce la distribuzione a barre sul prossimo token: `sul` (~30%), `un` (~22%), `morbido` (~15%), `nero` (~12%), `stanco` (~8%).
>
> **Tappa 3 — il confronto**: il token vero `sul` viene rivelato e messo accanto alla sua barra; un indicatore di punteggio etichettato `cross-entropy: quanta probabilità hai dato alla verità?` punta sulla barra di `sul`.
>
> **Tappa 4 — la correzione**: una freccia di ritorno etichettata `gradient descent: aggiusta di poco tutte le matrici` che dal confronto torna al blocco `modello`; il blocco modello mostra al suo interno, in miniatura, le matrici già viste (`embedding`, `Q K V`, `rilevatori`) con piccoli segni di aggiustamento su ciascuna.
>
> **Chiusura del ciclo**: dalla tappa 4 si riparte con un nuovo testo (etichetta `↻ trilioni di volte`).
>
> **Elementi focali**: il confronto tra la barra di `sul` e il token vero (il punteggio), e la freccia di correzione che tocca TUTTE le matrici in miniatura — l'apprendimento non aggiorna un archivio, aggiusta i pesi ovunque. Testi e token di natura token/codice.

## Slide 35 — Gradient descent: sbaglia, misura, correggi

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual a destra (~55%); nota in basso.

**Testo**:
- Titolo: *Gradient descent: sbaglia, misura, correggi*
- Punti:
  1. **L'errore è un paesaggio**: *immagina una valle: ogni punto è una configurazione dei pesi, l'altitudine è quanto il modello sbaglia.*
  2. **La discesa**: *il gradiente dice, per ogni singolo peso, in che direzione muoverlo per sbagliare un po' meno. Un passetto, e si ricomincia.*
  3. **Sistematico, non intelligente**: *nessuna comprensione: solo la pendenza locale, seguita miliardi di volte, su miliardi di pesi insieme.*
- Nota in basso: *Sarà lo stesso metodo per tutte e tre le fasi: cambia solo il punteggio da migliorare.*

**Visual**: la valle dell'errore con la pallina che scende a passetti, dalla configurazione iniziale al fondo valle.

**Prompt per schema SVG**:
> Diagramma a curva: il profilo di una valle (una curva morbida con un minimo evidente, e qualche ondulazione).
>
> **Assi**: orizzontale `configurazione dei pesi`, verticale `errore (loss)`.
>
> **Sulla curva**: una sequenza di 6–7 punti-pallina che scendono lungo il pendio a passi piccoli e decrescenti, collegati da freccette. Il primo punto, in alto, è etichettato `modello all'inizio: sbaglia molto`; una freccetta intermedia porta l'etichetta `un passetto nella direzione che riduce l'errore`; il punto finale, sul fondo, `modello addestrato`.
>
> **Elemento focale**: la sequenza dei passetti — la discesa è fatta di correzioni piccole e ripetute, non di salti. La forma della valle è di supporto.

## Slide 35b — Nasce il 1° loop

> Prima delle tre slide-anello. Chiude il pretraining: la capacità che lascia è una sola, e ripetuta *è* la generazione.

**Layout**: come le altre della sezione — titolo in alto; quattro punti a sinistra (~35%); figura al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Nasce il 1° loop*
- Punti:
  1. **Che cosa lascia il pretraining**: *una capacità sola: dato un contesto, qual è il prossimo token. Ripetuta, quella capacità è la generazione.*
  2. **Il loop interno**: *genera un token, lo accoda al contesto, rigenera — fino a `STOP`. È il loop della Slide 5.*
  3. **Nessuna meta, ancora**: *ottimizza il colpo, non il percorso: è il golfista senza mira della Slide 6.*
  4. **Con questo soltanto**: *il modello continua un testo. Non risponde a un turno, e non esegue niente.*
- Nota in basso: *Dei tre anelli, il pretraining ne accende uno solo — il più interno. Gli altri due arrivano dalle due fasi che seguono.*

**Visual**: `slide33-primo-loop.svg` — i tre anelli annidati con acceso il **nucleo**: cerchio burgundy su tinta, etichetta `1° LOOP` burgundy, frecce interne burgundy. Corona di mezzo e anello esterno restano neutri, con le loro etichette in grigio su fondo bianco.

**Prompt per schema SVG**: identico a quello della Slide 38, cambia solo quale anello è acceso e non c'è il callout.

## Slide 36 — RLHF: arriva la mira

> **La figura è stata rifatta.** Prima affiancava la vignetta del golfista con la mira al meccanismo; ora il golfista non c'è più — quella scena è la **Slide 10** — e il meccanismo occupa tutta la larghezza.
> Il motivo è di leggibilità: i riquadri delle due risposte erano segnaposto a 15px dentro un SVG largo 1550, che in slide rendevano a **~6.8px**, sotto il minimo del deck. A tutta larghezza il testo delle risposte sta a **12.5px**.
> **Contenuto della figura**: a sinistra la domanda *«Come posso aumentare le vendite?»* e le due risposte per esteso — A col bordo burgundy e il segno di scelta, B smorzata; a destra la catena *preferenze → reward model → reward → modello*; sotto, il callout invariato.
> **Le due risposte sono le stesse della Slide 9**, di proposito: là sono il prima e il dopo dell'addestramento, qui la coppia che gli umani confrontano. Stesso esempio, due letture.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *RLHF: arriva la mira*
- Punti:
  1. **Il problema**: *il completatore sa solo proseguire il testo: non risponde, completa. A "Come posso aumentare le vendite?" reagisce con altre domande — come farebbe un testo del web — non con una risposta.*
  2. **La mira**: *gli umani confrontano coppie di risposte e dicono quale preferiscono.*
  3. **Il trucco (reward model)**: *quelle preferenze addestrano un secondo modello, che impara a stimare il giudizio umano: è lui a dare la reward, milioni di volte, al posto nostro.*
- Nota in basso: *Il modello non ottimizza verso il giudizio umano — ottimizza verso la stima che il reward model fa di quel giudizio. Il golfista ora mira alla buca: ma la bandierina l'ha piantata il reward model.*
- Nota storica (piccola): *Novembre 2022, ChatGPT: non un nuovo modello — GPT-3 esisteva dal 2020. Un nuovo modo di addestrarlo a conversare.*

**Visual**: il golfista della Slide 6 che evolve — compare la linea di mira verso la buca — affiancato dal meccanismo: preferenze umane → reward model → punteggio.

**Prompt per schema SVG**:
> Diagramma in due parti affiancate.
>
> **Parte sinistra — il golfista, evoluto**: la stessa scena della vignetta del golfista (figura che colpisce, catena di traiettorie ad arco), ma ora la buca con la bandierina è in primo piano e una linea di mira tratteggiata collega i colpi alla buca (etichetta: `ora c'è una mira`). Accanto alla bandierina, una piccola etichetta: `piantata dal reward model`.
>
> **Parte destra — il meccanismo**: una catena verticale a tre blocchi:
>   1. `umani`: confrontano due risposte affiancate `A` e `B` e marcano la preferita (`A ✓`);
>   2. freccia `le preferenze addestrano…` verso il blocco `reward model`;
>   3. dal `reward model` esce un punteggio (`reward`) che entra nel ciclo di addestramento del blocco `modello` (freccia etichettata `stesso metodo: gradient descent — cambia solo il punteggio`).
>
> **Elementi focali**: la linea di mira del golfista (la novità di fase: prima non c'era alcuna mira) e il fatto che il punteggio arrivi dal `reward model`, non direttamente dagli `umani` — gli umani sono due passi a monte.

## Slide 36b — Nasce il 2° loop

> Seconda delle tre slide-anello. Chiude l'RLHF: quello che aggiunge non è vocabolario, è la forma del turno.

**Layout**: come la 35b.

**Testo**:
- Titolo: *Nasce il 2° loop*
- Punti:
  1. **Che cosa aggiunge l'RLHF**: *non parole nuove: la forma della risposta. Il modello smette di continuare il testo e comincia a rispondere a un turno.*
  2. **Il loop esterno**: *l'utente scrive, il modello lavora, la risposta si accoda alla storia, e si ricomincia. È il loop della Slide 7.*
  3. **A ogni giro si rispedisce tutto**: *l'API non ricorda niente: la storia la rimette il chiamante, per intero, ogni volta (Slide 39).*
  4. **Manca l'anello di mezzo**: *il modello sa parlare. Non sa ancora agire: per quello serve la terza fase.*
- Nota in basso: *Il secondo anello, quello più esterno. In mezzo resta un vuoto: fra «il modello lavora» e «la risposta si accoda» non c'è ancora niente.*

**Visual**: `slide33-secondo-loop.svg` — acceso l'**anello esterno**: cerchio burgundy, i tre riquadri (`l'utente scrive`, `il modello lavora`, `la risposta si accoda alla storia`) su tinta con bordo burgundy, pill `2° LOOP — CONVERSAZIONE` burgundy piena. Nucleo e corona di mezzo neutri.

**Prompt per schema SVG**: identico a quello della Slide 38, cambia solo quale anello è acceso e non c'è il callout. **Il vuoto in mezzo è voluto**: è lo spazio che la Slide 38 riempirà.

## Slide 37 — RL agentico: traiettorie

> Terza fase. Regge sul confronto con la **Slide 36**: stesso meccanismo (un punteggio, un gradiente, le stesse matrici che si aggiornano), ma cambiano due cose — l'unità giudicata (una traiettoria intera, non una risposta) e **chi dà il punteggio** (un controllo deterministico, non un reward model).

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~30%, classe `pts tight`); visual al centro-destra (~67%). **Niente nota in basso**: la figura è densa e la riga in più la comprimeva — il contenuto della vecchia nota è finito nell'ultimo punto.

**Testo**:
- Titolo: *RL agentico: traiettorie*
- Punti:
  1. **Cambia l'unità di giudizio**: *non più la frase migliore, ma la traiettoria che completa il task: n chiamate a sistemi esterni, una dopo l'altra.*
  2. **Il punteggio non lo dà un umano**: *il task è verificabile: un controllo deterministico dice se è stato completato. Niente reward model — questa è la differenza con la slide prima.*
  3. **GRPO**: *lo stesso task viene provato più volte; i punteggi del gruppo si confrontano con la loro media, e quel vantaggio è ciò che aggiorna i pesi.*
  4. **Cosa emerge**: *il modello impara che chiamare un tool al momento giusto è ciò che fa vincere — nasce la "volontà" della tool call. La traiettoria, non la risposta, diventa l'unità di valore.*

**Visual**: lo stesso task verificabile provato tre volte; ogni tentativo è una traiettoria di chiamate a sistemi esterni e riceve 1 o 0; il GRPO confronta i tre punteggi con la loro media, e da quel vantaggio esce il gradiente che aggiorna le matrici del modello.

**Prompt per schema SVG**:
> **A sinistra**, il `TASK` — `trova il prezzo e aggiorna il foglio` — con sotto, staccata da una riga, l'etichetta **`VERIFICABILE`** e la domanda del controllo: *il foglio ha il prezzo giusto? sì / no — lo dice un controllo, non un umano*. Da qui un fan-out verso le tre corsie.
>
> **Al centro, tre corsie orizzontali**: `TENTATIVO 1`, `2`, `3` — lo **stesso** task, tre volte. Ogni corsia è una sequenza di nodi collegati: `pensiero` (bianco, Poppins) e le chiamate `cerca()`, `leggi()`, `scrivi()` (grigio, monospaziato). Il tentativo 2 è quello che riesce: nodi burgundy su tinta.
>
> **Esiti e punteggi in colonna**, allineati fra le tre corsie: il riquadro d'esito (`non completato` / `task completato` / `esito sbagliato`) e, accanto, il reward in monospaziato — `r = 0`, `r = 1`, `r = 0`. L'allineamento è il punto: i tre punteggi si devono confrontare a colpo d'occhio, perché è quello che fa il GRPO.
>
> **Sotto la corsia vincente**, la freccia di reward che risale ALL'INDIETRO toccando ogni passo, tool call comprese: *il premio non va alla risposta finale: risale la traiettoria e premia ogni passo, tool call comprese*.
>
> **A destra, il pannello `GRPO`**: *il punteggio è relativo al gruppo*; sotto, il conto vero — `media dei tentativi (1 + 0 + 0) / 3 = 0,33` e `vantaggio = r − media` con i tre valori `+0,67 −0,33 −0,33`. Sotto ancora, su fondo grigio: *niente reward model: il critico è la media del gruppo, e il punteggio lo dà il controllo*.
>
> **In basso a destra**, una freccia burgundy `gradiente` che entra nel blocco `modello` **nero**, con dentro le **tre matricine** `embedding` · `Q K V` · `rilevatori` — ricopiate dalla TAPPA 4 della Slide 34 e dal blocco modello della Slide 36, stesse etichette e stesso schema di celle gialle.
>
> **Elemento focale**: la freccia di reward che risale la corsia vincente. Il secondo sono i tre `r =` in colonna col pannello GRPO accanto: è lì che si vede che il punteggio è *relativo*.

> **Nota di revisione (7 set 2026)**: la versione precedente aveva le tre corsie e la freccia di reward, ma il GRPO era solo una graffa con la scritta «i tentativi si confrontano tra loro» — si diceva, non si vedeva. Ora il confronto è fatto coi numeri, il punteggio ha una fonte dichiarata (il controllo, non un reward model) e il giro si chiude sulle matrici, come nelle Slide 34 e 36: **le tre slide dicono lo stesso meccanismo e cambiano solo il punteggio** — cross-entropy, reward model, controllo deterministico su una traiettoria intera.
>
> **Vincolo di misura**: viewBox `1120×560`, layout `tv-30` e nessuna nota HTML. Così la figura è vincolata in **larghezza** e rende a 763,9px (scala 0,68); con il `tv-35` e la nota di prima rendeva a 662px e i testi scendevano a 9,6px. Se si riaggiunge testo attorno, la figura torna vincolata in altezza e rimpicciolisce.

## Slide 38 — Nasce il 3° loop

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota-cliffhanger in basso.

**Testo**:
- Titolo: *Nasce il 3° loop*
- Punti:
  1. **Com'è fatta davvero**: *una tool call è testo: il modello emette una richiesta strutturata — nome del tool, parametri — e si ferma.*
  2. **I tool vanno dichiarati**: *il modello può volere solo i tool che conosce: l'elenco, con nome e descrizione di ciascuno, gli viene dato in apertura di contesto.*
  3. **Il giro**: *qualcuno esegue, il risultato rientra nel contesto, il modello riparte: giro dopo giro, fino a task completato.*
  4. **Il loop che mancava**: *è il 3° loop — e si infila esattamente lì, tra la generazione e la conversazione.*
- Nota in basso (cliffhanger): *Il modello sa solo chiedere. Chi esegue davvero — chi fa parsing, dispatch, sandbox — è il tema del prossimo incontro: l'harness.*

**Visual**: il diagramma degli anelli della Slide 7 completato: la corona tratteggiata col `?` si riempie con il loop del task.

**Prompt per schema SVG**:
> Diagramma di loop annidati a tre anelli concentrici — è il completamento del diagramma a due anelli con corona vuota già usato in precedenza (Slide 7): stessi anelli esterno e interno, ma la corona di mezzo ora è piena.
>
> **Anello esterno**: `2° loop — conversazione` (passi: `l'utente scrive` → `il modello lavora` → `la risposta si accoda alla storia` → torna a `l'utente scrive`).
>
> **Corona di mezzo (la novità, prima era tratteggiata con `?`)**: `3° loop — task`, con i passi: `il modello emette una tool call` → `qualcuno la esegue` → `il risultato rientra nel contesto` → `ripeti fino a task completato`. Sul passo `qualcuno la esegue`, un'etichetta appesa in evidenza: `chi? → prossimo incontro`.
>
> **Anello interno**: `1° loop — generazione` (fino a `STOP`).
>
> **Elementi focali**: la corona di mezzo appena riempita (il diagramma "si completa" rispetto alla versione precedente) e l'etichetta `chi? → prossimo incontro` — il cliffhanger visivo della lezione.

