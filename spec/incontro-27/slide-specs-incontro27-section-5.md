# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 5 — Observability: osservare e migliorare**
**Obiettivo di apprendimento**: il partecipante sa quali leve ha per migliorare un agente e in che ordine provarle, sa perché si valutano traiettorie e non risposte, conosce il processo di valutazione (chi giudica, dataset, cluster di fallimento, checker deterministici, giudice validato, ciclo in produzione) e i due ruoli che lo reggono, e sa a che cosa servono le tracce oltre al debug.
**Messaggio chiave (takeaway)**: Non si migliora ciò che non si legge. La traiettoria è il prodotto dell'agente: leggila a mano, classifica i fallimenti, automatizza solo dopo.
**Budget**: ~24 min, 11 slide + separatore. Ripartizione: leve 1, livelli e traiettoria 1, vibe eval 1, processo 7 (mappa · chi giudica · dataset · cluster · checker e giudice · errori nei tool · ciclo in produzione), tre usi del logging 1.
**Vincolo del docente**: per il processo di valutazione la sequenza dei concetti è quella del brief (`docs/incontro-27.md`, capitolo "Come monitoro e miglioro"); i dettagli statistici della validazione del giudice restano nelle note del relatore.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec5.html` | Separatore — Sezione 5: Observability |
| `slides/slide40-leve.html` | Slide 40 — Le leve di miglioramento |
| `slides/slide41-tre-livelli.html` | Slide 41 — Tre livelli di successo, e la traiettoria |
| `slides/slide42-vibe-eval.html` | Slide 42 — Il rischio del vibe eval |
| `slides/slide43-processo-eval.html` | Slide 43 — Il processo, in un colpo d'occhio |
| `slides/slide44-chi-giudica.html` | Slide 44 — Chi giudica: una persona sola, e le tracce a mano |
| `slides/slide45-dataset.html` | Slide 45 — Il dataset di test: cento casi, per dimensioni |
| `slides/slide46-cluster-leve.html` | Slide 46 — Clusterizzare i fallimenti, e risalire alla leva |
| `slides/slide47-checker-giudice.html` | Slide 47 — Checker deterministici, poi il giudice |
| `slides/slide48-errori-tool.html` | Slide 48 — Gli errori nei tool deterministici e nei tool non deterministici |
| `slides/slide49-ciclo-produzione.html` | Slide 49 — In produzione: il ciclo che non finisce |
| `slides/slide50-tre-usi-logging.html` | Slide 50 — Tre usi del logging |

---

> **Filo della sezione.** La fascia `Observability` della mappa si accende. La Slide 40 apre il menu delle leve (prompt, KB, tool, harness, modello); le 41–42 dicono che cosa si misura (la traiettoria) e come non si misura (il vibe eval); la 43 è la **mappa del processo**, che le Slide 44–49 richiamano in miniatura con la tappa corrente accesa (come la slide 34 del 26 con le tre fasi); la 46 chiude il cerchio con le leve: **tipicamente un cluster di fallimento è legato a una leva**; la 50 chiude la sezione e il cerchio con il 26 (le traiettorie di oggi sono i dati di domani).
>
> **Due ruoli** (decisi in intervista): l'**esperto di dominio** costruisce i dataset, decide i pass/fail e valida il giudice; il **team di sviluppo dell'agente** scrive checker e giudice, esegue i test e li rigira a ogni modifica. Si incontrano sulla validazione del giudice (Slide 47).
>
> **Riprese dal 26**: le traiettorie premiate (slide 38) e il valore delle traiettorie (slide 50) → Slide 41 e Slide 50.
>
> **La traccia annotata** (l'immagine del brief) compare due volte: incompleta nella Slide 44, completa e letta da tre lati nella Slide 50.

---

## Slide 40 — Le leve di miglioramento

**Messaggio**: un agente si migliora tirando cinque leve, in ordine crescente di costo e complessità; le quattro sopra il modello sono quelle che restano tue quando il modello cambia.

**Layout**: titolo in alto; visual al centro (~55%): la scala delle leve; i due punti di testo a destra (~40%); nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 5 · OBSERVABILITY*
- Titolo: *Le leve di miglioramento*
- Punti:
  1. **Cinque leve, in ordine**: *prompt, knowledge base, tool, harness, modello. Dal più economico al più costoso: cambiare una riga del system prompt costa minuti; cambiare modello costa una rivalidazione di tutto.*
  2. **La libertà di cambiare modello**: *le prime quattro leve sono tue: system prompt, KB, tool e harness restano quando sotto cambi l'LLM. Chi ha investito lì cambia modello in un giorno; chi ha investito solo nel modello (fine-tuning, prompt cuciti su un comportamento) ricomincia.*
- Nota in basso: *Migliorare e restare liberi sono lo stesso lavoro: ogni fix messo in una leva alta è un fix che sopravvive al prossimo modello. Ma per sapere quale leva tirare, prima bisogna misurare: è il resto della sezione.*

**Visual**: `slide40-leve.svg`.

**Prompt per schema SVG**:
> Cinque leve disegnate come una scala, dal basso verso l'alto in ordine di complessità crescente, ognuna un gradino con nome ed esempio: `Prompt` (*una riga nel system prompt, una descrizione di tool, il corpo di una skill*), `Knowledge base` (*un documento in più, un documento corretto, un indice migliore*), `Tool` (*uno schema più chiaro, un adattatore che restituisce meno, un errore scritto meglio*), `Harness` (*una soglia di pruning, una regola di memoria, un subagente*), `Modello` (*cambiarlo, o addestrarlo sulle tue traiettorie*). Accanto a ogni gradino, a destra, due indicatori: `costo` e `tempo`, che crescono salendo (tacche o barrette).
>
> Una graffa a sinistra abbraccia i primi quattro gradini con l'etichetta `resta tuo quando cambi modello`; il quinto gradino, `Modello`, è fuori dalla graffa con l'etichetta `cambia con il fornitore`.
>
> Nella formula in miniatura in un angolo (`Agent = LLM + Harness + System Prompt + Tools + KB + Skills`), i termini corrispondenti alle quattro leve alte sono accesi, `LLM` è attenuato.
>
> **Elemento focale**: la graffa dei quattro gradini "tuoi", contrapposta al quinto.

## Slide 41 — Tre livelli di successo, e la traiettoria

> Ripresa delle slide 38 e 50 del 26.

**Messaggio**: "funziona?" ha tre risposte a scale diverse: il singolo colpo, il turno con le sue tool call, il processo intero. E l'oggetto da guardare per rispondere non è mai la risposta finale: è la traiettoria.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso. Eyebrow *dall'incontro 26*.

**Testo**:
- Titolo: *Tre livelli di successo, e la traiettoria*
- Punti:
  1. **Il task single shot**: *una domanda, una risposta: è giusta? È il livello a cui si valutano i modelli, e il più facile da misurare.*
  2. **Il turno, end-to-end**: *dentro un turno, N tool call: ha scelto i tool giusti, con i parametri giusti, nell'ordine giusto, e ha usato i risultati? Una risposta finale corretta può nascondere tre chiamate sbagliate e una fortunata.*
  3. **Il processo complessivo**: *più turni, più sessioni, un obiettivo di business: il rimborso è stato gestito, il report è arrivato, il cliente non ha richiamato. È il livello che conta per chi paga, e il più lento da misurare.*
- Nota in basso: *Nel 26: la traiettoria è l'unità di valore del RL agentico. Oggi è l'unità di valutazione: la risposta è l'ultima riga di una traiettoria, e da sola non dice quasi niente.*

**Visual**: `slide41-tre-livelli.svg` — ripresa di `slide32-rl-agentico.svg` del 26 riletta a tre livelli.

**Prompt per schema SVG**:
> Una sola traiettoria orizzontale, disegnata come nella slide 38 del 26 (nodi `pensiero`, `tool call`, `risultato`, in fila da sinistra a destra), ma più lunga: attraversa **tre turni** dell'utente, separati da due tacche verticali `turno 1`, `turno 2`, `turno 3`, e finisce in un traguardo `rimborso gestito`.
>
> Sopra la traiettoria, tre graffe a scale diverse, impilate: la più piccola abbraccia un solo nodo `risposta` (`1 · task single shot: la risposta è giusta?`); la media abbraccia un turno intero con le sue tre tool call (`2 · il turno: tool giusti, ordine giusto, risultati usati?`); la più grande abbraccia tutto (`3 · il processo: l'obiettivo è raggiunto?`).
>
> In basso, una nota: *quello che si valuta è la traiettoria, non l'ultima riga*. Un nodo `tool call` a metà del turno 2 è marcato con un `✗` piccolo: *una chiamata sbagliata, e la risposta finale era giusta lo stesso*.
>
> **Elemento focale**: le tre graffe a scale diverse sulla stessa traiettoria.

