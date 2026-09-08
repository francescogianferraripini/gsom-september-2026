# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 7 — Superare i limiti, e il know-how**
**Obiettivo di apprendimento**: il partecipante sa che cosa manca a tutte le forme e a tutti i pattern (definizioni, identità, relazioni fra tipi: il gradino della semantica), conosce le due risposte del data management di oggi, data as a product (chi risponde) e semantic modeling con le ontologie (che cosa vuol dire), sa che un'ontologia si scrive con classi, proprietà e relazioni fin dal primo passo e si organizza in un'ontologia cross più ontologie di dominio, sa come entra nel dato strutturato (semantic linking: classi, proprietà, relazioni collegate a tabelle, colonne, join) e nel non strutturato (estrazione guidata, metadati di ciclo di vita), sa che cos'è l'approccio convergente, distingue di nuovo know-what e know-how, e rilegge la formula completa.
**Messaggio chiave (takeaway)**: Il significato, scritto una volta sopra le forme che ci sono, è ciò che rende la conoscenza utile a persone, pipeline e agenti.
**Budget**: ~20 min, 8 slide + separatore (più la demo, se c'è tempo). Ripartizione: il gradino 1, data as a product 1, ontologia 1, linking 1, non strutturato 1, convergenza 1, know-how 1, formula 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec7.html` | Separatore — Sezione 7: Superare i limiti, e il know-how |
| `slides/slide53-gradino-semantica.html` | Slide 53 — Il gradino della semantica |
| `slides/slide54-data-product.html` | Slide 54 — Managing data as a product |
| `slides/slide55-ontologia.html` | Slide 55 — Semantic modeling: l'ontologia |
| `slides/slide56-semantic-linking.html` | Slide 56 — Nel dato strutturato: il semantic linking |
| `slides/slide57-estrazione-guidata.html` | Slide 57 — Nel dato non strutturato: l'ontologia guida l'estrazione |
| `slides/slide58-convergente.html` | Slide 58 — L'approccio convergente |
| `slides/slide59-know-how.html` | Slide 59 — Know-how: le skill |
| `slides/slide60-formula-completa.html` | Slide 60 — La formula, completa |

---

> **Filo della sezione.** La banda dell'ontologia della figura madre si accende. Prima le tre mancanze e le due risposte (53); poi la risposta organizzativa, data as a product (54); poi l'ontologia, con classi, proprietà e relazioni fin dal primo passo e la struttura cross + domini (55); come entra nel dato strutturato, il semantic linking (56), e nel non strutturato, l'estrazione guidata e i metadati di ciclo di vita (57); la convergenza, con la prima pagella a quattro spunte (58); il know-how e la demo (59); la formula completa che chiude il corso (60). La mini-mappa dei separatori accende la banda dell'ontologia.
>
> **Decisioni prese in intervista**: nella Slide 55 non si citano RDF e OWL; relazioni e proprietà si modellano dal primo passo, non dopo un glossario piatto; l'ontologia è a due livelli (cross + domini). Nella Slide 56 la visione è il **semantic linking** (collegare gli elementi dell'ontologia, con le loro descrizioni, a tabelle e colonne e join), non uno strato di metriche: i semantic layer dei vendor sono citati in una nota come caso particolare. Nella Slide 57 le entità mappate vanno mostrate **evidenziate in una pagina di testo**, e si dice che agenti dedicati, data un'ontologia, sono molto bravi a trovarle nel testo libero.
>
> **Due demo, se c'è tempo**: Slide 56, l'ontologia di Quantyca e il suo linking alle tabelle; Slide 59, una skill vera dal repo Quantyca. Entrambe hanno un riquadro tratteggiato `DEMO` in slide; niente frontmatter inventati.
>
> **Riprese**: la piramide (Slide 3 → 53), la Data Governance (Slide 26 → 54), il grafo dei tipi (Slide 3 e 55), i requisiti del Text2SQL (Slide 45 → 56), il lexical graph (Slide 50 → 57), la figura madre (Slide 7 → 58 e 60), la skill `rimborsi-acme` del 27 (slide 26 → 59, eyebrow *dall'incontro 27*), la formula (26 slide 3, 27 slide 62 → 60).
>
> **Fatti verificati** per la nota della Slide 56 in `docs/ricerche-28/research-pattern-agentici.md` (Snowflake semantic view e MCP server gestito, nov 2025; Databricks metric view e Genie Ontology, 2026; dbt Semantic Layer e dbt MCP server, apr/ott 2025).
>
> **Esempio Acme in questa sezione**: la definizione di "ritardo" che cambia da dipartimento a dipartimento; `Corriere #17` = `dim_corriere.id_corriere = 17` = "il Vettore" del contratto; il contratto `C-2026-07` (firmato, valido dal 2026-03-01, sostituisce `C-2023-02`, owner acquisti); il prodotto dati `fatto_spedizioni · v3`.

---

## Slide 53 — Il gradino della semantica

**Messaggio**: tabelle, documenti, grafi e i pattern che li leggono falliscono tutti sullo stesso punto: il significato non è scritto da nessuna parte, o è scritto in dieci posti diversi. Sono tre mancanze precise, ed è il gradino "semantica" della piramide; le risposte sono due, e la sezione le percorre.

**Layout**: titolo in alto; le tre mancanze a sinistra (~50%); a destra (~45%) i due riquadri delle risposte e, sotto, la piramide della Slide 3 in miniatura con il gradino `semantica` evidenziato; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 7 · SUPERARE I LIMITI, E IL KNOW-HOW*
- Titolo: *Il gradino della semantica*
- Le tre mancanze:
  1. **Le definizioni**: *la definizione di "ritardo" sta nel codice di dieci pipeline, nella testa di chi le ha scritte, in una clausola di contratto; e cambia da dipartimento a dipartimento, se non da persona a persona: per la logistica sono giorni lavorativi dalla data prevista, per il servizio clienti giorni di calendario dalla data promessa, per l'amministrazione quelli che attivano la penale. Dieci definizioni, nessuna dichiarata. Il modello ne sceglie una, e non dice di aver scelto (slide 46).*
  2. **Le identità**: *`SpedFast` in `dim_corriere`, "SpedFast S.r.l." nel contratto, tre nodi `SpedFast` nel grafo estratto: la stessa cosa, senza un nome che lo dica. Ogni forma accumula per sé (slide 52).*
  3. **Le relazioni fra i tipi**: *che un corriere è vincolato da un contratto, che una spedizione ha un ritardo, che un ritardo attiva una penale: lo sa chi legge, non lo sa nessun sistema. È il grafo dei tipi della slide 3, che finora non abbiamo scritto.*
- Le due risposte (due riquadri):
  - **Chi ne risponde: data as a product** — *un proprietario, un contratto, dei controlli per ogni tabella, indice, grafo. Slide 54.*
  - **Che cosa vuol dire: l'ontologia** — *classi, proprietà, relazioni, definizioni, scritte una volta e lette da persone, pipeline e agenti. Slide 55–58.*
- Nota in basso: *È la piramide della slide 3, al gradino che mancava: contesto lo abbiamo messo (le tabelle, gli indici), azioni le abbiamo viste (i pattern). La semantica è ciò che trasforma informazione in conoscenza, e non la produce nessun motore: la scrive qualcuno.*

**Visual**: nessun SVG nuovo; la struttura a tre mancanze più due riquadri è il visual, con la piramide della Slide 3 (`slide3-piramide-4.svg` o un ritaglio) in miniatura, gradino `semantica` evidenziato, gli altri due spuntati.

## Slide 54 — Managing data as a product

**Messaggio**: la prima risposta è organizzativa: ogni tabella, indice, grafo che qualcuno legge è un prodotto, con un proprietario, un contratto, dei controlli e una documentazione, e chi lo usa è un cliente. È la Data Governance della slide 26 resa struttura; e per l'agente il contratto è, letteralmente, la descrizione del tool.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Managing data as a product*
- Punti:
  1. **Un prodotto, non una pipeline**: *`fatto_spedizioni` non è l'uscita di un ETL: è un prodotto che il team logistica pubblica per chi lo legge, con un nome, una versione, un proprietario che risponde alle domande e agli incidenti. Chi lo usa è un cliente, non un collega che passa di lì.*
  2. **Il contratto**: *lo schema con le descrizioni, il grano, le metriche definite, la frequenza di aggiornamento, i controlli di qualità che girano a ogni carico e che cosa succede se falliscono. Scritto, versionato, e rotto solo con preavviso: le dipendenze della slide 21 diventano un accordo, non una scoperta.*
  3. **Vale per tutte le forme**: *un indice di documenti è un prodotto (quali documenti, quale versione vale, chi li cura); un grafo è un prodotto (quali entità, estratte come, con quale affidabilità). I quattro punti della slide 26, qualità, completezza, ownership, dipendenze, hanno ciascuno una riga nel contratto.*
- Nota in basso: *Per l'agente: la descrizione di `esegui_sql`, e lo schema nel system prompt, sono il contratto del prodotto dati, letto da un modello. Un prodotto senza contratto è un tool senza descrizione: viene usato male, o a caso. È anche il principio del data mesh: i prodotti li pubblica chi conosce il dominio, e la piattaforma dà a tutti lo stesso modo di pubblicarli.*

**Visual**: `slide54-data-product.svg`.

**Prompt per schema SVG**:
> **A sinistra**, una scheda-prodotto grande, `fatto_spedizioni · v3`, con le sezioni impilate: `owner: team logistica (Giulia)` · `grano: una riga = una spedizione` · `schema + descrizioni` · `metriche: ordini_in_ritardo, ritardo_medio_gg` · `aggiornamento: ogni notte alle 02:00` · `controlli: ritardo ≥ 0 · corriere non nullo · righe ≥ 95% del giorno prima` · `consumatori: report ritardi · dashboard · esegui_sql (agente)` · `changelog: v3 aggiunta giorni_lavorativi_ritardo`.
>
> **A destra**, tre schede più piccole con la stessa struttura abbreviata: `indice contratti · v2` · `grafo logistica · v1` · `policy rimborsi · 2026`.
>
> Una freccia dalla scheda grande allo strato `system prompt` di una finestra a strati in miniatura, etichettata *il contratto, letto dal modello*.
>
> **Elemento focale**: la scheda grande, con `owner` e `controlli` in evidenza.

## Slide 55 — Semantic modeling: l'ontologia

**Messaggio**: la seconda risposta è l'ontologia: il grafo dei tipi di cose, con le proprietà, le relazioni fra i tipi, le definizioni e i sinonimi, scritto una volta e organizzato in un'ontologia cross più ontologie di dominio. Non contiene i dati; dice che cosa i dati vogliono dire, e vale per la tabella, per il documento e per il grafo delle istanze.

**Layout**: titolo in alto; i quattro punti di testo a sinistra (~40%, classe `tight`); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Semantic modeling: l'ontologia*
- Punti:
  1. **Che cos'è**: *un elenco di classi (`Cliente`, `Ordine`, `Spedizione`, `Corriere`, `Contratto`, `Penale`), le loro proprietà, le relazioni fra classi (`Spedizione` –consegnata da→ `Corriere`; `Contratto` –vincola→ `Corriere`), e per ciascuna una definizione in italiano e i sinonimi ("corriere, vettore, trasportatore"). È il grafo della slide 3, scritto per davvero.*
  2. **Che cosa non è**: *non contiene Rossi né 4471: quelli stanno nel grafo delle istanze (sezione 5), nelle tabelle, nei documenti. L'ontologia è lo schema del significato: come il DDL dice la forma di una tabella, l'ontologia dice che cosa vuol dire, e come si collega al resto.*
  3. **Da dove si comincia**: *da un'ontologia piccola ma completa, non da un glossario piatto: le classi, le loro proprietà (`Spedizione`: data prevista, data consegna, importo), le relazioni fra classi, una definizione e un responsabile per ciascuna. È la relazione che permette di rispondere, e la proprietà che permette di mappare una colonna.*
  4. **Un'ontologia cross, e le ontologie di dominio**: *i concetti validi per tutta l'organizzazione (`Cliente`, `Ordine`, `Prodotto`, `Fornitore`) stanno in un'ontologia principale, cross; ogni dipartimento ha la sua ontologia di dominio (la logistica: `Spedizione`, `Corriere`, `Ritardo`, `Penale`; l'amministrazione: `Fattura`, `Nota di credito`) che estende la principale e le si collega: `Corriere` è un `Fornitore`, `Penale` riduce una `Fattura`. Le definizioni locali restano locali; le identità sono condivise.*
