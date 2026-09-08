# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 2 — Il dato strutturato, 1/2: dove nasce**
**Obiettivo di apprendimento**: il partecipante sa collocare un dato strutturato su due assi (forma: relazionale o document; fine: transazionale o analitico), sa leggere una tabella relazionale (colonne, tipi, chiave primaria, chiave esterna) e una query nei suoi quattro verbi, sa che il transazionale è normalizzato per ottimizzare le scritture a scapito dell'accessibilità analitica, e sa perché non è opportuno che un agente lo raggiunga se non attraverso i tool.
**Messaggio chiave (takeaway)**: Il transazionale è fatto per scrivere bene, non per rispondere a domande. Sta dietro i tool; davanti all'agente serve un'altra forma dello stesso dato.
**Budget**: ~15 min, 6 slide + separatore. Ripartizione: assi 1, relazionale e SQL 2, transazionale e normalizzazione 2, pagella e cerniera 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec2.html` | Separatore — Sezione 2: Il dato strutturato, 1/2: dove nasce |
| `slides/slide8-due-assi.html` | Slide 8 — Forma e fine: due assi |
| `slides/slide9-relazionale.html` | Slide 9 — Il modello relazionale: tabelle, tipi, chiavi |
| `slides/slide10-sql-quattro-verbi.html` | Slide 10 — Il SQL: quattro verbi |
| `slides/slide11-transazionale.html` | Slide 11 — Il transazionale: per chi è fatto |
| `slides/slide12-normalizzazione.html` | Slide 12 — La normalizzazione |
| `slides/slide13-pagella-transazionale.html` | Slide 13 — La pagella del transazionale, e la cerniera |

---

> **Filo della sezione.** Due assi per orientarsi (Slide 8), poi il relazionale con il suo alfabeto (tabelle, tipi, chiavi: Slide 9) e la sua grammatica (i quattro verbi del SQL: Slide 10); poi per chi è fatto il transazionale (Slide 11) e la regola che ne deriva, la normalizzazione, dichiarata come ottimizzazione prestazionale *a scapito* dell'accessibilità analitica (Slide 12); infine la pagella e la cerniera verso la sezione 3 (Slide 13). La mini-mappa dei separatori accende la colonna della tabella.
>
> **La 3 è un approfondimento della 2** (vedi *Impianto*, sezione 1): la cerniera della Slide 13 lo dichiara. Il grano nasce nel transazionale: "nessuna trasformazione a valle inventa un dettaglio che a monte non c'è".
>
> **Slide tolta in intervista**: "Da Excel al data warehouse" (le tre forme del dato: foglio, transazionale, stella) era ridondante con la sezione 3; diventa la **prima slide della sezione 3**, come ingresso motivazionale a Kimball. Il suo messaggio sul grano è passato nella cerniera della Slide 13.
>
> **Il "perché solo dai tool"** è in Slide 11 (terzo blocco): le regole vivono nell'applicazione, e con esse la sicurezza (nel transazionale sta nell'applicazione, quindi nel tool; nell'analitico sta nel database: Slide 20); il transazionale è dimensionato per scritture piccole; lo schema è difficile da leggere per il modello. E la Slide 13 aggiunge: anche in sola lettura, l'accesso va mediato dai tool, perché lo schema è pieno di ambiguità rischiose.
>
> **La pagella** (Slide 13) si legge sempre *dal punto di vista di chi fa domande, una persona o un agente*, e la regola è scritta sotto la pagella; tre valori (✓ · ~ · ✗) e una riga di perché per ogni voto.
>
> **Esempio Acme in questa sezione**: le tabelle `clienti`, `ordini`, `spedizioni`, `prodotti` dietro `cerca_ordine`; l'ordine 4471; i corrieri SpedFast, Corriere Nord, PostaPro; la domanda della slide 20 del 27 ("quanti ordini di agosto sono in ritardo, e per quale corriere?") scritta in SQL nella Slide 10, con i numeri del 27 (187 in ritardo; SpedFast 121, Corriere Nord 44, PostaPro 22).
>
> **Codice in questa sezione**: DDL breve (Slide 9, da saltare a voce se il tempo stringe) e una query (Slide 10), sempre con la lettura in italiano a fianco.

---

## Slide 8 — Forma e fine: due assi

**Messaggio**: prima di parlare di tabelle, due domande su qualsiasi dato strutturato: in che forma è tenuto (relazionale o documento) e a che cosa serve (scrivere transazioni o rispondere a domande). Le risposte sono indipendenti, e l'AI vive quasi tutta in una cella.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): la matrice 2×2; nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 2 · IL DATO STRUTTURATO, 1/2: DOVE NASCE*
- Titolo: *Forma e fine: due assi*
- Punti:
  1. **La forma**: *relazionale: tabelle con colonne fisse, lo schema deciso prima, le relazioni per chiave. Document: un record è un documento JSON, con i campi che servono a lui, annidati; lo schema lo decide chi scrive.*
  2. **Il fine**: *transazionale: registrare ciò che succede, una riga alla volta, in fretta e senza perdere nulla. Analitico: rispondere a domande su ciò che è successo, leggendo milioni di righe insieme.*
  3. **Dove vive l'AI**: *l'agente scrive poco e chiede molto: quasi tutto ciò che vediamo oggi sta nella colonna analitica. Il transazionale lo raggiunge solo attraverso i tool, e la slide 11 dice perché.*
- Nota in basso: *Il relazionale è la forma che non si può non conoscere: anche chi sceglie il documento, o il grafo, ragiona per differenza da lì.*

**Visual**: `slide8-due-assi.svg` — matrice 2×2.

**Prompt per schema SVG**:
> Una matrice 2×2. Righe (la forma): `relazionale` · `document (JSON)`. Colonne (il fine): `transazionale` · `analitico`. In ogni cella un esempio Acme, con un titolo breve e una riga sotto:
> - relazionale × transazionale: `il DB degli ordini` — *dietro `cerca_ordine`*;
> - document × transazionale: `il carrello e il profilo cliente` — *un JSON per cliente, nell'e-commerce*;
> - relazionale × analitico: `il data warehouse vendite` — *fatti e dimensioni (sezione 3)*;
> - document × analitico: `gli eventi di navigazione e i log` — *un JSON per evento, letti a lotti*.
>
> La cella relazionale × analitico è l'**elemento focale**, con l'etichetta *qui entra l'agente*. Una freccia sottile dalla cella relazionale × transazionale a quella relazionale × analitico, etichettata *la struttura deriva da qui*.

## Slide 9 — Il modello relazionale: tabelle, tipi, chiavi

**Messaggio**: una tabella è una promessa fatta prima di scrivere: ogni colonna ha un nome e un tipo, ogni riga ha una chiave, e le relazioni fra tabelle sono chiavi che si rimandano. È per questo che il fatto sta in una cella e si può interrogare.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); a destra (~55%) il riquadro DDL con la lettura a fianco e, sotto, la mini-figura delle due tabelle con la freccia fra le chiavi; nota in basso.

**Testo**:
- Titolo: *Il modello relazionale: tabelle, tipi, chiavi*
- Punti:
  1. **Colonne e tipi**: *lo schema è deciso prima: ogni colonna ha un nome e un tipo. `3` in una colonna `giorni_ritardo INT` è un numero su cui si può sommare e confrontare; "3 giorni circa" in una cella di testo no. Il tipo è il primo pezzo di contesto della piramide.*
  2. **La chiave primaria**: *una colonna che identifica la riga una volta sola: `4471` è un ordine e uno solo. È ciò che rende un fatto ritrovabile.*
  3. **La chiave esterna**: *una colonna che contiene la chiave di un'altra tabella: la spedizione porta l'`id_ordine`, l'ordine porta l'`id_cliente`. Le relazioni non sono disegnate: sono valori che si rimandano.*
- Riquadro DDL (HTML, monospaziato, con la lettura in italiano a fianco di ogni riga; **da saltare a voce se il tempo stringe**):
  ```
  CREATE TABLE ordini (
    id_ordine    INT PRIMARY KEY,          -- un numero, unico: la chiave
    id_cliente   INT REFERENCES clienti,   -- rimanda a un cliente
    data_ordine  DATE,                     -- una data, non un testo
    importo      DECIMAL(10,2)             -- euro, con due decimali
  );
  CREATE TABLE spedizioni (
    id_spedizione  INT PRIMARY KEY,
    id_ordine      INT REFERENCES ordini,  -- rimanda a un ordine
    corriere       VARCHAR(40),
    data_prevista  DATE,
    data_consegna  DATE
  );
  ```
- Nota in basso: *Quattro tabelle così (`clienti`, `ordini`, `spedizioni`, `prodotti`) sono ciò che sta dietro `cerca_ordine`. Il ritardo non è una colonna: è `data_consegna − data_prevista`, calcolato quando serve. Segnatevelo: torna nella sezione 3.*

**Visual**: il riquadro DDL in HTML + `slide9-chiavi.svg` (mini-figura).

**Prompt per schema SVG**:
> Due tabelle disegnate come griglie, `ordini` a sinistra e `spedizioni` a destra, ognuna con l'intestazione delle colonne (quelle del DDL) e tre righe di esempio: in `ordini` gli id `4471`, `4472`, `4473` con `id_cliente`, data e importo; in `spedizioni` tre righe con `id_ordine` `4471`, `4471`, `4473` (un ordine con due spedizioni), corriere `SpedFast` / `Corriere Nord` / `SpedFast`, date previste e di consegna. La colonna `id_ordine` di `ordini` è marcata `PK`, quella di `spedizioni` `FK`. Una freccia dalla colonna `id_ordine` di `spedizioni` alla chiave di `ordini`, etichettata *chiave esterna → chiave primaria*.
>
> **Elemento focale**: la freccia fra le due colonne. Il viewBox è ritagliato al contenuto: la figura sta sotto il riquadro DDL, in una colonna da ~55%.

## Slide 10 — Il SQL: quattro verbi

> Slide a **quattro tempi** (fragment): a ogni tempo si accende un verbo a sinistra, la riga corrispondente nella query, e la parte dello schema che quel verbo tocca. La figura base è quella della Slide 9.

**Messaggio**: quasi ogni domanda a un dato strutturato si scrive con quattro verbi: che cosa voglio, da dove e con che cosa lo unisco, quali righe tengo, come le raggruppo. Il SQL è il modo standard di fare domande a una tabella, e sarà anche quello dell'agente.

**Layout**: titolo in alto; i quattro verbi a sinistra (~30%), che si accendono uno alla volta; al centro il riquadro della query (~30%), in cui a ogni tempo si accende la riga del verbo; a destra (~40%) lo schema con le righe di esempio, in cui si accende la parte che il verbo tocca; nota in basso. Le quattro tinte dei verbi sono le stesse nei tre elementi.

**Testo**:
- Titolo: *Il SQL: quattro verbi*
- I quattro verbi:
  1. **`SELECT`: che cosa voglio**: *dati (colonne così come sono: il corriere) e metriche (numeri calcolati su più righe: quante spedizioni, quanti giorni di ritardo in media).*
  2. **`FROM … JOIN`: da dove, e con che cosa**: *la tabella di partenza e quelle da unire, agganciate per chiave: la spedizione con il suo ordine. È la chiave esterna della slide 9, usata.*
  3. **`WHERE`: quali righe tengo**: *il filtro, riga per riga: solo agosto, solo le consegne arrivate dopo la data prevista.*
  4. **`GROUP BY`: come le raggruppo**: *una riga di risultato per ogni valore: un totale per corriere. È ciò che trasforma righe in metriche.*
- Riquadro query (HTML, monospaziato, con la lettura in italiano a fianco):
  ```
  SELECT   s.corriere,
           COUNT(*)                                AS ordini_in_ritardo,
           AVG(s.data_consegna - s.data_prevista)  AS ritardo_medio_gg
  FROM     spedizioni s
  JOIN     ordini o ON o.id_ordine = s.id_ordine
  WHERE    o.data_ordine BETWEEN '2026-08-01' AND '2026-08-31'
  AND      s.data_consegna > s.data_prevista
  GROUP BY s.corriere;
  ```
  Sotto il riquadro, il risultato in tre righe: `SpedFast · 121 · 3,8` · `Corriere Nord · 44 · 1,9` · `PostaPro · 22 · 1,2`.
- Nota in basso: *È la domanda della slide 20 del 27, quella che il modello aveva risolto con quattro righe di Python su un export. Qui è una query: la stessa domanda, fatta al dato dove sta. Nella sezione 6 la scriverà il modello.*

**Visual**: `slide10-sql-{1..4}.svg` — lo schema in quattro tempi (`.visual.stack` + fragment, stesso viewBox).

**Prompt per schema SVG**:
> La base è la figura della Slide 9: le due tabelle `ordini` e `spedizioni` come griglie, ora con **sei righe di esempio ciascuna** (ordini di agosto e non; consegne in orario e in ritardo; i tre corrieri) e la freccia fra le chiavi. Quattro tempi:
> 1. **`SELECT`**: si accendono, nella tabella `spedizioni`, la colonna `corriere` e, a lato, due colonne tratteggiate `ordini_in_ritardo` e `ritardo_medio_gg` con l'etichetta *non esistono nella tabella: si calcolano*. Il resto attenuato.
> 2. **`FROM … JOIN`**: si accendono le due tabelle intere e la freccia `id_ordine → id_ordine`; le righe si allineano a coppie spedizione–ordine.
> 3. **`WHERE`**: le coppie che non passano il filtro (ordine non di agosto, consegna in orario) si attenuano con una riga barrata; restano accese quattro righe.
> 4. **`GROUP BY`**: le righe accese si contraggono in tre righe di risultato, una per corriere, con i totali `121 · 3,8`, `44 · 1,9`, `22 · 1,2`; una piccola nota: *totali di agosto: le sei righe qui sopra sono un campione*.
>
> **Elemento focale**: a ogni tempo, la zona dello schema che il verbo tocca, con la stessa tinta della riga della query e del verbo a sinistra.

## Slide 11 — Il transazionale: per chi è fatto

**Messaggio**: il transazionale ha due requisiti, scrivere in fretta senza perdere nulla e cambiare le cose in un posto solo; il suo lettore è l'applicazione, non chi fa domande. Per questo non è opportuno che sia accessibile all'agente se non attraverso i tool.

**Layout**: titolo in alto; i due requisiti in alto come due colonne (~30% dell'altezza); sotto, il blocco a tre punti (~50%), con a destra, sbiadito, il riquadro-definizione di `cerca_ordine` dal 27 (HTML) e l'etichetta *l'unica porta*; nota in basso.

**Testo**:
- Titolo: *Il transazionale: per chi è fatto*
- I due requisiti:
  - **Performance operativa**: *migliaia di scritture piccole al secondo: un ordine, una spedizione, un cambio di stato. Ogni scrittura deve toccare poche righe, con un lucchetto brevissimo, e non perdere mai un fatto. La lettura tipica è per chiave: "l'ordine 4471", non "tutti gli ordini di agosto".*
  - **Semplicità del coding**: *l'applicazione che scrive deve poter cambiare un fatto in un posto solo: l'indirizzo del cliente sta in `clienti`, e basta. Ogni copia in più è un bug in attesa. È la ragione della normalizzazione, prossima slide.*
- Il terzo blocco — **Perché non è opportuno che sia accessibile all'agente**:
  1. **Le regole vivono nell'applicazione, non nel database**: *validazioni, vincoli fra tabelle, autorizzazioni, transazioni: è il codice dell'applicazione a garantirle, e con esse la sicurezza: chi può vedere e toccare che cosa, nel transazionale, lo decide l'applicazione, quindi il tool. Un `UPDATE` scritto dal modello le salta tutte, e un `UPDATE` senza `WHERE` è un danno reale sul sistema che tiene i conti. Il tool (`cerca_ordine`, `crea_rimborso`) passa dall'applicazione, quindi dalle regole.*
  2. **È dimensionato per scritture piccole, non per letture grandi**: *una query analitica lanciata dal modello (una scansione di milioni di righe, una join a cinque tabelle) rallenta le operazioni di tutti. L'API espone accessi puntuali, per chiave, indicizzati: un ordine alla volta.*
  3. **Difficile da leggere per il modello**: *centinaia di tabelle normalizzate con nomi tecnici (`ord_hdr`, `ord_ln`, `cust_addr_hist`): per una domanda semplice servono sei join che nessuna descrizione spiega. Il tool è il contratto scritto per il modello (il 27, slide 18); l'analitico, come vedremo, è già scritto per chi fa domande.*
- Riquadro-definizione (HTML, sbiadito, dal 27):
  ```
  name:        cerca_ordine
  description: Restituisce lo stato di un ordine dato il suo
               identificativo. Usalo quando il cliente chiede
               dove si trova un ordine o quando arriva.
  input_schema:
    id_ordine: string — l'identificativo, es. "4471"
  ```
- Nota in basso: *Vale anche per la sicurezza: dare a un agente il SQL diretto sul sistema di record è uno dei tre lati della trifecta del 27, un canale per fare danni, aperto senza motivo.*

**Visual**: nessun SVG; la struttura a due colonne più il blocco a tre punti è il visual, con il riquadro-definizione a lato.

## Slide 12 — La normalizzazione

**Messaggio**: la normalizzazione è un'ottimizzazione prestazionale del transazionale (scritture piccole, un fatto in un posto solo) ottenuta *a scapito* dell'accessibilità e della chiarezza per il lavoro analitico: per leggere bisogna ricomporre, e per capire bisogna conoscere lo schema.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): i due pannelli; nota in basso.

**Testo**:
- Titolo: *La normalizzazione*
- Punti:
  1. **Il problema**: *se in ogni riga d'ordine scrivo nome e indirizzo del cliente, il cliente Rossi sta in duecento righe. Cambia indirizzo: duecento aggiornamenti, e basta che uno manchi per avere due indirizzi veri. È l'anomalia di aggiornamento.*
  2. **La regola**: *un fatto, una riga: il cliente sta in `clienti` una volta sola, l'ordine porta solo `id_cliente`. Le forme normali sono i gradi di questa regola; per noi basta la sostanza: niente ripetizioni, tutto per chiave.*
  3. **Il prezzo, dichiarato**: *è un'ottimizzazione per chi scrive, pagata da chi legge. Per "gli ordini di Rossi con il corriere" servono tre tabelle e due join, e per sapere quali serve conoscere lo schema. Per il lavoro analitico, e per un agente, il transazionale normalizzato è il posto meno accessibile e meno chiaro in cui il dato possa stare.*
- Nota in basso: *"Non ridondante" (slide 4) qui è una regola di progetto che il database fa rispettare con le chiavi. L'analitico rinuncerà in parte a questa regola, di proposito, per riprendersi accessibilità e chiarezza: è la sezione 3.*

**Visual**: `slide12-normalizzazione.svg`.

**Prompt per schema SVG**:
> Due pannelli affiancati, divisi da un filo verticale.
>
> **Pannello sinistro — «denormalizzato»**: una tabella `ordini` sola, con le colonne `id_ordine · cliente · indirizzo · corriere · importo` e cinque righe, in cui `Rossi, via Verdi 3` è ripetuto tre volte; una delle tre righe ha l'indirizzo diverso (`via Verdi 5`) ed è evidenziata, con l'etichetta *due indirizzi "veri"*.
>
> **Pannello destro — «normalizzato»**: tre tabelle, `clienti` (una sola riga per Rossi, con l'indirizzo), `ordini` (con `id_cliente`, senza indirizzo), `spedizioni` (con `id_ordine` e `corriere`), collegate da frecce per chiave. Sotto il pannello: *per leggere "gli ordini di Rossi con il corriere": 3 tabelle, 2 join*.
>
> **Elemento focale**: la riga con l'indirizzo diverso a sinistra, e la riga unica di Rossi a destra. La lettura da lontano: a sinistra una cosa ripetuta e sbagliata, a destra una cosa sola e giusta, ma sparsa.

## Slide 13 — La pagella del transazionale, e la cerniera

> Prima apparizione della **pagella** con i voti. Sotto la pagella, la regola fissa del punto di vista.

**Messaggio**: giudicato con i quattro requisiti, il transazionale è veritiero e non ridondante per costruzione, ma non è fatto per essere cercato da chi fa domande e non accumula conoscenza oltre la propria applicazione. Sta dietro i tool; davanti all'agente serve un'altra forma.

**Layout**: titolo in alto; la pagella a sinistra (~45%) con i voti e i perché; a destra (~50%) la mini-figura della Slide 8 (la matrice 2×2) con la cella transazionale spuntata e la freccia verso la cella analitica accesa; blocco nero centrato in basso (la cerniera).

**Testo**:
- Titolo: *La pagella del transazionale, e la cerniera*
- Pagella (HTML, `.pagella`), voti dati dal punto di vista di chi fa domande:
  1. **Ricercabile in modo progressivo**: **~** — *per chiave sì: l'ordine 4471 si trova in un istante. Per domanda no: non c'è un livello generale da cui scendere, e lo schema è spesso complesso e pieno di ambiguità rischiose: nomi di tabelle e campi che si somigliano, join che sembrano giuste e non lo sono. Anche in sola lettura, l'accesso va mediato dai tool.*
  2. **Non ridondante**: **✓** — *per costruzione: la normalizzazione, e le chiavi che la fanno rispettare.*
  3. **Veritiera**: **✓** — *è il sistema di record: i fatti nascono qui, in tempo reale, e l'applicazione ne risponde. Con un'avvertenza: nei dati più vecchi restano spesso errori e problemi di qualità mai sanati, e non tutto è storicizzato (l'indirizzo di ieri è sparito). Molto spesso questa pulizia si fa nel data warehouse, non qui.*
  4. **Compounding**: **✗** — *ogni applicazione ha il suo: gli ordini in un sistema, i reclami in un altro, i contratti in un terzo. I fatti non si agganciano fra loro, e la conoscenza non si accumula: si moltiplicano i silos.*
- Regola sotto la pagella (in piccolo, fissa in tutte le apparizioni): *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Blocco nero centrato (la cerniera): *Il transazionale è dove il dato nasce, ed è dietro i tool: `cerca_ordine` lo interroga per chiave, dall'applicazione. Il grano con cui scrive è il grano di tutto ciò che verrà dopo: nessuna trasformazione a valle inventa un dettaglio che a monte non c'è. Davanti all'agente, che fa domande, serve un'altra forma dello stesso dato. Sezione 3.*

**Visual**: la pagella in HTML + la matrice della Slide 8 in miniatura (`slide8-due-assi.svg` riusato, o una variante `slide13-assi-cerniera.svg` con la cella `relazionale × transazionale` spuntata, la freccia *la struttura deriva da qui* accesa e la cella `relazionale × analitico` come elemento focale).