## Slide 42 — Il rischio del vibe eval

**Messaggio**: provare l'agente "a sensazione" (qualche domanda, si guarda se risponde bene) non è una valutazione: non è ripetibile, e di solito misura solo i casi che chi prova aveva già in mente.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~45%); a destra (~50%) una vignetta-contrasto in due riquadri; blocco nero centrato in fondo.

**Testo**:
- Titolo: *Il rischio del vibe eval*
- Punti:
  1. **Non è stabile**: *si provano dieci domande, oggi sembra meglio, domani peggio: senza un insieme fisso di casi non si sa se è cambiato l'agente o le domande.*
  2. **Tipicamente un campione distorto**: *chi prova sceglie i casi che ha in mente, cioè quelli su cui l'agente è già stato messo a punto. I fallimenti veri stanno nei casi che nessuno ha pensato di provare.*
  3. **E il whack-a-mole**: *si corregge il caso visto, e senza saperlo se ne rompe un altro: non c'è modo di accorgersene, perché non c'è nulla da rieseguire.*
- Blocco nero centrato: *"Sembra che funzioni" non è una misura. Serve un insieme di casi fisso, un giudizio ripetibile, e qualcuno che guardi le tracce.*

**Visual**: `slide42-vibe-eval.svg`.

**Prompt per schema SVG**:
> Due riquadri affiancati. **A sinistra, `vibe eval`**: una persona davanti a una chat e una sequenza in tre giorni: `lun` domanda A `✓` → `mar` domanda B `✗` → *si corregge il martedì* → `mer`: la domanda B ora `✓`, ma la domanda A, riprovata, `✗`. Etichetta: *il fix del martedì ha rotto il lunedì, e nessuno lo sa*; un punto interrogativo grande: *è migliorato?*. **A destra, `eval`**: la stessa persona davanti a una griglia fissa di 100 caselle (i casi), rieseguita tre volte con tre righe di risultato sotto (`72/100`, `74/100`, `81/100`) e una freccia che sale: *è migliorato*. Sotto la griglia, dieci caselle evidenziate: *i casi che nessuno avrebbe provato a mano*.
>
> **Elemento focale**: il lunedì che si rompe a sinistra, contro i tre numeri a destra.

