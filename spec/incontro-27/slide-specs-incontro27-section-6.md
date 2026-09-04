# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 6 — Orchestrazione: quando un agente non basta**
**Obiettivo di apprendimento**: il partecipante sa distinguere un workflow da un sistema multi-agente, conosce i tre pattern con il problema di harness che li motiva, sa perché diffidare degli swarm, e sa riconoscere i tre pattern dentro un sistema reale.
**Messaggio chiave (takeaway)**: Un secondo agente si aggiunge quando il contesto del primo non basta, non prima. E un agente, per un altro agente, è un tool.
**Budget**: ~17 min, 7 slide + separatore. Ripartizione: criterio 1, pattern 3, swarm 1, esempio 2.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec6.html` | Separatore — Sezione 6: Orchestrazione |
| `slides/slide51-workflow-vs-agente.html` | Slide 51 — Quando un agente non basta: il criterio |
| `slides/slide52-subagente-tool.html` | Slide 52 — Pattern 1: il subagente come tool |
| `slides/slide53-worker-paralleli.html` | Slide 53 — Pattern 2: worker paralleli |
| `slides/slide54-reviewer.html` | Slide 54 — Pattern 3: evaluator / reviewer |
| `slides/slide55-swarm.html` | Slide 55 — Swarm e multi-agente conversazionale: un giudizio |
| `slides/slide56-deep-research.html` | Slide 56 — Deep research: com'è fatto davvero |
| `slides/slide57-deep-research-pattern.html` | Slide 57 — Deep research: i tre pattern, colorati |

---

> **Filo della sezione.** Si parte dal criterio e dalla distinzione workflow/agente; i tre pattern uno per slide con la stessa figura di base (un esoscheletro padre, uno o più figli più piccoli, le finestre a strati che mostrano che cosa entra in ciascuno); lo swarm come controesempio; poi l'esempio finale in due tempi: il diagramma unico (Slide 56), poi colorato con i tre pattern (Slide 57, stesso viewBox, fragment). Ogni pattern è motivato da un problema di harness già visto: contesto (sezione 4), tempo (Slide 17), giudizio (sezione 5).
>
> **L'esempio finale è Anthropic** (deciso in intervista): il post "How we built our multi-agent research system" (13 giugno 2025) è l'unico che documenta ruoli e numeri (lead researcher, 3–10+ subagenti paralleli con contesto proprio, citation agent; ~90% di miglioramento rispetto a un agente singolo; ~15× i token di una chat; fino a −90% di tempo). Google non documenta Gemini Deep Research come multi-agente a ruoli; in slide si dice che verosimilmente gli altri sistemi lavorano allo stesso modo. Nel sistema di Anthropic il lead usa un modello più grande e i subagenti uno più economico: lo si dice, a sfumare "stesso modello".
>
> **Mini-mappa**: in questa sezione la mappa non si accende su una zona: si **duplica** (due esoscheletri, un padre e un figlio), a dire che siamo fuori dalla figura singola.

---

## Slide 51 — Quando un agente non basta: il criterio

**Messaggio**: un secondo agente si aggiunge quando il contesto del primo non basta più, non prima. E un `if` nell'harness non è un secondo agente: è un workflow, e va chiamato con il suo nome.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): workflow e agente affiancati; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 6 · ORCHESTRAZIONE*
- Titolo: *Quando un agente non basta: il criterio*
- Punti:
  1. **Il criterio**: *un secondo agente si aggiunge quando il contesto del primo non basta più: troppi risultati da tenere, troppi tool da esporre insieme, un giudizio che il contesto che ha lavorato non può dare. Non prima. Ogni pattern che vedremo è motivato da un problema di harness già visto.*
  2. **Un `if` non è un agente**: *se l'harness decide con una regola (chaining: prima A poi B; routing: se la richiesta è di tipo X va ad A, altrimenti a B) e chiama il modello in sequenza, è un workflow: deterministico, prevedibile, economico. Va usato ogni volta che basta.*
  3. **Un agente è chi decide**: *si ha un secondo agente quando è un modello, non una regola, a decidere quando e se chiamarlo, con che compito, e a leggere ciò che torna. Cioè: quando il secondo agente è un tool del primo.*
- Nota in basso: *La prima domanda, sempre: "lo può fare un `if`?" Se sì, non serve un agente. Il multi-agente costa di più, è più lento e si spiega peggio: si giustifica solo con il contesto.*

**Visual**: `slide51-workflow-vs-agente.svg`.

**Prompt per schema SVG**:
> Due pannelli affiancati, divisi da un filo verticale.
>
> **Pannello sinistro — «WORKFLOW»**: l'harness disegnato come un flusso deterministico: un rombo `tipo di richiesta?` con due rami, ciascuno verso un blocco `chiamata al modello` con un prompt diverso (`prompt A: rimborsi`, `prompt B: reclami`), poi un blocco `unisci` e l'uscita. Etichetta: *l'`if` è dell'harness: decide una regola, il modello esegue*. Sotto: `chaining · routing · deterministico`.
>
> **Pannello destro — «AGENTE + SUBAGENTE»**: l'esoscheletro della mappa in miniatura (l'agente padre), che nella lista dei tool ha, oltre a `cerca_ordine`, un tool `ricerca_approfondita` disegnato come un **secondo esoscheletro più piccolo**, con la propria finestra e i propri tool. Una pill burgundy dal padre: `→ ricerca_approfondita("…")`, e una riga `[tool]` di ritorno con un paragrafo. Etichetta: *è il modello a decidere se, quando e con che compito*. Sotto: `il secondo agente è un tool del primo`.
>
> **Elemento focale**: il rombo a sinistra (una regola) contro la pill burgundy a destra (una decisione del modello).

## Slide 52 — Pattern 1: il subagente come tool

**Messaggio**: il primo pattern risolve un problema di contesto: venti giri di ricerca sporcano la finestra del padre, allora si fanno in una finestra separata, e al padre torna un paragrafo. Il contratto è quello del tool calling: un agente è un tool per un altro agente.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Pattern 1: il subagente come tool*
- Punti:
  1. **La motivazione: isolamento del contesto**: *una ricerca fatta bene sono venti giri, venti risultati, decine di migliaia di token. Se li fa il padre, la sua finestra è piena prima di aver iniziato il lavoro vero. Se li fa un figlio, nella finestra del padre entra solo un paragrafo.*
  2. **Stesso contratto del tool calling**: *il figlio si dichiara come un tool: nome, descrizione, un parametro (il compito). Il padre lo chiama con un `tool_use`, aspetta, riceve un `tool_result`. Non sa e non deve sapere quanti giri ha fatto il figlio.*
  3. **Il figlio è un harness completo**: *ha la propria finestra, i propri tool (spesso meno del padre: è anche un confine di fiducia, Slide 19), il proprio system prompt. Quando finisce, la sua finestra muore: resta solo ciò che ha riportato.*
- Nota in basso: *È il pattern che copre quasi tutti i casi reali. Gli altri due sono sue varianti: molti figli insieme, o un figlio che giudica.*

**Visual**: `slide52-subagente-tool.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la finestra a strati del padre, corta: prefisso (con nella lista dei tool la definizione `ricerca(compito)`, in evidenza), storia, una pill `→ ricerca("normativa resi 2026")`, e sotto una riga `[tool]` in teal di **tre righe**: il paragrafo di risposta. Etichetta: *nel padre: una richiesta e un paragrafo*.
>
> **A destra**, collegata alla pill da una freccia, la finestra del figlio: un esoscheletro più piccolo con la propria finestra **molto alta**: il proprio system prompt (`sei un ricercatore…`), i propri tool (`cerca_web`, `leggi_pagina`: meno del padre), e una lunga sequenza di giri: `→ cerca_web` / `[tool] 10 risultati` / `→ leggi_pagina` / `[tool] 4.000 token` / … per venti giri, abbreviati con `⋯`, e in fondo la risposta finale di tre righe. Una freccia dal fondo della finestra del figlio torna alla riga `[tool]` del padre, etichettata `solo questo torna indietro`. Sotto la finestra del figlio, un'etichetta: `~60.000 token, che il padre non vede mai`; e un piccolo taglio: *poi la finestra del figlio muore*.
>
> **Elemento focale**: il contrasto di altezza fra le due finestre, e la freccia sottile che riporta solo il paragrafo.

