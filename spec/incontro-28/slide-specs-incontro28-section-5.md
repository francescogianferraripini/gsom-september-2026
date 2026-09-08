# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 5 — In mezzo allo spettro: i grafi**
**Obiettivo di apprendimento**: il partecipante sa che cos'è un property graph (nodi con etichette e proprietà, archi diretti e tipizzati con proprietà), sa leggere una query Cypher come un pattern disegnato, sa perché un database relazionale soffre sui percorsi a profondità variabile, sa che il grafo è un modello di dati che vive su motori diversi, sa perché sta in mezzo allo spettro (la struttura si evolve nel tempo, la navigazione resta deterministica e rigorosa), sa che qui è un knowledge graph di istanze e non l'ontologia, e sa che nessun modello è un silver bullet: ogni forma ha le sue domande.
**Messaggio chiave (takeaway)**: Le relazioni scritte una per una si percorrono come una tabella e si aggiungono come un documento. Ma ogni forma serve le sue domande.
**Budget**: ~14 min, 6 slide + separatore. Ripartizione: nodi e archi 2, Cypher 1, perché non relazionale 1, modello vs motore 1, pagella 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec5.html` | Separatore — Sezione 5: In mezzo allo spettro: i grafi |
| `slides/slide37-nodi-archi.html` | Slide 37 — Le relazioni, scritte una per una |
| `slides/slide38-property-graph.html` | Slide 38 — Il property graph |
| `slides/slide39-cypher.html` | Slide 39 — Cypher: un mini focus |
| `slides/slide40-traversal.html` | Slide 40 — Perché non un database relazionale |
| `slides/slide41-modello-motore.html` | Slide 41 — Il grafo è un modello, non un motore |
| `slides/slide42-pagella-grafi.html` | Slide 42 — La pagella dei grafi, e la cerniera |

---

> **Filo della sezione.** I tre fatti lasciati scollegati dalla cerniera della sezione 4 diventano un grafo (37); il modello vero dei motori a grafo, il property graph, con la coerenza delle proprietà per etichetta (38); Cypher come pattern disegnato, in una slide a cinque tempi in cui il grafo si accende segmento per segmento, come la slide 10 per il SQL (39); perché il relazionale rappresenta bene ma percorre male (40); il grafo come modello che vive su motori diversi, con la tesi del "perché sta in mezzo" e l'avvertenza che non è un silver bullet (41); pagella e cerniera verso i pattern agentici (42). La mini-mappa dei separatori accende la colonna del grafo.
>
> **Tesi della sezione** (dall'*Impianto*): il grafo sta in mezzo allo spettro perché la struttura non va decisa tutta prima, si crea e si evolve nel tempo, un tipo di nodo o di relazione alla volta; ma ciò che c'è si percorre e si interpreta in modo deterministico e rigoroso, come una tabella.
>
> **Principio (deciso in intervista, Slide 41)**: **nessun modello è un silver bullet**. Il data warehouse resta la forma giusta per somme e metriche, un sistema documentale ben organizzato per testi e clausole, il grafo per relazioni e percorsi. Ogni punto dello spettro ha i suoi casi d'uso; il lavoro è mettere ciascun dato nella forma delle domande che riceve, e collegare le forme fra loro (sezione 7). Questo principio va tenuto anche nelle sezioni 6 e 7.
>
> **Due ruoli del grafo** (dall'*Impianto*): qui il grafo delle **cose** (Rossi, 4471, SpedFast); l'ontologia, il grafo dei **tipi di cose**, è la sezione 7. La Slide 37 lo dichiara nella nota; la Slide 38 accenna alle triple RDF come forma delle ontologie.
>
> **Storia**: solo una riga di apertura nella Slide 37 (Eulero 1736, Berners-Lee 1989), con i fatti verificati in `docs/ricerche-28/research-storia-classificazione.md`.
>
> **Esempio Acme in questa sezione**: i nodi `Rossi`, `ordine 4471`, `SpedFast`, `contratto SpedFast 2026`, `reclamo #88`, `Bianchi`, `PostaPro` (contratto senza penale); gli archi `ORDINA`, `SPEDITO_DA` (con `prevista` e `consegna`), `VINCOLA`, `APRE`, `RIGUARDA`, `CONTIENE`; la domanda della Slide 39: "i clienti che hanno fatto un reclamo su un ordine spedito da un corriere il cui contratto prevede una penale" → Rossi, Bianchi.
>
> **Codice in questa sezione**: la query SQL a quattro join e la query Cypher (Slide 39), con la lettura in italiano a fianco.