- Nota in basso: *L'ontologia è compounding per definizione: ogni classe nuova si aggancia alle esistenti, e ogni fonte nuova (una tabella, un archivio, un grafo) si mappa sulle classi che ci sono invece di inventare le proprie. Ed è ciò che l'agente legge per capire che `dim_corriere.nome`, "il Vettore" del contratto e il nodo `SpedFast` sono la stessa cosa.*

**Visual**: `slide55-ontologia.svg`.

**Prompt per schema SVG**:
> Un'ontologia a due livelli. **In alto**, un riquadro `ontologia cross` con le classi `Cliente` · `Ordine` · `Prodotto` · `Fornitore` (ellissi) e le relazioni fra loro (`Cliente –ordina→ Ordine`, `Ordine –contiene→ Prodotto`). **Sotto**, due riquadri affiancati: `dominio logistica` con `Spedizione` (proprietà: `data prevista · data consegna · importo`) · `Corriere` · `Ritardo` · `Penale` · `Contratto`, e le relazioni (`Spedizione –consegnata da→ Corriere`, `Contratto –vincola→ Corriere`, `Spedizione –ha→ Ritardo`, `Ritardo –attiva→ Penale`); `dominio amministrazione` con `Fattura` · `Nota di credito`. Archi tratteggiati verso l'alto e fra domini: `Corriere ⊂ Fornitore`, `Spedizione –di→ Ordine`, `Penale –riduce→ Fattura`.
>
> Accanto a due classi, un riquadro con definizione e sinonimi: per `Corriere`: *"azienda che effettua la consegna di una spedizione per conto di Acme" · vettore, trasportatore · owner: acquisti*; per `Ritardo`: *"giorni lavorativi fra data prevista e consegna, festivi esclusi" · owner: logistica*.
>
> **Sotto i domini**, tre frecce di mappatura dalla classe `Corriere` verso tre forme in miniatura: `dim_corriere` (tabella), `Corriere #17` (nodo del grafo delle istanze), `"il Vettore"` (entità nel contratto).
>
> **Elemento focale**: gli archi tratteggiati fra i domini e l'ontologia cross, e la classe `Corriere` con le tre mappature.