## Slide 53 — Pattern 2: worker paralleli

**Messaggio**: quando il compito si spezza in parti indipendenti, più figli lavorano insieme e il tempo si divide. Vale solo se le parti sono davvero indipendenti, e il punto fragile è rimettere insieme i pezzi.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Pattern 2: worker paralleli*
- Punti:
  1. **La motivazione: il tempo**: *tre ricerche da venti giri l'una, in sequenza, sono un'ora. Tre figli insieme, venti minuti. È la Slide 17 (le chiamate parallele) applicata agli agenti: il padre emette tre `tool_use` nello stesso giro, l'harness lancia tre figli.*
  2. **Solo se indipendenti**: *se il secondo figlio ha bisogno del risultato del primo, il parallelo è un'illusione: aspetta, o lavora su un'ipotesi. Il padre deve decomporre il compito in parti che non si parlano.*
  3. **Il merge è il punto fragile**: *tre paragrafi tornano insieme, e possono contraddirsi, sovrapporsi, usare fonti diverse per lo stesso fatto. Rimetterli insieme è un lavoro del padre, e spesso è il passaggio in cui si sbaglia.*
- Nota in basso: *Regola pratica: prima si prova con un figlio solo (pattern 1). Si passa al parallelo quando il tempo è il problema, e si è capito come si decompone il compito.*

