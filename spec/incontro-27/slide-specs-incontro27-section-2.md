# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 2 — Context Initialization: la finestra al giro zero**
**Obiettivo di apprendimento**: il partecipante sa elencare gli strati della finestra prima che l'utente scriva una parola (system prompt, dichiarazioni dei tool, indice delle skill), sa com'è fatta una chiamata al modello (richiesta, risposta, `stop_reason`), sa che le definizioni dei tool sono un campo API a parte reso nel formato dell'addestramento, e sa che quanti tool e skill esporre è una decisione di progetto.
**Messaggio chiave (takeaway)**: Al giro zero il modello non sa nulla del tuo mondo: sa solo ciò che l'harness gli ha messo davanti. Tutto ciò che può volere, deve essere già dichiarato lì.
**Budget**: ~15 min, 7 slide + separatore.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec2.html` | Separatore — Sezione 2: Context Initialization |
| `slides/slide7-finestra-vuota.html` | Slide 7 — La finestra al giro zero |
| `slides/slide8-system-prompt.html` | Slide 8 — Il system prompt: ruolo e regole |
| `slides/slide9-chiamata-api.html` | Slide 9 — Com'è fatta una chiamata al modello |
| `slides/slide10-dichiarazione-tool.html` | Slide 10 — La dichiarazione dei tool: un contratto |
| `slides/slide11-indice-skill.html` | Slide 11 — Le skill, al giro zero: solo l'indice |
| `slides/slide12-finestra-piena.html` | Slide 12 — La finestra piena, e l'utente non ha ancora scritto |
| `slides/slide13-utente-scrive.html` | Slide 13 — Ora l'utente scrive |

---

> **Filo della sezione — la finestra a strati, in cinque tempi.** Le Slide 7, 8, 10, 11 e 12 portano la stessa figura (`slide7-finestra-strati-{0..4}.svg`, stesso viewBox, pattern `.visual.stack` + fragment come la torre della slide 20 del 26): uno scheletro di strati vuoti che si riempie uno strato per slide. **Si legge dall'alto**, come i riquadri di payload delle slide 8 e 9 del 26 dove `[system]` è la prima riga: `system prompt` in cima, poi `dichiarazione dei tool`, `indice delle skill`, e `messaggi` in fondo, che crescono verso il basso.
>
> ⚠️ **Coerenza con il 26**: la slide 42 del 26 (la pila che cresce) ha gli strati stabili **in fondo**. Quando viene ripresa in sezione 4 va ridisegnata dall'alto, altrimenti contraddice questa figura.
>
> **MCP in questa sezione**: una riga sola (nella Slide 9 e nella Slide 10, "è lì che MCP si innesta"), senza spiegare che cos'è: la sezione 2 mostra *che cosa c'è nella finestra*, la 3 spiega *da dove arriva e chi lo esegue*.
>
> **L'esempio che attraversa la sezione**: l'assistente clienti di Acme, il tool `cerca_ordine` (lo stesso della slide 9 del 26) e le skill `rimborsi-acme` (che rima con il limite del system prompt) e `risposta-reclami-acme` (di sole istruzioni, usata nella Slide 26) ("non promettere mai rimborsi").

---

## Slide 7 — La finestra al giro zero

**Messaggio**: prima ancora che l'utente scriva una parola, la finestra non è vuota: l'harness l'ha preparata. Questa sezione la riempie uno strato alla volta.

**Layout**: titolo in alto; i due punti di testo a sinistra (~35%); visual al centro-destra (~60%): il tempo 1 della finestra a strati; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 2 · CONTEXT INITIALIZATION*
- Titolo: *La finestra al giro zero*
- Punti:
  1. **Il giro zero**: *il momento prima della prima chiamata. L'utente non ha ancora scritto nulla; l'harness sì.*
  2. **A strati**: *ciò che entra non è un testo solo: sono strati distinti, ognuno con un compito, e l'ordine conta: ciò che sta in cima non cambia mai.*
- Nota in basso: *Nel 26 abbiamo visto il contesto come una pila che cresce. Oggi guardiamo la testa della pila: chi l'ha messa lì, e perché.*

**Visual**: `slide7-finestra-strati-0.svg` — tempo 1 della finestra a strati.

**Prompt per schema SVG**:
> Una **finestra di contesto** disegnata come un contenitore verticale alto, con l'etichetta `la finestra al giro zero` in cima. Dentro, **dall'alto verso il basso**, quattro strati impilati, ognuno un rettangolo con la sola etichetta a sinistra e il corpo vuoto, tratteggiato:
> 1. `system prompt: ruolo e regole` (in cima)
> 2. `dichiarazione dei tool`
> 3. `indice delle skill`
> 4. `messaggi` (in fondo, vuoto: *ancora nessuno*; è lo strato che crescerà verso il basso)
>
> A destra della finestra, una colonna sottile etichettata `token`, vuota, allineata agli strati: si riempirà nella Slide 12.
>
> In basso, fuori dalla finestra: `→ chiamata n. 1: non ancora`.
>
> **Elemento focale**: il vuoto. La figura deve leggersi come uno scheletro pronto a riempirsi: gli strati esistono già, il contenuto no.

## Slide 8 — Il system prompt: ruolo e regole

**Messaggio**: il system prompt è il primo strato: dice al modello chi è, che cosa deve fare e che cosa non deve fare; e ha un peso diverso dalle parole dell'utente, per come il modello è stato addestrato.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); a destra (~55%) un riquadro-payload nell'idioma del 26 con un system prompt reale e, sotto, la finestra a strati (tempo 2); nota in basso.

**Testo**:
- Titolo: *Il system prompt: ruolo e regole*
- Punti:
  1. **Che cos'è**: *il testo che l'harness mette in cima alla finestra, prima di ogni conversazione: chi sei, che cosa fai, come rispondi, che cosa non fai mai.*
  2. **Due ruoli, non uno**: *quasi tutti i modelli distinguono il ruolo `system` dal ruolo `user`. Non è solo etichetta: il post-addestramento ha premiato il modello che segue con più rigore ciò che sta nel system prompt, anche quando l'utente chiede il contrario.*
  3. **Chi lo scrive**: *non l'utente: chi costruisce l'agente. È la prima leva di miglioramento, e la più economica.*
- Riquadro-payload (HTML, monospaziato con tag di ruolo, testo esatto):
  ```
  [system]
  Sei l'assistente del servizio clienti di Acme.
  Rispondi in italiano, in modo breve.
  Puoi consultare lo stato degli ordini.
  Non promettere mai rimborsi: rimanda a un operatore.
  ```
  con a lato, in piccolo, la glossa dei quattro elementi: *ruolo · stile · capacità · limiti*.
- Nota in basso: *Nel 26, la mira arrivava con il RL. Qui la vediamo all'opera: la gerarchia fra system e user è una cosa che il modello ha imparato, non una regola del software.*

**Visual**: riquadro-payload (HTML) + `slide7-finestra-strati-1.svg` (tempo 2).

**Prompt per schema SVG** (tempo 2): stessa figura della Slide 7, con lo strato `system prompt: ruolo e regole` pieno e in evidenza, il testo abbreviato dentro (`Sei l'assistente di Acme…`), gli altri tre ancora tratteggiati.