## Slide 56 — Nel dato strutturato: il semantic linking

> Riquadro `DEMO` in slide: l'ontologia di Quantyca e il suo linking alle tabelle, se c'è tempo.

**Messaggio**: l'ontologia diventa utile quando ogni sua classe, proprietà e relazione è collegata a una tabella, una colonna, una join: è il semantic linking. Da quel legame escono, senza inventarle, le descrizioni dello schema, le join note, le identità condivise; e l'agente legge tabelle che sanno che cosa vogliono dire.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); in basso a destra, il riquadro tratteggiato `DEMO`; nota in basso.

**Testo**:
- Titolo: *Nel dato strutturato: il semantic linking*
- Punti:
  1. **Che cos'è**: *un collegamento esplicito, mantenuto, fra gli elementi dell'ontologia e gli elementi fisici: la classe `Spedizione` → la tabella `fatto_spedizioni` (una riga = un'istanza: il grano, dichiarato dalla classe); la proprietà `data consegna` → la colonna `data_consegna`; la relazione `Spedizione –consegnata da→ Corriere` → la join `fatto_spedizioni.id_corriere = dim_corriere.id_corriere`. Ogni colonna sa di quale proprietà è la forma fisica, e ne eredita definizione, sinonimi, owner.*
  2. **Che cosa ne esce**: *le descrizioni dello schema non le scrive nessuno a mano: vengono dall'ontologia, una volta, per tutte le tabelle che mappano la stessa classe. Le join note sono le relazioni. La definizione di "ritardo" è una sola, quella della classe, e chi calcola la colonna la deve rispettare. E `dim_corriere.id_corriere = 17` e il nodo `SpedFast` sono la stessa istanza della stessa classe: l'identità è condivisa per costruzione.*
  3. **Come lo usa l'agente**: *nel system prompt entra lo schema annotato dal linking: i requisiti 1, 2, 3 e 4 della slide 45 prodotti dall'ontologia, non da un analista di buona volontà. Il modello scrive SQL su tabelle che sanno che cosa vogliono dire; e quando la domanda usa un concetto che non è mappato, la risposta giusta è "non ho una tabella per questo", non un numero plausibile.*
- Riquadro tratteggiato: *DEMO — l'ontologia di Quantyca e il suo linking alle tabelle. Se c'è tempo.*
- Nota in basso: *I semantic layer dei vendor (le semantic view di Snowflake, le metric view di Databricks, il Semantic Layer di dbt, tutti esposti agli agenti via MCP) fanno una parte di questo lavoro, quella delle metriche. Il linking è più largo: parte dall'ontologia, non dalla metrica, e copre anche ciò che non si somma.*

**Visual**: `slide56-semantic-linking.svg`.

**Prompt per schema SVG**:
> **In alto**, l'ontologia di dominio logistica della Slide 55 (classi `Spedizione`, `Corriere`, `Contratto` con le proprietà elencate e le relazioni). **In basso**, lo star schema della Slide 16 (`fatto_spedizioni`, `dim_corriere`) con le colonne elencate.
>
> **Fra i due, i link**, linee che uniscono: la classe `Spedizione` alla tabella `fatto_spedizioni` (etichetta *classe → tabella: il grano*); la proprietà `data consegna` alla colonna `data_consegna`; la proprietà `giorni lavorativi di ritardo` (con la definizione accanto) alla colonna `giorni_lavorativi_ritardo`; la relazione `consegnata da` alla join `id_corriere` (una linea che tocca entrambe le tabelle, etichetta *relazione → join*). Una proprietà dell'ontologia senza link (`margine`) con l'etichetta *non mappata: il modello lo sa*.
>
> **A destra**, la finestra a strati del 27 in miniatura, con lo strato `system prompt` che riceve `schema annotato` da una freccia che parte dai link.
>
> **Elemento focale**: le linee di link, e in particolare quella della relazione che diventa join.

## Slide 57 — Nel dato non strutturato: l'ontologia guida l'estrazione

**Messaggio**: nel testo l'ontologia fa due cose: dice al modello che estrae quali tipi di entità e relazione cercare, con gli stessi nomi e le stesse identità del dato strutturato; e dà a ogni documento i metadati di ciclo di vita che la slide 28 non aveva. Il lexical graph smette di essere un grafo a sé.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): la pagina evidenziata, l'agente, il grafo estratto; nota in basso.

**Testo**:
- Titolo: *Nel dato non strutturato: l'ontologia guida l'estrazione*
- Punti:
  1. **Il prompt di estrazione è l'ontologia**: *nella slide 50 il modello estraeva "le cose di cui parla il chunk", a modo suo: tre nodi `SpedFast`, un `ritardo` che non si sa se è la classe o l'istanza. Con l'ontologia nel prompt estrae solo classi note (`Corriere`, `Penale`, `Clausola`), con le relazioni note, e ogni entità la risolve a un'identità: "il Vettore" del contratto → `Corriere #17`, lo stesso di `dim_corriere`. Il grafo estratto dal testo e la stella parlano degli stessi oggetti. Ed è un lavoro in cui agenti dedicati sono molto bravi: data un'ontologia, trovano nel testo libero le entità e le relazioni con precisione alta, pagina dopo pagina, e segnalano ciò che non sanno mappare.*
  2. **I metadati del documento**: *l'ontologia ha anche la classe `Documento`, con le sue proprietà: tipo (contratto, policy, reclamo), data di validità, versione, proprietario, stato (bozza, firmato, sostituito), e le relazioni (`Contratto –vincola→ Corriere`, `Policy –sostituisce→ Policy`). Compilarle è il ciclo di vita che mancava: `contratto_SpedFast_v3_FINALE.docx` diventa `Contratto C-2026-07, firmato, valido dal 2026-03-01, sostituisce C-2023-02`.*
  3. **Che cosa cambia per la search**: *i filtri della slide 34 (data, fonte, autorità) diventano proprietà dichiarate, non indovinate dal nome del file; una bozza non entra nell'indice, o entra marcata; e il retrieval può partire dal grafo ("i documenti che vincolano SpedFast") invece che dalla somiglianza.*
- Nota in basso: *È la piramide al contrario, chiusa: dal testo si estraggono fatti (slide 29), ma con i tipi e le identità decisi prima. L'estrazione resta un'interpretazione, e può sbagliare: per questo il grafo estratto è un prodotto (slide 54), con un owner e un'affidabilità dichiarata.*

**Visual**: `slide57-estrazione-guidata.svg`.

**Prompt per schema SVG**:
> **A sinistra, grande, una pagina del contratto**: l'art. 7 e le righe intorno, sette o otto righe di testo leggibile, con le entità **evidenziate nel testo** con un colore per classe e l'etichetta della classe sopra la parola: `il Vettore` → `Corriere #17`; `penale pari al 2%` → `Penale (2%)`; `terzo giorno lavorativo` → `Soglia ritardo (3 gg lavorativi)`; `data concordata` → `Data prevista`; `Acme S.p.A.` → `Cliente del contratto`; una parola non mappata (`franco magazzino`) con un'evidenza grigia e un `?`. Accanto alla pagina, una legenda delle classi con i colori: è l'ontologia di dominio in forma di lista.
>
> **Al centro**, il blocco `agente di estrazione`, con in ingresso dall'alto un riquadro `ontologia: classi, relazioni, identità`.
>
> **A destra**, il grafo estratto: `Contratto C-2026-07` con la scheda `tipo: contratto · stato: firmato · valido dal 2026-03-01 · sostituisce C-2023-02 · owner: acquisti`, –`vincola`→ `Corriere #17 (SpedFast)`; `Clausola art. 7` –`prevede`→ `Penale 2%` –`oltre`→ `Soglia 3 gg lavorativi`; da `Corriere #17` una linea tratteggiata verso `dim_corriere · id 17` in miniatura, con l'etichetta *la stessa identità della tabella*.
>
> **Elemento focale**: le evidenziazioni nella pagina, e la corrispondenza uno a uno con i nodi a destra.

## Slide 58 — L'approccio convergente

> La figura madre con la banda dell'ontologia accesa, e la **prima pagella con quattro spunte**.

**Messaggio**: un'ontologia sola sopra tutto lo spettro: le dimensioni della stella, le etichette del grafo, le entità dei documenti condividono classi, definizioni e identità. Ogni forma resta la forma giusta per le sue domande; ciò che converge è il significato.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~30%, classe `tight`); visual al centro (~45%); la pagella a destra (~22%); nota in basso.

**Testo**:
- Titolo: *L'approccio convergente*
- Punti:
  1. **Una sola ontologia, tre forme**: *`Corriere` è una classe; `dim_corriere` ne è la forma tabellare, il nodo `Corriere #17` quella a grafo, "il Vettore" evidenziato nel contratto quella testuale. Stessa definizione, stesso owner, stessa identità. Nessuna forma sostituisce le altre: la stella somma, il grafo percorre, il documento conserva la clausola intera.*
  2. **Le domande attraversano le forme**: *"quanto ci costano i ritardi di SpedFast, contratto alla mano?": la metrica dalla stella, la penale dalla clausola, il legame dal grafo. L'agente della slide 48 lo faceva a fatica, indovinando che erano la stessa cosa; qui lo sa, perché l'ontologia lo dice. Il modo agentico funziona su una KB convergente; su una KB a silos funziona per fortuna.*
  3. **Che cosa non converge**: *i motori, che restano diversi; la governance, che resta per prodotto; e il lavoro, che resta di persone: scrivere e mantenere l'ontologia, fare il linking, decidere le identità. Gli agenti aiutano nell'estrazione e nel controllo; non decidono che cosa vuol dire "ritardo".*
- Pagella (HTML, `.pagella`), quattro ✓, con il perché in piccolo: *progressiva: dalla classe alla forma giusta* · *non ridondante: un'identità per cosa* · *veritiera: un owner per definizione, un contratto per prodotto* · *compounding: ogni fonte nuova si mappa su classi che esistono*. Regola sotto: *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Nota in basso: *"Superare i limiti del data management" non è un altro strumento: è scrivere il significato una volta, sopra gli strumenti che ci sono. È la conoscenza della piramide, ed è ciò che il blocco `KB` della formula contiene davvero.*

**Visual**: `slide58-convergente.svg` — la figura madre con la banda accesa.

**Prompt per schema SVG**:
> La figura della Slide 7: la formula in basso con `KB` esploso nella callout con le tre fasce (`tabella · grafo · documento`; `si interroga · si percorre · si cerca`; `Text2SQL · GraphRAG · RAG · agentic search`). **La banda dell'ontologia sopra le fasce è accesa**, e da una sua classe, `Corriere`, scendono tre linee verso le tre colonne: alla tabella (`dim_corriere`), al nodo del grafo (`Corriere #17`), all'entità nel documento (`il Vettore`), con l'etichetta condivisa *stessa classe, stessa identità*. Le tre colonne restano distinte e accese: nessuna è più grande delle altre.
>
> **Elemento focale**: le tre linee che scendono dalla banda.

## Slide 59 — Know-how: le skill

> Ripresa della slide 26 del 27 (`rimborsi-acme`), eyebrow *dall'incontro 27*. Placeholder per la demo dal vivo sul repo Quantyca.

**Messaggio**: tutto ciò che abbiamo visto oggi è know-what: come stanno le cose. Il know-how, come si fa, sta nelle skill del 27, e usa il know-what: una procedura chiama i tool, e i tool trovano dall'altra parte una KB fatta bene. Se c'è tempo, si vede dal vivo.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~45%); a destra (~50%) il riquadro-skill del 27, sbiadito, e sotto il riquadro tratteggiato `DEMO`; nota in basso.

