# Slide realizzate — Incontro 27

Lista di lavoro nell'ordine del deck. Ogni riga: numero, titolo, ancora HTML in `presentation-27/presentation.html`, figure usate (in `presentation-27/svg/`).
Per commentare, scrivi sotto la riga della slide.

---


## Copertina — «Agentic AI: dentro l'harness»  
`#cover`

> **Primo giro di fix (6 settembre 2026), sezioni 1-3.** Il deck passa da 71 a **74 pagine**: la 10 spostata come 3a, la 15 sdoppiata in 15 + 15b, la 18 in 18 + 18b, nuova 20b. **Secondo giro (stesso giorno)**: 18b invertita, la 25 spostata come 18c, la 22 in due tempi sulla figura della 15b, la 23 ridisegnata, la 27 con la tool call `skill(nome)`; figure nuove `slide22-mcp-registro.svg`, rifatte `slide18-tool-vs-api.svg` e `slide23-primitive-mcp.svg`. Come nel 26, le slide nuove o spostate prendono una lettera e nessuna slide è stata rinumerata: tutte le ancore già citate qui e nelle spec restano valide. Figure nuove: `slide15-giro-completo.svg`, `slide18-dietro-un-tool.svg`, `slide20b-salva-e-cerca.svg`; ritoccate `slide10-chiamata-api.svg`, `slide15-sequence-giro.svg`, `slide18-tool-vs-api.svg`. **Terzo giro (9 settembre 2026), sezione 5**: la slide 46 chiude il ciclo con un quarto momento, dalla leva alla correzione alla rimisurazione (`slide46-cluster-leve.svg` rifatta a viewBox invariato). Verifica: screenshot decktape di tutte le pagine toccate e controllo nel browser delle colonne di testo (nessuna sfora) e della transizione 15 → 15b.


## Separatore di sezione 1 — «Tutto ciò che non è il modello»  
`#div-sec1` — `minimap-sec1.svg`

- **01 · Ieri il modello, oggi chi esegue** — `#slide-1` — *nessuna figura*
- **02 · Dalle aspettative ai requisiti** — `#slide-2` — *nessuna figura*
- **03 · La formula: oggi il sistema operativo** — `#slide-3` — `slide3-formula-harness.svg`
	- ✅ FATTO — «anticipiamo qui la #slide-10. riprendiamo l'esempio dell'incontro 26.»
		- La slide 10 è **spostata qui, subito dopo la formula**, con id `#slide-3a` e footnote `3a / Sezione 1`. Eyebrow `SEZIONE 1 · DALL'INCONTRO 26`.
		- ⚠️ Non ho rinumerato le slide 4-9: `#slide-4` resta `#slide-4`. Il numero 10 non esiste più nel deck (dopo la 09 viene la 11). Come nel 26, le slide nuove o spostate prendono la lettera; se vuoi la numerazione contigua la faccio come passo a sé.
