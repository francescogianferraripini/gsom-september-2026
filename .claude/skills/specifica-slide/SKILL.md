---
name: specifica-slide
description: "Dato un draft di lezione, conduce un'intervista in stile grill-me al docente per produrre la specifica delle slide (testo, layout, prompt SVG), sezione per sezione e slide per slide. Usare quando si vuole trasformare un outline/bozza di lezione in specifiche di slide, progettare le slide di un incontro, o quando si dice 'intervistami sulle slide' / 'specifica slide' / 'dal draft alle slide'."
---

# Dalla bozza di lezione alla specifica delle slide

Questa skill trasforma un **draft di lezione** (es. `docs/incontro-NN.md`, o l'outline in `docs/raw/`) in una **specifica di slide** pronta per l'implementazione, nel formato del corso (vedi `references/spec-template.md`).

Punto centrale: **la specifica non si genera da sola.** Il valore è nell'intervista. Come `grill-me`, interroghi il docente in modo relentless, un ramo alla volta, partendo dagli spunti del draft — ma con un obiettivo di dominio preciso: far emergere sezioni, slide, testo e prompt SVG. Ogni domanda arriva **con la tua risposta consigliata**, dedotta dal draft.

Non riempire la specifica di ipotesi tue non validate. Proponi, il docente dispone.

## Deliverable

Uno o più file `spec/slide-specs-incontroNN-section-K.md`, un file per sezione, nel formato di `references/spec-template.md`. Ogni slide ha: **Layout**, **Testo** (esatto, non parafrasato), **Visual**, e — dove serve — **Prompt per schema SVG**.

La skill **non** genera gli SVG né costruisce le slide HTML: produce la specifica. La generazione degli SVG è a valle, tramite l'agente `svg-generator` (vedi "Passaggio a valle").

## Fase 0 — Prepararsi (prima di qualsiasi domanda)

1. Individua e **leggi per intero il draft** indicato (o chiedi quale, se non è chiaro): tipicamente `docs/incontro-NN.md`. Leggi anche `docs/raw/outline.md` per il contesto (calendario, incontri adiacenti, cliffhanger tra lezioni).
2. Se esiste già una spec parziale in `spec/` per quella lezione, leggila: si **continua**, non si riparte.
3. Leggi `references/spec-template.md` e `references/guida-prompt-svg.md`.
4. Dal draft, ricava una **proposta di struttura**: le `#` di primo livello sono candidate sezioni, le sottovoci candidate slide. Tienila pronta come punto di partenza dell'intervista — non come verità.
5. Se il draft rimanda a materiale esistente (slide già fatte, un diagramma "già disponibile", un repo), **esploralo tu** invece di chiederlo.

Poi annuncia brevemente il piano (numero di sezioni candidate, come procederai) e parti.

## Regole di conduzione (stile grill-me)

- **Una domanda, o un cluster stretto, alla volta.** Mai riversare un questionario. Cammina i rami dell'albero decisionale risolvendo le dipendenze una per una.
- **Ogni domanda porta la tua raccomandazione**, dedotta dal draft ("Dal draft direi X — confermi o cambi?"). Il docente deve poter rispondere anche solo "ok".
- **Separa un ramo prima di aprire il successivo.** Non passare alla slide/sezione dopo finché quella corrente non è risolta.
- **Rifletti indietro** ciò che hai capito prima di scriverlo nella spec.
- Lascia sempre al docente la possibilità di ridefinire (spezzare, unire, tagliare, riordinare). Il draft è uno spunto, non un vincolo.
- Se una risposta si ricava dal materiale (draft, outline, slide esistenti), **ricavala tu** invece di chiedere.
- Scrivi la spec **man mano**: al termine di ogni sezione, materializza/aggiorna il file di quella sezione, così il lavoro è incrementale e recuperabile.

## Fase 1 — Le sezioni (l'ossatura della lezione)

Obiettivo: concordare in quante e quali sezioni si divide la lezione, e per ciascuna l'arco narrativo. Procedi così, un ramo alla volta:

1. **Proposta di sezionamento**: presenta le sezioni candidate ricavate dai `#` del draft e chiedi conferma su numero e confini. (Es: "Il draft ha 4 blocchi; li tengo come 4 sezioni, o l'apertura e 'Cosa è un agente' vanno fuse?")
2. Per **ogni sezione**, risolvi prima di procedere:
   - **Obiettivo di apprendimento** — cosa il partecipante deve capire/saper fare a fine sezione.
   - **Messaggio chiave (takeaway)** — la frase che resta.
   - **Arco / ordine** — il filo che lega le slide; eventuali agganci alla sezione precedente e successiva (il draft spesso li esplicita: "ribaltamento dell'incontro 1…", cliffhanger finali).
   - **Budget** indicativo di slide/tempo per la sezione.
3. Ricapitola la mappa delle sezioni concordata prima di scendere nelle slide.

## Fase 2 — Le slide, sezione per sezione

Prendi **una sezione alla volta** (nell'ordine concordato). Per la sezione corrente:

1. **Proposta di elenco slide**: dal draft, proponi la sequenza di slide della sezione (titolo provvisorio + funzione di ciascuna). Fatti confermare/riordinare il conteggio e la scaletta prima di entrare nel dettaglio.
2. Poi, **slide per slide**, cammina questi rami (con raccomandazione, uno alla volta):
   - **Messaggio della slide** — la una cosa che questa slide deve trasmettere.
   - **Testo esatto** — titolo, e poi il contenuto reale: definizione centrale / bullet (con le label in grassetto) / citazione con attribuzione / didascalia. Scrivi le stringhe vere, pronte per la slide, non parafrasi. Dove il draft è già scritto bene, proponilo verbatim; dove è telegrafico, proponi una formulazione e falla validare.
   - **Layout** — come si dispongono gli elementi (cosa in alto/centro/lati/basso, quanto spazio al visual).
   - **Visual** — *serve un SVG?* Applica la "prima domanda, sempre" della `guida-prompt-svg.md`: se la struttura testuale basta → `Visual: nessuno`; se c'è un meccanismo/proporzione da mostrare → apri il ramo SVG.
   - **Prompt SVG** (solo se serve) — conduci l'intervista sul visual seguendo `references/guida-prompt-svg.md`: messaggio del diagramma → forma → elementi ed etichette esatte → elemento focale → rilettura. Poi redigi un prompt **di contenuto**: descrivi cosa il diagramma mostra e qual è l'elemento focale, **senza** vincoli di rendering (colori, palette, font, "monocromatico"): quelli li aggiunge l'agente `svg-generator`. La specifica resta indipendente dallo stile grafico.
   - Rileggi il blocco completo della slide e fatti dare l'ok prima della slide successiva.
3. **Materializza la sezione**: scrivi/aggiorna `spec/slide-specs-incontroNN-section-K.md` con l'intestazione, la tabella file→slide e i blocchi slide, esattamente nel formato del template. Numera le slide progressivamente nell'arco dell'intera lezione.
4. Passa alla sezione successiva.

## Fase 3 — Chiusura

- Verifica la **coerenza globale**: numerazione slide continua, tabelle file→slide allineate, agganci tra sezioni e con gli incontri adiacenti coerenti col draft/outline.
- Riepiloga al docente: sezioni prodotte, numero di slide, quante con SVG.
- Ricorda che gli SVG si generano a valle con `svg-generator`.

## Passaggio a valle (SVG)

I prompt SVG vivono **dentro** la specifica. Per generarli, si passa ciascun prompt all'agente `svg-generator` (presente in questo repo, `.claude/agents/svg-generator.md`). Fallo **solo quando il docente lo chiede** — non è compito di questa skill produrre gli SVG: lancia l'agente sul prompt della specifica e salva l'output in `svg/` con nome coerente al numero di slide. Ogni SVG segue la house style descritta nell'agente e nel prompt.