---

## Slide 37 — Le relazioni, scritte una per una

**Messaggio**: un grafo è la forma più semplice per scrivere una relazione: due cose e un legame con un nome. È un oggetto matematico da tre secoli, è la forma del web da trent'anni, ed è ciò che mancava ai tre fatti della cerniera.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 5 · IN MEZZO ALLO SPETTRO: I GRAFI*
- Titolo: *Le relazioni, scritte una per una*
- Punti:
  1. **Da Eulero a Berners-Lee**: *nel 1736 Eulero risolve il problema dei ponti di Königsberg riducendo la città a punti e linee: nasce la teoria dei grafi. Nel 1989 Berners-Lee propone al CERN "una rete di note con collegamenti, molto più utile di un sistema gerarchico fisso": cerchi e frecce, nodi e link, il web. In mezzo, due secoli e mezzo di matematica su nodi e archi.*
  2. **Nodi e archi**: *un nodo è una cosa: Rossi, l'ordine 4471, SpedFast, il contratto. Un arco è una relazione fra due nodi, con una direzione e un nome: Rossi –ordina→ 4471; 4471 –spedito da→ SpedFast; contratto –vincola→ SpedFast. Niente altro.*
  3. **I tre fatti, collegati**: *nella sezione 4 stavano in tre posti e nessun indice li univa. Qui sono quattro nodi e tre archi, e la domanda "il reclamo di Rossi riguarda un corriere con penale?" è un percorso: da Rossi, lungo gli archi, fino al contratto. Chi legge segue le frecce; non deve sapere nulla dello schema.*
- Nota in basso: *È il grafo delle cose, non dei tipi di cose: Rossi e 4471, non "Cliente" e "Ordine". L'altro grafo, l'ontologia della slide 3, torna nella sezione 7.*

**Visual**: `slide37-nodi-archi.svg`.

**Prompt per schema SVG**:
> **A sinistra**, piccola e attenuata, la vignetta storica in due quadretti: i sette ponti di Königsberg ridotti a quattro punti e sette linee, con la data `1736`; accanto, lo schizzo di cerchi e frecce della proposta del CERN, con la data `1989` e l'etichetta *nodi e link*.
>
> **A destra**, grande, il grafo dei tre fatti: nodi `Rossi` · `ordine 4471` · `SpedFast` · `contratto SpedFast 2026` · `reclamo #88`; archi diretti con il nome: `Rossi –ordina→ ordine 4471`, `ordine 4471 –spedito da→ SpedFast`, `contratto SpedFast 2026 –vincola→ SpedFast`, `reclamo #88 –riguarda→ ordine 4471`. Un percorso evidenziato da `Rossi` a `contratto` lungo tre archi, con l'etichetta *tre passi*.
>
> **Elemento focale**: il percorso evidenziato.

## Slide 38 — Il property graph

**Messaggio**: il modello che i database a grafo usano davvero è il property graph: nodi con un'etichetta e delle proprietà, archi diretti con un tipo e, anche loro, delle proprietà. Le proprietà stanno dove appartengono: la data di un ordine sul nodo, la data di consegna sull'arco.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%): il grafo Acme completo con le proprietà; nota in basso.

