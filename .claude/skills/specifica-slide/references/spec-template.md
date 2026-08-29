# Template della specifica slide

La specifica è la **fonte di verità** del contenuto e dell'ordine delle slide. Un file per sezione, in `spec/`, nel formato qui sotto.

Convenzioni:
- Nome file: `spec/slide-specs-incontroNN-section-K.md` (NN = numero incontro, K = numero sezione).
- Le slide sono numerate a partire da 1 nel contesto dell'intera lezione (non della singola sezione), coerentemente con l'ordine di presentazione.
- Ogni file di sezione apre con un'intestazione e la **tabella file→slide** delle slide di quella sezione.

---

## Intestazione di sezione (in cima al file)

```markdown
# Specifica slide — <Titolo lezione / incontro>
## <Autore> — <contesto/corso>

**Sezione K — <Titolo sezione>**
**Obiettivo di apprendimento**: <cosa il partecipante deve saper fare/capire a fine sezione>
**Messaggio chiave (takeaway)**: <la frase che resta>
**Stato**: <bozza | in revisione | consolidata>

### Tabella file → slide

| File | Slide |
|------|-------|
| `slides/slide-div-secK.html`   | Separatore — Sezione K: <titolo> |
| `slides/slideN-<nome>.html`    | Slide N — <titolo> |
| ...                            | ... |
```

---

## Blocco per singola slide

Ogni slide segue **sempre** questi campi (nell'ordine). Ometti `Prompt per schema SVG` solo quando `Visual` è "nessuno".

```markdown
## Slide N — <Titolo>

**Layout**: <disposizione degli elementi: cosa in alto, al centro, a destra/sinistra, in basso; quanto spazio occupa il visual>.

**Testo**:
- Titolo: *<titolo slide>*
- <Sottotitolo / definizione centrale / bullet / citazione / didascalia — il testo ESATTO che andrà in slide, non una parafrasi>
  1. **<label bullet>**: <testo>
  2. ...
- Citazione / nota in basso (se presente): *<testo>* <— con attribuzione se serve>

**Visual**: <descrizione dell'elemento grafico; oppure "nessuno" se la struttura testuale è essa stessa l'elemento visivo>.

**Prompt per schema SVG**:
> <prompt dettagliato e autoconsistente per l'agente svg-generator — vedi guida-prompt-svg.md>
```

---

## Esempio completo

> Questo è il livello di dettaglio atteso: testo pronto per la slide e prompt SVG che un agente può eseguire senza altre informazioni.

```markdown
## Slide 8 — Loop 1/4: Come l'LLM genera testo

**Layout**: titolo in alto, grande visual narrativo al centro (~70% della slide), didascalia sotto.

**Testo**:
- Titolo: *Loop 1/4: Come l'LLM genera testo*
- Didascalia (sotto il diagramma): *Il modello non pianifica una risposta. Produce un token alla volta. Ogni nuovo token viene appeso al contesto e il contesto completo viene rivalutato per produrre il successivo.*

**Visual**: sequenza narrativa che mostra il contesto che cresce token dopo token, con freccia laterale che chiarisce che ogni riga è una chiamata indipendente al modello. Ogni riga è divisa in due zone: il context (sfondo scuro) e il token appena generato (sfondo accento). Una legenda in alto spiega i due colori.

**Prompt per schema SVG**:
> Visual narrativo verticale che mostra l'evoluzione del contesto token dopo token.
>
> **Legenda in alto**: due riquadri con etichetta — "context (input al modello)" (sfondo scuro) e "token generato (output)" (sfondo accento).
>
> **Colonna centrale** — una pila verticale di 7-8 righe, ognuna è un "contesto" a un certo istante. Ogni riga è composta da due rettangoli adiacenti: uno scuro per il context, uno con sfondo accento semitrasparente per il token appena generato.
>
> Sequenza delle righe (dall'alto verso il basso):
>   1. `Il`  →  2. `Il gatto`  →  3. `Il gatto è`  →  ...  →  8. `Il gatto è sul tavolo e dorme.` (ultimo token "." con simbolo di STOP).
>
> **A destra della pila** — diagramma del loop a 4 passi: ① contesto → ② LLM → ③ token → ④ freccia tratteggiata accent che torna a ① ("appeso al contesto"). Footer: "↻ si ripete fino al token di STOP".
>
> **A sinistra** — graffa verticale che abbraccia le righe: "il contesto cresce di un token per volta".
>
> Elementi focali (da mettere in risalto): l'ultimo token di ogni riga, il diagramma del loop a destra e il badge STOP. Il testo delle righe è di natura "token/codice".
```

> Nota: il prompt descrive **contenuto e significato** (elementi, etichette, elemento focale), non il rendering (colori, palette, font, "monocromatico"): quello lo aggiunge l'agente `svg-generator`, che conosce la house style del deck. La specifica resta indipendente dallo stile grafico.

---

## Quando `Visual: nessuno`

Molte slide **non** hanno un SVG: è la struttura testuale (due colonne contrastive, due blocchi paralleli, una mappa di bullet, una pull-quote) a fare da elemento visivo. In quei casi scrivi `**Visual**: nessuno. <perché la struttura basta>` e ometti il prompt SVG. Non forzare un diagramma dove non aggiunge comprensione.
