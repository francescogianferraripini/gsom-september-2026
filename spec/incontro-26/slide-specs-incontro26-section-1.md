# Specifica slide — PC AI 26: Agentic AI — da LLM ad agenti (basi concettuali)
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 1 — Cosa è un agente?**
**Obiettivo di apprendimento**: il partecipante sa dire cosa ci si aspetta funzionalmente da un agente e sa scomporlo nei suoi componenti tecnici (le due formule `Agent =` e `Harness =`).
**Messaggio chiave (takeaway)**: Un agente non è un modello: è un modello dentro un'impalcatura. `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`.
**Budget**: ~15 min, 4 slide + separatore. Copertina della lezione fuori sezione (slide 0 a parte). Il passaggio finale all'LLM ("oggi apriamo il primo termine della formula") è fatto a voce, senza slide dedicata.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec1.html` | Separatore — Sezione 1: Cosa è un agente? |
| `slides/slide1-aspettative.html` | Slide 1 — Cosa è un agente? Le aspettative |
| `slides/slide2-spazio-soluzioni.html` | Slide 2 — Lo spazio delle soluzioni |
| `slides/slide3-formula-agent.html` | Slide 3 — La formula: Agent = |
| `slides/slide4-ruolo-harness.html` | Slide 4 — Il ruolo dell'harness |

---

## Slide 1 — Cosa è un agente? Le aspettative

> Slide interattiva: domanda aperta alla classe. Le ipotesi in slide sono semi di discussione (mix di naïf e mature, non distinte graficamente); la nota in basso è la frase d'atterraggio e compare solo alla fine della discussione.

**Layout**: titolo in alto; domanda centrale grande al centro; le 8 ipotesi disposte sparse attorno alla domanda (stile appunti/post-it, leggermente disallineate, a suggerire un brainstorming e non un elenco chiuso); nota d'atterraggio in basso.

**Animazione** (3 step, guidata dal docente durante la discussione in aula):
1. Compaiono titolo e domanda centrale.
2. Compaiono le ipotesi sparse.
3. Compare la nota d'atterraggio in basso.

**Testo**:
- Titolo: *Cosa è un agente?*
- Domanda centrale: *Che aspettative abbiamo da un agente?*
- Ipotesi sparse (naïf e mature mescolate, senza distinzione grafica):
  - *"Un chatbot, ma più intelligente"*
  - *"Che risponda a qualsiasi domanda"*
  - *"Che non sbagli mai"*
  - *"Che sostituisca una persona"*
  - *"Che faccia da solo, senza che io lo guidi passo passo"*
  - *"Che usi i miei strumenti: mail, file, gestionali"*
  - *"Che si accorga quando sbaglia — e ci riprovi"*
  - *"Che sappia spiegarmi cosa ha fatto e perché"*
- Nota in basso (a comparsa finale): *Ci aspettiamo che porti a termine un task — non che risponda a una domanda.* — resa come **blocco nero pieno, testo bianco centrato** (`.nota.dark.center`): è la frase d'atterraggio della discussione e deve staccarsi dai post-it.

**Visual**: nessuno. La disposizione sparsa delle ipotesi attorno alla domanda è essa stessa l'elemento visivo (brainstorming), un diagramma non aggiungerebbe comprensione.

## Slide 2 — Lo spazio delle soluzioni

**Layout**: titolo in alto; grande mappa 2D al centro (~75% della slide); nota ponte in basso.

**Testo**:
- Titolo: *Lo spazio delle soluzioni*
- Didascalia (sotto il titolo): *La jagged frontier: non tutti i task sono uguali.*
- Nota ponte in basso: *La frontiera si sposta costantemente. La verificabilità deterministica del risultato è l'elemento determinante per poter addestrare gli LLM ad abilitare correttamente gli agenti.*

**Visual**: mappa 2D dei task (verificabilità × ampiezza di contesto), con 8 task posizionati come punti; coding e ragionamento matematico come sweet spot evidenziati, ragionamento strategico aziendale come quadrante difficile.

**Prompt per schema SVG**:
> Griglia 2D cartesiana, pulita e ariosa.
>
> **Asse X (orizzontale)**: `Ampiezza di contesto richiesta` — etichette agli estremi: `Basso` (sinistra), `Alto` (destra).
> **Asse Y (verticale)**: `Verificabilità del risultato` — etichette agli estremi: `Bassa` (basso), `Alta` (alto).
>
> **8 punti** come cerchi pieni con etichetta accanto, coordinate indicative (x, y) su scala 0–100:
>   1. `Q&A / recupero conoscenza` — (15, 85)
>   2. `Classificazione / giudizio` — (20, 88)
>   3. `Ragionamento matematico` — (85, 65) — **stessa ampiezza di contesto di `Coding`** (stessa X) e **stesso trattamento grafico**: cerchio grande, etichetta in evidenza
>   4. `Coding` — (85, 90) — il punto in risalto: cerchio più grande, etichetta in evidenza
>   5. `Trasformazione di testo` — (25, 55)
>   6. `Multi-step planning / task agentici` — (80, 50)
>   7. `Generazione (scrittura, email, brief)` — (40, 25)
>   8. `Ragionamento strategico aziendale` — (85, 15) — reso attenuato/tratteggiato: il quadrante difficile
>
> Nessuna etichetta di quadrante: i punti parlano da soli.
>
> **Elementi focali**: `Coding` e `Ragionamento matematico` come estremo positivo (alta verificabilità + alto contesto: il sweet spot del lavoro agentico — sono verificabili in modo deterministico, ed è questo che permette di addestrarci sopra gli LLM) e, per contrasto, `Ragionamento strategico aziendale` come punto più difficile da automatizzare bene.