**Testo**:
- Titolo: *Il property graph*
- Punti:
  1. **I nodi**: *ogni nodo ha una o più etichette, che dicono che tipo di cosa è (`Cliente`, `Ordine`, `Corriere`), e delle proprietà chiave-valore (`nome: "Rossi"`, `importo: 184.30`). Il motore non impone uno schema: due nodi `Cliente` possono avere proprietà diverse. Ma è meglio che non lo facciano: la stessa etichetta, le stesse proprietà, altrimenti chi percorre il grafo, persona o modello, non sa che cosa aspettarsi. La libertà serve per aggiungere un tipo nuovo, non per tenere in disordine quelli che ci sono.*
  2. **Gli archi**: *ogni arco ha una direzione, un tipo (`ORDINA`, `SPEDITO_DA`, `VINCOLA`) e, se serve, proprietà sue: su `SPEDITO_DA` stanno `data_prevista` e `data_consegna`, perché appartengono alla relazione fra quell'ordine e quel corriere, non a uno dei due.*
  3. **L'altra forma: le triple**: *il web semantico scrive lo stesso grafo come triple soggetto–predicato–oggetto (`4471 spedito_da SpedFast`), con nomi globali (URI) e senza proprietà sugli archi. Stessa idea, più rigida e più interoperabile: è la forma delle ontologie, sezione 7.*
- Nota in basso: *Nel data warehouse il ritardo era una colonna del fatto; qui è una proprietà dell'arco `SPEDITO_DA`, o si calcola dalle sue date. Il fatto di Kimball e l'arco del grafo sono la stessa cosa vista da due modelli: una relazione fra dimensioni, con delle misure sopra.*

**Visual**: `slide38-property-graph.svg`.

**Prompt per schema SVG**:
> Il grafo Acme completo. I nodi sono cerchi con l'etichetta dentro e un riquadro di proprietà accanto; gli archi sono frecce con il tipo in maiuscolo e, dove ci sono, le proprietà in un riquadro più piccolo sull'arco:
> - `Cliente {nome: Rossi, regione: Lombardia}` –`ORDINA {data: 2026-08-12}`→ `Ordine {id: 4471, importo: 184.30}`
> - `Ordine 4471` –`SPEDITO_DA {prevista: 2026-08-14, consegna: 2026-08-19}`→ `Corriere {nome: SpedFast, tipo: espresso}`
> - `Contratto {id: C-2026-07, penale: 2%}` –`VINCOLA {dal: 2026-03-01}`→ `Corriere SpedFast`
> - `Reclamo {id: 88, testo: "terza consegna in ritardo"}` –`RIGUARDA`→ `Ordine 4471`; `Cliente Rossi` –`APRE`→ `Reclamo 88`
> - `Ordine 4471` –`CONTIENE {q: 2}`→ `Prodotto {sku: AX-210}`
>
> **Elemento focale**: l'arco `SPEDITO_DA` con il riquadro delle sue proprietà in evidenza e l'etichetta *le proprietà stanno dove appartengono*.

## Slide 39 — Cypher: un mini focus

> Slide a **cinque tempi** (fragment), in rima con la Slide 10: a ogni tempo si accende un segmento del pattern nel riquadro Cypher e, nel grafo a fianco, i nodi e gli archi che quel segmento raggiunge; al quinto tempo il `WHERE` spegne un ramo e il `RETURN` evidenzia la risposta.

**Messaggio**: una query a grafo si scrive disegnando il percorso: parentesi tonde per i nodi, frecce per gli archi, il pattern che si cerca. La stessa domanda in SQL è una catena di join che nasconde il percorso dentro le chiavi.

**Layout**: titolo in alto; a sinistra (~30%) i tre punti, con il riquadro SQL piccolo e statico sotto (resta come confronto, attenuato); al centro (~30%) il riquadro Cypher, in cui a ogni tempo si accende un segmento del pattern; a destra (~40%) il grafo Acme in cui si accendono o spengono nodi e archi; nota in basso.