**Visual**: `slide53-worker-paralleli.svg`.

**Prompt per schema SVG**:
> **In alto**, la finestra del padre con una risposta che contiene **tre pill affiancate** nello stesso giro: `→ ricerca("normativa resi")` · `→ ricerca("prassi dei concorrenti")` · `→ ricerca("reclami ricevuti")`.
>
> **Al centro**, tre finestre-figlio affiancate, ognuna un esoscheletro piccolo con la propria sequenza di giri (altezze diverse: i tre figli non finiscono insieme), con una linea del tempo verticale a sinistra che mostra la durata: `20 min` per la più lunga, contro una barra tratteggiata a lato `in sequenza: 60 min`.
>
> **In basso**, i tre `[tool]` di ritorno entrano nel padre in un unico messaggio, e sotto un blocco `merge` disegnato con un bordo tratteggiato e un piccolo `⚠`: dentro, tre frammenti di testo con due frasi sottolineate che si contraddicono (*"30 giorni"* / *"14 giorni"*). Etichetta: *il punto fragile*.
>
> Un cartello fra i figli: `indipendenti: nessuna freccia fra loro`.
>
> **Elemento focale**: il blocco `merge` con la contraddizione, e la barra del tempo.

## Slide 54 — Pattern 3: evaluator / reviewer

**Messaggio**: chi ha fatto un lavoro lo giudica male, perché ha davanti tutto il percorso che l'ha portato lì. Un secondo agente con la finestra pulita giudica meglio; e per giudicare legge la traiettoria, non solo il risultato.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%); nota in basso.

**Testo**:
- Titolo: *Pattern 3: evaluator / reviewer*
- Punti:
  1. **La motivazione: un contesto pulito giudica meglio**: *il lavoratore ha in finestra venti giri di tentativi, false partenze e risultati parziali: quando rilegge il proprio output, lo legge con quegli occhi. Il reviewer riceve solo il compito e il risultato, e vede ciò che il lavoratore non vede più.*
  2. **Il reviewer legge la traiettoria**: *non solo l'output: la traccia (sezione 5). "Ha aperto il ticket prima o dopo aver risposto al cliente? Ha verificato l'ordine?" Le domande del checker e del giudice, fatte da un agente dentro il loop, prima che il risultato esca.*
  3. **Chiude un ciclo, con un limite**: *il verdetto torna al lavoratore, che corregge e riprova: uno, due giri. Non di più: un reviewer che boccia all'infinito è un loop, e un reviewer che promuove sempre è decorazione. Il numero di giri lo fissa l'harness.*
- Nota in basso: *È l'LLM-as-a-judge della Slide 47 messo in linea: stesso prompt, stessa validazione, un momento diverso: prima della consegna invece che dopo.*

**Visual**: `slide54-reviewer.svg`.

