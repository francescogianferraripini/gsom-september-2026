# Specifica slide — PC AI 27: Agentic AI — agenti e pattern di orchestrazione, tool call, protocollo MCP
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 7 — L'offerta di harness**
**Obiettivo di apprendimento**: il partecipante sa collocare i prodotti di mercato sulla mappa dell'harness (che cosa espongono, per chi, e soprattutto chi ospita harness e sandbox), sa rileggere la formula con tutti i termini aperti e sa qual è l'unico termine ancora chiuso.
**Messaggio chiave (takeaway)**: Sono tutti lo stesso harness con superfici diverse, e gli stessi modelli. Ciò che li distingue è chi ospita, e il software installato: e dietro i tool, la conoscenza.
**Budget**: ~14 min, 6 slide + separatore. Ripartizione: Anthropic 2, open 2, formula 1, cliffhanger 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec7.html` | Separatore — Sezione 7: L'offerta di harness |
| `slides/slide58-superfici-anthropic.html` | Slide 58 — L'offerta Anthropic: stesso harness, superfici diverse |
| `slides/slide59-tabella-anthropic.html` | Slide 59 — L'offerta Anthropic: che cosa espongono |
| `slides/slide60-tre-filosofie.html` | Slide 60 — L'offerta open: tre filosofie |
| `slides/slide61-tabella-open.html` | Slide 61 — L'offerta open: sulle stesse colonne |
| `slides/slide62-formula-riletta.html` | Slide 62 — La formula, riletta |
| `slides/slide63-dietro-i-tool.html` | Slide 63 — Dietro i tool, la conoscenza |

---

> **Filo della sezione.** La mappa si riaccende tutta e diventa la griglia di confronto dei prodotti (le righe delle tabelle sono le zone della mappa); poi la formula della Slide 3 con quattro termini accesi; l'ultima slide è il blocco nero: `KB` è l'unico termine non ancora aperto, e il 28 è tutto lì.
>
> **Dati verificati** (4 set 2026): tutte le celle delle tabelle vengono dalla matrice in `docs/ricerche-27/research-offering-matrix.md` (49 fonti ufficiali: docs Anthropic, Claude Code, Managed Agents, Help Center; docs smolagents, LangChain/LangGraph, Agno). Le fonti vanno riportate nelle note del relatore. Le celle marcate non verificabili nella matrice sono state rese in forma prudente ("come chat", "nessuno documentato").
>
> **Liste**: i cinque prodotti Anthropic e i tre framework del brief, più Managed Agents come sesta colonna (è l'unico caso in cui harness e sandbox sono entrambi ospitati e si chiama un'API). Claude in Chrome e in Slack restano nelle note del relatore.

---

## Slide 58 — L'offerta Anthropic: stesso harness, superfici diverse

**Messaggio**: i prodotti Anthropic sono lo stesso harness (il loop di Claude Code) sugli stessi modelli, offerto su superfici diverse e con un'unica variabile che cambia davvero: chi ospita l'harness e il sandbox.

**Layout**: titolo in alto; visual a tutta larghezza (~60%): la mappa delle superfici; i due punti sotto; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 7 · L'OFFERTA DI HARNESS*
- Titolo: *L'offerta Anthropic: stesso harness, superfici diverse*
- Punti:
  1. **Cinque superfici, un harness**: *Claude.ai (la chat nel browser), Claude Desktop (l'app, con i server MCP locali), Claude Cowork (il lavoro d'ufficio senza codice), Claude Code (il terminale e l'IDE), l'Agent SDK (lo stesso loop di Claude Code come libreria, nel tuo processo). Il loop è lo stesso; cambia chi lo usa e da dove. E sotto girano gli stessi modelli: la differenza fra i prodotti non è mai il modello, è l'harness e chi lo ospita.*
  2. **La variabile che conta: chi ospita**: *nella chat e in Cowork ospita Anthropic, sandbox compreso; su Desktop e in Claude Code l'harness gira sul tuo computer; con l'Agent SDK gira nella tua infrastruttura, e il sandbox lo porti tu. E c'è la sesta via: Managed Agents, dove Anthropic ospita harness e sandbox e tu chiami un'API.*
- Nota in basso: *Leggetela con la mappa della Slide 4: ogni prodotto è la stessa figura, con alcune zone che stanno da Anthropic e altre da voi. La tabella della prossima slide dice quali.*

**Visual**: `slide58-superfici-anthropic.svg`.

**Prompt per schema SVG**:
> Un asse orizzontale, `chi ospita l'harness`, da sinistra `Anthropic` a destra `tu`. Sei riquadri-prodotto disposti lungo l'asse, ognuno con il nome, un'icona di superficie e una riga:
> - `Claude.ai` (browser) — *chat; Anthropic ospita tutto*
> - `Claude Cowork` (desktop, web, mobile) — *lavoro d'ufficio; nel cloud Anthropic di default, in locale su desktop*
> - `Managed Agents` (API) — *harness e sandbox ospitati, tu chiami un'API* (riquadro con bordo tratteggiato: *e altri*)
> - `Claude Desktop` (app) — *chat + MCP locali; l'app sul tuo computer*
> - `Claude Code` (terminale, IDE) — *harness sul tuo computer, o nel cloud a scelta*
> - `Agent SDK` (libreria) — *il loop di Claude Code nel tuo processo: sandbox e hosting tuoi*
>
> Sotto tutti i riquadri, una fascia unica a due righe che li collega: `lo stesso loop agentico · gli stessi modelli`. Due etichette di gruppo sopra: `per chi usa` (Claude.ai, Cowork, Desktop) e `per chi costruisce` (Code, Agent SDK, Managed Agents).
>
> **Elemento focale**: l'asse `chi ospita` e la fascia comune sotto.