**Testo**:
- Titolo: *Cypher: un mini focus*
- Punti:
  1. **La domanda**: *"i clienti che hanno fatto un reclamo su un ordine spedito da un corriere il cui contratto prevede una penale". Quattro relazioni in fila: cliente → reclamo → ordine → corriere → contratto.*
  2. **In SQL**: *quattro join, ognuna con la sua coppia di chiavi, e bisogna sapere quali. Il percorso c'è, ma è nascosto nelle condizioni `ON`.*
  3. **In Cypher**: *si disegna il percorso: le parentesi tonde sono nodi, le frecce archi, i nomi fra parentesi quadre i tipi. Si legge come si pensa; e il pattern è lo schema.*
- Riquadro SQL (HTML, piccolo, attenuato, con la lettura a fianco):
  ```
  -- SQL: quattro join
  SELECT DISTINCT c.nome
  FROM clienti c
  JOIN reclami    r ON r.id_cliente = c.id_cliente
  JOIN ordini     o ON o.id_ordine  = r.id_ordine
  JOIN spedizioni s ON s.id_ordine  = o.id_ordine
  JOIN contratti  t ON t.corriere   = s.corriere
  WHERE t.penale > 0;
  ```
- Riquadro Cypher (HTML, con i cinque segmenti colorati a tempi, lettura a fianco):
  ```
  // Cypher: un pattern
  MATCH (c:Cliente)-[:APRE]->(:Reclamo)
        -[:RIGUARDA]->(:Ordine)
        -[:SPEDITO_DA]->(:Corriere)
        <-[:VINCOLA]-(t:Contratto)
  WHERE t.penale > 0
  RETURN DISTINCT c.nome
  ```
- Nota in basso: *Per un modello, il secondo è più facile da scrivere giusto: il pattern è la domanda, e gli errori di join (la chiave sbagliata, il fanout) non hanno dove nascondersi. Torna nella sezione 6.*

**Visual**: i due riquadri in HTML + `slide39-cypher-{1..5}.svg` (`.visual.stack` + fragment, stesso viewBox).

**Prompt per schema SVG**:
> La base è il grafo Acme della Slide 38, allargato a una decina di nodi: tre clienti (`Rossi`, `Bianchi`, `Verdi`), quattro reclami, quattro ordini, tre corrieri (`SpedFast`, `Corriere Nord`, `PostaPro`), tre contratti, di cui quello di `PostaPro` con `penale: 0`. `Verdi` non ha reclami; un reclamo riguarda un ordine senza spedizione. Tutto parte attenuato. Cinque tempi:
> 1. **`(c:Cliente)-[:APRE]->(:Reclamo)`**: si accendono i nodi `Cliente` che hanno un arco `APRE` verso un `Reclamo`, e quegli archi e reclami; `Verdi` resta spento.
> 2. **`-[:RIGUARDA]->(:Ordine)`**: si accendono gli ordini raggiunti dai reclami accesi; il percorso si allunga di un passo.
> 3. **`-[:SPEDITO_DA]->(:Corriere)`**: si accendono i corrieri raggiunti; il reclamo il cui ordine non ha spedizione si spegne, con l'etichetta *il pattern non chiude*.
> 4. **`<-[:VINCOLA]-(t:Contratto)`**: si accendono i contratti dei corrieri accesi; una piccola nota: *la freccia è al contrario, e nel grafo si vede*.
> 5. **`WHERE t.penale > 0` · `RETURN DISTINCT c.nome`**: il contratto di `PostaPro` (`penale: 0`) si spegne e con lui tutto il percorso che ci arrivava; restano accesi due percorsi completi, e in cima ai due percorsi i nodi `Cliente` ricevono un bordo in evidenza: `Rossi` · `Bianchi`, con l'etichetta *la risposta*.
>
> **Elemento focale**: a ogni tempo, il segmento del pattern e i nodi che accende, con la stessa tinta; al tempo 5, i due clienti in evidenza e il ramo spento di PostaPro.

## Slide 40 — Perché non un database relazionale