## Slide 43 — Il processo, in un colpo d'occhio

> Slide-mappa della sezione, aggiunta in intervista: le Slide 44–49 la richiamano in miniatura con la tappa corrente accesa.

**Messaggio**: valutare un agente non è un test da fare una volta: è un processo con dei passi in ordine, due ruoli e una parte che non finisce mai. Prima di entrare nei passi, la mappa.

**Layout**: titolo in alto; il visual a tutta larghezza (~65%): la pipeline dei passi; didascalia sotto; nota in basso.

**Testo**:
- Titolo: *Il processo, in un colpo d'occhio*
- Didascalia: *Sei passi, in quest'ordine, e poi un ciclo. Nessun passo si salta: ognuno produce ciò che serve al successivo. Il primo non è tecnico: è decidere chi giudica.*
- Nota in basso: *Due responsabilità, non una: l'esperto di dominio decide che cosa è giusto e costruisce i casi; il team dell'agente rende quel giudizio automatico e lo riesegue. Senza il primo si misura la cosa sbagliata; senza il secondo si misura una volta sola.*

**Visual**: `slide43-processo-eval.svg`.

**Prompt per schema SVG**:
> Pipeline orizzontale di **sei tappe** numerate, ognuna un blocco con il nome, una riga *che cosa si fa*, una riga *che cosa ne esce*, e il rimando alla slide:
> 1. `Chi giudica` — *si sceglie una persona esperta del dominio e le si fanno leggere le tracce delle prime fasi di test dell'agente, prodotte per esempio da utenti di prova, per valutarle e interpretarle* → *un giudizio coerente su che cosa è "giusto"* → Slide 44
> 2. `Il dataset di test` — *si scrivono ~100 casi, anche sintetici, per dimensioni, ispirati dalle tracce* → *un insieme fisso su cui rieseguire* → Slide 45
> 3. `I cluster di fallimento` — *si rileggono i fallimenti e si raggruppano per tipo, finché le categorie non finiscono* → *le categorie, e per ciascuna la leva da tirare* → Slide 46
> 4. `Checker deterministici` — *si scrive codice che verifica il pass/fail dove è verificabile* → *un punteggio automatico e ripetibile* → Slide 47
> 5. `Il giudice` — *si costruisce un LLM-as-a-judge e lo si valida contro i giudizi dell'esperto* → *un punteggio automatico anche dove non c'è un checker* → Slide 47
> 6. `In produzione` — *si campionano ~100 tracce al mese, si rileggono a mano, il dataset cresce* → *regressioni scoperte a ogni modifica* → Slide 49
>
> Dall'ultima tappa una **freccia di ritorno** verso la tappa 3, etichettata `a ogni modifica (prompt, modello, tool): si rigira tutto`.
>
> **Due fasce di ownership** sopra la pipeline, in due colori: `l'esperto di dominio` che abbraccia le tappe 1, 2, 3 e rientra sulla 5 (*costruisce i dataset, decide i pass/fail, valida il giudice*) e `il team di sviluppo dell'agente` che abbraccia le tappe 4, 5, 6 (*scrive i checker e il giudice, esegue i test, li rigira a ogni modifica*). La tappa 5 sta sotto entrambe: è dove i due si incontrano.
>
> Sotto la pipeline, la fascia `Observability` con i quattro sottoblocchi e frecce sottili verso le tappe che alimentano: `Tracing` → 1, 3, 6; `Eval` → 4, 5; `Metrics` → 6; `Logging` → 1.
>
> **Elemento focale**: le due fasce di ownership e la tappa 5 dove si sovrappongono; secondo elemento, la freccia di ritorno.