**Prompt per schema SVG**:
> **A sinistra**, la finestra del `lavoratore`: alta, piena di giri (tentativi, `[tool]`, correzioni), con in fondo il `risultato`. **A destra**, la finestra del `reviewer`: corta e pulita: il proprio system prompt (`sei un revisore: verifica che…`), il `compito`, il `risultato` del lavoratore e, sotto, la **traccia** del lavoratore in forma compatta (etichetta: *legge la traiettoria, non solo l'output*). Dal reviewer esce un `verdetto: rivedi · motivo: il ticket è stato aperto dopo la risposta`, che torna con una freccia nella finestra del lavoratore come riga `[tool]`. Un contatore sulla freccia: `giro 1 di 2`.
>
> Sopra le due finestre, un'etichetta che le confronta: *stesso modello, due contesti: uno sporco, uno pulito*.
>
> **Elemento focale**: la differenza di altezza e "pulizia" fra le due finestre, e la traccia dentro il reviewer.

## Slide 55 — Swarm e multi-agente conversazionale: un giudizio

**Messaggio**: le architetture in cui molti agenti "si parlano" tra pari, senza un padre che decide, sono instabili, costose e difficili da spiegare; quasi sempre un padre con dei figli-tool fa lo stesso lavoro meglio.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): confronto; blocco nero centrato in fondo.

**Testo**:
- Titolo: *Swarm e multi-agente conversazionale: un giudizio*
- Punti:
  1. **Che cosa sono**: *N agenti con ruoli ("il ricercatore", "il critico", "il redattore") che si scambiano messaggi in una conversazione condivisa, senza un padre: chi parla dopo lo decide il turno, o un agente moderatore.*
  2. **Perché non funzionano bene**: *instabili: due agenti possono rimpallarsi all'infinito, o convincersi a vicenda di una cosa sbagliata. Costosi: ogni messaggio entra nella finestra di tutti, e la finestra condivisa cresce come la peggiore delle Slide 31. Opachi: nessuna traiettoria singola da leggere, e il debug diventa una lettura di dialoghi.*
  3. **Quasi sempre sostituibili dal pattern 1**: *un padre che chiama figli-tool con compiti chiari fa lo stesso lavoro con contesti isolati, una traccia leggibile e un punto di decisione solo. La "conversazione fra agenti" era un modo di non progettare la decomposizione.*
- Blocco nero centrato: *Se non sai dire chi decide, non hai un'architettura: hai una chat.*

**Visual**: `slide55-swarm.svg`.

**Prompt per schema SVG**:
> Due pannelli affiancati. **A sinistra, `swarm`**: quattro esoscheletri piccoli disposti in cerchio, con frecce in tutte le direzioni fra loro (un groviglio), e al centro una finestra condivisa che cresce, disegnata alta e piena, etichettata `finestra condivisa: entra tutto, per tutti`. Su due frecce, un anello con `↻ ×12` (*si rimpallano*). Nessun nodo è in evidenza: *chi decide?*.
>
> **A destra, `orchestrator-workers` (pattern 1)**: un esoscheletro padre in alto, tre figli sotto collegati solo al padre con frecce verticali (`compito` in giù, `paragrafo` in su), nessuna freccia fra i figli; la finestra del padre corta. Etichetta: *un punto di decisione, contesti isolati, una traccia per figlio*.
>
> **Elemento focale**: il groviglio di frecce a sinistra contro le tre frecce verticali a destra.

## Slide 56 — Deep research: com'è fatto davvero

> Primo tempo di una figura a due tempi (fragment, `.visual.stack`): la Slide 57 sovrappone i colori dei pattern.

**Messaggio**: un sistema di ricerca approfondita reale, documentato da chi lo ha costruito: un lead che pianifica, subagenti paralleli con contesti isolati, un agente che verifica le citazioni. Tutti "agenti", tutti ruoli dell'harness.

**Layout**: titolo in alto; il diagramma a tutta larghezza (~70%); didascalia in basso.

**Testo**:
- Titolo: *Deep research: com'è fatto davvero*
- Didascalia: *Il sistema di ricerca di Anthropic, come lo descrive chi lo ha costruito (giugno 2025). Un lead pianifica e delega; i ricercatori lavorano in parallelo, ognuno nella propria finestra; un agente finale verifica le citazioni. Circa quindici volte i token di una chat, e un miglioramento di circa il 90% rispetto a un agente solo. Verosimilmente gli altri sistemi di deep research lavorano allo stesso modo; questo è l'unico documentato con i ruoli e i numeri.*

**Visual**: `slide56-deep-research.svg` (tempo 1).