## Slide 9 — Com'è fatta una chiamata al modello

> Slide nuova nel corso: il 26 non ha mai mostrato la struttura dell'API (la sua slide 41 parla solo di costo). I nomi sono quelli dell'API Messages di Anthropic (verificati a set 2026); gli altri provider hanno la stessa forma con nomi diversi.

**Messaggio**: il modello si raggiunge con una chiamata HTTP la cui struttura è esattamente la finestra a strati; la risposta dice che cosa ha generato e perché si è fermato.

**Layout**: titolo in alto; visual a tutta larghezza (~70%): richiesta a sinistra, risposta a destra, freccia di ritorno sotto; didascalia in basso. Nessun punto di testo.

**Testo**:
- Titolo: *Com'è fatta una chiamata al modello*
- Didascalia: *I nomi sono quelli dell'API di Anthropic; gli altri provider hanno la stessa forma con nomi diversi. La richiesta è la finestra a strati, campo per campo. La risposta porta i blocchi generati e uno `stop_reason`: è il bit che l'harness legge per decidere se il giro continua.*

**Visual**: `slide9-chiamata-api.svg`.

**Prompt per schema SVG**:
> **A sinistra, la richiesta** (`POST /v1/messages`), un riquadro in monospaziato con i soli campi che contano, ognuno con la glossa a lato:
> ```
> model:      "…"
> system:     "Sei l'assistente di Acme…"                 ← lo strato 1
> tools:      [ {name, description, input_schema}, … ]   ← lo strato 2
> messages:   [ {role: "user", content: "…"} ]           ← la storia
> max_tokens: 4096
> ```
> Su `system` e sull'ultimo tool, una piccola bandierina `cache_control` con la glossa *fin qui non cambia: riusalo* (il prefix caching si spiega in sezione 4).
>
> **A destra, la risposta**, stesso stile:
> ```
> content: [
>   { type: "text", text: "Controllo subito." },
>   { type: "tool_use", id: "tu_01", name: "cerca_ordine", input: {id_ordine: "4471"} }
> ]
> stop_reason: "tool_use"
> ```
> `stop_reason` è l'elemento focale: accanto, i due valori possibili con la glossa: `end_turn` → *ha finito: il turno è chiuso*; `tool_use` → *vuole un tool, e aspetta*.
>
> **Sotto, la freccia di ritorno**: dalla risposta alla richiesta, etichettata `giro successivo: messages += tool_use + tool_result`, con il blocco `{ type: "tool_result", tool_use_id: "tu_01", content: "…" }` disegnato in **teal** (è la riga `[tool]` del 26: non l'ha scritta il modello).
>
> In un angolo, due righe piccole: *anche le skill entrano da qui (`container.skills`)* · *anche i server MCP (`mcp_servers`)*.
>
> **Elemento focale**: `stop_reason: "tool_use"`, e la corrispondenza uno-a-uno fra i campi della richiesta e gli strati della finestra.

## Slide 10 — La dichiarazione dei tool: un contratto

**Messaggio**: un tool, per il modello, è solo la sua definizione: nome, descrizione, parametri. È documentazione scritta per un lettore che non può fare domande, e viene resa nel formato su cui il modello è stato addestrato.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); a destra (~55%) la definizione reale di un tool nell'idioma dei riquadri e, sotto, la finestra a strati (tempo 3); nota in basso.

