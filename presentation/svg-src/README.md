# Sorgenti degli SVG — Sezione 3

Gli SVG in `../svg/` **non vanno modificati a mano**: sono generati da questi
script. Modificare l'SVG e non il generatore fa divergere le due fonti, e il
prossimo `regen.py` cancella la modifica.

```bash
python3 presentation/svg-src/regen.py
```

Non servono dipendenze: solo Python 3.

## I file

| file | produce |
|------|---------|
| `alfa.py` | **le primitive dell'alfabeto visivo** — non genera nulla da solo |
| `gen_a.py` | slide 10, 12, 14 — le tre che l'alfabeto lo *insegnano* |
| `gen15.py` | slide 15 — la torre, nei tre tempi |
| `gen_b.py` | slide 16, 17, 21, 22 — gli zoom |
| `gen_griglia.py` | slide 18, 19, 20 e 20b — la griglia dell'attention |
| `gen_c.py` | slide 23, 24, 27 — le slide che chiudono la sezione |
| `gen_minimap.py` | le sei mini-mappe "sei qui" |

## L'alfabeto

Le regole stanno scritte per esteso nella spec
(`spec/incontro-26/slide-specs-incontro26-section-3.md`, blocco *Alfabeto
visivo della sezione*). In sintesi: il vettore è una riga di **4 celle**, q/k/v
sono **3 celle**, la matrice di proiezione è una griglia **4×3**, e i diagrammi
di flusso si leggono **dal basso verso l'alto** (unica eccezione la slide 12,
che è una lista numerata e va dall'alto; la 25 è una slide-metafora e non usa l'alfabeto).

Il colore codifica il **ruolo**, non l'enfasi: teal = embedding, burgundy = q,
grafite = k, lightblue = v, giallo = posizione.

## Un debito da sapere

`gen15.py`, `gen_griglia.py` e `gen_minimap.py` sono nati **prima** di
`alfa.py` e portano ciascuno la propria copia delle primitive. Producono lo
stesso alfabeto, ma il codice è duplicato: se metti mano a uno di questi tre,
conviene migrarlo su `alfa.py`. Attenzione che le primitive non sono
byte-identiche (per esempio il raggio degli angoli delle celle), quindi una
migrazione cambia l'output: va riverificata a schermo, slide per slide.

## Verificare le slide

Il deck si serve con la configurazione `deck` in `.claude/launch.json`
(python http.server sulla porta 8001), poi
`http://localhost:8001/presentation/presentation.html`.

Dopo ogni rigenerazione il browser tiene gli SVG in cache: per vederli
aggiornati serve forzare il ricaricamento degli `img`, non basta ricaricare
la pagina.
