# Sorgenti degli SVG — Sezioni 2 e 3 dell'incontro 26

> **Perimetro**: quanto segue vale **solo per gli SVG dell'incontro 26 elencati nella tabella**.
> Dall'incontro 27 in poi gli SVG si scrivono **direttamente come markup** (a mano o con
> l'agente `svg-generator`) e si modificano nel file: niente generatori Python. Il passaggio
> per Python era servito a condividere l'alfabeto visivo della sezione 3; per figure una
> per una è un giro in più che non ripaga. Non è un divieto: se per una famiglia di figure
> un generatore avesse senso, lo si propone al docente e si decide caso per caso.

Gli SVG in `../svg/` **non vanno modificati a mano**: sono generati da questi
script. Modificare l'SVG e non il generatore fa divergere le due fonti, e il
prossimo `regen.py` cancella la modifica.

```bash
python3 presentation/svg-src/regen.py      # Sezione 3
python3 presentation/svg-src/gen_sez2.py   # Sezione 2 (slide 9 e 9b)
```

Non servono dipendenze: solo Python 3.

`gen_sez2.py` sta **fuori** da `regen.py` di proposito: `regen.py` e' il contratto della
Sezione 3 ("dopo averlo lanciato `git status` dev'essere pulito") e non va allargato.
Le altre figure delle Sezioni 1–2 — slide 2, 4, 7 — sono piccole e restano scritte a mano
direttamente nell'SVG: quelle si modificano nel file, non qui.

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
| `gen_sez2.py` | **Sezione 2** — slide 9 e 9b, i loop. Fuori da `regen.py`: si lancia a mano |

## L'alfabeto

Le regole stanno scritte per esteso nella spec
(`spec/incontro-26/slide-specs-incontro26-section-3.md`, blocco *Alfabeto
visivo della sezione*). In sintesi: il vettore è una riga di **4 celle**, q/k/v
sono **3 celle**, la matrice di proiezione è una griglia **4×3**, e i diagrammi
di flusso si leggono **dal basso verso l'alto** (unica eccezione la slide 12,
che è una lista numerata e va dall'alto; la 31 è una slide-metafora e non usa l'alfabeto).

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