**Testo**:
- Titolo: *La dichiarazione dei tool: un contratto*
- Punti:
  1. **Tre campi**: *un nome, una descrizione in linguaggio naturale, lo schema dei parametri. Il modello non vede il codice del tool: vede solo questo.*
  2. **È documentazione per il modello**: *la descrizione decide se e quando il tool verrà scelto. Un tool descritto male è un tool che non viene chiamato, o viene chiamato a sproposito.*
  3. **Un campo a parte, ma è system prompt**: *si passa all'API come parametro separato (`tools`), e il provider lo rende nel formato esatto su cui il modello è stato addestrato con il RL agentico. Concettualmente è uno strato del system prompt; tecnicamente è un campo a sé: è lì che MCP si innesta.*
- Riquadro-definizione (HTML, testo esatto):
  ```
  name:        cerca_ordine
  description: Restituisce lo stato di un ordine dato il suo
               identificativo. Usalo quando il cliente chiede
               dove si trova un ordine o quando arriva.
  input_schema:
    id_ordine: string — l'identificativo, es. "4471"
  ```
  con a lato, in piccolo e sbiadito, una descrizione cattiva: `description: "ordine"`, e la glossa *così non viene mai scelto*.
- Nota in basso: *Ogni definizione entra nella finestra a ogni giro, letta o no. Segnatevelo: torna nella sezione 4.*

**Visual**: riquadro-definizione (HTML) + `slide7-finestra-strati-2.svg` (tempo 3).

**Prompt per schema SVG** (tempo 3): stessa figura, con lo strato `dichiarazione dei tool` pieno e in evidenza (dentro: `cerca_ordine`, `…`), `system prompt` pieno ma attenuato, gli altri due tratteggiati.

## Slide 11 — Le skill, al giro zero: solo l'indice

> Qui solo l'inizializzazione. Che cos'è una skill per esteso (istruzioni, e a volte uno script) è in sezione 3; il conto della progressive disclosure è in sezione 4.

**Messaggio**: di ogni skill, al giro zero entra solo l'indice: nome e descrizione. Il corpo aspetta di essere richiesto. È la stessa logica della dichiarazione dei tool, applicata a documenti di istruzioni.

**Layout**: titolo in alto; i due punti di testo a sinistra (~40%); a destra (~55%) il frontmatter reale di una skill e, sotto, la finestra a strati (tempo 4); nota in basso.

**Testo**:
- Titolo: *Le skill, al giro zero: solo l'indice*
- Punti:
  1. **Che cosa entra**: *per ogni skill, due righe: il nome e una descrizione che dice quando usarla. Sono l'indice di un libro di cui il modello non ha ancora letto nessun capitolo.*
  2. **Che cosa non entra**: *il corpo della skill, cioè le istruzioni vere e proprie, resta fuori dalla finestra finché il modello non decide che gli serve. Come la carichi, e che cosa contiene, lo vediamo nelle sezioni 3 e 4.*
- Riquadro-indice (HTML, testo esatto, come appare nella finestra):
  ```
  skills disponibili:
  - rimborsi-acme — Procedura per gestire una richiesta di rimborso:
    verifica, soglie, quando passare a un operatore.
  - risposta-reclami-acme — Come rispondere a un reclamo: struttura,
    tono, cosa non dire mai.
  ```
  A lato, sbiadito e tratteggiato, un blocco più grande etichettato `corpo della skill: non ancora nella finestra`.
- Nota in basso: *Un tool si dichiara con uno schema; una skill si dichiara con una frase. In entrambi i casi, la descrizione è ciò che decide se verrà scelta.*

**Visual**: riquadro-indice (HTML) + `slide7-finestra-strati-3.svg` (tempo 4).

