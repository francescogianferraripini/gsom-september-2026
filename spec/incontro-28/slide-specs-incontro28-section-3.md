# Specifica slide — PC AI 28: Agentic AI — la preparazione della KB, regole per l'organizzazione dei dati
## Francesco Gianferrari Pini — Corso PC AI

**Sezione 3 — Il dato strutturato, 2/2: dove si interroga**
**Obiettivo di apprendimento**: il partecipante sa leggere uno star schema (fatti, dimensioni, grano, metriche), sa perché l'analitico denormalizza e storicizza di proposito, riconosce il fanout e sa come si evita, sa che la sicurezza analitica sta nel database e che l'agente deve interrogare con l'identità dell'utente, sa che cosa fa il data management (cambia forma e arricchisce) e qual è il suo antipattern, sa dove Kimball regge e dove no (e che cos'è un data vault), sa collocare gli strumenti su tre scale, e sa quali punti aperti sono il mandato della Data Governance.
**Messaggio chiave (takeaway)**: L'analitico è il dato riscritto per chi fa domande. È il posto dove entra l'agente.
**Budget**: ~32 min, 14 slide + separatore. Ripartizione: ingresso e nascita 2, star e sue regole 4 (fatti/dimensioni, denormalizzazione, grano, fanout), sicurezza 1, data management 2, Kimball pregi e limiti 2, tool 1, governance 1, pagella 1.
**Stato**: bozza

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-sec3.html` | Separatore — Sezione 3: Il dato strutturato, 2/2: dove si interroga |
| `slides/slide14-excel-dwh.html` | Slide 14 — Da Excel al data warehouse |
| `slides/slide15-dwh-nasce.html` | Slide 15 — Data warehouse: dove e come nasce |
| `slides/slide16-star.html` | Slide 16 — Fatti e dimensioni: lo star schema |
| `slides/slide17-denormalizzazione.html` | Slide 17 — La denormalizzazione, di proposito |
| `slides/slide18-grano.html` | Slide 18 — Il grano e le metriche |
| `slides/slide19-fanout.html` | Slide 19 — Join e fanout |
| `slides/slide20-sicurezza.html` | Slide 20 — Sicurezza: tabella, colonna, riga |
| `slides/slide21-data-management.html` | Slide 21 — Il data management come trasformazione di forma |
| `slides/slide22-pipeline-per-report.html` | Slide 22 — L'antipattern: una pipeline per report |
| `slides/slide23-pregi-kimball.html` | Slide 23 — Pregi di Kimball |
| `slides/slide24-limiti-vault.html` | Slide 24 — Limiti di Kimball, e cenni al data vault |
| `slides/slide25-spettro-tool.html` | Slide 25 — Lo spettro dei tool: da Databricks a DuckDB |
| `slides/slide26-governance.html` | Slide 26 — Qualità, completezza, ownership, dipendenze |
| `slides/slide27-pagella-analitico.html` | Slide 27 — La pagella dell'analitico, e la cerniera |

---

> **Filo della sezione.** È l'approfondimento della sezione 2, dichiarato nel titolo (2/2) e nella cerniera della Slide 13. Si entra dal foglio Excel (Slide 14), si vede da dove viene il warehouse (Slide 15, l'ETL), poi il modello di Kimball con le sue quattro regole (fatti e dimensioni, denormalizzazione di proposito, grano, fanout: 16–19), la sicurezza a tre livelli (20), il data management come trasformazione di forma che arricchisce (21) e il suo antipattern (22), pregi e limiti di Kimball con il data vault (23–24), gli strumenti (25), i punti aperti che sono il mandato della Data Governance (26), la pagella e la cerniera al non strutturato (27). La mini-mappa dei separatori accende la colonna della tabella, con uno zoom.
>
> **Slide 14** è quella tolta dalla sezione 2 ("Da Excel al data warehouse"): qui è l'ingresso motivazionale a Kimball.
>
> **La sicurezza** è detta in due posti: nel transazionale sta nell'applicazione, quindi nel tool (Slide 11, aggiornata); nell'analitico sta nel database, a tre livelli (Slide 20). È la ragione per cui l'agente può interrogare l'analitico direttamente, purché con l'identità di chi gli parla.
>
> **Il data vault** (Slide 24): detto a voce che spesso è un formato intermedio, da cui vengono comunque rigenerati i data mart a star schema; il visual è una transizione a due tempi dalla stella al vault.
>
> **Ripresa dal 27** (Slide 25): il riquadro-payload della slide 20 del 27 (`ordini_08.json`) con DuckDB al posto dello script Python; eyebrow *dall'incontro 27*.
>
> **Slide 26** è la candidata al taglio se il budget stringe.
>
> **Esempio Acme in questa sezione**: `fatto_spedizioni`, `fatto_reclami`, `dim_corriere`, `dim_cliente`, `dim_prodotto`, `dim_data`; SpedFast che passa da `standard` a `espresso` (storicizzazione); i totali del 27 (121 · 44 · 22; 184.300 €); i tre "ritardo medio" (3,8 · 3,2 · 4,1); il responsabile della Lombardia (Marco) per la row level security.
>
> **Codice in questa sezione**: DDL di fatto e dimensione (Slide 16, da saltare se serve), le due query del fanout (Slide 19), il SQL DuckDB nel sandbox (Slide 25). Sempre con la lettura in italiano a fianco.

---

## Slide 14 — Da Excel al data warehouse

**Messaggio**: l'analisi, nelle aziende, nasce in un foglio: una tabella sola, che chiunque legge. Il foglio non regge per due ragioni precise, le copie che divergono e il volume; il data warehouse è il foglio che tutti volevano, costruito perché regga.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Eyebrow: *SEZIONE 3 · IL DATO STRUTTURATO, 2/2: DOVE SI INTERROGA*
- Titolo: *Da Excel al data warehouse*
- Punti:
  1. **Perché piace**: *una tabella sola, una riga per spedizione, con dentro cliente, prodotto, corriere, importo, ritardo. Niente join, niente schema da conoscere: si filtra, si fa una pivot, si legge. È la forma in cui una persona vuole il dato.*
  2. **Perché non regge**: *ogni analista se ne fa una copia, e le copie divergono: tre "ritardo medio" diversi nella stessa riunione, nessuno sa quale sia vero. E a un milione di righe il foglio si ferma. Il foglio fallisce su "non ridondante" e su "veritiera".*
  3. **Il data warehouse**: *la stessa tabella larga, tenuta una volta sola, in un database, alimentata dal transazionale e con un responsabile. Kimball ne ha scritto la forma trent'anni fa: una tabella dei fatti e le sue dimensioni. Sembra il foglio; regge un milione di righe e non diverge.*
- Nota in basso: *L'analitico non è "un altro database": è il transazionale riscritto per chi fa domande. Ed è dove entra l'agente, che fa domande.*

**Visual**: `slide14-excel-dwh.svg`.

**Prompt per schema SVG**:
> **A sinistra**, il foglio `spedizioni.xlsx`: una griglia larga con le colonne `cliente · prodotto · corriere · importo · giorni_ritardo` e alcune righe; dietro, due copie sfalsate etichettate `v2_marco.xlsx` e `FINALE_def.xlsx`. Le tre copie mostrano tre valori di `ritardo medio` diversi (`3,8` · `3,2` · `4,1`), con l'etichetta *tre verità*.
>
> **A destra**, la stessa griglia, una sola, dentro un cilindro etichettato `data warehouse`, con sotto tre righe: `una copia · un responsabile · 1.000.000 di righe`.
>
> Fra i due, una freccia etichettata *lo stesso foglio, costruito perché regga*.
>
> **Elemento focale**: i tre valori diversi a sinistra contro il valore unico (`3,8`) a destra.

## Slide 15 — Data warehouse: dove e come nasce

**Messaggio**: il data warehouse è una derivazione: nasce sugli stessi database relazionali del transazionale, alimentato da processi ETL che leggono i sistemi di record, li trasformano e li caricano in una forma fatta per le domande.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): il flusso di alimentazione; nota in basso.

**Testo**:
- Titolo: *Data warehouse: dove e come nasce*
- Punti:
  1. **Una derivazione**: *negli anni Novanta i database relazionali erano il solo motore serio, e servivano a scrivere transazioni. Il data warehouse è nato come un modo di usarli al contrario: pochi scriventi, molti lettori, letture su milioni di righe. Stesse tabelle, stesso SQL, un altro mestiere.*
  2. **Alimentato da ETL**: *ogni notte (o ogni ora) un processo estrae dai sistemi di record (ordini, CRM, reclami), trasforma (pulisce, ricompone le join, calcola il ritardo, allinea i nomi) e carica nel warehouse. Il dato non nasce qui: arriva qui, in un'altra forma. Chi scrive l'ETL decide quella forma.*
  3. **E i motori si sono adattati**: *i database analitici moderni tengono i dati per colonna: sommare gli importi di un milione di righe legge una colonna sola. Da qui gli strumenti della slide 25, che parlano tutti lo stesso SQL.*
- Nota in basso: *Per l'agente conta una cosa: la lingua è la stessa del transazionale, il SQL della slide 10. Cambia il dato che trova dall'altra parte, e quanto è leggibile.*

**Visual**: `slide15-etl.svg`.

**Prompt per schema SVG**:
> Flusso orizzontale da sinistra a destra. **A sinistra** tre cilindri, `ordini (gestionale)` · `CRM` · `reclami (ticketing)`, ognuno con dentro le proprie tabelle normalizzate in miniatura (tre o quattro rettangolini collegati) e l'etichetta `24/7, scritture`. **Al centro** un blocco `ETL` con dentro i tre verbi in verticale, `estrai · trasforma · carica`, e a lato `ogni notte`; sopra il blocco l'etichetta *pulisce, ricompone, calcola, allinea i nomi*. **A destra** un cilindro `data warehouse` con dentro una stella in miniatura (`fatto` al centro, quattro `dim` intorno) e l'etichetta `letture, milioni di righe`. Frecce dai tre cilindri all'ETL e dall'ETL al warehouse.
>
> **Elemento focale**: il blocco ETL, e il cambio di forma dei dati che attraversa: a sinistra tabelle sparse, a destra una stella.

## Slide 16 — Fatti e dimensioni: lo star schema

**Messaggio**: il modello di Kimball ha due tipi di tabella soltanto: i fatti, una riga per evento misurabile, e le dimensioni, una riga per cosa con cui si guarda il fatto. Al centro il fatto, intorno le dimensioni: una stella. È la forma che chi fa domande legge senza conoscere lo schema.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); a destra (~60%) il riquadro DDL con la lettura a fianco e, sotto, la stella; nota in basso.

**Testo**:
- Titolo: *Fatti e dimensioni: lo star schema*
- Punti:
  1. **Il fatto**: *una riga per evento: una spedizione. Porta le misure (importo, giorni di ritardo) e le chiavi verso le dimensioni. È lunga (milioni di righe) e stretta.*
  2. **Le dimensioni**: *una riga per cosa: un corriere, un cliente, un prodotto, un giorno. Portano gli attributi con cui si filtra e si raggruppa: il nome del corriere, la regione del cliente, la categoria del prodotto, il mese. Sono corte e larghe.*
  3. **La stella**: *ogni dimensione si aggancia al fatto con una join sola, sempre uguale. Non serve conoscere lo schema: si parte dal fatto e si esce verso la dimensione che serve. È leggibile da una persona, e da un modello.*
- Riquadro DDL (HTML, monospaziato, lettura a fianco; **da saltare a voce se serve**):
  ```
  CREATE TABLE dim_corriere (
    id_corriere   INT PRIMARY KEY,
    nome          VARCHAR(40),        -- SpedFast
    tipo          VARCHAR(20),        -- espresso / standard
    contratto_dal DATE
  );
  CREATE TABLE fatto_spedizioni (
    id_spedizione   INT PRIMARY KEY,
    id_corriere     INT REFERENCES dim_corriere,   -- una join, sempre questa
    id_cliente      INT REFERENCES dim_cliente,
    id_data         INT REFERENCES dim_data,
    importo         DECIMAL(10,2),    -- misura
    giorni_ritardo  INT               -- misura, già calcolata
  );
  ```
- Nota in basso: *Nel transazionale il ritardo era `data_consegna − data_prevista`, da calcolare ogni volta e da sapere. Qui è una colonna: qualcuno l'ha calcolata una volta, per tutti, con una regola sola.*

**Visual**: il riquadro DDL in HTML + `slide16-star.svg`.

**Prompt per schema SVG**:
> Al centro il rettangolo `fatto_spedizioni` con le sue colonne elencate (le tre chiavi `id_corriere · id_cliente · id_data` e, in evidenza, le due misure `importo · giorni_ritardo`). Intorno, ai quattro lati, quattro rettangoli `dim_corriere` · `dim_cliente` · `dim_prodotto` · `dim_data`, ciascuno con tre attributi (es. `nome · tipo · contratto_dal`; `nome · regione · segmento`; `nome · categoria · fornitore`; `giorno · mese · festivo`). Ogni dimensione è collegata al fatto da una linea sola, etichettata con la chiave.
>
> **Elemento focale**: il fatto al centro e le quattro linee identiche: la lettura da lontano è "una stella".

## Slide 17 — La denormalizzazione, di proposito

**Messaggio**: la dimensione ripete e storicizza di proposito: tiene in una riga sola tutto ciò che si vuole sapere di un corriere, e quando il corriere cambia non sovrascrive, aggiunge una riga. È il contrario della slide 12, e ha ragione per la stessa ragione al contrario: qui il lettore conta più dello scrivente.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *La denormalizzazione, di proposito*
- Punti:
  1. **La dimensione ripete**: *nel transazionale il corriere, il suo tipo di contratto e la sua sede stavano in tre tabelle. In `dim_corriere` stanno in una riga: chi legge trova tutto con una join. Se l'ETL sbaglia, sbaglia in un posto solo: la ridondanza è controllata, non accidentale.*
  2. **La dimensione storicizza**: *nel transazionale il nuovo indirizzo sovrascrive il vecchio (slide 13: "non tutto è storicizzato"). Qui, quando il cliente cambia regione, la dimensione aggiunge una riga con le date di validità, e le spedizioni di ieri restano agganciate alla regione di ieri. Il passato non si riscrive.*
  3. **Il prezzo, dichiarato anche qui**: *più spazio, e un ETL che deve sapere che cosa ripetere e quando aprire una riga nuova. È il lavoro del data management, slide 21. Si paga una volta, lo incassano tutti i lettori.*
- Nota in basso: *Slide 12 e 17 sono la stessa scelta vista dai due lati: normalizzare ottimizza chi scrive, denormalizzare ottimizza chi legge. Il dato è lo stesso; cambia per chi è tenuto.*

**Visual**: `slide17-dimensione.svg`.

**Prompt per schema SVG**:
> **A sinistra** le tre tabelle transazionali `corrieri`, `contratti`, `sedi`, collegate per chiave, ognuna con la riga di SpedFast. Una freccia `ETL` verso destra. **A destra** la tabella `dim_corriere` con una riga larga per SpedFast che contiene tutti gli attributi delle tre tabelle (`nome · tipo · sede · contratto_dal`); sotto, una seconda riga per SpedFast con `tipo: standard → espresso`, `valido_dal 2026-03-01`, `valido_al` aperto (`—`), mentre la prima riga porta `valido_al 2026-02-28`. Etichetta accanto alle due righe: *due righe, una storia*.
>
> **Elemento focale**: le due righe di SpedFast con le date di validità.

## Slide 18 — Il grano e le metriche

**Messaggio**: la prima decisione di un fatto è il grano: che cosa è una riga. Da lì discende tutto: quali metriche si possono sommare, quali domande hanno risposta. E il grano non si sceglie liberamente: è quello con cui il transazionale scrive.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *Il grano e le metriche*
- Punti:
  1. **Il grano**: *"una riga è una spedizione" è una frase che va scritta prima di ogni altra. Cambia tutto: una riga per spedizione risponde a "quanti ritardi per corriere"; una riga per collo risponde anche a "quanti colli in ritardo"; una riga per ordine non risponde a nessuna delle due se un ordine ha due spedizioni.*
  2. **Le metriche additive**: *l'importo si somma su qualsiasi dimensione: per corriere, per mese, per regione. I giorni di ritardo si sommano, ma la media va ricalcolata dai totali, non mediando le medie. Il numero di clienti distinti non si somma affatto. Il grano dice quali somme sono legittime.*
  3. **Il grano viene da monte**: *è la cerniera della slide 13: se il gestionale registra le spedizioni e non i colli, il fatto è la spedizione. Nessun ETL inventa un dettaglio che il sistema di record non ha scritto. Chi vuole un grano più fine deve cambiare il transazionale, non il warehouse.*
- Nota in basso: *Per l'agente il grano è la prima cosa da sapere e l'ultima che gli viene detta: "una riga è una spedizione" vale più di cento descrizioni di colonne. Torna nella sezione 6 e nella 7.*

**Visual**: `slide18-grano.svg`.

**Prompt per schema SVG**:
> Tre righe orizzontali, una per grano, ciascuna con a sinistra l'etichetta del grano, al centro una mini-tabella di esempio, a destra tre domande con un segno ✓ o ✗:
> - **`una riga = un ordine`**: mini-tabella con `4471 · SpedFast?` e l'etichetta *due spedizioni, un corriere solo?*; domande: *ritardi per corriere* ✗ · *colli in ritardo* ✗ · *importo per mese* ✓;
> - **`una riga = una spedizione`** (evidenziata: il grano scelto): ✓ · ✗ · ✓;
> - **`una riga = un collo`**: ✓ · ✓ · ✓, con la nota *solo se il gestionale lo scrive*.
>
> **Elemento focale**: la riga `spedizione`, evidenziata come il grano scelto, e la nota sulla riga `collo`.

## Slide 19 — Join e fanout

**Messaggio**: il pericolo classico dell'analitico è unire due fatti con grani diversi: le righe si moltiplicano e i totali raddoppiano senza che nessuno se ne accorga. La query multimetrica giusta aggrega ogni fatto per conto suo e unisce solo i totali.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); a destra (~60%) la mini-figura del fanout sopra e i due riquadri di query sotto, con la lettura a fianco; nota in basso.

**Testo**:
- Titolo: *Join e fanout*
- Punti:
  1. **La domanda**: *"per corriere: importo spedito e numero di reclami". Due fatti, `fatto_spedizioni` e `fatto_reclami`, con grani diversi: una riga per spedizione, una riga per reclamo.*
  2. **Il fanout**: *se li unisco per corriere prima di aggregare, ogni spedizione si accoppia con ogni reclamo dello stesso corriere: 121 spedizioni × 9 reclami = 1.089 righe, e l'importo di SpedFast esce nove volte più grande. Nessun errore, nessun avviso: un numero sbagliato con l'aria di un numero giusto.*
  3. **La forma giusta**: *aggrega ciascun fatto al grano della domanda (per corriere), e unisci i due totali: una subquery per fatto, poi una join fra risultati di una riga per corriere. È la regola: mai una join fra fatti, sempre fra aggregati.*
- I due riquadri (HTML, monospaziato, lettura a fianco; il primo marcato `✗`, il secondo `✓`):
  ```
  -- ✗ fanout: join prima di aggregare
  SELECT c.nome, SUM(s.importo), COUNT(r.id_reclamo)
  FROM   fatto_spedizioni s
  JOIN   fatto_reclami r ON r.id_corriere = s.id_corriere
  JOIN   dim_corriere c  ON c.id_corriere = s.id_corriere
  GROUP BY c.nome;                 -- SpedFast: 1.660.000 € (×9)
  ```
  ```
  -- ✓ una subquery per fatto, join fra totali
  SELECT c.nome, sp.importo, rc.reclami
  FROM   (SELECT id_corriere, SUM(importo) AS importo
          FROM fatto_spedizioni GROUP BY id_corriere) sp
  JOIN   (SELECT id_corriere, COUNT(*) AS reclami
          FROM fatto_reclami GROUP BY id_corriere) rc USING (id_corriere)
  JOIN   dim_corriere c USING (id_corriere);   -- SpedFast: 184.300 € · 9
  ```
- Nota in basso: *È l'errore più frequente di chi scrive SQL, persone e modelli: torna nella sezione 6 come primo modo in cui Text2SQL sbaglia con l'aria di aver ragione. Un semantic layer che conosce i grani lo impedisce alla radice: sezione 7.*

**Visual**: i due riquadri in HTML + `slide19-fanout.svg` (piccolo, sopra i riquadri).

**Prompt per schema SVG**:
> Due pannelli piccoli affiancati. **A sinistra**: tre righe `spedizione` (SpedFast) e tre righe `reclamo` (SpedFast) che si incrociano in nove coppie, disegnate come una griglia 3×3 di linee; etichetta *3 × 3 = 9 righe: l'importo esce 3 volte*. **A destra**: le stesse righe che convergono ciascun gruppo nel proprio totale (`Σ importo` per le spedizioni, `n reclami` per i reclami), e i due totali uniti in una riga sola; etichetta *2 totali, 1 riga*.
>
> **Elemento focale**: la griglia di incroci a sinistra. Il viewBox è ritagliato al contenuto: la figura sta sopra i due riquadri, bassa e larga.

## Slide 20 — Sicurezza: tabella, colonna, riga

**Messaggio**: nel warehouse la sicurezza si applica a tre livelli, e per un agente la domanda che conta è con quale identità interroga: se con la propria, vede tutto ciò che il warehouse gli concede; se con quella dell'utente, vede solo ciò che l'utente vedrebbe.

**Layout**: titolo in alto; i tre livelli a sinistra (~40%); visual al centro-destra (~55%); sotto, a tutta larghezza, il blocco per l'agente; nota in basso.

**Testo**:
- Titolo: *Sicurezza: tabella, colonna, riga*
- I tre livelli:
  1. **Tabella**: *chi può leggere `fatto_spedizioni` e chi no. È il permesso più grossolano: o tutto o niente.*
  2. **Colonna**: *chi vede `importo` e chi no; chi vede il nome del cliente e chi solo il suo id. Le colonne sensibili si mascherano, non si tolgono: la query gira, il valore no.*
  3. **Riga**: *il responsabile di zona vede solo le spedizioni della sua regione: la stessa tabella, filtrata per chi la legge. Il filtro lo applica il database, non la query.*
- Il blocco per l'agente — **Con quale identità interroga l'agente?**: *Con un'utenza tecnica sua: semplice, e pericoloso: risponde al magazziniere con i margini che vede il direttore. Con l'identità dell'utente che gli parla: il warehouse applica le tre regole a lui, e l'agente non può mostrare ciò che l'utente non potrebbe vedere. È la seconda scelta quella giusta, e va fatta nell'harness, dove sta il tool.*
- Nota in basso: *Nel transazionale la sicurezza sta nell'applicazione, quindi nel tool (slide 11): è per questo che l'agente ci entra solo da lì. Nell'analitico sta nel database, a questi tre livelli: è per questo che un agente può interrogarlo direttamente, purché lo faccia con l'identità di chi gli parla. Il tool resta codice dell'harness (il 27), ed è lì che si decide con quali credenziali chiama.*

**Visual**: `slide20-sicurezza.svg`.

**Prompt per schema SVG**:
> La tabella `fatto_spedizioni` disegnata tre volte in fila, una per livello, ciascuna con l'etichetta sopra: (1) **`tabella`**: la tabella intera con un lucchetto sul bordo; (2) **`colonna`**: la stessa tabella con la colonna `importo` oscurata (celle annerite, valori illeggibili); (3) **`riga`**: la stessa tabella con le righe di `Lazio` e `Veneto` attenuate e solo quelle di `Lombardia` accese, etichetta *responsabile Lombardia*.
>
> Sotto, due figure stilizzate di agente: `agente (utenza tecnica)` che vede le tre tabelle piene, con un segno ✗; `agente come Marco (responsabile Lombardia)` che vede la terza versione, con un segno ✓.
>
> **Elemento focale**: la terza tabella e la figura con il ✓.

## Slide 21 — Il data management come trasformazione di forma

**Messaggio**: il data management non registra fatti nuovi: cambia la forma di fatti che esistono già e li arricchisce, con formule (il ritardo calcolato), integrazioni fra fonti (gli ordini del gestionale con i reclami del ticketing sullo stesso corriere), storicizzazioni. Lo fa con pipeline che qualcuno scrive, mantiene e di cui risponde.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%): il grafo di dipendenze; nota in basso.

**Testo**:
- Titolo: *Il data management come trasformazione di forma*
- Punti:
  1. **Che cosa fa**: *prende il dato dove nasce e lo riscrive nella forma di chi lo legge: dal transazionale allo star, dallo star alle tabelle larghe di un report, da un documento a un fatto (sezione 4). E lo arricchisce: calcola ciò che a monte non c'è come colonna (i giorni di ritardo, il margine), integra fonti che non si parlano (il corriere del gestionale e quello del ticketing sono lo stesso SpedFast), aggiunge la storia (slide 17). Non registra fatti nuovi: ne cambia la forma e ne aumenta il valore.*
  2. **Le pipeline**: *ogni trasformazione è codice che gira a orari, dipende da ciò che c'è a monte e alimenta ciò che c'è a valle. Ha un proprietario, dei test, una storia di guasti. È software, e va trattato come software.*
  3. **Le dipendenze**: *`fatto_spedizioni` dipende da `spedizioni` e da `ordini`; il report dei ritardi dipende da `fatto_spedizioni`. Se cambia una colonna a monte, si rompe qualcosa a valle. Sapere che cosa dipende da che cosa (il lineage) è metà del mestiere.*
- Nota in basso: *Chi ha fatto la trasformazione sa che cosa vuol dire "giorni di ritardo": festivi esclusi? dalla data prevista o da quella promessa? Quel sapere è la semantica della piramide, e di solito sta solo nel codice della pipeline. Sezione 7.*

**Visual**: `slide21-lineage.svg`.

**Prompt per schema SVG**:
> Un grafo di dipendenze da sinistra a destra. **A sinistra** le fonti transazionali: `ordini`, `spedizioni`, `reclami (ticketing)`. Le tre frecce convergono in un blocco `ETL` con le etichette *ricompone · calcola · integra · storicizza*. **Al centro** le tabelle del warehouse: `fatto_spedizioni` (con l'etichetta `owner: team logistica`), `fatto_reclami`, `dim_corriere`. **A destra** i consumatori: `report ritardi`, `dashboard direzione`, `tool: ritardi_per_corriere` (il tool dell'agente). Ogni freccia porta un piccolo orologio (`ogni notte`, `ogni ora`).
>
> La colonna `spedizioni.data_prevista` è evidenziata a sinistra, e da lei un'onda (una linea spessa di colore d'allarme) si propaga lungo le frecce fino ai tre consumatori, con l'etichetta *se cambia questa, si rompono questi*.
>
> **Elemento focale**: la propagazione dalla colonna a monte ai consumatori a valle.

## Slide 22 — L'antipattern: una pipeline per report

**Messaggio**: il modo più comune di rompere il compounding è costruire una pipeline per ogni report, dal transazionale in giù, ognuna con le sue regole. Dieci report, dieci "ritardo medio", nessuno che riusa il lavoro dell'altro: il warehouse esiste, ma non accumula.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~40%); visual al centro-destra (~55%); nota in basso.

**Testo**:
- Titolo: *L'antipattern: una pipeline per report*
- Punti:
  1. **Come nasce**: *arriva la richiesta "voglio il report dei ritardi per regione". Il modo più veloce è una pipeline nuova: dal transazionale, con le sue join, il suo calcolo del ritardo, la sua tabella finale. Funziona in una settimana. La richiesta dopo fa lo stesso.*
  2. **Che cosa produce**: *dieci report, dieci pipeline, dieci definizioni di ritardo (festivi sì, festivi no, dalla data promessa, da quella prevista). Tre "ritardo medio" nella stessa riunione: il foglio Excel della slide 14, rifatto in grande e con più fatica.*
  3. **Che cosa si perde**: *il compounding. Ogni pipeline parte da zero invece di agganciarsi al fatto che esiste; il lavoro dell'undicesima non rende migliori le dieci prima. E per un agente è peggio: dieci tabelle con lo stesso nome e numeri diversi, nessun modo di sapere quale sia quella buona.*
- Nota in basso: *Il pattern giusto è la stella: un fatto, calcolato una volta con una regola sola, e dieci report che lo leggono. La pipeline in più si scrive solo quando manca un fatto, non quando manca un report.*

**Visual**: `slide22-pipeline-per-report.svg`.

**Prompt per schema SVG**:
> Due pannelli affiancati, divisi da un filo verticale.
>
> **Pannello sinistro — «una pipeline per report»**: in alto il cilindro `transazionale`; da lì partono dieci frecce parallele verso il basso, ognuna con la propria scatola `ETL 1 … ETL 10` e la propria tabella finale `report_1 … report_10`; tre delle tabelle portano `ritardo medio: 3,8` · `3,2` · `4,1`. Piede: `10 pipeline · 10 definizioni`.
>
> **Pannello destro — «una stella, dieci report»**: dal cilindro `transazionale` una freccia sola verso una scatola `ETL` e poi `fatto_spedizioni`; da lì dieci frecce corte a ventaglio verso i dieci report, tutti con `3,8`. Piede: `1 pipeline · 1 definizione · 10 lettori`.
>
> **Elemento focale**: i tre valori diversi a sinistra.

## Slide 23 — Pregi di Kimball

**Messaggio**: il modello di Kimball è durato trent'anni perché ottimizza il lettore: si legge senza conoscere lo schema, parla la lingua del business, e le dimensioni condivise fra i fatti sono il compounding che il transazionale non aveva.

**Layout**: titolo in alto; le quattro righe a sinistra (~50%); visual a destra (~45%); nota in basso.

**Testo**:
- Titolo: *Pregi di Kimball*
- Le quattro righe:
  1. **Leggibile senza lo schema**: *un fatto al centro, le dimensioni intorno, una join per dimensione, sempre uguale. Chi arriva capisce dove sono le cose in un'ora; un modello lo capisce dalla lista delle tabelle. Gli errori restano possibili, sul grano prima di tutto (slide 18 e 19), ma sono molti meno che sui modelli transazionali tipici, e sono sempre gli stessi: si possono prevenire.*
  2. **Nomi di business**: *`dim_corriere.nome`, `fatto_spedizioni.giorni_ritardo`: le colonne si chiamano come le cose di cui si parla in riunione, non `ord_hdr.dlv_dt`. La traduzione l'ha fatta l'ETL, una volta.*
  3. **Dimensioni conformi**: *la stessa `dim_corriere` serve al fatto delle spedizioni e a quello dei reclami. Quando arriva un terzo fatto (le fatture dei corrieri) si aggancia alla dimensione che c'è già: è il compounding, reso struttura.*
  4. **Metriche definite una volta**: *"giorni di ritardo" ha una regola, scritta nell'ETL, uguale per tutti i report. La riunione con tre ritardi medi finisce.*
- Nota in basso: *Misurato con la pagella: ricercabile dal generale al particolare (dal totale per corriere alla singola spedizione), non ridondante dove conta, e compounding per costruzione. È la ragione per cui l'agente entra qui e non nel transazionale.*

**Visual**: `slide23-conformi.svg`.

**Prompt per schema SVG**:
> Tre fatti in fila in alto: `fatto_spedizioni` · `fatto_reclami` · `fatto_fatture_corrieri` (il terzo con bordo tratteggiato e l'etichetta *nuovo*). Sotto, tre dimensioni condivise: `dim_corriere` · `dim_data` · `dim_cliente`. I primi due fatti sono collegati alle dimensioni con linee piene; il terzo con linee tratteggiate che arrivano alle **stesse** dimensioni. Etichetta accanto alle linee tratteggiate: *si aggancia a ciò che c'è: compounding*.
>
> **Elemento focale**: le linee tratteggiate del terzo fatto.

## Slide 24 — Limiti di Kimball, e cenni al data vault

> Visual a **due tempi**: la stella della Slide 16 che si apre nel vault. Note del relatore: spesso il vault è un formato intermedio, da cui vengono comunque rigenerati i data mart a star schema.

**Messaggio**: lo star schema è la forma migliore per leggere, non per integrare: quando le fonti sono molte e cambiano, quando serve tutta la storia e non solo quella prevista, il modello che ottimizza il lettore diventa rigido. Il data vault separa l'integrazione dalla lettura, e paga in leggibilità ciò che guadagna in flessibilità.

**Layout**: titolo in alto; i tre punti di testo a sinistra (~35%); visual al centro-destra (~60%), a due tempi; nota in basso.

**Testo**:
- Titolo: *Limiti di Kimball, e cenni al data vault*
- Punti:
  1. **Dove lo star non regge**: *molte fonti che cambiano (un nuovo gestionale, un'acquisizione): ogni cambiamento a monte costringe a rifare l'ETL e a volte il fatto. La storia: la dimensione storicizza gli attributi che qualcuno ha previsto, non tutto. L'integrazione: due sistemi che chiamano "cliente" cose diverse vanno riconciliati prima di arrivare alla stella, e lo star non ha un posto per quel lavoro.*
  2. **Il data vault**: *un modello in tre tipi di tabella: hub (le chiavi di business: il cliente, il corriere), link (le relazioni fra chiavi: questa spedizione, questo corriere), satellite (gli attributi, con la loro storia completa, una tabella per fonte). Si aggiunge una fonte aggiungendo satelliti, senza toccare nulla. Tutto è storicizzato, sempre.*
  3. **Il prezzo**: *nessuno lo legge direttamente: decine di tabelle strette, join ovunque. Il vault sta in mezzo, fra le fonti e le stelle: integra e conserva; poi da lì si costruiscono gli star schema per i lettori. Due forme, due lavori.*
- Nota in basso: *Notate la forma del vault: chiavi, relazioni fra chiavi, attributi. È un grafo scritto in tabelle, e non è un caso: quando la struttura deve evolvere nel tempo, il grafo torna. Sezione 5, e sezione 7 per le ontologie.*

**Visual**: `slide24-star-vault-{1,2}.svg` (`.visual.stack` + fragment, stesso viewBox; in reveal `data-auto-animate` se gli elementi restano gli stessi).

**Prompt per schema SVG**:
> **Tempo 1**: la stella della Slide 16, identica: `fatto_spedizioni` al centro, `dim_corriere` · `dim_cliente` · `dim_prodotto` · `dim_data` intorno, una linea per dimensione.
>
> **Tempo 2**: la stella si apre nel vault, ogni pezzo nel suo posto. Le dimensioni diventano **hub** (cerchi con la sola chiave di business: `hub_corriere`, `hub_cliente`, `hub_prodotto`); gli attributi che stavano dentro le dimensioni escono in **satellite** appesi a ciascun hub, uno per fonte (`sat_corriere_gestionale`, `sat_corriere_ticketing`, ognuno con `valido_dal / valido_al` e l'etichetta *storia completa, per fonte*); il fatto diventa un **link** (`link_spedizione`) che tiene solo le chiavi degli hub che collega, e le sue misure escono in un satellite del link (`sat_spedizione_misure`). Accanto alle frecce di movimento, le etichette di trasformazione: *dimensione → hub + satelliti* · *fatto → link + satellite*. In un angolo, sbiadita, una stella piccola con l'etichetta *da qui si ricostruiscono le stelle per chi legge*.
>
> **Elemento focale** (tempo 2): i satelliti multipli sullo stesso hub (una fonte in più = un satellite in più, nulla da toccare) e la forma complessiva a grafo.

## Slide 25 — Lo spettro dei tool: da Databricks a DuckDB

> Ripresa della slide 20 del 27 (il riquadro-payload su `ordini_08.json`), eyebrow *dall'incontro 27*.

**Messaggio**: gli strumenti analitici di oggi parlano tutti lo stesso SQL e leggono per colonna; si distinguono per dove girano e quanto costano, dalla piattaforma condivisa al motore che gira in un processo. E il motore piccolo è quello che entra nel sandbox dell'agente.

**Layout**: titolo in alto; la tabella nella metà superiore (~45%); sotto, i due punti a sinistra (~45%) e il riquadro-payload a destra (~50%); nota in basso.

**Testo**:
- Titolo: *Lo spettro dei tool: da Databricks a DuckDB*
- Tabella (HTML, `.tbl`):

| | **Piattaforma** (Databricks, Snowflake, BigQuery) | **Database analitico** (SQL Server, ClickHouse, Postgres con estensioni) | **Motore in-process** (DuckDB) |
|---|---|---|---|
| Dove gira | nel cloud, condivisa da tutta l'azienda | su un server tuo, o gestito | dentro un programma: un processo, un file |
| Per che cosa | il warehouse aziendale, le pipeline, la governance | analisi su volumi medi, tempo reale | un export, un file Parquet, una sessione |
| Che cosa serve | un team, un contratto, un budget | un DBA | `pip install`, e niente altro |
| Lo stesso SQL | sì | sì | sì |

- Punti:
  1. **Stesso linguaggio, tre scale**: *la query della slide 10 gira su tutti e tre. Cambia chi la ospita, quanto costa, quanti dati regge; non cambia come si fa la domanda.*
  2. **Il motore piccolo entra nel sandbox**: *nel 27 (slide 20) il modello aveva scritto quattro righe di Python su `ordini_08.json`. Con DuckDB nel sandbox scrive SQL sullo stesso file. Stessa lingua del warehouse, senza il warehouse, sui dati che ha davanti.*
- Riquadro-payload (HTML, idioma del 26/27; le righe `[tool]` in teal, le pill del modello in burgundy):
  ```
  [user]      Quanti ordini di agosto sono in ritardo, e per quale corriere?
  [assistant] → esporta_ordini(mese="2026-08")
  [tool]      salvato in ordini_08.json (12.480 righe): cerca o elabora con bash
  [assistant] → bash("duckdb -c \"SELECT corriere, COUNT(*) AS n
                FROM 'ordini_08.json' WHERE consegna > prevista
                GROUP BY corriere ORDER BY n DESC\"")
  [tool]      SpedFast 121 · Corriere Nord 44 · PostaPro 22
  ```
- Nota in basso: *Per l'agente conta la seconda riga: il warehouse lo interroga attraverso un tool (sezione 6); un export, un file, un risultato salvato li interroga nel sandbox, con lo stesso SQL. Due porte, una lingua.*

**Visual**: la tabella e il riquadro-payload in HTML; nessun SVG.

## Slide 26 — Qualità, completezza, ownership, dipendenze

> Candidata al taglio se il budget stringe.

**Messaggio**: il warehouse eredita quattro problemi che nessuna struttura risolve da sola: la qualità dei dati che arrivano, la completezza di ciò che manca, chi risponde di ogni tabella, e che cosa dipende da che cosa. Tenerli sotto controllo è il mandato della Data Governance; la sezione 7 li riprende come "data as a product".

**Layout**: titolo in alto; le quattro righe a sinistra (~60%); a destra (~35%), sbiadita, la pagella con la sola riga *veritiera* evidenziata e un `~` a matita, con l'etichetta *è qui che si gioca*; nota in basso.

**Testo**:
- Titolo: *Qualità, completezza, ownership, dipendenze*
- Le quattro righe:
  1. **Qualità**: *il warehouse pulisce (slide 13: gli errori vecchi del transazionale si sanano qui), ma pulisce ciò che sa: una data di consegna sbagliata di un giorno passa. Servono controlli scritti (il ritardo non può essere negativo; ogni spedizione ha un corriere) che girino a ogni carico, e qualcuno che guardi quando falliscono.*
  2. **Completezza**: *ciò che manca non si vede: i reclami arrivati per telefono non stanno nel ticketing, quindi non stanno nel fatto. Un numero giusto su un insieme incompleto è un numero sbagliato con l'aria di un numero giusto: la stessa faccia del fanout.*
  3. **Ownership**: *ogni tabella ha bisogno di un nome: chi risponde di `fatto_spedizioni`, chi decide che cosa vuol dire "ritardo", chi avvisa quando cambia. Senza, la definizione la dà chi l'ha usata per ultimo.*
  4. **Dipendenze**: *il lineage della slide 21: se nessuno sa che il tool dell'agente legge `fatto_spedizioni`, la prima modifica alla pipeline lo rompe in silenzio. Le dipendenze vanno dichiarate, non scoperte.*
- Nota in basso: *Tenere sotto controllo questi quattro punti è tipicamente il mandato principale della Data Governance: chi risponde di che cosa, con quali regole, misurato come. Per l'agente sono i quattro modi in cui una risposta esce sbagliata da una query giusta. La forma che la governance prende oggi, trattare ogni tabella come un prodotto con un proprietario, un contratto e dei controlli, è la sezione 7.*

**Visual**: nessuno; le quattro righe sono la struttura, con la pagella sbiadita a lato.

## Slide 27 — La pagella dell'analitico, e la cerniera

**Messaggio**: lo star schema è, fra i modi di tenere il dato strutturato, il più vicino ai quattro requisiti: ricercabile dal generale al particolare, compounding per costruzione, veritiero quanto la sua governance. Ma copre solo ciò che sta in una cella; il resto della conoscenza aziendale è testo.

**Layout**: come la Slide 13: la pagella a sinistra (~45%) con voti e perché, regola del punto di vista sotto; a destra (~50%) la mini-mappa dello spettro con la colonna della tabella spuntata e la colonna del documento che si accende; blocco nero centrato in basso.

**Testo**:
- Titolo: *La pagella dell'analitico, e la cerniera*
- Pagella (HTML, `.pagella`), voti dal punto di vista di chi fa domande:
  1. **Ricercabile in modo progressivo**: **✓** — *dal totale per corriere alla singola spedizione, scendendo lungo le dimensioni; lo schema si legge senza conoscerlo. Restano gli errori di grano e di fanout: pochi, e sempre gli stessi.*
  2. **Non ridondante**: **~** — *ridondante di proposito nelle dimensioni, ma controllata: un fatto calcolato una volta, una regola sola. Diventa ✗ appena si cede all'antipattern della slide 22.*
  3. **Veritiera**: **~** — *più del transazionale, perché qui si pulisce e si storicizza; ma vale quanto la governance della slide 26: controlli, completezza, un proprietario. Senza, è un numero giusto su dati sbagliati.*
  4. **Compounding**: **✓** — *dimensioni conformi, metriche definite una volta: il terzo fatto si aggancia ai primi due. È il requisito in cui l'analitico batte tutto il resto.*
- Regola sotto la pagella: *Voti dati dal punto di vista di chi fa domande: una persona, o un agente.*
- Blocco nero centrato (la cerniera): *Il dato strutturato copre ciò che qualcuno ha deciso di mettere in una cella prima di scriverlo. Il contratto con SpedFast, il reclamo del cliente, la policy sui rimborsi non stanno in nessuna cella: sono testo. Come si cerca un fatto dentro un testo, e che cosa cambia per l'agente: sezione 4.*

**Visual**: la pagella in HTML + la mini-mappa dello spettro (`minimap` della Slide 7 con la colonna `tabella` spuntata e la colonna `documento` come elemento focale).