**Messaggio**: un relazionale rappresenta un grafo benissimo (una tabella di nodi, una di archi); soffre quando lo deve percorrere: ogni passo è una join, e una domanda a profondità variabile ("in quanti passi da Rossi a SpedFast?") diventa una join ricorsiva che costa sempre di più. Nel grafo un passo costa sempre uguale.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Perché non un database relazionale*
- Punti:
  1. **Rappresentare è facile**: *due tabelle, `nodi (id, etichetta, proprietà)` e `archi (da, a, tipo, proprietà)`, tengono qualsiasi grafo. Il modello non è il problema.*
  2. **Percorrere è il problema**: *ogni passo lungo un arco è una join fra `archi` e `nodi`; un percorso di quattro passi è quattro join; "tutti i nodi raggiungibili da Rossi" non ha un numero di passi noto prima, e vuole una query ricorsiva. Il costo di una join dipende dalla dimensione delle tabelle: con milioni di archi, ogni passo rilegge milioni di righe.*
  3. **Nel grafo un passo costa uguale**: *un motore a grafo tiene, per ogni nodo, i puntatori ai suoi archi (adiacenza senza indice): andare da Rossi ai suoi ordini costa quanto i suoi ordini, non quanto tutti gli ordini. Il percorso più breve, i vicini a tre passi, le comunità: domande che nel relazionale sono ore, qui sono millisecondi.*
- Nota in basso: *La regola pratica: se le domande hanno una profondità fissa e piccola (una o due join), il relazionale basta. Se la profondità è variabile o alta, o la domanda è "come sono collegati questi due?", serve un grafo.*

**Visual**: `slide40-traversal.svg`.

**Prompt per schema SVG**:
> Due pannelli affiancati, divisi da un filo verticale.
>
> **Pannello sinistro — «relazionale»**: in alto le due tabelle `nodi` e `archi`; sotto, tre fotogrammi di join con altezze crescenti, etichettati `1 passo: 1 join · 2 M righe lette` → `2 passi: 2 join` → `3 passi: 3 join`, ognuno visibilmente più alto del precedente; etichetta sotto: *ogni passo rilegge la tabella*.
>
> **Pannello destro — «grafo»**: il nodo `Rossi` al centro; intorno, in tre cerchi concentrici, i suoi tre ordini (1 passo), poi i corrieri (2 passi), poi i contratti (3 passi), collegati da archi; etichetta `1 passo = i vicini · 2 passi · 3 passi`; sotto, un costo piatto: `~10 · ~30 · ~90 nodi toccati`.
>
> **Elemento focale**: le altezze crescenti a sinistra contro il costo piatto a destra.

## Slide 41 — Il grafo è un modello, non un motore

> Qui la **tesi della sezione** e il principio **"nessun modello è un silver bullet"** (deciso in intervista).

**Messaggio**: il grafo sta in mezzo allo spettro per una ragione precisa: la struttura si evolve nel tempo, un tipo di nodo o di relazione alla volta, senza migrazioni; ma ciò che c'è si percorre in modo deterministico e rigoroso, come una tabella. E questo modello vive su motori diversi: si sceglie il modello, poi il motore.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il grafo è un modello, non un motore*
- Punti:
  1. **La struttura si evolve**: *arrivano le fatture dei corrieri: un'etichetta nuova, `Fattura`, e un arco nuovo, `FATTURA`→`Spedizione`. Nessuna tabella da alterare, nessun ETL da rifare, nessun fatto da ridisegnare: i nodi vecchi non se ne accorgono. È la libertà del documento, sulla struttura invece che sul contenuto.*
  2. **Ma la navigazione resta rigorosa**: *un arco c'è o non c'è; un percorso esiste o non esiste; il risultato di un pattern è lo stesso oggi e domani. Niente punteggi, niente "forse": è il determinismo della tabella, sulle relazioni.*
  3. **Motori diversi, stesso modello**: *Neo4j e simili, nati per questo (Cypher, adiacenza senza indice). Ma anche due tabelle `nodi` e `archi` in Postgres o DuckDB con query ricorsive, quando i percorsi sono corti. E il data vault della slide 24: hub, link, satelliti sono un grafo scritto in tabelle. Il modello è la decisione; il motore è una conseguenza del volume e della profondità.*