**Prompt per schema SVG**:
> Diagramma verticale, dall'alto verso il basso, con esoscheletri in miniatura per ogni agente.
>
> 1. In cima, `l'utente`: *"Quali sono le opzioni per…?"*.
> 2. **`lead researcher`**: un esoscheletro con etichetta *pianifica la ricerca, decide quanti ricercatori e con quale compito, poi assembla*. Accanto: *un modello più grande*. Dalla sua finestra partono N pill `→ ricerca(compito_i)` in parallelo.
> 3. **`ricercatori`**: da 3 a 10 esoscheletri piccoli affiancati (disegnarne 4 e un `⋯`), ognuno con la propria finestra alta piena di giri (`cerca_web`, `leggi`), tool ridotti, e in fondo un paragrafo di risultato. Accanto: *un modello più economico, contesto proprio: ~15× i token di una chat, in tutto*. Nessuna freccia fra i ricercatori.
> 4. I paragrafi risalgono nel lead, che ha una seconda fase: *legge, trova i buchi, rilancia* (una freccia curva che torna ai ricercatori con `→ ricerca(compito nuovo)`), poi `bozza del report`.
> 5. **`citation agent`**: un esoscheletro piccolo in fondo che riceve la bozza e le fonti, e restituisce `report con citazioni verificate`.
> 6. In fondo, l'utente riceve il report.
>
> A destra, una scala verticale del tempo con due barre: `in sequenza` (lunga) e `così` (corta, `−90%`).
>
> **Elemento focale**: la fila dei ricercatori paralleli con le finestre alte, e il lead con la finestra corta sopra.

> Fonte: Anthropic Engineering, "How we built our multi-agent research system", 13 giugno 2025 (URL nel file di ricerca in scratchpad); da citare nelle note del relatore.

## Slide 57 — Deep research: i tre pattern, colorati

> Secondo tempo della Slide 56: stesso viewBox, si sovrappongono le zone colorate; i tre punti compaiono con lo stesso fragment.

**Messaggio**: nello stesso diagramma si riconoscono i tre pattern, e niente altro. Gli "agenti" sono ruoli dell'harness: stesso tipo di macchina, contesti e tool diversi.

**Layout**: come la Slide 56; i tre punti di testo sotto la figura, come tre colonne brevi; blocco nero centrato in fondo.

**Testo**:
- Titolo: *Deep research: i tre pattern, colorati*
- Le tre colonne:
  1. **Pattern 1, il subagente come tool**: *ogni ricercatore è un tool del lead: riceve un compito, riporta un paragrafo, e la sua finestra muore. Il rilancio è lo stesso pattern, una seconda volta.*
  2. **Pattern 2, i worker paralleli**: *i ricercatori partono insieme, nello stesso giro del lead, e non si parlano. Il merge è il lavoro del lead: leggere i paragrafi, trovare i buchi, assemblare.*
  3. **Pattern 3, il reviewer**: *il citation agent non ha fatto la ricerca: riceve bozza e fonti con una finestra pulita, e verifica. È il giudice messo in linea.*
- Blocco nero centrato: *Gli "agenti" sono ruoli dell'harness: stesso tipo di macchina, con finestre e tool diversi. La differenza è tutta in ciò che ogni finestra contiene.*

**Visual**: `slide57-deep-research-pattern.svg` (tempo 2, stesso viewBox della Slide 56).

**Prompt per schema SVG**:
> La figura della Slide 56, identica, con sopra **tre zone colorate traslucide** e un'etichetta ciascuna, in tre colori distinti:
> - **pattern 1** (`il subagente come tool`): una zona che abbraccia la coppia lead → un singolo ricercatore → paragrafo di ritorno, e una seconda zona più piccola sulla freccia di rilancio (`di nuovo`);
> - **pattern 2** (`worker paralleli`): una zona orizzontale che abbraccia tutta la fila dei ricercatori, con la scritta `nessuna freccia fra loro`, e un cerchietto sul blocco del lead dove assembla: `il merge`;
> - **pattern 3** (`evaluator / reviewer`): una zona intorno al citation agent, con la scritta `finestra pulita`.
>
> Nessuna parte del diagramma resta senza colore, tranne l'utente in cima e in fondo: è il messaggio, *tre pattern, e nient'altro*.
>
> **Elemento focale**: le tre zone che coprono tutto il diagramma.