**Testo**:
- Titolo: *Know-how: le skill*
- Punti:
  1. **Il termine che mancava**: *la formula ha due termini per la conoscenza: `KB`, ciò che l'organizzazione sa, e `Skills`, ciò che sa fare. Oggi abbiamo aperto il primo. Il secondo l'abbiamo visto nel 27: un documento di istruzioni, la procedura che un esperto scriverebbe a un collega nuovo, caricato a richiesta.*
  2. **Il know-how usa il know-what**: *`rimborsi-acme` chiamava `cerca_ordine` e `crea_rimborso`; una skill di oggi chiamerebbe `esegui_sql` sul data warehouse mappato, `cerca_documenti` sui contratti con i metadati, `percorri_grafo`. La procedura è buona quanto ciò che trova dall'altra parte: una skill perfetta su una KB a silos produce risposte perfette e sbagliate.*
  3. **Chi la scrive**: *chi il lavoro lo sa fare, nella lingua in cui lo spiegherebbe a una persona. È il punto in cui l'organizzazione mette il proprio modo di lavorare a disposizione dell'agente, e il posto in cui l'ontologia torna: i nomi che la skill usa sono quelli delle classi.*
- Riquadro-skill (HTML, ripreso dalla slide 26 del 27, sbiadito): il frontmatter e il corpo di `rimborsi-acme`, tali e quali.
- Riquadro tratteggiato: *DEMO — una skill vera, dal repo Quantyca: frontmatter, corpo, i tool che chiama. Se c'è tempo.*
- Nota in basso: *Nel 27: "la KB dice come stanno le cose, la skill dice come si fa; nella formula sono due termini diversi, e nel 28 vedremo perché". Il perché: si scrivono in posti diversi, da persone diverse, e si leggono in momenti diversi. Ma si chiamano a vicenda.*

