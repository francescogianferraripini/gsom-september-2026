# -*- coding: utf-8 -*-
"""Lotto C: le slide che chiudono la sezione (23, 27, 24)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alfa import *
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

# ================= SLIDE 23 — il contesto ha un costo =================
def slide23():
    W, H = 760, 392
    TOK = ["Il", "gatto", "è", "sul", "tavolo", "e"]
    ROWS = [("strato N", 88), (None, 130), ("strato 2", 144), ("strato 1", 180)]
    RH, CW, PITCH, GX = 30, 32, 40, 76
    o = []

    def cell(cx, y, on, dim=False):
        s = []
        if on:
            s.append(rect(cx - CW / 2.0 - 3, y - 3, CW + 6, RH + 6, "none", BUR, rx=4, sw=1.3))
        op = 0.4 if dim else None
        s.append(rect(cx - CW / 2.0, y + 5, CW, 8, GRA_F, GRA, rx=2, sw=0.8, op=op))
        s.append(rect(cx - CW / 2.0, y + 17, CW, 8, BLU_F, BLU, rx=2, sw=0.8, op=op))
        return "".join(s)

    def panel(x0, title, cached, notes):
        cols = [x0 + GX + i * PITCH for i in range(7)]
        s = [txt(x0, 22, title, 12.5, BODY, "start", "700")]
        for i, n in enumerate(notes):
            s.append(txt(x0, 40 + i * 12, n, 9, GREYD if cached else BUR, "start"))
        if cached:
            s.append(rect(cols[0] - 22, 80, 6 * PITCH + 4, 148, SOFT, "none", rx=6))
            s.append(txt(cols[0] - 22 + (6 * PITCH + 4) / 2.0, 222, "K, V in cache",
                         10, GREYD, "middle", "600"))
            s.append(txt(cols[6], 74, "riusate, non ricalcolate", 9.5, BUR, "middle", "600"))
        for cx in cols:
            s.append(line(cx, 226, cx, 84, "#e9ecef", 1.2))
        for lab, y in ROWS:
            if lab is None:
                s.append(txt(cols[0] - 22 + (6 * PITCH) / 2.0, y + 4, "⋯", 14, GREYD, "middle"))
                continue
            s.append(txt(x0 + 50, y + 19, lab, 9.5, GREYD, "end"))
            for j, cx in enumerate(cols):
                nuovo = (j == 6)
                s.append(cell(cx, y, on=(nuovo or not cached), dim=(cached and not nuovo)))
        for j, cx in enumerate(cols):
            lab = "token nuovo" if j == 6 else TOK[j]
            s.append(txt(cx + 4, 292, lab, 9.5, BUR if j == 6 else GREYD,
                         "start", "700" if j == 6 else "400", None if j == 6 else MONO, rot=-90))
        if cached:
            s.append(arrow(cols[5] + 22, 160, cols[6] - 24, 160, BUR, 1.5, marker="ab"))
        return "".join(s)

    o.append(panel(0, "senza KV cache", False,
                   ["K e V: ricalcolate a ogni giro", "fully connected: rifatti",
                    "Q del passato: calcolate e buttate"]))
    o.append(panel(368, "con KV cache", True,
                   ["K e V dei token già visti: salvati", "si calcola solo la colonna nuova"]))
    o.append(line(342, 16, 342, 300, "#eef0f2", 1))

    for x0, cost, sub in ((0, "costo del token n-esimo ≈ n²", "ricalcoli tutto il passato, a ogni strato"),
                          (368, "costo del token n-esimo ≈ n", "paghi solo il token nuovo")):
        o.append(rect(x0, 306, 3, 34, BUR, "none", rx=1.5))
        o.append(txt(x0 + 14, 320, cost, 12, BODY, "start", "700"))
        o.append(txt(x0 + 14, 334, sub, 10, GREYD))
    o.append(txt(380, 362, "la masked attention rende il passato immutabile → si può salvare",
                 11, BODY, "middle", "600"))
    o.append(rect(150, 376, 22, 7, GRA_F, GRA, rx=2, sw=0.8))
    o.append(txt(178, 383, "k", 9.5, BODY, "start", "600", MONO))
    o.append(rect(198, 376, 22, 7, BLU_F, BLU, rx=2, sw=0.8))
    o.append(txt(226, 383, "v", 9.5, BODY, "start", "600", MONO))
    o.append(txt(248, 383, "— ogni cella è la chiave e il valore di quel token a quello strato",
                 9.5, GREYD, "start"))
    return svg(W, H, "".join(o),
               "Due griglie token per strato: senza KV cache si ricalcola tutto, con la cache solo la colonna del token nuovo")


# ================= SLIDE 27 — MoE =================
def slide27():
    W, H = 700, 430
    o = []
    EXP = [(66, False), (148, False), (230, True), (312, False),
           (394, False), (476, True), (558, False), (640, False)]

    o.append(vec(350, 392, 4, 22, TEAL, TEAL_F))
    o.append(txt(296, 400, "l'embedding", 11, TEAL_D, "end", "700"))
    o.append(txt(296, 412, "in transito", 9.5, GREYD, "end"))
    o.append(arrow(350, 388, 350, 358))

    o.append(rect(300, 322, 100, 32, "#ffffff", BUR, rx=6, sw=1.6))
    o.append(txt(350, 343, "router", 13, BUR, "middle", "500", MONO))
    o.append(txt(412, 336, "un piccolo selettore:", 9.5, BODY, "start", "600"))
    o.append(txt(412, 348, "decide chi lavora su questo token", 9.5, GREYD))

    for cx, on in EXP:
        o.append(curve(350, 318, 350, 300, cx, 306, cx, 292,
                       BUR if on else "#e3e6ea", 1.6 if on else 1.1,
                       marker="ab" if on else "a"))
        o.append(rect(cx - 36, 236, 72, 56, BUR_F if on else "#ffffff",
                      BUR if on else LINE, rx=6, sw=1.5 if on else 1.1))
        for k in range(3):
            o.append(rect(cx - 24, 252 + k * 12, 48, 7, "#ffffff" if on else SOFT,
                          BUR if on else LINE, rx=2, sw=0.7))
        o.append(txt(cx, 248, "E%d" % (EXP.index((cx, on)) + 1), 8.5,
                     BUR if on else GREYD, "middle", "700"))
        if on:
            o.append(curve(cx, 232, cx, 214, 350, 214, 350, 200, BUR, 1.6, marker="ab"))
    o.append(txt(0, 228, "ogni esperto è un fully connected più piccolo", 9.5, GREYD))

    o.append(plus(350, 188))
    o.append(arrow(350, 178, 350, 160))
    o.append(vec(350, 132, 4, 22, TEAL, TEAL_F))
    o.append(txt(412, 148, "il vettore in uscita", 11, TEAL_D, "start", "700"))

    o.append(rect(150, 40, 400, 56, BLACK, "none", rx=8))
    o.append(txt(350, 63, "parametri totali: tutti gli esperti", 12, "#ffffff", "middle", "600"))
    o.append(txt(350, 81, "lavoro per token: solo 2", 12, YEL, "middle", "700"))
    return svg(W, H, "".join(o),
               "Dal basso: l'embedding entra nel router, che accende due esperti su otto; le loro uscite si sommano nel vettore finale")

# ================= SLIDE 24 — la conoscenza e' nei pesi =================
def slide24():
    W, H = 700, 434
    o = []
    o.append(rect(170, 396, 360, 30, BLACK, "none", rx=6))
    o.append(txt(350, 416, "Qual è la capitale della Francia?", 12.5, "#ffffff", "middle", "600"))
    o.append(curve(300, 394, 220, 386, 170, 380, 168, 366, ARROW, 1.4))
    o.append(curve(400, 394, 480, 386, 530, 380, 532, 366, ARROW, 1.4))
    o.append(line(350, 40, 350, 372, "#eef0f2", 1))

    # --- sinistra: un database
    o.append(eyebrow(0, 356, "UN DATABASE"))
    rows = [("Italia", "Roma", False), ("Francia", "Parigi", True), ("Germania", "Berlino", False)]
    for i, (a, b, hot) in enumerate(rows):
        y = 300 - i * 28
        o.append(rect(10, y, 300, 26, BUR_F if hot else "#ffffff", BUR if hot else LINE,
                      rx=3, sw=1.4 if hot else 1.0))
        o.append(txt(24, y + 17, a, 10.5, BUR if hot else BODY, "start", "700" if hot else "400"))
        o.append(txt(180, y + 17, b, 10.5, BUR if hot else BODY, "start", "700" if hot else "400"))
    o.append(txt(10, 228, "trova la riga: il recupero è esatto", 10.5, BODY, "start", "600"))
    o.append(txt(10, 241, "la risposta è scritta da qualche parte", 9.5, GREYD))
    o.append(arrow(160, 214, 160, 90, "#c3c8cd", 1.4))
    o.append(rect(10, 34, 300, 44, SOFT, LINE, rx=6, sw=1.1))
    o.append(txt(24, 52, "la risposta è SCRITTA", 11, BODY, "start", "700"))
    o.append(txt(24, 67, "esiste una riga che la contiene", 9.5, GREYD))

    # --- destra: un LLM
    o.append(eyebrow(370, 356, "UN LLM"))
    o.append(vec(420, 320, 4, 20, TEAL, TEAL_F))
    o.append(txt(510, 334, "l'embedding della domanda", 9.5, TEAL_D, "start"))
    o.append(arrow(420, 316, 420, 300))
    o.append(vvec(420, 236, 4, 16, GREYD, SOFT))
    o.append(txt(444, 250, "un rilevatore = una colonna di matrice", 9.5, BODY, "start", "600"))
    o.append(txt(444, 262, "pattern: «capitale della Francia»", 9.5, GREYD, "start", "400", MONO))
    o.append(txt(444, 276, "scatta", 10, BUR, "start", "700"))
    o.append(arrow(420, 232, 420, 216))
    o.append(vec(420, 194, 4, 20, TEAL, TEAL_F))
    o.append(txt(510, 208, "il contributo spinge verso Parigi", 9.5, BUR, "start", "600"))
    o.append(rect(370, 96, 320, 84, "url(#dots)", LINE, rx=6))
    pts = [(410, 158, "Francia"), (410, 122, "Italia"), (560, 148, "Parigi"), (560, 112, "Roma")]
    for x, y, lab in pts:
        o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, BODY))
        o.append(txt(x, y - 7, lab, 8.5, BODY, "middle"))
    o.append(arrow(418, 156, 552, 150, BUR, 1.4, marker="ab"))
    o.append(arrow(418, 120, 552, 114, BUR, 1.4, marker="ab"))
    o.append(txt(486, 174, "la stessa direzione: «capitale di»", 8.5, BUR, "middle"))
    o.append(rect(370, 34, 320, 44, BLACK, "none", rx=6))
    o.append(txt(384, 52, "la risposta è DISTRIBUITA", 11, "#ffffff", "start", "700"))
    o.append(txt(384, 67, "vettori appresi + una geometria emersa", 9.5, YEL, "start"))
    return svg(W, H, "".join(o),
               "A sinistra un database trova la riga; a destra un LLM ricostruisce la risposta da un rilevatore che scatta e da una direzione nello spazio delle idee")

if __name__ == "__main__":
    for fn, body in (("slide23-costo-contesto.svg", slide23()),
                     ("slide27-moe.svg", slide27()),
                     ("slide24-conoscenza-nei-pesi.svg", slide24())):
        open(os.path.join(OUT, fn), "w").write(body)
        print(fn)