## Slide 3 — La formula: Agent =

**Layout**: titolo in alto; il diagramma-formula occupa il centro della slide (~65%), protagonista assoluto; nota in basso. I sei termini della formula devono restare blocchi visivamente distinti e autonomi: l'incontro 27 riprenderà lo stesso diagramma con LLM sbiadito e Harness in evidenza.

**Testo**:
- Titolo: *Un agente è un sistema composto*
- Formula (dentro il visual): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Nota in basso: *LLM e Harness sono il sistema operativo. Il resto è come se fosse il software che, a parità di infrastruttura, organizza il lavoro a seconda dell'obiettivo.*

**Visual**: diagramma-formula orizzontale a blocchi con due graffe di raggruppamento (sistema operativo / software installato).

**Prompt per schema SVG**:
> Diagramma-formula orizzontale a blocchi, su una sola riga.
>
> **A sinistra**: un blocco `Agent`, seguito dal segno `=`.
>
> **A destra del segno `=`**: sei blocchi in fila, separati dal segno `+`. Ogni blocco contiene il termine in evidenza e, sotto, la sua glossa in piccolo:
>   1. `LLM` — *il motore che genera*
>   2. `Harness` — *l'impalcatura che lo fa lavorare*
>   3. `System Prompt` — *ruolo e regole*
>   4. `Tools` — *interagire con l'ecosistema IT*
>   5. `KB` — *ciò che l'organizzazione sa: il know-what*
>   6. `Skills` — *il know-how procedurale*
>
> **Sotto la fila**, due graffe orizzontali di raggruppamento:
>   - una che abbraccia `LLM` e `Harness`, con etichetta *il sistema operativo*;
>   - una che abbraccia `System Prompt`, `Tools`, `KB` e `Skills`, con etichetta *il software installato*.
>
> **Elementi focali**: le due graffe con le loro etichette — portano il messaggio (il modello è solo uno dei sei ingredienti; è il "software installato" a distinguere un agente da un altro). I sei blocchi devono essere visivamente distinti e autonomi (ognuno un rettangolo a sé), perché una versione futura dello stesso diagramma riprenderà i medesimi blocchi sbiadendo `LLM` ed evidenziando `Harness`.

## Slide 4 — Il ruolo dell'harness

**Layout**: titolo in alto; le tre affermazioni sulla sinistra (~40% della larghezza); il visual esoscheletro sulla destra (~60%).

**Testo**:
- Titolo: *Il ruolo dell'harness*
- Testo: *L'Harness è un software "classico", deterministico, che orchestra le attività che fa l'agente sotto la direzione del LLM. Se pensiamo all'agente come un'entità neuro-simbolica, l'LLM è la parte Neuro, l'Harness quella simbolica. È come l'esoscheletro operativo, all'interno del quale c'è un cervello, l'LLM.*

**Visual**: l'esoscheletro a blocchi — cornice composta dalle **3 categorie** di componenti, con al centro il blocco `LLM` (il cervello). Nessun blocco-titolo `Harness` dentro la figura: il titolo della slide basta.

**Prompt per schema SVG**:
> Diagramma "esoscheletro": una cornice che racchiude un blocco centrale, organizzata in **tre categorie distinte da colori**.
>
> **Al centro**: un blocco `LLM`, con sotto-etichetta *il cervello (neuro)*, in burgundy — colore riservato a lui.
>
> **Intorno**, tre zone contigue che insieme formano l'involucro. Ogni zona ha un'intestazione col nome della categoria, nel colore pieno della categoria, e contiene i propri sotto-blocchi:
>
>   1. **`Context management`** — quattro sotto-blocchi:
>      `Context Initialization` · `Context Optimization (compaction, pruning, etc.)` · `Memory management` · `Skill management`
>   2. **`Agentic loop management`** — blocco unico, senza sotto-blocchi: è l'anello che gira attorno all'LLM.
>   3. **`Environment management`** — tre sotto-blocchi:
>      `Tool Calling execution and response management` · `Execution Sandbox` · `Skill execution management`
>
> Le tre zone non sono satelliti staccati: sono i segmenti della cornice, a comunicare che l'harness *è* l'involucro. Il blocco `LLM` è dentro, completamente racchiuso.
>
> **Elemento focale**: il contrasto tra il centro (`LLM`, la parte neuro) e la cornice (la parte simbolica/deterministica) — le due nature devono leggersi come zone distinte; e, dentro la cornice, la tripartizione per colore. I nomi delle categorie e dei sotto-blocchi sono etichette esatte, da non parafrasare.

<!-- I blocchi slide successivi verranno aggiunti qui durante l'intervista (Fase 2). -->