## Slide 44 — Chi giudica: una persona sola, e le tracce a mano

**Messaggio**: il primo passo è organizzativo, non tecnico: una persona decide che cosa è giusto, e lo fa leggendo le tracce delle prime prove dell'agente, una per una.

**Layout**: titolo in alto; i due punti di testo a sinistra (~40%); a destra (~55%) una traccia reale con le annotazioni a margine; nota in basso. La pipeline della Slide 43 in miniatura, con la tappa 1 accesa, in fondo alla colonna di testo.

**Testo**:
- Titolo: *Chi giudica: una persona sola, e le tracce a mano*
- Punti:
  1. **Una persona sola**: *nel caso il compito sia di dominio, l'esperto di quel dominio: decide lei che cosa è una risposta giusta. Non un comitato: un comitato non converge, e l'agente ha bisogno di un giudizio coerente. La persona può cambiare; il fatto che sia una no.*
  2. **Le tracce delle prime prove, lette a mano**: *nelle prime fasi di test l'agente viene usato da utenti di prova; ogni sessione lascia una traccia. L'esperto le apre e le legge, giro per giro, e per ciascuna dice se è andata bene e perché. Non un dashboard: la traccia. È lì che si vede la tool call sbagliata dietro la risposta giusta.*
- Nota in basso: *È il passo che tutti saltano perché sembra lento. È il più veloce: nelle prime trenta tracce si trovano già i cluster di fallimento della Slide 46.*

**Visual**: `slide44-traccia-annotata.svg` — la prima versione della traccia annotata; torna completa nella Slide 50.

**Prompt per schema SVG**:
> Una traccia disegnata come il riquadro-payload del 26, in verticale, con i tag di ruolo: `[user]`, `[assistant] → tool`, `[tool]`, `[assistant]`, per due turni; in testa, un'etichetta `sessione di prova · utente 7 · 2 set`. A margine destro, **annotazioni a mano** (stile penna, in un colore diverso da tutto il resto): accanto a una tool call, *"parametro sbagliato: 4471 invece di 004471"*; accanto a un `[tool]` lungo, *"12.000 token per una riga"*; accanto alla risposta finale, *"giusta, ma per caso"*; in fondo, il verdetto: *"FAIL"* con una riga di motivazione. In alto a sinistra, la persona (una sagoma) con l'etichetta `l'esperto di dominio`.
>
> **Elemento focale**: le annotazioni a margine, e il verdetto binario con la motivazione in fondo.