- **03a · Com'è fatta una chiamata al modello** — `#slide-3a` — `slide10-chiamata-api.svg` — **SPOSTATA (ex 10)**
	- ✅ FATTO — «riprendiamo l'esempio dell'incontro 26»
		- *Figura*: la richiesta ora contiene la conversazione della slide 8 del 26: `system: "Sei l'assistente di Acme…"`, `tools: [ {name: "cerca_ordine", description, schema} ]`, `messages: [ {role: "user", content: "Dov'è l'ordine 4471?"} ]`. Le etichette a destra non dicono più «lo strato 1 / 2 / la storia» (gli strati arrivano in sezione 2) ma **`← [system]` · `← Tool:` · `← [user]`**: i riquadri del 26, uno per campo.
		- *Didascalia*: «È la scena della slide 8 del 26 (Acme, l'ordine 4471), vista da chi la esegue: una richiesta HTTP. […] Ogni riquadro del 26 è un campo della richiesta; la risposta porta i blocchi generati e uno `stop_reason` […]».
		- Riferimenti aggiornati: la slide 7 («A strati») chiude con *«Sono i campi della richiesta della slide 3a, letti come li vede il modello»*; le note della 6 e il punto sui checkpoint della 33 (`cache_control`) citano la 3a invece della 10.

- **04 · La mappa dell'harness** — `#slide-4` — `slide4-mappa-harness.svg`
- **05 · I tre anelli: dove si infila il loop agentico** — `#slide-5` — `slide5-tre-anelli.svg`
- **06 · L'harness più semplice possibile** — `#slide-6` — `slide6-harness-minimo.svg`

## Separatore di sezione 2 — «Context Initialization»  
`#div-sec2` — `minimap-sec2.svg`

- **07 · La finestra al giro zero** — `#slide-7` — `slide7-finestra-strati-0.svg`
- **08 · Il system prompt: ruolo e regole** — `#slide-8` — `slide7-finestra-strati-1.svg`
	- ✅ FATTO — «Aggiungiamo qui che tipicamente il system prompt ha anche una sezione iniettata di default dai provider di api, con le istruzioni più importanti, tipicamente di security, che noi sviluppatori non possiamo vedere e sono sempre iniettate.»
		- Quarto punto **«Una parte non la vedi»**: *«sopra il tuo testo il provider ne inietta di norma una sezione sua: istruzioni di base, per lo più di sicurezza, uguali per tutti. Chi sviluppa non la legge e non la toglie: c'è sempre.»*
		- Nel riquadro «lo strato 1 · testo esatto» una **prima riga `[provider]` attenuata** (grigio, come le righe già lette del 26): *«Istruzioni di base del provider (sicurezza; non visibili)»*, glossa «iniettato». La finestra a strati non cambia.
		- Per farci stare il quarto punto i tre esistenti sono passati da `pts tight` (11.5pt) a `pts micro` (10.5pt) e il primo punto perde «come rispondi».
		- ⚠️ Nelle note del relatore ho messo una precisazione: sui prodotti ospitati (Claude.ai, ChatGPT, Copilot) e sulle API con agente integrato la sezione iniettata è reale e non leggibile; sull'API grezza di Anthropic è più sottile, perché le regole stanno soprattutto nel post-addestramento. In slide il messaggio è quello che hai chiesto; se preferisci attenuare anche lì, dimmelo.
- **09 · Le istruzioni di progetto: AGENTS.md, CLAUDE.md** — `#slide-9` — `slide7-finestra-strati-1b.svg`
	- ✅ FATTO — «uno dei messaggi della slide è dire che questo alla fine è un modo pratico per far inizializzare l'agente dall'harness in base alla struttura del file system, ma l'effetto netto è identico, ed è semplicemente l'harness che carica da file le istruzioni.»
		- Secondo punto riscritto: **«L'harness lo appende sempre»** — *«al giro zero guarda la cartella in cui è lanciato, legge il file e lo mette nel system prompt, sotto le regole generali. È un modo pratico di inizializzare l'agente in base a dove sta nel file system; ma l'effetto netto è identico alla slide 8: l'harness carica istruzioni da un file.»*
		- Testo a `pts micro` per lo stesso motivo della 8 (sforava sopra e sotto).
- **11 · La dichiarazione dei tool: un contratto** — `#slide-11` — `slide7-finestra-strati-2.svg`
- **12 · Le skill, al giro zero: solo l'indice** — `#slide-12` — `slide7-finestra-strati-3.svg`
- **13 · La finestra piena, e l'utente non ha ancora scritto** — `#slide-13` — `slide7-finestra-strati-4.svg`
- **14 · Ora l'utente scrive** — `#slide-14` — `slide14-giro-uno.svg`

## Separatore di sezione 3 — «Environment management»  
`#div-sec3` — `minimap-sec3.svg`

- **15 · Il giro, visto dall'harness** — `#slide-15` — `slide15-giro-completo.svg` — **NUOVA**
	- ✅ FATTO — «Qui facciamo una transizione in cui prima riprendiamo la conversazione di slide 14, ma completa con la risposta, nel formato di slide 14, che con una transizione diventa l'svg attualmente presente.»
		- La 15 è la **slide 14 completata**: stesso formato e stessa scala (righe da 18px, mono 12.5). A sinistra il `giro 1` com'era; a destra il riquadro «?» è ora il `giro 2` del 26: le righe già lette in grigio, poi **`[tool] { stato: "in consegna", data: "6 set" }`** in teal (la riga che il modello non ha scritto), la risposta `[assistant] Il tuo ordine è in consegna, arriva il 6.` e `stop_reason: end_turn`. Una linea tratteggiata teal collega la tool call del giro 1 alla riga `[tool]`: «fra i due giri: l'harness». Eyebrow `SEZIONE 3 · DALL'INCONTRO 26`.
		- Chiude col blocco nero: *«Che cosa è successo fra la riga `[assistant] → cerca_ordine("4471")` e la riga `[tool]`?»*
		- **La transizione**: 15 e 15b hanno entrambe `data-auto-animate`; al click la conversazione dissolve e compare il sequence diagram (titolo invariato, colonne di testo che entrano). È la prima slide del deck con auto-animate; verificata nel browser, non da decktape (che non la cattura).
- **15b · Il giro, visto dall'harness** — `#slide-15b` — `slide15-sequence-giro.svg` — *(era la 15)*
	- ✅ FATTO — «Nel testo far capire bene che l'esecuzione del dispatch è verso una parte di codice. nell'immagine, sopra e sotto al blocco giallo tool: cerca ordine creare altri due blocchi gialli piccolini con altre due funzioni, per far capire che per ogni tool dichiarato all'llm ci deve essere una funzione dichiarata. magari in cima fare un miniblocco con def cerca_ordine (id) etc in cui si fa vedere che vengono dichiarate nel runtime dell'harness»
		- *Testo*, punto **«Dispatch»**: *«cerca il tool con quel nome nel proprio registro e chiama la funzione corrispondente: per ogni tool dichiarato al modello c'è una funzione nel runtime dell'harness. Qui si esegue codice, non testo: a volte calcola o legge un file, molto spesso chiama un'API esterna e ne traduce la risposta.»* Testo a `pts micro`.
		- *Figura*: la colonna gialla è diventata un **«registro dei tool · codice nel runtime dell'harness»** (contenitore tratteggiato giallo). Dentro, dall'alto: il miniblocco di codice `def cerca_ordine(id): r = api.get(f"/orders/{id}") … return {stato: …, data: …}`; un **blocchetto giallo `tool: lista_ordini`** (`def lista_ordini(cliente): …`); il blocco grande **`tool: cerca_ordine` — «la funzione qui sopra, in esecuzione»**, con la linea di vita solo lì; un **blocchetto giallo `tool: apri_reso`** (`def apri_reso(id, motivo): …`); in fondo la scritta *«per ogni tool dichiarato al modello, una funzione nel runtime dell'harness»*. La freccia del dispatch porta l'etichetta «chiama la funzione».
		- viewBox allargato da `760×440` a `840×440` per far posto al registro: la figura è vincolata in altezza, quindi resa alla stessa scala di prima.
- **16 · Errori come feedback** — `#slide-16` — *nessuna figura*
- **17 · Chiamate parallele nello stesso giro** — `#slide-17` — `slide17-parallele.svg`
	- ✅ FATTO — «Qui è importante capire che sono gli llm stessi che possono richiedere l'esecuzione parallela, se in base alla definizione del tool capiscono che le cose sono indipendenti»
		- Primo punto riscritto: **«Più `tool_use` in una risposta»** — *«è il modello a deciderlo: se dalle descrizioni dei tool capisce che tre chiamate sono indipendenti, le chiede tutte insieme: tre blocchi nella stessa risposta, un solo `stop_reason`. Nessuno glielo impone; lo legge nel contratto della slide 11.»* Figura invariata.
- **18 · Dietro un tool: spesso un'API, non sempre** — `#slide-18` — `slide18-dietro-un-tool.svg` — **NUOVA**
	- ✅ FATTO — «Qui secondo me vanno spiegati due concetti, magari separando in due slide. Il primo è che spessissimo le funzioni dichiarate come tool dall'harness all'llm sono dei proxy di chiamate ad API esterne, come anche nell'esempio prima, ma non sempre! esempio li vedremo dopo la chiamata bash.»
		- Sdoppiata: questa è il **primo concetto**. Tre punti: **«Il caso più comune: un proxy»** (è `cerca_ordine` della 15b: dietro c'è `GET /orders/4471`, e il modello non lo sa); **«Ma non sempre»** (puro codice: un calcolo, una lettura da file, una query locale; oppure un intero computer: `bash`, alla slide 20); **«Il modello vede sempre la stessa cosa»** (nome, descrizione, schema: che cosa c'è dietro è invisibile dal contesto).
		- *Figura nuova* (`660×384`, layout `tv-40`): tre righe. A sinistra **tre contratti con la stessa forma** (`cerca_ordine`, `calcola_totale`, `bash`: nome, descrizione, schema); al centro il blocchetto giallo `def …():` (la funzione nel registro, richiamo alla 15b); a destra che cosa c'è dietro: **un'API esterna** (tratteggiata, `GET /orders/4471 → JSON, 5.000 righe → 3 campi`), **puro codice** (tre righe di Python, «nessuna rete»), **un intero computer** (blocco nero con `$ grep …` e `$ python3 …`, «il sandbox: slide 20 e 21»).
		- Nota: *«Il contratto della slide 11 è la stessa cosa in tutti e tre i casi. La differenza sta nel registro dell'harness: che cosa fa la funzione quando viene chiamata.»*
- **18b · Un tool non è un'API: non mappare 1:1** — `#slide-18b` — `slide18-tool-vs-api.svg` — *(era la 18)*
	- ✅ FATTO — «Il secondo concetto è quello presente nella slide, che spesso non è una buona scelta di design mappare 1:1 le api presenti in un sistema (spesso legacy) come tool.»
		- Titolo da «Un tool non è un'API» a **«Un tool non è un'API: non mappare 1:1»**. Nuovo primo punto **«La tentazione»**: *«il sistema (spesso legacy) ha già le sue API: prendile tutte, una per una, e dichiarale come tool. Venti endpoint, venti tool, zero lavoro di progetto. È quasi sempre una cattiva scelta.»* Seguono «Due lettori diversi» e «Le response grandi» com'erano (l'ultimo chiude su «nell'adattatore, che sceglie i campi e li traduce»).
		- Nota nuova: *«Il tool è progettato per il modello, non per l'API […]. Quando la risposta non si può accorciare, c'è un pattern apposta: dopo bash, alla slide 20b.»*
	- ✅ FATTO — «Il pattern salva e cerca lo riprendiamo dopo aver spiegato la bash»
		- Tolti da qui il terzo punto «Il pattern: salva e cerca» e la nota sul sandbox che governa il contesto: sono alla **20b**.
		- *Figura* ritagliata: via la fascia «SALVA E CERCA» in basso, viewBox da `640×440` a `640×296` (resta API → adattatore → tool).
		- Riferimento aggiornato: la slide 36 (offload) diceva «È la slide 18, promossa a regola generale», ora dice **20b**.
	- ✅ FATTO — «inverti destra con sinistra l'immagine per mantenere coerenza con le immagini precedenti. Magari fa vedere come viene esposto un tool ottimizzato al modello mentre il proxy per le api chiama delle api più atomiche e dispersive organizzando le chiamate»
		- *Figura* rifatta (`660×320`), orientata come la 15b e la 18: **a sinistra «IL TOOL · per il modello»** (`cerca_ordine(id_ordine)`, descrizione che dice quando usarlo, un parametro, risposta teal `stato · data · corriere ~40 token`, «un tool per compito del modello»); **al centro l'adattatore** «dentro l'harness · orchestra tre chiamate, tiene tre campi»; **a destra «LE API · atomiche, disperse»**: tre endpoint tratteggiati chiamati in sequenza (`① GET /orders/{id}` con i 20 parametri, `② GET /shipments?order={id}`, `③ GET /customers/{cid}` «solo per sapere il nome sull'etichetta»), frecce dall'adattatore a ciascuno, e sotto la risposta che scende oltre il bordo: «tre risposte · ~5.000 righe · ~50.000 token».
		- *Testo*, punto «Due lettori diversi» riscritto: *«le API sono atomiche e disperse: tre endpoint, venti parametri, e restituiscono tutto. […] Il tool espone un parametro, dice quando usarlo e restituisce tre campi […]. In mezzo, l'adattatore orchestra.»*
	- ✅ FATTO — «sposta qui #slide-25»
		- La 25 è ora la **18c**, subito dopo questa (vedi sotto). Le note del relatore di questa slide rimandano alla 18c invece che alla 25.
- **18c · Non mappare 1:1 le API: il costo nascosto** — `#slide-18c` — `slide25-peso-mcp.svg` — **SPOSTATA (ex 25)**
	- ✅ FATTO — «da spostare» (dalla 25)
		- Spostata qui, prima che MCP sia introdotto: nel testo «tre server» → «tre sistemi», «esporre solo i server» → «solo i sistemi»; nella figura le quattro etichette «server MCP «ordini»» ecc. sono diventate **«i tool di «ordini»», «i tool del «CRM»»…** Il resto della figura (la fascia CRM da 9.000 token nella finestra, il CRM rifatto a 6 tool) è invariato. Primo punto: «La tentazione, in grande» (la 18b ha già introdotto la tentazione sul singolo tool).
		- Nota: aggiunta la coda *«E quando i tool arrivano da un server esterno (MCP, fra poco), il conto è lo stesso.»* così il ponte con la sezione MCP resta.
		- Riferimenti aggiornati: le note della 33 (numeri coerenti con «la slide 18c»), la nota della 27 («i cinquanta tool sempre presenti della slide 18c»). Nel deck non esiste più il numero 25: dopo la 24 viene la 26.
- **19 · Il risultato è testo: la prompt injection** — `#slide-19` — `slide19-trifecta.svg`
- **20 · Bash: un tool come gli altri, che può fare tutto** — `#slide-20` — *nessuna figura*
- **20b · Il pattern salva e cerca, con bash** — `#slide-20b` — `slide20b-salva-e-cerca.svg` — **NUOVA**
	- ✅ FATTO — «qui mettiamo una slide che spiega il pattern salva e cerca con la bash»
		- Tre punti: **«Il problema»** (un risultato che non si può accorciare: cinquantamila token che entrerebbero in un colpo solo e resterebbero a ogni giro); **«Il pattern»** (l'harness, o il tool stesso, scrive su file nel sandbox e restituisce solo riassunto e percorso; il modello ci cerca con `bash`: `grep`, `head`, quattro righe di Python); **«Perché serve bash»** (senza un tool universale il file sarebbe irraggiungibile: servirebbe un tool «cerca nel file» per ogni formato; è l'esempio della slide 20 letto come pattern: `esporta_ordini` ha salvato, `bash` ha cercato).
		- *Figura nuova* (`660×384`, `tv-40`), in due tempi: **① SALVA** — la risposta dell'API (5.000 righe · ~50.000 token) → adattatore «scrive, invece di iniettare» → il file `export_4471.json` nel sandbox; al modello torna solo la riga teal `[tool] salvato in export_4471.json (5.000 righe): cerca con grep o elabora con bash`. **② CERCA** — `[assistant] → bash("grep -n -E 'stato|data_consegna' export_4471.json")` (freccia tratteggiata «legge nel sandbox» verso il file), `[tool]` con le due righe trovate, la risposta finale. In basso: *«in finestra: ~60 token invece di 50.000»* e *«il file resta lì, se al giro dopo serve un'altra riga»*.
		- Nota (spostata dalla 18): *«È il primo caso in cui il sandbox serve a governare il contesto, non a eseguire un compito. […] l'offload su file è la tecnica principe della sezione 4.»*
- **21 · Perché non gira in produzione: il sandbox** — `#slide-21` — `slide21-sandbox.svg`
- **22 · Dal contratto al protocollo: MCP** — `#slide-22` — `slide15-sequence-giro.svg` + `slide22-mcp-registro.svg` (in transizione)
	- ✅ FATTO — «Qui ci devono essere due immagini in transizione. La prima è ripresa da slide #slide-15b , la seconda mostra come gli stessi servizi sono esposti dal server MCP-CRM»
		- **Tempo 1**: la figura della 15b, tale e quale (stesso file `slide15-sequence-giro.svg`): il registro dei tool dentro l'harness. In slide c'è solo il punto «Il problema» (*«ogni harness riscrive lo stesso registro: le tre funzioni della slide 15b esistono in dieci versioni, una per prodotto»*).
		- **Tempo 2** (al click, `.visual.stack` + `fragment`, stesso viewBox `840×440` così nulla si sposta): `slide22-mcp-registro.svg`. Un confine tratteggiato «dentro l'harness» si ferma prima della colonna gialla, che è diventata **«server MCP «ordini» · lo stesso registro, fuori dall'harness»** con le stesse tre funzioni (`def cerca_ordine(id)`, `lista_ordini`, `apri_reso`) e in fondo «scritto una volta da chi possiede l'API, usato da ogni harness». L'harness porta l'etichetta «+ client MCP». Compare un **GIRO 0** con `tools/list` → «3 × {name, description, schema}», e nel giro 1 al posto di «chiama la funzione» c'è **`tools/call` cerca_ordine, {id: "4471"}** e il ritorno «la risposta del protocollo» (in ocra, il colore del protocollo). La colonna del modello è identica al tempo 1. Insieme compare il punto «La soluzione» (fragment con lo stesso indice).
		- ⚠️ Il server è **«ordini»**, non «CRM»: sono le tre funzioni della 15b (`cerca_ordine`, `lista_ordini`, `apri_reso`), e nella 23 e nella 18c «ordini» e «CRM» sono due server distinti. Se preferisci «CRM» anche qui, è un cambio di etichetta.
		- ⚠️ `slide22-mcp-specchio.svg` (i due pannelli affiancati) non è più referenziato. Non l'ho cancellato: dimmi se vuoi rimuoverlo.
- **23 · Le primitive di MCP: tools, resources, prompts** — `#slide-23` — `slide23-primitive-mcp.svg`
	- ✅ FATTO — «Metti in ordine l'immagine, è un po' confusa»
		- Ridisegnata senza incroci. Le tre frecce colorate non partono più dai server per attraversare tutto: **partono dal client 1** e arrivano ciascuna nel suo strato (prompts → system prompt, tools → dichiarazione dei tool, resources → messaggi); dentro la finestra ogni strato porta l'etichetta colorata «← prompts / ← tools / ← resources». I due client sono in colonna sul bordo destro dell'host, ognuno con **una sola linea** al suo server, etichettata col trasporto («locale · stdio», «remoto · HTTP»). Nei server le righe sono nell'ordine **prompts, tools, resources**, lo stesso degli strati dall'alto in basso.
		- L'elicitation non taglia più la figura in diagonale: corre tratteggiata dal client 1 lungo il fondo dell'host fino all'utente, con la didascalia «il server chiede un dato all'utente, attraverso il client».
- **24 · Da stateful a stateless: un protocollo che cresce** — `#slide-24` — `slide24-mcp-timeline.svg`
- **~~25~~ · Non mappare 1:1 le API: il costo nascosto** — *(numerazione precedente; ora è la 18c)*
	- ✅ FATTO — «da spostare» → vedi **18c**.
- **26 · Che cos'è una skill** — `#slide-26` — *nessuna figura*
- **27 · Come entra: dall'indice al corpo** — `#slide-27` — `slide27-skill-caricamento.svg`
	- ✅ FATTO — «rendere evidente che l'espansione della skill è richiesta dall'llm con un tool dedicato»
		- *Testo*, secondo punto ora **«E la chiede con un tool»**: *«nella dichiarazione dei tool c'è uno strumento apposta, `skill(nome)`: il modello lo chiama con un `tool_use` come per `cerca_ordine`, e l'harness appende il corpo come `tool_result`. È il giro della slide 15b, con una differenza: il risultato non è un dato, è una procedura.»* Via la frase «in alcuni è il modello a chiederlo, in altri l'harness».
		- *Figura*: in tutti e tre i fotogrammi lo strato «dichiarazione dei tool» porta **`· skill(nome)`** in burgundy. Nel giro 1, fra la richiesta del cliente e il corpo, c'è la pill burgundy **`[assistant] → skill("risposta-reclami-acme")`**, e il corpo è ora una riga **`[tool]`** in teal (il colore del tool_result, come nel 26), con la didascalia «la chiede il modello, con un tool; il corpo torna come tool_result». Nel giro 2 le stesse due righe sono in grigio, già lette; la chiusura dice «nessun altro tool: la skill era solo istruzioni».
		- Nelle note del relatore: in Claude Code il tool è `Skill`; nell'API di Anthropic (Agent Skills) il modello legge `SKILL.md` con il tool di esecuzione codice, quindi ancora una tool call, con un tool generico; l'eccezione è il comando `/nome` digitato dall'utente. In slide si mostra il caso normale.
- **28 · Quando la skill porta uno script** — `#slide-28` — `slide28-skill-script.svg`

## Separatore di sezione 4 — «Context management»  
`#div-sec4` — `minimap-sec4.svg`

- **29 · Costo fisso e costo a richiesta** — `#slide-29` — `slide29-costo-fisso-richiesta.svg`
- **30 · Quando conviene cosa** — `#slide-30` — *nessuna figura*
- **31 · La finestra a ogni giro: tre parti, tre velocità** — `#slide-31` — `slide31-finestra-giri.svg`
- **32 · Il prefisso non si tocca: prefix caching** — `#slide-32` — `slide32-prefix-caching.svg`
- **33 · Che cosa rompe la cache** — `#slide-33` — `slide33-cache-regole.svg`
- **34 · Non basta che ci stia: il context rot** — `#slide-34` — `slide36b-tool-context-rot.svg`
- **35 · Pruning e compaction: togliere e riassumere** — `#slide-35` — `slide35-pruning-compaction.svg`
- **36 · Offload su file: spostare, non perdere** — `#slide-36` — `slide36-offload.svg`
- **37 · La memoria: ciò che l'agente salva da solo** — `#slide-37` — `slide37-memoria-agente.svg`
- **38 · La memoria è un tool** — `#slide-38` — *nessuna figura*
- **39 · Le tre domande della memoria** — `#slide-39` — *nessuna figura*

## Separatore di sezione 5 — «Observability: osservare e migliorare»  
`#div-sec5` — `minimap-sec5.svg`

- **40 · Le leve di miglioramento** — `#slide-40` — `slide40-leve.svg`
- **41 · Tre livelli di successo, e la traiettoria** — `#slide-41` — `slide41-tre-livelli.svg`
- **42 · Il rischio del vibe eval** — `#slide-42` — `slide42-vibe-eval.svg`
- **43 · Il processo, in un colpo d'occhio** — `#slide-43` — `slide43-processo-eval.svg`
- **44 · Chi giudica: una persona sola, e le tracce a mano** — `#slide-44` — `slide43-mini-1.svg`, `slide44-traccia-annotata.svg`, `slide44-annotazione-ui.svg`
- **45 · Il dataset di test: cento casi, per dimensioni** — `#slide-45` — `slide43-mini-2.svg`, `slide45-dataset-dimensioni.svg`
- **46 · Clusterizzare i fallimenti, e risalire alla leva** — `#slide-46` — `slide43-mini-3.svg`, `slide46-cluster-leve.svg`
	* Testo o Visual: rendere evidenti che individuata la leva, viene applicata la correzione
	- ✅ FATTO — entrambi: un quarto punto nel testo e un quarto momento nella figura.
		- *Testo*: nuovo quarto punto **«Poi si corregge, e si rimisura»** — *«la correzione si applica sulla leva, poi si rilancia il dataset: senza la seconda misura non si sa se è servita. In figura: una riga sul formato delle date porta "rescheduling" dal 33% al 95%.»* La frase sull'esempio reale esce dal terzo punto, dove era un inciso, e diventa la prova del quarto.
		- *Figura*: i tre blocchi esistenti sono ora numerati ① i casi falliti · ② i cluster · ③ la leva, e in fondo c'è il **④ individuata la leva, si applica la correzione — e si rimisura**: una fascia a tutta larghezza con tre celle e le frecce fra loro. I cluster contati sul caso reale (con `rescheduling · 60` evidenziato in giallo) → la correzione sulla leva (il riquadro con la riga aggiunta al system prompt: *«+ Le date vanno sempre espresse in formato europeo: gg/mm/aaaa»*) → la rimisurazione, due barre a confronto, **prima 33% / dopo 95%**.
		- Dalla leva `1 · Prompt` scende una freccia nera fino alla fascia, etichettata **«è qui che si corregge»**: è il collegamento esplicito fra il terzo e il quarto momento.
		- La riga *«senza la seconda misura non si sa se è servita»* chiude la fascia: la rimisurazione non è un di più, è ciò che distingue la correzione dal vibe eval della slide 42 (detto anche nelle note del relatore).
		- **Misure.** Il viewBox resta `760×440`: è già esattamente il rapporto dello slot (1.726) e la figura rende **706,9×409,3 px**, cioè tutto lo spazio disponibile — allargarla avrebbe rimpicciolito tutto. Lo spazio per la fascia è stato ricavato **comprimendo in verticale la nuvola dei casi sparsi** (le sette righe di punti da y 58–376 a y 56–294), senza toglierne nessuno: restano 28.
		- ⚠️ **La colonna di testo era già al limite** (sforava di 4px prima di questa fix, e il quarto punto l'ha portata a 25). Per rientrare a **0** ho accorciato i quattro punti e spostato nelle note del relatore il criterio di stop (*«si continua finché non emergono categorie nuove»*). Se aggiungi testo a questa slide, rimisura: non c'è più margine.
- **47 · Checker deterministici, poi il giudice** — `#slide-47` — `slide43-mini-45.svg`, `slide47-checker-giudice.svg`
- **48 · Gli errori nei tool deterministici e nei tool non deterministici** — `#slide-48` — `slide43-mini-3.svg`, `slide48-errori-tool.svg`
- **49 · In produzione: il ciclo che non finisce** — `#slide-49` — `slide43-mini-6.svg`, `slide49-ciclo-produzione.svg`
- **50 · Tre usi del logging** — `#slide-50` — `slide50-traccia-tre-usi.svg`

## Separatore di sezione 6 — «Orchestrazione: quando un agente non basta»  
`#div-sec6` — `minimap-sec6.svg`

- **51 · Quando un agente non basta: il criterio** — `#slide-51` — `slide51-workflow-vs-agente.svg`
- **52 · Pattern 1: il subagente come tool** — `#slide-52` — `slide52-subagente-tool.svg`
- **53 · Pattern 2: worker paralleli** — `#slide-53` — `slide53-worker-paralleli.svg`
- **54 · Pattern 3: evaluator / reviewer** — `#slide-54` — `slide54-reviewer.svg`
- **55 · Swarm e multi-agente conversazionale: un giudizio** — `#slide-55` — `slide55-swarm.svg`
- **56 · Deep research: com'è fatto davvero** — `#slide-56` — `slide56-deep-research.svg`
- **57 · Deep research: i tre pattern, colorati** — `#slide-57` — `slide56-deep-research.svg`, `slide57-deep-research-pattern.svg`

## Separatore di sezione 7 — «L'offerta di harness»  
`#div-sec7` — `minimap-sec7.svg`

- **58 · L'offerta Anthropic: stesso harness, superfici diverse** — `#slide-58` — `slide58-superfici-anthropic.svg`
- **59 · L'offerta Anthropic: che cosa espongono** — `#slide-59` — *nessuna figura*
- **60 · L'offerta open: tre filosofie** — `#slide-60` — `slide60-tre-filosofie.svg`
- **61 · L'offerta open: sulle stesse colonne** — `#slide-61` — *nessuna figura*
- **62 · La formula, riletta** — `#slide-62` — `slide62-formula-riletta.svg`
- **63 · Dietro i tool, la conoscenza** — `#slide-63` — *nessuna figura*