**Visual**: nessun SVG. Se la demo si fa, la slide resta aperta sullo schermo mentre si passa al repo.

## Slide 60 — La formula, completa

> Ripresa della slide 3 del 26 e della 62 del 27: ultimo dei quattro stati della formula lungo il corso. Chiude il corso; nessun cliffhanger, nessun blocco nero.

**Messaggio**: la formula con cui il corso si è aperto, con tutti e sei i termini accesi. Due si aprono in figura: l'harness nella mappa del 27, la KB nello spettro di oggi con la banda dell'ontologia. È la fotografia completa di un agente.

**Layout**: titolo in alto; la figura occupa tutto il resto della slide (~85%); nessuna nota in basso.

**Testo**:
- Titolo: *La formula, completa*
- Formula (nel visual): `Agent = LLM + Harness + System Prompt + Tools + KB + Skills`
- Le righe di sintesi sotto i termini (nel visual, corte):
  - `LLM` — *sa volere, non sa eseguire (26)*
  - `Harness` — *prepara la finestra, esegue, governa, osserva (27)*
  - `System Prompt` — *ruolo, regole, e lo schema annotato (27, 28)*
  - `Tools` — *un contratto; dietro, un prodotto dati (27, 28)*
  - `KB` — *lo spettro, e il significato sopra (28)*
  - `Skills` — *il know-how che usa il know-what (27, 28)*

**Visual**: `slide60-formula-completa.svg`.

**Prompt per schema SVG**:
> La stessa figura della slide 3 del 26: blocco `Agent`, `=`, sei blocchi in fila alle stesse coordinate, le tre graffe *la CPU* / *il sistema operativo* / *il software installato*. **Tutti e sei i blocchi accesi**, nessuna spunta e nessuna etichetta di incontro.
>
> **Sotto la fila**, la fascia delle sintesi a sei colonne (come la slide 62 del 27, canvas alto), una riga corta per blocco, con il testo elencato sopra.
>
> **Sopra la fila**, due callout affiancate alla stessa altezza: da `Harness` sale la mappa dell'harness del 27 in miniatura (le tre zone, i tre anelli, la fascia di observability); da `KB` sale lo spettro di oggi (le tre fasce e la banda dell'ontologia accesa). Il canvas cresce sopra e sotto; la geometria dei blocchi e delle graffe non cambia.
>
> **Elemento focale**: nessun blocco più degli altri. La lettura da lontano deve essere: tutto acceso, due aperti.