**Prompt per schema SVG** (tempo 4): stessa figura, con lo strato `indice delle skill` pieno e in evidenza (dentro: `rimborsi-acme`, `risposta-reclami-acme`), i due strati sopra pieni ma attenuati, `messaggi` ancora vuoto.

## Slide 12 — La finestra piena, e l'utente non ha ancora scritto

**Messaggio**: prima della prima parola dell'utente, la finestra pesa già migliaia di token, torna a ogni giro, e più voci ci sono, peggio il modello sceglie.

**Layout**: titolo in alto; visual al centro (~60%): la finestra a strati completa, con la colonna dei token riempita (tempo 5, definitivo); i tre punti di testo a destra (~35%); nota in basso.

**Testo**:
- Titolo: *La finestra piena, e l'utente non ha ancora scritto*
- Punti:
  1. **Il conto**: *un system prompt di qualche centinaio di token; ogni tool dichiarato da uno a qualche centinaio; ogni riga di indice delle skill poche decine. Con quindici tool e venti skill si parte da diverse migliaia di token, a finestra "vuota".*
  2. **Ed è il prefisso**: *questi strati non cambiano da un giro all'altro, e l'API li mette in cache. Se la cache è usata bene, il costo in denaro di questo pezzo è basso: si paga per intero una volta, poi una frazione. Il conto è la sezione 4.*
  3. **La confusione decisionale**: *il peso in token non è il problema principale. Con trenta tool e cinquanta skill il modello sceglie peggio: descrizioni che si somigliano, tool che si sovrappongono, e la scelta sbagliata costa più di mille token. Nel 26: "meglio tool specifici che generici".*
- Nota in basso (takeaway): *Quanti tool e quante skill esporre è una decisione di progetto, non un accumulo: ogni voce in più deve giustificare il suo posto nell'indice.*

**Visual**: `slide7-finestra-strati-4.svg` (tempo 5).

**Prompt per schema SVG** (tempo 5):
> Stessa figura, con **tutti e tre gli strati del prefisso pieni** e `messaggi` ancora vuoto con l'etichetta *ancora nessuno*. La colonna `token` a destra ora è riempita, con una barra proporzionale per strato e il numero: `system prompt ~400` · `dichiarazione dei tool ~3.000 (15 tool)` · `indice delle skill ~800 (20 skill)` · `messaggi 0`. In fondo alla colonna, il totale in evidenza: `~4.200 token, prima della prima parola`, e sotto, in piccolo: `in cache: si ripaga a frazione`.
> Una graffa a destra abbraccia i tre strati pieni, etichettata `il prefisso: non cambia da un giro all'altro`.
>
> **Elemento focale**: il totale in fondo alla colonna, letto insieme al `messaggi 0`.

> I numeri sono ordini di grandezza plausibili, non misure; va detto in aula. In Fase 3 si possono sostituire con numeri misurati su un agente reale (endpoint di conteggio token).

## Slide 13 — Ora l'utente scrive

> Ripresa della slide 9 del 26 (i due giri), **solo la metà destra e solo il `giro 1`**. È la cerniera verso la sezione 3.

**Messaggio**: la prima domanda entra nello strato `messaggi`, il modello genera, vuole un tool, e si ferma. Da qui in poi tocca all'harness.

**Layout**: titolo in alto; visual a tutta larghezza (~65%); didascalia sotto; blocco nero centrato in fondo. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *Ora l'utente scrive*
- Didascalia: *La stessa scena del 26: il system prompt in testa con il tool dichiarato, la domanda dell'utente, e la richiesta del modello: `cerca_ordine("4471")`. Lì il modello si ferma, con `stop_reason: tool_use`. Nel 26 dicevamo "qualcun altro esegue". Ora entriamo nella zona gialla della mappa.*
- Blocco nero centrato: *Il modello ha chiesto. Chi esegue, come, e che cosa torna indietro: sezione 3.*

**Visual**: `slide13-giro-uno.svg` — ripresa di `slide9b-tool-call.svg` del 26.

**Prompt per schema SVG**:
> Riprende il riquadro `giro 1` della metà destra della slide 9 dell'incontro 26, alla stessa scala. Le prime righe del riquadro sono ora i tre strati della finestra della Slide 12 (system prompt, dichiarazione dei tool, indice delle skill) in forma compatta; poi la riga `[user] Dov'è il mio ordine 4471?`; poi la pill del modello con la richiesta `→ cerca_ordine("4471")` e, accanto, in piccolo, `stop_reason: tool_use`.
>
> A destra, dove nel 26 stava il `giro 2`, un riquadro tratteggiato vuoto con un `?` al centro.
>
> **Elemento focale**: la pill della richiesta con `stop_reason: tool_use` e il riquadro vuoto accanto.