## Slide 45 — Il dataset di test: cento casi, per dimensioni

**Messaggio**: per rieseguire serve un insieme fisso di casi. Un centinaio bastano, si possono generare anche in modo sintetico ragionando per dimensioni, e vanno scritti mentre si progetta l'agente, non dopo.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso. Pipeline in miniatura con la tappa 2 accesa.

**Testo**:
- Titolo: *Il dataset di test: cento casi, per dimensioni*
- Punti:
  1. **Circa cento casi**: *abbastanza per vedere i cluster, pochi abbastanza da leggerli tutti a mano. Ogni caso: la richiesta dell'utente, il contesto che serve, e ciò che l'esperto considera un esito giusto.*
  2. **Anche sintetici, per dimensioni**: *si elencano le dimensioni del compito (tipo di richiesta, stato dell'ordine, tono del cliente, canale) e si combinano. Con l'ispirazione delle tracce originali (Slide 44) e con la competenza di dominio dell'esperto, si scrivono i casi sintetici: le dimensioni danno la copertura, le tracce vere danno il realismo. Vale in contesti semplici; in medicina o in legge un caso inventato è un caso falso.*
  3. **Insieme al design dell'agente**: *i casi si scrivono quando si decide che cosa l'agente deve fare, non quando è finito: definire l'esito giusto è già progettare. Un dataset scritto dopo misura ciò che l'agente fa, non ciò che dovrebbe fare.*
- Nota in basso: *Il dataset è dell'esperto di dominio: è la sua definizione di "giusto", scritta in cento esempi. Il team dell'agente lo esegue.*

**Visual**: `slide45-dataset-dimensioni.svg`.

**Prompt per schema SVG**:
> **A sinistra**, una griglia di dimensioni: tre righe etichettate `tipo di richiesta` (`stato ordine · rimborso · reclamo · altro`), `stato dell'ordine` (`in consegna · consegnato · smarrito · non trovato`), `tono del cliente` (`neutro · urgente · arrabbiato`). In ingresso alla griglia, da un'icona `tracce di prova`, una freccia etichettata *ispirano i casi*. Da una cella per riga partono tre linee che convergono in un **caso** generato, a destra.
>
> **Al centro**, il caso, disegnato come una scheda: `#037 · rimborso · ordine smarrito · cliente arrabbiato` con dentro la richiesta (*"Terza consegna in ritardo, voglio i soldi indietro"*) e sotto, in un riquadro a parte etichettato `esito giusto (l'esperto)`: *"verifica l'ordine, apre un ticket, non promette rimborsi, risponde con un contatto diretto"*.
>
> **A destra**, la pila dei cento casi (schede impilate, `#001 … #100`) con l'etichetta `~100: leggibili tutti a mano`.
>
> Sotto, una riga: `4 × 4 × 3 = 48 combinazioni → si scelgono le ~100 che contano, alcune a mano, altre generate`.
>
> **Elemento focale**: la scheda del caso con i due riquadri, richiesta ed esito giusto.

## Slide 46 — Clusterizzare i fallimenti, e risalire alla leva

**Messaggio**: i fallimenti si raggruppano per tipo finché le categorie non finiscono; già al primo giro ne emergono di evidenti, e tipicamente un cluster è legato a una leva. I più frequenti sono spesso i più facili da correggere.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): dai fallimenti sparsi ai cluster, e da ogni cluster la leva; nota in basso. Pipeline in miniatura con la tappa 3 accesa.

**Testo**:
- Titolo: *Clusterizzare i fallimenti, e risalire alla leva*
- Punti:
  1. **Si raggruppano per tipo**: *si rileggono i casi falliti e si dà un nome a ciò che è andato storto: "parametro sbagliato", "promette il rimborso", "non trova il documento". Già al primo giro i cluster evidenti ci sono; si continua finché non emergono categorie nuove.*
  2. **Tipicamente un cluster è legato a una leva**: *un cluster di regole ignorate punta al prompt; uno di fatti sbagliati alla KB; uno di chiamate errate al tool; uno di vincoli persi a metà sessione all'harness. Ciò che resta dopo tutto questo punta al modello.*
  3. **I frequenti sono spesso i facili**: *le categorie più numerose, molte volte, si correggono specificando meglio una riga nel system prompt o nella descrizione di un tool. Si parte da lì: il guadagno maggiore al costo minore.*
