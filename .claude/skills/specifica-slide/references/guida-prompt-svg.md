# Guida — scrivere il "Prompt per schema SVG"

Il prompt SVG dentro la specifica descrive **cosa** il diagramma deve mostrare: il meccanismo, gli elementi, le etichette, le relazioni e qual è l'elemento che porta il significato. **Non** descrive il rendering (colori, palette, font, stile): quello è compito dell'agente `svg-generator`, che conosce la house style del deck. La specifica resta indipendente dal rendering grafico.

Questa guida serve a condurre bene l'intervista sulla parte visiva e a redigere un prompt di contenuto autoconsistente.

## Prima domanda, sempre: serve davvero un SVG?

Un SVG si giustifica solo se rende visibile un **meccanismo, una relazione o una proporzione** che il testo da solo non trasmette (un loop, un flusso, una scala, una struttura a strati, un confronto quantitativo). Se il contenuto è un elenco di concetti, un contrasto tra due colonne, una definizione o una citazione, spesso la **struttura testuale è già il visual** → `Visual: nessuno`. Non decorare: ogni diagramma deve insegnare qualcosa.

Chiedi al docente: *"Questa slide ha un meccanismo o una proporzione da mostrare, o il messaggio sta già nel testo?"* Proponi tu una raccomandazione.

## Anatomia di un buon prompt (di contenuto)

Quando un SVG serve, il prompt deve fissare:

1. **Tipo di diagramma / orientamento** — es. "diagramma orizzontale a 3 livelli paralleli", "sequenza narrativa verticale", "infografica a 5 righe su scala logaritmica", "sequence diagram su due giri".
2. **Gli elementi, con le etichette esatte** — nomi dei box, testo dentro i rettangoli, valori delle barre, testo delle frecce. Niente segnaposto: scrivi le stringhe vere.
3. **Le relazioni** — chi punta a chi, cosa entra e cosa esce, l'ordine, gli eventuali loop di ritorno.
4. **L'elemento focale** — indica esplicitamente quale elemento (o quali pochi) porta il significato e va messo in risalto rispetto agli altri, e perché. È un'informazione di contenuto ("il fulcro è il blocco LLM"), non una scelta di colore: sarà l'agente a decidere *come* evidenziarlo.

Non chiudere il prompt con vincoli di stile (colore accento, "monocromatico", font): li aggiunge l'agente. Se un requisito grafico è davvero essenziale al *significato* (es. "due zone che devono leggersi come opposte"), esprimilo come requisito di leggibilità/semantica, non come istruzione di palette.

## Micro-esempio di un buon incipit

> Diagramma orizzontale a 3 livelli paralleli, tutti convergenti su un unico blocco centrale "LLM (funzione)". A sinistra tre rettangoli input impilati: "Il gatto è sul…", "La capitale di Francia è…", "Buongiorno, come…". Ogni rettangolo ha una freccia verso il blocco centrale. Dal blocco escono 3 frecce verso destra, ognuna verso un mini grafico a barre etichettato con i token e le probabilità: … L'elemento focale è il blocco centrale "LLM" e, in ciascuna distribuzione, la barra del token più probabile.

## Come intervistare sul visual

Sezione per sezione, per ogni slide che potrebbe avere un SVG, cammina questi rami uno alla volta (con la tua raccomandazione):

1. Serve un SVG? (se no → `Visual: nessuno`, chiudi)
2. Qual è la **una cosa** che deve capire chi guarda? (il messaggio del diagramma)
3. Che **forma** lo comunica meglio? (flusso / loop / scala / strati / confronto / sequenza)
4. Quali **elementi ed etichette** esatte? (falli dettare o proponili dal draft)
5. Qual è l'**elemento focale**, quello che porta il significato?
6. Rileggi il prompt di contenuto che hai composto e fatti confermare prima di passare alla slide successiva.
