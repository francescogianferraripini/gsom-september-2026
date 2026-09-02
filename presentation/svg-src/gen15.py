# -*- coding: utf-8 -*-
"""Genera i tre tempi della slide 15 (la torre) con geometria condivisa."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

W, H = 1240, 420

# --- palette (brand Quantyca) ---
TEAL, TEAL_F, TEAL_D = "#1ab197", "#d1efea", "#0e7c6a"
YEL,  YEL_F,  YEL_D  = "#e0a500", "#fff2ce", "#8a6500"
BUR,  BUR_F          = "#a1245a", "#ecd3de"
LINE, GREYD, BODY    = "#dee2e6", "#838383", "#212529"
BLACK, SOFT, GHOST   = "#161719", "#f6f6f6", "#e9ecef"

FONT = "Poppins, system-ui, -apple-system, 'Segoe UI', sans-serif"
MONO = "'SFMono-Regular', Menlo, Monaco, Consolas, monospace"

# --- geometria condivisa ---
GUT_R = 138                      # bordo destro della colonna etichette
CONT  = (150, 52, 730, 302)      # contenitore "blocco x N"
BLK   = (162, 718)               # x delle bande
LANES = [215, 333, 451, 569]     # corsie: ghost, Il, gatto, e'
TOKENS = ["⋯", "Il", "gatto", "è"]
ACTIVE = 3
CELL, NCELL = 22, 4
VEC_W = CELL * NCELL             # 88

TOK_Y, TOK_H = 374, 26
EMB_Y = 340
PLUS_Y = 332
POS_Y = 306

B1 = (150, 292)
B2 = (114, 142)
ELL_Y = 103
BN = (62, 90)

MSA_Y, MSA_H = 250, 36
MSA_X = (172, 630)
FC_Y, FC_H, FC_W = 190, 32, 60
PLUS_MSA_Y = 238
PLUS_FC_Y = 176

HEAD_X = 796
VF_X, VF_Y = 802, 36
RE_BOX = (796, 78, 980, 136)
SM_BOX = (802, 154, 898, 182)
BAR_Y0, BAR_H, BAR_GAP = 204, 15, 5
BAR_X = 856
PX = 230.0 / 30.0
DIST = [("sul", 30), ("un", 22), ("morbido", 15), ("nero", 12), ("stanco", 8)]

# ---------- helpers ----------
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def txt(x, y, s, size=11, fill=BODY, anchor="start", weight="400",
        font=None, ls=None, op=None, style=None):
    a = ['x="%s" y="%s"' % (x, y), 'font-family="%s"' % (font or FONT),
         'font-size="%s"' % size, 'fill="%s"' % fill, 'text-anchor="%s"' % anchor,
         'font-weight="%s"' % weight]
    if ls is not None: a.append('letter-spacing="%s"' % ls)
    if op is not None: a.append('opacity="%s"' % op)
    if style: a.append('font-style="%s"' % style)
    return '<text %s>%s</text>' % (" ".join(a), esc(s))

def rect(x, y, w, h, fill="none", stroke="none", rx=0, sw=1, op=None, dash=None):
    a = ['x="%s" y="%s" width="%s" height="%s"' % (x, y, w, h),
         'fill="%s"' % fill, 'stroke="%s"' % stroke, 'stroke-width="%s"' % sw, 'rx="%s"' % rx]
    if op is not None: a.append('opacity="%s"' % op)
    if dash: a.append('stroke-dasharray="%s"' % dash)
    return '<rect %s/>' % " ".join(a)

def line(x1, y1, x2, y2, stroke=LINE, sw=1.5, op=None, dash=None, marker=False):
    a = ['x1="%s" y1="%s" x2="%s" y2="%s"' % (x1, y1, x2, y2),
         'stroke="%s"' % stroke, 'stroke-width="%s"' % sw]
    if op is not None: a.append('opacity="%s"' % op)
    if dash: a.append('stroke-dasharray="%s"' % dash)
    if marker: a.append('marker-end="url(#ah)"')
    return '<line %s/>' % " ".join(a)

def path(d, stroke=LINE, sw=1.5, fill="none", op=None, dash=None, marker=False):
    a = ['d="%s"' % d, 'stroke="%s"' % stroke, 'stroke-width="%s"' % sw, 'fill="%s"' % fill,
         'stroke-linejoin="round"', 'stroke-linecap="round"']
    if op is not None: a.append('opacity="%s"' % op)
    if dash: a.append('stroke-dasharray="%s"' % dash)
    if marker: a.append('marker-end="url(#ah)"')
    return '<path %s/>' % " ".join(a)

def vector(cx, y, stroke, fill, n=NCELL, cell=CELL, op=None):
    """Riga di n celle centrata su cx: la forma canonica di un vettore."""
    x0 = cx - (n * cell) / 2.0
    o = []
    for i in range(n):
        o.append(rect(x0 + i * cell, y, cell, cell, fill=fill, stroke=stroke, sw=1.4, rx=3, op=op))
    return "".join(o)

def plus(cx, cy, r=8, stroke=BUR):
    return ('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
            % (cx, cy, r, stroke)) + txt(cx, cy + 4, "+", 12, stroke, "middle", "600")

DEFS = """<defs>
<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>
<marker id="aht" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>
</defs>""" % (GREYD, BUR, TEAL)

# ---------- pezzi condivisi ----------
def token_row():
    o = [txt(GUT_R, 391, "input", 11, GREYD, "end", "600")]
    for i, cx in enumerate(LANES):
        ghost = (i == 0)
        act = (i == ACTIVE)
        o.append(rect(cx - VEC_W / 2.0, TOK_Y, VEC_W, TOK_H, fill="#ffffff",
                      stroke=BUR if act else LINE, sw=1.6 if act else 1.3, rx=5,
                      op=0.45 if ghost else None))
        o.append(txt(cx, TOK_Y + 18, TOKENS[i], 14 if not ghost else 15,
                     BUR if act else BODY, "middle", "500", MONO,
                     op=0.45 if ghost else None))
    o.append(txt(LANES[0], 415, "il contesto precedente", 9, GREYD, "middle", "400", op=0.7))
    return "".join(o)

def lane_overlay(y0, y1):
    """Segmenti di corsia disegnati SOPRA una banda chiusa: le corsie non si interrompono mai."""
    o = []
    for i, cx in enumerate(LANES):
        act = (i == ACTIVE)
        o.append(line(cx, y0, cx, y1, BUR if act else "#adb5bd", 1.6 if act else 1.2,
                      op=0.75 if act else 0.4))
    return "".join(o)

def lanes(y_top, faint=False):
    o = []
    for i, cx in enumerate(LANES):
        act = (i == ACTIVE)
        col = BUR if act else (GHOST if i == 0 else "#ced4da")
        o.append(line(cx, TOK_Y - 2, cx, y_top, col, 2 if act else 1.5,
                      op=0.35 if faint else (0.5 if i == 0 else None)))
    return "".join(o)

def emb_rows():
    o = [txt(GUT_R, EMB_Y + 15, "embedding", 11, TEAL_D, "end", "600"),
         txt(GUT_R, POS_Y + 15, "+ posizione", 11, YEL_D, "end", "600"),
         txt(GUT_R, POS_Y + 28, "l'ordine entra nel vettore", 8.5, GREYD, "end")]
    for i, cx in enumerate(LANES):
        op = 0.4 if i == 0 else None
        o.append(vector(cx, EMB_Y, TEAL, TEAL_F, op=op))
        o.append(vector(cx, POS_Y, YEL, YEL_F, op=op))
        o.append(plus(cx, PLUS_Y, 7, YEL if i else GHOST))
    return "".join(o)

def head(full=True):
    x0, y0, x1, y1 = RE_BOX
    o = []
    if full:
        # vettore finale
        o.append(vector(VF_X + VEC_W / 2.0, VF_Y, TEAL, TEAL_F))
        o.append(txt(VF_X + VEC_W + 14, VF_Y + 10, "vettore finale", 10.5, TEAL_D, "start", "600"))
        o.append(txt(VF_X + VEC_W + 14, VF_Y + 23, "solo la corsia dell'ultimo token", 9, GREYD))
        o.append(line(VF_X + VEC_W / 2.0, VF_Y + CELL, VF_X + VEC_W / 2.0, y0 - 4, GREYD, 1.4, marker=True))
        # reverse embedding
        o.append(rect(x0, y0, x1 - x0, y1 - y0, fill=SOFT, stroke=LINE, sw=1.2, rx=6))
        o.append(txt(x0 + 12, y0 + 17, "matrice di reverse embedding", 10, BODY, "start", "600"))
        gx, gy = x0 + 12, y0 + 26
        for r in range(4):
            for c in range(9):
                o.append(rect(gx + c * 14, gy + r * 7, 12, 5.5, fill="#ffffff", stroke=LINE, sw=0.7, rx=1))
        o.append(txt(x1 + 10, y0 + 26, "~100.000 righe:", 9, GREYD))
        o.append(txt(x1 + 10, y0 + 38, "una per token del", 9, GREYD))
        o.append(txt(x1 + 10, y0 + 50, "vocabolario", 9, GREYD))
        o.append(line((x0 + x1) / 2.0, y1, (x0 + x1) / 2.0, SM_BOX[1] - 4, GREYD, 1.4, marker=True))
        # softmax
        sx0, sy0, sx1, sy1 = SM_BOX
        o.append(rect(sx0, sy0, sx1 - sx0, sy1 - sy0, fill=BLACK, stroke="none", rx=6))
        o.append(txt((sx0 + sx1) / 2.0, sy0 + 19, "softmax", 13, "#ffffff", "middle", "500", MONO))
        o.append(line((sx0 + sx1) / 2.0, sy1, (sx0 + sx1) / 2.0, BAR_Y0 - 12, GREYD, 1.4, marker=True))
    # distribuzione
    o.append(txt(SM_BOX[2] + 16, SM_BOX[1] + 19, "la distribuzione sul", 9, GREYD))
    o.append(txt(SM_BOX[2] + 16, SM_BOX[1] + 30, "prossimo token", 9, BUR, "start", "700"))
    for i, (w, p) in enumerate(DIST):
        y = BAR_Y0 + i * (BAR_H + BAR_GAP)
        o.append(txt(BAR_X - 8, y + 12, w, 11, BODY, "end", "400", MONO))
        o.append(rect(BAR_X, y, p * PX, BAR_H, fill=BUR if i == 0 else BUR_F, stroke="none", rx=2))
        o.append(txt(BAR_X + p * PX + 8, y + 12, "%d%%" % p, 10, GREYD if i else BUR,
                     "start", "600" if i == 0 else "400"))
    yb = BAR_Y0 + len(DIST) * (BAR_H + BAR_GAP)
    for i in range(3):
        o.append(rect(BAR_X, yb + i * 7, 26 - i * 7, 4, fill=BUR_F, stroke="none", rx=1, op=0.7))
    o.append(txt(BAR_X + 40, yb + 12, "… e gli altri ~100.000 token", 9, GREYD))
    return "".join(o)

def legend():
    lx, ly = HEAD_X, 336
    o = [txt(lx, ly, "COME LEGGERE", 9, GREYD, "start", "700", ls="0.14em")]
    rows = [
        (TEAL, TEAL_F, "una riga di 4 celle = un vettore", None),
        (YEL, YEL_F, "stesso oggetto, altro ruolo: la posizione", None),
    ]
    y = ly + 20
    for stroke, fill, label, _ in rows:
        o.append(vector(lx + 34, y - 11, stroke, fill, n=4, cell=17))
        o.append(txt(lx + 82, y, label, 9.5, BODY))
        y += 26
    o.append(line(lx + 34, y - 16, lx + 34, y + 2, "#adb5bd", 1.8))
    o.append('<circle cx="%s" cy="%s" r="2.6" fill="#ced4da"/>' % (lx + 34, y - 7))
    o.append(txt(lx + 82, y - 4, "una corsia verticale = un token", 9.5, BODY))
    return "".join(o)

def wrap(body, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img" aria-label="%s">%s<rect width="%d" height="%d" fill="#ffffff"/>%s</svg>'
            % (W, H, W, H, esc(title), DEFS, W, H, body))

# ---------- TEMPO 1: scatola nera ----------
def tempo1():
    o = []
    x0, y0, x1, y1 = CONT
    for i, cx in enumerate(LANES):
        o.append(line(cx, TOK_Y - 2, cx, y1 + 6, "#ced4da", 1.5,
                      op=0.5 if i == 0 else None, marker=True))
    o.append(token_row())
    o.append(rect(x0, y0, x1 - x0, y1 - y0, fill=BLACK, stroke="none", rx=10))
    o.append(txt((x0 + x1) / 2.0, 165, "LLM", 40, "#ffffff", "middle", "700"))
    o.append(txt((x0 + x1) / 2.0, 195, "una funzione: testo → distribuzione sul prossimo token",
                 12, "#ffffff", "middle", "300", op=0.75))
    o.append(txt((x0 + x1) / 2.0, 224, "è quello che abbiamo definito finora", 10, YEL, "middle"))
    o.append(path("M %s %s H %s V %s" % (x1, 177, HEAD_X + 60, BAR_Y0 - 20), GREYD, 1.6, marker=True))
    o.append(head(full=False))
    return wrap("".join(o), "L'LLM come scatola nera: dal testo alla distribuzione sul prossimo token")

# ---------- torre (tempi 2 e 3) ----------
def tower(open_block):
    o = []
    x0, y0, x1, y1 = CONT
    b1a, b1b = B1
    b2a, b2b = B2
    bna, bnb = BN

    o.append(lanes(y0 - 30))
    o.append(token_row())
    o.append(emb_rows())

    # contenitore
    o.append(txt(x0, 44, "IL BLOCCO, RIPETUTO ×N", 10, BUR, "start", "700", ls="0.12em"))
    o.append(txt(x0 + 176, 44, "~100 nei modelli grandi", 9.5, GREYD))
    o.append(rect(x0, y0, x1 - x0, y1 - y0, fill="none", stroke=BUR, sw=1.6, rx=10, dash="6 5"))

    # bande chiuse (N e 2)
    for (ya, yb, lab) in ((bna, bnb, "BLOCCO N"), (b2a, b2b, "BLOCCO 2")):
        o.append(rect(BLK[0], ya, BLK[1] - BLK[0], yb - ya, fill=SOFT, stroke=LINE, sw=1.2, rx=6))
        o.append(lane_overlay(ya, yb))
        o.append(rect((BLK[0] + BLK[1]) / 2.0 - 52, ya + 6, 104, yb - ya - 12, fill=SOFT, stroke="none", rx=3))
        o.append(txt((BLK[0] + BLK[1]) / 2.0, ya + 19, lab, 11.5, GREYD, "middle", "600", ls="0.1em"))
    o.append(txt((BLK[0] + BLK[1]) / 2.0, ELL_Y + 6, "⋯", 22, GREYD, "middle"))

    # blocco 1
    if not open_block:
        o.append(rect(BLK[0], b1a, BLK[1] - BLK[0], b1b - b1a, fill=SOFT, stroke=LINE, sw=1.2, rx=6))
        o.append(lane_overlay(b1a, b1b))
        o.append(rect((BLK[0] + BLK[1]) / 2.0 - 172, 192, 344, 48, fill=SOFT, stroke="none", rx=4))
        o.append(txt((BLK[0] + BLK[1]) / 2.0, 210, "BLOCCO 1", 13, BODY, "middle", "600", ls="0.1em"))
        o.append(txt((BLK[0] + BLK[1]) / 2.0, 232, "tutti i blocchi sono uguali: cambiano solo i pesi",
                     10, GREYD, "middle"))
        o.append(txt(GUT_R, 215, "il cuore", 11, BODY, "end", "600"))
        o.append(txt(GUT_R, 229, "è sempre la stessa cosa,", 8.5, GREYD, "end"))
        o.append(txt(GUT_R, 240, "ripetuta in profondità", 8.5, GREYD, "end"))
    else:
        o.append(rect(BLK[0], b1a, BLK[1] - BLK[0], b1b - b1a, fill="#ffffff", stroke=BUR, sw=1.6, rx=6))
        o.append(txt(BLK[0] + 12, b1a + 18, "BLOCCO 1", 11, BUR, "start", "700", ls="0.1em"))

        # --- masked self-attention: una banda che ATTRAVERSA le corsie
        o.append(rect(MSA_X[0], MSA_Y, MSA_X[1] - MSA_X[0], MSA_H, fill=SOFT, stroke=LINE, sw=1.2, rx=5))
        ymid = MSA_Y + 25
        o.append(line(LANES[0], ymid, LANES[ACTIVE], ymid, BUR, 1.8))
        for i, cx in enumerate(LANES):
            o.append('<circle cx="%s" cy="%s" r="3.4" fill="%s"/>' % (cx, ymid, BUR))
            if i < len(LANES) - 1:
                mx = (cx + LANES[i + 1]) / 2.0
                o.append(path("M %s %s L %s %s" % (mx - 7, ymid, mx + 3, ymid), BUR, 1.8, marker=True))
        o.append(txt(GUT_R, MSA_Y + 14, "masked self-attention", 10.5, BODY, "end", "600"))
        o.append(txt(GUT_R, MSA_Y + 27, "qui le corsie si parlano", 8.5, BUR, "end"))
        o.append(txt(GUT_R, MSA_Y + 38, "e solo verso destra", 8.5, GREYD, "end"))

        # --- fully connected: una cella per corsia, separate
        for i, cx in enumerate(LANES):
            o.append(rect(cx - FC_W / 2.0, FC_Y, FC_W, FC_H, fill=SOFT, stroke=LINE, sw=1.2, rx=5,
                          op=0.5 if i == 0 else None))
            o.append(txt(cx, FC_Y + 20, "FC", 11, GREYD, "middle", "600",
                         op=0.5 if i == 0 else None))
        o.append(txt(GUT_R, FC_Y + 14, "fully connected", 10.5, BODY, "end", "600"))
        o.append(txt(GUT_R, FC_Y + 27, "ogni corsia per conto suo", 8.5, GREYD, "end"))

        # --- nodi + e skip connection (sulla corsia attiva)
        for cx in LANES:
            o.append(plus(cx, PLUS_MSA_Y, 7))
            o.append(plus(cx, PLUS_FC_Y, 7))
        ax = LANES[ACTIVE]
        o.append(path("M %s %s H 648 V %s H %s" % (ax, b1b - 6, PLUS_MSA_Y, ax + 9),
                      BUR, 1.3, dash="4 3", marker=True))
        o.append(path("M %s %s H 676 V %s H %s" % (ax, 228, PLUS_FC_Y, ax + 9),
                      BUR, 1.3, dash="4 3", marker=True))
        o.append('<g transform="rotate(-90 700 236)">' +
                 txt(700, 240, "skip connection", 8.5, BUR, "middle", "600") + '</g>')

    # uscita verso la testa
    ax = LANES[ACTIVE]
    o.append(path("M %s %s V 24 H %s V %s" % (ax, y0, VF_X + VEC_W / 2.0, VF_Y - 4),
                  BUR, 1.6, marker=True))
    o.append(head(full=True))
    o.append(legend())
    return "".join(o)

files = {
    "slide15a-scatola-nera.svg": tempo1(),
    "slide15b-torre.svg": wrap(tower(False),
        "La torre: il blocco transformer ripetuto N volte, dalle corsie dei token alla distribuzione"),
    "slide15c-torre-aperta.svg": wrap(tower(True),
        "Dentro il blocco: masked self-attention collega le corsie, il fully connected lavora su ognuna separatamente"),
}
for name, svg in files.items():
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)
    print(name, len(svg), "bytes")