- Nota in basso: *È il passo che trasforma "non funziona" in una lista di cose da fare, ordinata. Ed è quello che va rifatto ogni volta che il dataset cresce (Slide 49).*

**Visual**: `slide46-cluster-leve.svg`.

**Prompt per schema SVG**:
> **A sinistra**, i fallimenti sparsi: una trentina di punti disordinati, ognuno con un'etichetta brevissima (`"4471 invece di 004471"`, `"promette rimborso"`, `"non cita il listino"`, `"loop di 12 chiamate"`, …). **Al centro**, una freccia `si raggruppano`, e gli stessi punti riordinati in cinque gruppi di dimensione diversa, con un nome e un conteggio: `regola ignorata · 11`, `parametro sbagliato · 7`, `fatto mancante · 5`, `vincolo perso a metà sessione · 3`, `altro · 2`. **A destra**, la scala delle cinque leve della Slide 40 in miniatura, e da ogni cluster una freccia verso una leva: `regola ignorata → Prompt`, `parametro sbagliato → Tool`, `fatto mancante → Knowledge base`, `vincolo perso → Harness`, `altro → Modello` (tratteggiata). Il cluster più grande (`regola ignorata · 11`) e la sua freccia verso `Prompt` sono in evidenza, con l'etichetta *il più frequente, e il più facile*.
>
> **Elemento focale**: il passaggio da punti sparsi a gruppi contati, e le frecce verso le leve.

## Slide 47 — Checker deterministici, poi il giudice

**Messaggio**: prima si automatizza ciò che è verificabile con codice; solo dopo, per ciò che non lo è, si costruisce un giudice-modello, e lo si valida contro l'esperto prima di fidarsi.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): le due vie, in ordine; nota in basso. Pipeline in miniatura con le tappe 4 e 5 accese.

**Testo**:
- Titolo: *Checker deterministici, poi il giudice*
- Punti:
  1. **Prima i checker**: *il prima possibile, per ogni cluster che lo permette, un pezzo di codice che dice pass o fail: la tool call ha il parametro a sei cifre? La risposta contiene la parola "rimborso"? Il ticket è stato aperto? Deterministico, gratis, ripetibile. Anche scritto con l'aiuto dell'AI.*
  2. **Poi il giudice**: *per ciò che un checker non può vedere (il tono, la pertinenza, "ha risposto alla domanda vera?") si costruisce un LLM-as-a-judge: un modello con un prompt che dà pass o fail su una traccia.*
  3. **Validato, non creduto**: *il giudice si valida statisticamente: si prendono le tracce già giudicate dall'esperto, si confrontano con i suoi verdetti, e si misura quanto concorda. Se non concorda abbastanza, si corregge il prompt del giudice, non si abbassa l'asticella.*
- Nota in basso: *L'ordine conta: un giudice costa una chiamata per caso ed è meno affidabile di un `if`. Si usa solo dove l'`if` non arriva. Ed è il punto in cui i due ruoli si incontrano: il team scrive il giudice, l'esperto lo valida.*

**Visual**: `slide47-checker-giudice.svg`.

**Prompt per schema SVG**:
> Una traccia (la scheda di un caso, come nella Slide 45) entra da sinistra e si biforca in **due vie in sequenza**, una sopra l'altra.
>
> **Via 1, `checker deterministico`**: un blocco di codice in monospaziato con tre righe (`assert len(id_ordine) == 6`, `assert "rimborso" not in risposta`, `assert ticket_aperto`) e in uscita un verdetto `PASS / FAIL` con l'etichetta *gratis, ripetibile, esatto*. Accanto: *copre i cluster verificabili*.
>
> **Via 2, `LLM-as-a-judge`**: un blocco `modello giudice` con un prompt abbreviato (*"Data la traccia, la risposta riconosce il fatto senza giustificarsi? pass/fail e motivo"*) e in uscita `PASS / FAIL`. Accanto: *copre ciò che il codice non vede*. Sotto questa via, il **riquadro di validazione**: due colonne affiancate, `verdetti dell'esperto` e `verdetti del giudice`, sulle stesse venti tracce, con le righe concordi in un colore e le discordi in evidenza; sotto, `concordanza: 17/20`, e una freccia di ritorno verso il prompt del giudice etichettata *se non basta: si corregge il giudice*.
>
> **Elemento focale**: il riquadro di validazione, con le righe discordi in evidenza.

