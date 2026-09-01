# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 4 — Come viene addestrato**
**Obiettivo di apprendimento**: il partecipante distingue le tre fasi di addestramento — pretraining (cross-entropy, gradient descent), RLHF (dal completamento alla conversazione), RL agentico (tool calling, traiettorie, GRPO) — e capisce come nasce la "volontà" del modello di chiamare un tool.
**Messaggio chiave (takeaway)**: Tre fasi lo trasformano: da completatore di testo, a conversatore, a modello che *sa volere* i tool — ed è qui che nasce il 3° loop.
**Budget**: ~25 min, 8 slide.
**Riusi narrativi**: il golfista della Slide 7 (l'RL aggiunge la mira alla buca); il seme di Shannon della Slide 5 (cross-entropy = fronte 1 della compressione).
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec4.html` | Separatore — Sezione 4: Come viene addestrato |
| `slides/slide27-tre-fasi.html` | Slide 27 — Le tre fasi |
| `slides/slide28-pretraining.html` | Slide 28 — Pretraining: indovinare il prossimo token |
| `slides/slide29-gradient-descent.html` | Slide 29 — Gradient descent: sbaglia, misura, correggi |
| `slides/slide30-rlhf.html` | Slide 30 — RLHF: arriva la mira |
| `slides/slide31-rl-agentico.html` | Slide 31 — RL agentico: traiettorie |
| `slides/slide32-terzo-loop.html` | Slide 32 — Nasce il 3° loop |
| `slides/slide33-stateless.html` | Slide 33 — Il modello è stateless: il contesto è tutto |
| `slides/slide34-figlio-dei-dati.html` | Slide 34 — Il modello è figlio dei suoi training set |

---

## Slide 27 — Le tre fasi

**Layout**: titolo e sottotitolo in alto; visual-pipeline al centro (~65%); nota in basso.

**Testo**:
- Titolo: *Le tre fasi*
- Sottotitolo: *Ogni fase produce un modello diverso — e ognuna parte dal modello prodotto dalla precedente.*
- Le tre tappe (dentro il visual):
  1. **Pretraining** → *il completatore: un modello linguistico puro*
  2. **RLHF** → *il conversatore*
  3. **RL agentico** → *il modello che sa usare i tool*

**Visual**: pipeline orizzontale a tre stadi concatenati, ognuno che riceve in ingresso il modello prodotto dallo stadio precedente. Slide-mappa: verrà richiamata alle slide 28, 30 e 31 evidenziando lo stadio corrente.

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

## Slide 28 — Pretraining: indovinare il prossimo token

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Pretraining: indovinare il prossimo token*
- Punti:
  1. **Il gioco**: *prendi un testo vero, nascondi il seguito, chiedi al modello il prossimo token.*
  2. **Il punteggio (cross-entropy)**: *quanta probabilità hai dato al token che era davvero lì? Tanta: punteggio buono. Poca: penalità.*
  3. **La correzione (gradient descent)**: *un metodo sistematico e iterativo che, a ogni errore, aggiusta di poco i valori di tutte le matrici che abbiamo visto — embedding, Q, K, V, rilevatori.*
  4. **Cosa si impara davvero**: *il giudizio è sul singolo token successivo, ma ciò che alla fine viene stimata è l'intera distribuzione.*
- Nota in basso: *Minimizzare la cross-entropy è letteralmente comprimere: è il fronte 1 della Slide 5. E tutto questo, ripetuto su trilioni di token.*

**Visual**: il ciclo del gioco: testo vero troncato → distribuzione del modello → confronto col token vero → correzione che torna sulle matrici del modello.

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

## Slide 29 — Gradient descent: sbaglia, misura, correggi

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
> **Sulla curva**: una sequenza di 6-7 punti-pallina che scendono lungo il pendio a passi piccoli e decrescenti, collegati da freccette. Il primo punto, in alto, è etichettato `modello all'inizio: sbaglia molto`; una freccetta intermedia porta l'etichetta `un passetto nella direzione che riduce l'errore`; il punto finale, sul fondo, `modello addestrato`.
>
> **Elemento focale**: la sequenza dei passetti — la discesa è fatta di correzioni piccole e ripetute, non di salti. La forma della valle è di supporto.

## Slide 30 — RLHF: arriva la mira

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *RLHF: arriva la mira*
- Punti:
  1. **Il problema**: *il completatore sa solo proseguire il testo: non risponde, completa.*
  2. **La mira**: *gli umani confrontano coppie di risposte e dicono quale preferiscono.*
  3. **Il trucco (reward model)**: *quelle preferenze addestrano un secondo modello, che impara a stimare il giudizio umano: è lui a dare la reward, milioni di volte, al posto nostro.*
- Nota in basso: *Il modello non ottimizza verso il giudizio umano — ottimizza verso la stima che il reward model fa di quel giudizio. Il golfista ora mira alla buca: ma la bandierina l'ha piantata il reward model.*

**Visual**: il golfista della Slide 7 che evolve — compare la linea di mira verso la buca — affiancato dal meccanismo: preferenze umane → reward model → punteggio.

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

## Slide 31 — RL agentico: traiettorie

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *RL agentico: traiettorie*
- Punti:
  1. **Cambia l'unità di giudizio**: *non più la frase migliore, ma la traiettoria che completa il task.*
  2. **Come si allena**: *il modello prova il task molte volte; le traiettorie che arrivano in fondo vengono premiate, le altre no (GRPO: si confrontano gruppi di tentativi).*
  3. **Cosa emerge**: *il modello impara che chiamare un tool al momento giusto è ciò che fa vincere — nasce la "volontà" della tool call.*
- Nota in basso: *La traiettoria — non la risposta — diventa l'unità di valore. Ce lo ritroveremo: è l'artefatto primario di un agente.*

**Visual**: gruppo di traiettorie dello stesso task a confronto: una arriva al completamento e viene premiata, le altre no; la reward scorre all'indietro lungo la traiettoria vincente, toccando anche le tool call intermedie.

**Prompt per schema SVG**:
> Diagramma a corsie orizzontali: 3 traiettorie dello stesso task, una sotto l'altra, tutte partono dallo stesso punto a sinistra (`task: trova il prezzo e aggiorna il foglio`).
>
> Ogni traiettoria è una sequenza di passi collegati: nodi `pensiero`, nodi `tool call` (es. `cerca()`, `leggi()`, `scrivi()`) e nodi `risultato`.
>
> **Corsia 1**: si interrompe a metà (etichetta `si perde: nessun premio`).
> **Corsia 2**: arriva in fondo a un traguardo `task completato ✓` — è la traiettoria premiata: una freccia di reward parte dal traguardo e scorre ALL'INDIETRO lungo tutta la corsia, toccando ogni passo, comprese le tool call intermedie (etichetta: `la reward premia ogni passo della traiettoria vincente`).
> **Corsia 3**: arriva a un esito sbagliato `✗` (etichetta `fallisce: nessun premio`).
>
> A lato del gruppo di corsie, una graffa con etichetta `GRPO: i tentativi si confrontano tra loro`.
>
> **Elemento focale**: la freccia di reward che scorre all'indietro sulla corsia vincente e "bagna" le tool call intermedie — è così che il modello impara a volere i tool. I nomi dei tool sono di natura token/codice.

## Slide 32 — Nasce il 3° loop

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota-cliffhanger in basso.

**Testo**:
- Titolo: *Nasce il 3° loop*
- Punti:
  1. **Com'è fatta davvero**: *una tool call è testo: il modello emette una richiesta strutturata — nome del tool, parametri — e si ferma.*
  2. **I tool vanno dichiarati**: *il modello può volere solo i tool che conosce: l'elenco, con nome e descrizione di ciascuno, gli viene dato in apertura di contesto.*
  3. **Il giro**: *qualcuno esegue, il risultato rientra nel contesto, il modello riparte: giro dopo giro, fino a task completato.*
  4. **Il loop che mancava**: *è il 3° loop — e si infila esattamente lì, tra la generazione e la conversazione.*
- Nota in basso (cliffhanger): *Il modello sa solo chiedere. Chi esegue davvero — chi fa parsing, dispatch, sandbox — è il tema del prossimo incontro: l'harness.*

**Visual**: il diagramma degli anelli della Slide 9 completato: la corona tratteggiata col `?` si riempie con il loop del task.

**Prompt per schema SVG**:
> Diagramma di loop annidati a tre anelli concentrici — è il completamento del diagramma a due anelli con corona vuota già usato in precedenza (Slide 9): stessi anelli esterno e interno, ma la corona di mezzo ora è piena.
>
> **Anello esterno**: `2° loop — conversazione` (passi: `l'utente scrive` → `il modello lavora` → `la risposta si accoda alla storia` → torna a `l'utente scrive`).
>
> **Corona di mezzo (la novità, prima era tratteggiata con `?`)**: `3° loop — task`, con i passi: `il modello emette una tool call` → `qualcuno la esegue` → `il risultato rientra nel contesto` → `ripeti fino a task completato`. Sul passo `qualcuno la esegue`, un'etichetta appesa in evidenza: `chi? → prossimo incontro`.
>
> **Anello interno**: `1° loop — generazione` (fino a `STOP`).
>
> **Elementi focali**: la corona di mezzo appena riempita (il diagramma "si completa" rispetto alla versione precedente) e l'etichetta `chi? → prossimo incontro` — il cliffhanger visivo della lezione.

## Slide 33 — Il modello è stateless: il contesto è tutto

**Layout**: titolo in alto; i due punti di testo a sinistra (~30%); visual al centro-destra (~65%); nota in basso.

**Testo**:
- Titolo: *Il modello è stateless: il contesto è tutto*
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

## Slide 34 — Il modello è figlio dei suoi training set

**Layout**: titolo in alto; i tre punti di testo al centro; box di riflessione in basso (~30% della slide), visivamente distinto.

**Testo**:
- Titolo: *Il modello è figlio dei suoi training set*
- Punti:
  1. **Tutto viene dai dati**: *ciò che il modello sa, come parla, cosa considera ovvio — è la conseguenza di ciò che ha letto, con i bias di chi quei testi li ha scritti.*
  2. **Il cut-off**: *il mondo del modello si ferma alla data di raccolta dei dati: di ciò che accade dopo, nei pesi non c'è nulla.*
  3. **Anche il carattere**: *cosa risponde volentieri, come si comporta — viene anch'esso da un training set: le preferenze umane, stimate dal reward model.*
- Box di riflessione: *La conoscenza sui modelli fa parte dei training set: un'AI ha letto i paper che descrivono il suo stesso funzionamento interno. L'uomo non sa progettare un cervello — un'AI ha conoscenza di dettaglio del proprio.*

**Visual**: nessuno. È una slide di riflessione: i tre punti e il box finale in evidenza sono essi stessi la struttura visiva; un diagramma diluirebbe il peso della chiusura.
