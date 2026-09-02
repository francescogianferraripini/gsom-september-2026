# -*- coding: utf-8 -*-
"""Lotto B: i quattro zoom sui blocchi della torre (16, 17, 21, 22)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alfa import *
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

# ================= SLIDE 16 — Fanout =================
def slide16():
    W, H = 700, 360
    GUT = 170
    COLS = [218, 302, 386, 470, 554, 638]
    CONC = ["animale domestico", "arriva un luogo", "frase al presente",
            "contesto giuridico", "linguaggio matematico", "… e altre migliaia"]
    ACTV = [110, 100, 62, 9, 6, 0]
    o = []
    BASE, GATE0, GATE1 = 218, 68, 100

    # embedding in transito (in basso)
    o.append(vec(428, 328, 4, 22, TEAL, TEAL_F))
    o.append(txt(GUT - 8, 342, "l'embedding", 11, TEAL_D, "end", "700"))
    o.append(txt(GUT - 8, 354, "in transito", 9.5, GREYD, "end"))
    for cx in COLS:                                   # il fanout
        o.append(curve(428, 324, 428, 310, cx, 312, cx, 300, ARROW, 1.0))

    # la batteria di rilevatori
    for cx in COLS:
        o.append(vvec(cx, 226, 4, 18, GREYD, SOFT))
    o.append(txt(GUT - 8, 250, "la batteria", 11, BODY, "end", "700"))
    o.append(txt(GUT - 8, 262, "un rilevatore per concetto", 9.5, GREYD, "end"))
    o.append(txt(GUT - 8, 274, "migliaia, a ogni token", 9.5, GREYD, "end"))

    # attivazioni: barre verticali
    o.append(txt(GUT - 8, 160, "attivazione", 11, BUR, "end", "700"))
    o.append(txt(GUT - 8, 172, "quanto l'embedding", 9.5, GREYD, "end"))
    o.append(txt(GUT - 8, 184, "somiglia al rilevatore", 9.5, GREYD, "end"))
    for cx, a, c in zip(COLS, ACTV, CONC):
        passa = a > 40
        if a:
            o.append(rect(cx - 13, BASE - a, 26, a, BUR if passa else BUR_F,
                          "none", rx=3))
        o.append(txt(cx - 22, BASE - 2, c, 9, BODY if passa else GREYD, "start", "500", rot=-90))

    # il gate
    o.append(rect(GUT, GATE0, W - GUT - 10, GATE1 - GATE0, BLACK, "none", rx=5))
    o.append(txt(GUT - 8, GATE0 + 14, "non linearità", 11, BODY, "end", "700"))
    o.append(txt(GUT - 8, GATE0 + 26, "il gate", 9.5, GREYD, "end"))
    for cx, a in zip(COLS, ACTV):
        if a > 40:
            o.append(arrow(cx, GATE1 + 6, cx, GATE0 - 22, BUR, 1.6, marker="ab"))
        elif a:
            o.append('<circle cx="%s" cy="%s" r="7.5" fill="none" stroke="#5c6066" '
                     'stroke-width="1.2"/>' % (cx, (GATE0 + GATE1) / 2.0))
            o.append(txt(cx, (GATE0 + GATE1) / 2.0 + 4, "0", 10, "#9aa0a6", "middle", "600", MONO))

    o.append(txt(GUT, 30, "i concetti sopravvissuti proseguono nel blocco", 11.5, BODY, "start", "600"))
    o.append(txt(GUT, 44, "passa solo ciò che è davvero affine; tutto il resto viene azzerato", 9.5, GREYD))
    return svg(W, H, "".join(o),
               "Dal basso: l'embedding interroga in parallelo una batteria di rilevatori; il gate lascia passare solo le attivazioni forti")

# ================= SLIDE 17 — Compressione =================
def slide17():
    W, H = 700, 440
    o = []
    # --- spazio delle idee, in cima: il significato che si sposta
    o.append(rect(0, 16, W, 186, "url(#dots)", LINE, rx=6))
    o.append(eyebrow(12, 34, "SPAZIO DELLE IDEE", GREYD))
    o.append('<ellipse cx="215" cy="78" rx="105" ry="38" fill="#f0f1f2"/>')
    o.append(txt(215, 50, "ANIMALI DOMESTICI", 8.5, GREYD, "middle", "700", ls="0.1em"))
    o.append('<ellipse cx="520" cy="96" rx="105" ry="38" fill="#f0f1f2"/>')
    o.append(txt(520, 68, "LUOGHI DELLA CASA", 8.5, GREYD, "middle", "700", ls="0.1em"))
    for x, y in ((178, 88), (232, 74), (258, 98)):
        o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, GREYD))
    for x, y in ((486, 106), (540, 92), (566, 114)):
        o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, GREYD))
    o.append('<circle cx="150" cy="170" r="5" fill="%s"/>' % BODY)
    o.append(txt(150, 188, "«gatto» in ingresso", 9.5, BODY, "middle"))
    o.append(arrow(158, 165, 342, 122, BUR, 2, marker="ab"))
    o.append('<circle cx="350" cy="118" r="5.5" fill="%s"/>' % BUR)
    o.append(txt(362, 122, "«gatto» dopo il blocco", 9.5, BUR, "start", "600"))
    o.append(txt(232, 124, "= il contributo del blocco", 9, BUR, "middle"))

    # --- la somma, dal basso: concetti -> contributo -> + skip -> embedding spostato
    o.append(line(250, 222, 250, 202, "#c3c8cd", 1.2, dash="3 3"))
    o.append(txt(262, 214, "→ nello spazio delle idee", 8.5, GREYD))
    o.append(vec(250, 226, 4, 22, BUR, TEAL_F))
    o.append(txt(310, 234, "l'embedding, spostato", 11.5, BODY, "start", "600"))
    o.append(txt(310, 247, "è quello che esce dal blocco", 9.5, GREYD))
    o.append(plus(250, 274))
    o.append(arrow(250, 266, 250, 252))
    o.append(vec(84, 262, 4, 22, TEAL, TEAL_F))
    o.append(txt(84, 296, "embedding originale", 9.5, GREYD, "middle"))
    o.append(txt(84, 308, "(skip connection)", 9.5, GREYD, "middle"))
    o.append(arrow(132, 273, 238, 273))
    o.append(vec(250, 306, 4, 22, TEAL, TEAL_F))
    o.append(txt(310, 314, "contributo del blocco", 11.5, BUR, "start", "600"))
    o.append(txt(310, 327, "una direzione nello spazio delle idee", 9.5, GREYD))
    o.append(arrow(250, 302, 250, 288))
    conc = [(120, "animale domestico", 38), (250, "arriva un luogo", 34), (380, "frase al presente", 22)]
    for cx, lab, h in conc:
        o.append(rect(cx - 11, 410 - h, 22, h, BUR, "none", rx=3))
        o.append(txt(cx, 426, lab, 9, GREYD, "middle"))
        o.append(curve(cx, 406 - h, cx, 372, 250, 366, 250, 340, ARROW, 1.1))
    o.append(txt(96, 372, "le attivazioni sopravvissute al gate (Slide 16)", 9, GREYD))
    o.append(txt(470, 392, "i concetti sopravvissuti al gate", 11, BODY, "start", "600"))
    o.append(txt(470, 405, "si ri-sommano in un vettore solo:", 9.5, GREYD))
    o.append(txt(470, 417, "più significati, sovrapposti", 9.5, GREYD))
    return svg(W, H, "".join(o),
               "Dal basso: i concetti sopravvissuti si sommano nel contributo del blocco, che sommato all'embedding lo sposta nello spazio delle idee")

# ================= SLIDE 21 — Positional encoding =================
def slide21():
    W, H = 700, 430
    o = []
    def bag(x0, y0, x1, y1, seed, label, dash, col, ordered=False, marks=None):
        s = [rect(x0, y0, x1 - x0, y1 - y0, "#ffffff", col, rx=6, dash=dash)]
        s.append(txt(x0 + 10, y0 + 16, label, 9, col, "start", "700", ls="0.1em"))
        import math
        for i in range(5):
            cx = x0 + 40 + i * 52
            if ordered:
                f = (marks or {}).get(i, TEAL_F)
                s.append(vec(cx, y0 + 42, 4, 11, TEAL, f, sw=1.0))
                s.append(rect(cx - 22, y0 + 56, 44, 6, YEL_F, YEL, rx=1.5, sw=0.8))
                s.append(txt(cx, y0 + 74, "pos %d" % (i + 1), 7.5, YEL_D, "middle", "600"))
            else:
                a = (seed * 37 + i * 53) % 40 - 20
                cy = y0 + 50 + ((seed * 13 + i * 29) % 18) - 9
                s.append('<g transform="rotate(%s %s %s)">%s</g>'
                         % (a, cx, cy, vec(cx, cy - 6, 4, 11, TEAL, TEAL_F, sw=1.0)))
        return "".join(s)

    # --- SCENA A (in basso): senza posizione, un solo sacchetto
    o.append(eyebrow(0, 300, "SENZA POSIZIONE — L'ATTENTION NON SA CHI VIENE PRIMA"))
    for k, (yy, toks) in enumerate(((316, ["il", "gatto", "morde", "il", "cane"]),
                                    (348, ["il", "cane", "morde", "il", "gatto"]))):
        for i, t in enumerate(toks):
            o.append(tile(58 + i * 62, yy, 58, 24, t, 11))
        o.append(txt(0, yy + 16, "frase %d" % (k + 1), 8.5, GREYD, "start"))
    o.append(curve(344, 328, 380, 328, 380, 346, 392, 346, ARROW, 1.3))
    o.append(curve(344, 360, 380, 360, 380, 346, 392, 346, ARROW, 1.3))
    o.append(bag(400, 302, 692, 392, 3, "UN SOLO INSIEME, NON ORDINATO", "5 4", BUR))
    o.append(txt(546, 412, "stesso sacchetto: per l'attention sono indistinguibili", 9.5, BUR, "middle"))

    # --- SCENA B (in alto): con positional encoding
    o.append(eyebrow(0, 30, "CON POSITIONAL ENCODING — L'ORDINE ENTRA NEI VETTORI"))
    o.append(tile(120, 232, 120, 28, "gatto", 13))
    o.append(arrow(120, 228, 120, 216))
    o.append(vec(120, 190, 4, 22, TEAL, TEAL_F))
    o.append(txt(186, 205, "l'embedding di «gatto»", 9.5, TEAL_D, "start"))
    o.append(arrow(120, 186, 120, 178))
    o.append(plus(120, 168, 8, YEL))
    o.append(arrow(120, 158, 120, 148))
    o.append(vec(120, 122, 4, 22, YEL, YEL_F))
    o.append(txt(186, 137, "il vettore della posizione 2", 9.5, YEL_D, "start"))
    o.append(arrow(120, 118, 120, 104))
    o.append(vec(120, 78, 4, 22, YEL, TEAL_F))
    o.append(txt(186, 87, "«gatto», secondo token:", 9.5, BODY, "start", "600"))
    o.append(txt(186, 99, "lo stesso punto, spostato un po'", 9.5, GREYD, "start"))
    o.append(bag(400, 46, 692, 136, 3, "FRASE 1 — «il gatto morde il cane»", None, TEAL,
                 ordered=True, marks={1: "#7fd4c3", 4: "#b9e6dc"}))
    o.append(bag(400, 150, 692, 240, 8, "FRASE 2 — «il cane morde il gatto»", None, TEAL,
                 ordered=True, marks={1: "#b9e6dc", 4: "#7fd4c3"}))
    o.append(txt(546, 262, "«gatto» sta in posizione 2 o in posizione 5: ora i due insiemi sono diversi",
                 9.5, BODY, "middle", "600"))
    return svg(W, H, "".join(o),
               "In basso senza posizione le due frasi collassano nello stesso insieme; in alto la somma del vettore di posizione le rende distinte")

# ================= SLIDE 22 — Reverse embedding =================
def slide22():
    W, H = 700, 430
    o = []
    VOC = [("sul", "4.2"), ("un", "3.9"), ("morbido", "3.5"), ("nero", "3.3"),
           ("stanco", "2.8"), ("Parigi", "−3.1")]
    DIST = [("sul", 30), ("un", 22), ("morbido", 15), ("nero", 12), ("stanco", 8)]

    # embedding finale (in basso)
    o.append(vec(350, 398, 4, 22, TEAL, TEAL_F))
    o.append(txt(296, 408, "embedding finale", 11, TEAL_D, "end", "700"))
    o.append(txt(296, 420, "dopo tutti i blocchi", 9.5, GREYD, "end"))
    o.append(arrow(350, 394, 350, 378))
    o.append(txt(424, 406, "Simmetria: all'ingresso da token a vettore.", 9.5, BODY, "start", "600"))
    o.append(txt(424, 418, "Qui il percorso si inverte: da vettore a token.", 9.5, GREYD))

    # il vocabolario: un prodotto scalare per riga
    o.append(rect(40, 232, 620, 142, "#ffffff", LINE, rx=6))
    o.append(txt(54, 250, "IL VOCABOLARIO — UNA RIGA PER TOKEN, OGNUNA COL SUO VETTORE",
                 8.5, GREYD, "start", "700", ls="0.1em"))
    for i, (tok, lg) in enumerate(VOC):
        y = 262 + i * 16
        neg = lg.startswith("−")
        o.append(txt(150, y + 11, tok, 10.5, GREYD if neg else BODY, "end", "400", MONO))
        o.append(vec(190, y, 4, 13, GREYD, SOFT, sw=0.9))
        o.append(txt(256, y + 11, "·", 12, GREYD, "middle", "600"))
        o.append(txt(322, y + 11, lg, 11, GREYD if neg else BUR, "end", "700", MONO))
    o.append(txt(150, 262 + 6 * 16 + 11, "⋯", 11, GREYD, "end"))
    o.append(txt(190, 262 + 6 * 16 + 11, "~100.000 righe", 9.5, GREYD, "start"))
    o.append(txt(360, 276, "ogni riga: un prodotto scalare", 11, BODY, "start", "600"))
    o.append(txt(360, 289, "fra l'embedding finale e il vettore del token.", 9.5, GREYD))
    o.append(txt(360, 309, "Il risultato è il logit: l'affinità grezza.", 9.5, GREYD))
    o.append(txt(360, 331, "Parigi ha logit negativo:", 10, BUR, "start", "600"))
    o.append(txt(360, 344, "l'affinità non seleziona soltanto, esclude.", 9.5, GREYD))
    o.append(arrow(350, 228, 350, 214))

    # softmax
    o.append(rect(298, 186, 104, 28, BLACK, "none", rx=6))
    o.append(txt(350, 205, "softmax", 13, "#ffffff", "middle", "500", MONO))
    o.append(txt(414, 199, "la stessa macchina del budget di ascolto", 9.5, GREYD))
    o.append(arrow(350, 182, 350, 166))

    # la distribuzione (in cima)
    o.append(eyebrow(40, 34, "LA DISTRIBUZIONE SUL PROSSIMO TOKEN"))
    for i, (w, p) in enumerate(DIST):
        y = 48 + i * 21
        o.append(txt(150, y + 12, w, 10.5, BODY, "end", "400", MONO))
        o.append(rect(160, y, p * 12.0, 15, BUR if i == 0 else BUR_F, "none", rx=2))
        o.append(txt(160 + p * 12.0 + 8, y + 12, "%d%%" % p, 10, BUR if i == 0 else GREYD,
                     "start", "600" if i == 0 else "400"))
    o.append(txt(160, 48 + 5 * 21 + 12, "… e gli altri ~100.000 token", 9.5, GREYD))
    return svg(W, H, "".join(o),
               "Dal basso: l'embedding finale confrontato con ogni token del vocabolario da i logits, che la softmax trasforma nella distribuzione")

for fn, body in (("slide16-fanout.svg", slide16()),
                 ("slide17-compressione.svg", slide17()),
                 ("slide21-positional-encoding.svg", slide21()),
                 ("slide22-reverse-embedding.svg", slide22())):
    open(os.path.join(OUT, fn), "w").write(body)
    print(fn)