> Note del relatore: dettagli della validazione (quante etichette, metriche separate per veri positivi e veri negativi, soglie) restano fuori slide.

## Slide 48 — Gli errori nei tool deterministici e nei tool non deterministici

**Messaggio**: i fallimenti sui tool si separano per natura del tool: un'API applicativa fallisce perché è stata chiamata male; un tool che è a sua volta AI, come la RAG, fallisce in due punti diversi, che si misurano separatamente.

**Layout**: titolo in alto; i due punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso. Pipeline in miniatura con la tappa 3 accesa (è un approfondimento dei cluster).

**Testo**:
- Titolo: *Gli errori nei tool deterministici e nei tool non deterministici*
- Punti:
  1. **Tool deterministici**: *un'API applicativa fa sempre la stessa cosa: se fallisce, il modello l'ha chiamata male o non ha capito a che cosa serve. Il fix è nella descrizione o nello schema del tool (la leva Tool), e il checker lo verifica.*
  2. **Tool che sono a loro volta AI**: *l'esempio classico è la RAG: una ricerca che restituisce documenti, e una sintesi. Un fallimento si scompone in due domande diverse: il retrieval ha trovato i documenti giusti, e li ha messi in cima? E la sintesi li ha usati bene? Si misurano separatamente, perché si correggono in posti diversi.*
- Nota in basso: *Separare i due tipi serve a non correggere nel posto sbagliato: un retrieval che sbaglia non si aggiusta nel prompt della sintesi.*

**Visual**: `slide48-errori-tool.svg`.

**Prompt per schema SVG**:
> Due riquadri affiancati. **`tool deterministico`** (`cerca_ordine`): freccia in ingresso `chiamata`, freccia in uscita `risultato, sempre lo stesso`; sotto, i due modi di fallire: *parametri sbagliati* · *tool scelto male*, con la freccia verso la leva `Tool` e l'etichetta *lo verifica un checker*. **`tool non deterministico`** (`cerca_documenti` = RAG): dentro, due stadi in fila, `retrieval / ranking` e `sintesi`, ognuno con la propria domanda di valutazione sotto (*ha trovato i documenti giusti, in cima?* · *li ha usati bene?*) e il proprio strumento (*confronto con i documenti attesi* · *il giudice*), e due frecce verso due leve diverse: `KB` per il retrieval, `Prompt` per la sintesi.
>
> **Elemento focale**: i due stadi del tool AI con le due domande separate.

## Slide 49 — In produzione: il ciclo che non finisce

**Messaggio**: il processo, una volta costruito, non si chiude: le tracce di produzione lo alimentano ogni mese, e ogni modifica all'agente lo fa ripartire da capo. È un'attività con un costo fisso e un responsabile.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): l'anello; nota in basso. Pipeline in miniatura con la tappa 6 accesa e la freccia di ritorno in evidenza.

**Testo**:
- Titolo: *In produzione: il ciclo che non finisce*
- Punti:
  1. **Le tracce arrivano da sole**: *in produzione ogni sessione lascia una traccia. Se ne campionano circa cento al mese e si rileggono a mano, con l'esperto: come nella Slide 44, ma per sempre.*
  2. **Il dataset cresce**: *i fallimenti nuovi diventano casi nuovi; i cluster si aggiornano, e con loro i checker e il giudice. Il processo delle Slide 44–47 si ripete, incrementale.*
  3. **A ogni modifica, si rigira tutto**: *un prompt cambiato, un modello nuovo, un tool aggiunto: la catena si riesegue per intero, per trovare le regressioni e per sapere se un fix ha funzionato davvero. Senza, si torna al vibe eval della Slide 42.*