## Slide 59 — L'offerta Anthropic: che cosa espongono

**Messaggio**: la mappa dell'harness letta come griglia di confronto: per ogni prodotto, quale zona sta da Anthropic, quale da te, e che cosa espone di MCP, skill, memoria, observability, subagenti.

**Layout**: titolo in alto; la tabella occupa il corpo (~75%); nota in basso. Nessuna figura: la tabella è il visual (come la slide 52 del 26), classe `micro` se serve.

**Testo**:
- Titolo: *L'offerta Anthropic: che cosa espongono*
- Tabella (dati verificati su documentazione ufficiale al 4 settembre 2026):

| | Claude.ai | Claude Desktop | Claude Cowork | Claude Code | Agent SDK | Managed Agents |
|---|---|---|---|---|---|---|
| **Harness ospitato da** | Anthropic | tu (l'app) | Anthropic; locale a scelta | tu; cloud a scelta | tu (tua infra) | Anthropic |
| **Sandbox** | Anthropic | Anthropic (chat), VM locale (Cowork) | Anthropic; VM locale | sul tuo computer, opt-in; o cloud | **nessuno incluso**: lo porti tu | Anthropic, o self-hosted |
| **MCP** | solo server remoti | remoti + **locali** | remoti; locali solo in locale | remoti + locali; è anche server | remoti + locali + in-process | solo remoti (locali in anteprima) |
| **Skill** | sì | sì | sì | sì (`.claude/skills`) | sì (come Claude Code) | sì (API + repo) |
| **Memoria** | memoria di chat | come chat | solo se in cloud | `CLAUDE.md` + memoria automatica su file | file locali del container | memory store montato |
| **Observability** | Compliance API (enterprise) | come chat | Compliance API | OpenTelemetry, hooks, trascrizioni | OpenTelemetry (eredita) | event stream, webhook |
| **Subagenti** | no | via Cowork/Code | sì | sì (`.claude/agents`, max 20) | sì | sì (coordinator, 1 livello, max 20) |
| **Stato** | GA | GA | beta (web/mobile) | GA (web in anteprima) | libreria < 1.0 | beta pubblica |

- Nota in basso: *Le righe sono le zone della mappa. Due letture: scendendo, ogni prodotto è un harness completo; attraversando, la stessa zona cambia solo per chi la ospita. La riga da guardare prima di scegliere è "Sandbox": è quella che decide che cosa devi costruire tu.*

**Visual**: nessuno. In Fase 3 la tabella va verificata a schermo: otto righe per sette colonne a `micro` sono al limite; se sfora, si tolgono le righe **Skill** (tutti sì) e **Stato**, che vanno nelle note del relatore.

## Slide 60 — L'offerta open: tre filosofie

**Messaggio**: i framework open non sono prodotti: sono modi diversi di scrivere l'harness. Tre filosofie, verificate sulla loro documentazione: l'agente che agisce scrivendo codice, il loop che diventa un grafo, gli agenti con un runtime per esercirli.

**Layout**: titolo in alto; tre colonne che occupano il corpo (~65%), una per framework, ognuna con un mini-diagramma in testa e il testo sotto; nota in basso.

**Testo**:
- Titolo: *L'offerta open: tre filosofie*
- Colonna 1 — **smolagents** (Hugging Face): *il code-agent: il modello non emette `tool_use` in JSON, scrive un blocco di Python che chiama i tool, e l'harness lo esegue. È il sandbox come tool universale portato all'estremo (Slide 20). Piccolo (circa mille righe di core), multi-provider. Attenzione: l'esecuzione locale è dichiaratamente non sicura; il sandbox remoto si aggiunge.*
- Colonna 2 — **LangChain / LangGraph**: *il loop diventa un grafo esplicito: stato, nodi, archi, con esecuzione durevole (si può fermare e riprendere). È la scelta di chi vuole vedere e controllare ogni passo dell'harness; memoria per sessione e fra sessioni con checkpointer e store; observability con LangSmith. Nessun sandbox: lo porti tu. Il più maturo (LangGraph v1).*
- Colonna 3 — **Agno**: *agenti, team e workflow più un runtime, AgentOS, che li espone come servizio nella tua infrastruttura (REST, MCP, chat). Implementa lo standard Agent Skills, tracing OpenTelemetry nativo, memoria in database. Multi-provider.*
- Nota in basso: *Tutti e tre parlano MCP e girano con qualsiasi modello: qui la libertà di cambiare LLM (Slide 40) è la regola. In cambio, ospitare, isolare e osservare è tutto lavoro tuo.*

**Visual**: `slide60-tre-filosofie.svg` — tre mini-diagrammi in testa alle colonne.

**Prompt per schema SVG**:
> Tre pannelli affiancati, ognuno un piccolo esoscheletro con l'anello, in cui è evidenziata la cosa che caratterizza il framework:
> - **smolagents**: al posto della pill `tool_use` JSON, una pill che contiene **tre righe di Python** (`r = cerca("…")`, `for x in r: …`, `print(…)`), con la freccia verso un blocco `esegui il codice`; etichetta *l'azione è codice*.
> - **LangGraph**: l'anello è sostituito da un **grafo** di quattro nodi con archi e un rombo di decisione, e un'icona di salvataggio su un nodo (`checkpoint`); etichetta *il loop è un grafo, con stato*.
> - **Agno**: l'esoscheletro dentro un contenitore più grande etichettato `AgentOS`, con tre porte in uscita (`REST`, `MCP`, `chat`) e un piccolo database; etichetta *agenti + runtime*.
>
> **Elemento focale**: in ciascun pannello, la parte evidenziata.

## Slide 61 — L'offerta open: sulle stesse colonne

**Messaggio**: la stessa griglia della Slide 59 sui tre framework, con una riga in più: chi ospita. Nell'open la risposta è sempre "tu", ed è il prezzo della libertà sui modelli.

**Layout**: come la Slide 59: titolo in alto, tabella nel corpo (~70%), nota in basso. Nessuna figura.

**Testo**:
- Titolo: *L'offerta open: sulle stesse colonne*
- Tabella (dati verificati su documentazione ufficiale al 4 settembre 2026):

| | smolagents | LangChain / LangGraph | Agno |
|---|---|---|---|
| **Filosofia** | l'azione è codice | il loop è un grafo, con stato | agenti + runtime (AgentOS) |
| **Harness ospitato da** | tu | tu; hosting gestito a pagamento (LangSmith) | tu (AgentOS nella tua infra) |
| **Sandbox** | locale, **non sicuro** di default; remoto opzionale | **nessuno**: lo porti tu | nessuno documentato |
| **MCP** | sì: locali e remoti | sì (adattatore ancora in beta) | sì: locali e remoti; AgentOS è anche server |
| **Skill** | no | pattern di prompt a richiesta, non lo standard | sì, standard Agent Skills |
| **Memoria** | solo in RAM, per esecuzione | checkpointer (sessione) + store (fra sessioni) | in database, automatica o agentica |
| **Observability** | OpenTelemetry, replay | LangSmith; OTLP | OpenTelemetry nativo, in database |
| **Subagenti** | manager con agenti gestiti come tool | 5 pattern: subagenti, handoff, router, … | Teams (delega, routing, broadcast) |
| **Modelli** | qualsiasi | qualsiasi | qualsiasi |
| **Maturità** | v1.x, nessuna dichiarazione di produzione | LangGraph v1, stabile | v3.x |

- Nota in basso: *Confrontate la riga "Sandbox" con quella della Slide 59: nei prodotti la porta Anthropic, nell'open non la porta nessuno. È lì che si decide se un framework open costa meno di un prodotto, o di più.*

**Visual**: nessuno. Stessa avvertenza della 59: se dieci righe sforano, si tolgono **Modelli** (tutti "qualsiasi", detto nella nota) e **Maturità**.

## Slide 62 — La formula, riletta

> Terzo dei quattro stati della formula lungo il corso (vedi *Impianto*, sezione 1).

**Messaggio**: la formula con cui abbiamo aperto, ora con quattro termini accesi. Sotto ciascuno, una riga che dice che cosa abbiamo capito oggi. Uno resta spento.

**Layout**: come la Slide 3: titolo in alto, diagramma protagonista al centro (~65%), nota in basso.

**Testo**:
- Titolo: *La formula, riletta*
- Formula (nel visual): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Le righe di sintesi sotto i termini (nel visual):
  - sotto `LLM` (sbiadito, spunta *incontro 26*): *sa volere, non sa eseguire: aspetta di essere chiamato*
  - sotto `Harness` (acceso, con la mappa in miniatura): *il sistema operativo: prepara la finestra, esegue, la governa, la osserva*
  - sotto `System Prompt` (acceso): *ruolo e regole, più le istruzioni di progetto: il primo strato, quello che non cambia*
  - sotto `Tools` (acceso): *un contratto: dichiarato al giro zero, eseguito dall'harness, standardizzato da MCP*
  - sotto `Skills` (acceso): *il know-how, a richiesta: istruzioni, e a volte uno script*
  - sotto `KB` (spento): *incontro 28*
- Nota in basso: *L'LLM è la CPU, l'harness il sistema operativo, il resto il software installato. Oggi abbiamo aperto il sistema operativo e tre programmi. Ne manca uno.*

**Visual**: `slide62-formula-riletta.svg` — `slide3-formula-harness.svg` con lo stato dei blocchi cambiato e le righe di sintesi.

**Prompt per schema SVG**:
> La stessa figura della Slide 3 (stesso viewBox, blocchi e graffe nella stessa posizione). Stato dei blocchi: `LLM` attenuato con la spunta e l'etichetta *incontro 26*; `Harness`, `System Prompt`, `Tools`, `Skills` pieni, accesi; `KB` attenuato con l'etichetta *incontro 28*. Sotto ogni blocco, al posto della glossa originale, la riga di sintesi elencata nel testo (in piccolo, due righe al massimo). Sotto `Harness`, in aggiunta, la mappa dell'harness in miniatura (l'esoscheletro con le tre zone, gli anelli e la fascia), a dire "questo l'abbiamo aperto tutto".
>
> **Elemento focale**: i quattro blocchi accesi in fila, e il quinto spento accanto: si deve leggere "manca uno".