- Nota in basso: *Il grafo non è la forma migliore: è la forma giusta per le domande di relazione e di percorso. Le somme per corriere restano più semplici e più veloci nello star schema; una clausola di contratto resta un documento, e un sistema documentale ben organizzato la serve meglio di qualsiasi nodo. Ogni punto dello spettro ha i suoi casi d'uso: il lavoro è mettere ciascun dato nella forma delle domande che riceve, e collegare le forme fra loro (sezione 7).*

**Visual**: `slide41-modello-motore.svg`.

**Prompt per schema SVG**:
> **In alto**, il grafo Acme in piccolo, con un nodo `Fattura` e un arco `FATTURA` tratteggiati che si aggiungono di lato, etichetta *aggiunto senza toccare il resto*.
>
> **Al centro**, tre riquadri affiancati, tutti con la stessa mini-figura del grafo dentro: `Neo4j · Cypher · adiacenza senza indice` · `Postgres / DuckDB · tabelle nodi + archi · query ricorsive` · `data vault · hub + link + satelliti`; una graffa sopra i tre con l'etichetta *lo stesso modello*.
>
> **In basso**, una riga a tre celle, promemoria del principio: `somme e metriche → star schema` · `relazioni e percorsi → grafo` · `testi e clausole → documentale`.
>
> **Elemento focale**: la graffa e le tre figure identiche dentro riquadri diversi; secondo elemento, la riga a tre celle in basso.

## Slide 42 — La pagella dei grafi, e la cerniera

**Messaggio**: il grafo è il modello che accumula meglio: ogni relazione nuova rende più utili quelle che c'erano. Il suo costo è che le relazioni le deve scrivere qualcuno, una per una; e quello che scrive decide se il grafo è vero.

**Layout**: come le Slide 13, 27 e 36: la pagella a sinistra (~45%) con voti e perché, regola del punto di vista sotto; a destra (~50%) la mini-mappa dello spettro con le tre colonne degli oggetti spuntate e la fascia dei pattern agentici che si accende; blocco nero centrato in basso.

**Testo**:
- Titolo: *La pagella dei grafi, e la cerniera*
- Pagella (HTML, `.pagella`), voti dal punto di vista di chi fa domande:
  1. **Ricercabile in modo progressivo**: **✓** — *si parte da un nodo e si scende lungo gli archi, un passo alla volta: da Rossi ai suoi ordini, da un ordine al suo corriere. È la ricerca progressiva per costruzione, sulle relazioni invece che sulle dimensioni. Non sostituisce le somme (star) né la ricerca nel testo (search).*
  2. **Non ridondante**: **✓** — *ogni cosa è un nodo, una volta: SpedFast è un nodo solo, e tutte le spedizioni, i contratti, i reclami lo puntano. La ridondanza del documento (SpedFast scritto in mille chunk) qui sparisce.*
  3. **Veritiera**: **~** — *un arco è vero se chi l'ha scritto aveva ragione. Se gli archi vengono da un ETL dal transazionale, valgono quanto il transazionale; se li ha estratti un modello da un testo (sezione 6 e 7), valgono quanto l'estrazione. Il grafo non ha un modo proprio di sapere che un arco è sbagliato.*
  4. **Compounding**: **✓** — *il requisito in cui il grafo batte tutto: un nodo o un arco nuovo si aggancia a ciò che c'è e rende raggiungibile ciò che prima non lo era. Il contratto aggiunto oggi rende rispondibile la domanda sul reclamo di ieri.*
- Regola sotto la pagella: *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Blocco nero centrato (la cerniera): *Tabelle da interrogare, documenti da cercare, grafi da percorrere: tre forme, ognuna per le sue domande. Ora la domanda la fa un agente: come entra in ciascuna forma, e dove sbaglia. Sezione 6.*

**Visual**: la pagella in HTML + la mini-mappa dello spettro (`minimap` della Slide 7 con le tre colonne degli oggetti spuntate e la fascia `pattern agentici` come elemento focale).