- Nota in basso: *Non è un progetto: è un'attività che ha un costo fisso mensile e un responsabile nel team dell'agente. Un agente senza questo ciclo peggiora in silenzio, perché il mondo intorno cambia e nessuno lo misura.*

**Visual**: `slide49-ciclo-produzione.svg`.

**Prompt per schema SVG**:
> Un anello con quattro tappe, in senso orario: `tracce di produzione` → `~100 al mese lette a mano (con l'esperto)` → `dataset e cluster aggiornati` → `checker e giudice rieseguiti` → torna all'inizio. Sull'anello, tre tacche esterne etichettate `modifica al prompt`, `cambio di modello`, `tool nuovo`, ognuna con una freccia che entra nella tappa `rieseguiti`: *ogni modifica rigira la catena*. In uscita dall'anello, due etichette: `regressioni trovate` e `fix confermati`. Al centro dell'anello, un calendario stilizzato con `ogni mese` e un'icona di persona con `un responsabile`.
>
> **Elemento focale**: le tre tacche delle modifiche che entrano nell'anello.

## Slide 50 — Tre usi del logging

**Messaggio**: le tracce servono a tre cose diverse, a tre persone diverse: capire perché ha fatto quella chiamata, confrontare traiettorie invece di risposte, e addestrare. La terza chiude il cerchio con il 26: le traiettorie di oggi sono i dati di domani.

**Layout**: titolo in alto; il visual a tutta larghezza (~60%): la stessa traccia della Slide 44, ora completa, letta da tre lati; le tre colonne di testo sotto; nota in basso. Chiude la sezione: niente pipeline in miniatura.

**Testo**:
- Titolo: *Tre usi del logging*
- Le tre colonne:
  1. **Debug**: *"perché ha fatto quella chiamata?" La risposta sta nella finestra che il modello aveva davanti a quel giro: la traccia la conserva. Senza, si tira a indovinare.*
  2. **Eval**: *si confrontano traiettorie, non output: due versioni dell'agente sullo stesso caso, giro per giro. Una risposta finale identica può venire da due percorsi molto diversi, uno dei quali fragile.*
  3. **Training set per un RL privato**: *nel 26: il modello impara a volere i tool dalle traiettorie premiate. Le tracce di produzione, con il verdetto dell'esperto o del checker, sono esattamente quel materiale: i task veri, con un modo per dire se sono riusciti. È l'ultima leva, e le tracce ne sono la materia prima.*
- Nota in basso: *Ed è il motivo per cui la traiettoria è l'artefatto primario dell'agente, non la risposta: la risposta serve all'utente una volta; la traiettoria serve a chi lo costruisce, per sempre.*

**Visual**: `slide50-traccia-tre-usi.svg` — la traccia della Slide 44, completa e annotata giro per giro, con tre lettori.

**Prompt per schema SVG**:
> Al centro, la traccia della Slide 44, **completa**: tre turni con i tag di ruolo, ogni giro numerato (`giro 1` … `giro 7`), e per ogni giro, a margine, una riga di annotazione (parametri, token, esito). In fondo, il verdetto `PASS` con motivazione.
>
> Intorno, tre lettori, ognuno con una lente puntata su una parte diversa della traccia: **`debug`** (a sinistra, in alto) con la lente sul `giro 3` e il fumetto *"aveva 12.000 token di export davanti: per questo ha scelto male"*; **`eval`** (a destra) con due copie sottili della stessa traccia affiancate, `versione A` e `versione B`, e la lente sul punto in cui divergono: *"stessa risposta, percorsi diversi"*; **`training`** (in basso) con una freccia che dalla traccia intera, col suo verdetto, va verso un blocco `dataset di traiettorie premiate`, e da lì verso un blocco `modello`, con l'etichetta *le traiettorie di oggi sono i dati di domani*, disegnata come la reward che scorre all'indietro nella slide 38 del 26.
>
> **Elemento focale**: le tre lenti sulla stessa traccia.

> Note del relatore: a settembre 2026 le tracce di produzione si usano come insieme di task con verificatore (RFT e simili), non come traiettorie da imitare grezze; serve un grader, e il rischio è il reward hacking. Fonti nel file di ricerca in scratchpad.