## Slide 63 — Dietro i tool, la conoscenza

**Messaggio**: abbiamo dato all'agente tool, skill e memoria. Ma quasi tutto ciò che deve sapere non lo scrive lui e non sta nei suoi pesi: sta nella conoscenza dell'organizzazione, dietro i tool. Come si organizza perché un agente la possa usare è il prossimo incontro.

**Layout**: titolo in alto; il blocco nero centrato al centro della slide, grande; sotto, i quattro requisiti come quattro parole in fila; nessuna figura. Chiude la lezione.

**Testo**:
- Titolo: *Dietro i tool, la conoscenza*
- Blocco nero centrato: *Abbiamo dato all'agente un loop, dei tool, delle skill, una memoria. Ma quando chiama `cerca_ordine`, o `cerca_documenti`, che cosa trova dall'altra parte? La conoscenza dell'organizzazione: dati, documenti, procedure. Come va organizzata perché un agente la possa usare: incontro 28.*
- Riga sotto il blocco (in burgundy, anticipazione del 28): **ricercabile in modo progressivo · non ridondante · veritiera · compounding**, con la glossa in piccolo: *i requisiti di una conoscenza utile, per una persona e per un agente*.

**Visual**: nessuno. Il blocco nero è la struttura, e il deck si chiude su una frase, non su una figura.
