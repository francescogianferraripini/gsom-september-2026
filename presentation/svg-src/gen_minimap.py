# -*- coding: utf-8 -*-
"""Mini-mappa "sei qui": la torre della slide 15 ridotta a localizzatore."""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

W, H = 120, 172
BUR, BUR_F = "#a1245a", "#ecd3de"
BASE_F, BASE_S = "#f1f3f5", "#dee2e6"
LANE = "#e3e6ea"
DIM = "#adb5bd"

LANES = [26, 50, 74, 98]
CW = 16
ACT = 3

HEAD = (60, 2, 108, 22)
BN = (28, 38)
ELL_Y = 47
B2 = (52, 62)
B1 = (68, 128)
PLUS_FC_Y = 76
FC = (82, 94)
PLUS_ATT_Y = 102
ATT = (108, 120)
POS = (132, 139)
EMB = (142, 149)
TOK = (153, 165)

def r(x, y, w, h, on, rx=2, sw=1.0):
    f, s = (BUR_F, BUR) if on else (BASE_F, BASE_S)
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (x, y, w, h, rx, f, s, 1.5 if on else sw))

def plus(cx, cy, on):
    col = BUR if on else DIM
    return ('<circle cx="%s" cy="%s" r="3.2" fill="#ffffff" stroke="%s" stroke-width="%s"/>'
            '<path d="M %s %s h 3.2 M %s %s v 3.2" stroke="%s" stroke-width="1" '
            'stroke-linecap="round"/>'
            % (cx, cy, col, 1.5 if on else 1.0,
               cx - 1.6, cy, cx, cy - 1.6, col))

def build(target):
    o = ['<rect width="%s" height="%s" fill="#ffffff"/>' % (W, H)]
    # corsie
    for i, cx in enumerate(LANES):
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>'
                 % (cx, TOK[0], cx, BN[0], BUR if (target == "corsie" and i == ACT) else LANE,
                    1.6 if target == "corsie" else 1.2))
    # testa
    hx0, hy0, hx1, hy1 = HEAD
    on = target == "testa"
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>'
             % (LANES[ACT], BN[0], LANES[ACT], hy1, BUR if on else DIM))
    o.append(r(hx0, hy0, hx1 - hx0, hy1 - hy0, on, rx=3))
    for i, bw in enumerate((30, 21, 13)):
        o.append('<rect x="%s" y="%s" width="%s" height="3" rx="1" fill="%s"/>'
                 % (hx0 + 5, hy0 + 4 + i * 5, bw, BUR if on else DIM))
    # blocchi chiusi
    for (ya, yb) in (BN, B2):
        o.append(r(12, ya, 96, yb - ya, False, rx=3))
    o.append('<text x="60" y="%s" font-size="9" fill="%s" text-anchor="middle" '
             'font-family="system-ui, sans-serif">⋯</text>' % (ELL_Y, DIM))
    # blocco 1 aperto
    o.append('<rect x="8" y="%s" width="104" height="%s" rx="4" fill="none" stroke="%s" '
             'stroke-width="1" stroke-dasharray="3 2.5"/>' % (B1[0], B1[1] - B1[0], DIM))
    for cx in LANES:
        o.append(plus(cx, PLUS_FC_Y, target == "somma"))
        o.append(plus(cx, PLUS_ATT_Y, target == "somma"))
    on_fc = target == "fc"
    for cx in LANES:
        o.append(r(cx - CW / 2.0, FC[0], CW, FC[1] - FC[0], on_fc))
    on_at = target == "attn"
    o.append(r(14, ATT[0], 92, ATT[1] - ATT[0], on_at, rx=3))
    mid = (ATT[0] + ATT[1]) / 2.0
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>'
             % (LANES[0], mid, LANES[ACT], mid, BUR if on_at else DIM))
    for cx in LANES:
        o.append('<circle cx="%s" cy="%s" r="1.8" fill="%s"/>' % (cx, mid, BUR if on_at else DIM))
    # posizione / embedding / token
    on_pos = target == "pos"
    for cx in LANES:
        o.append(r(cx - CW / 2.0, POS[0], CW, POS[1] - POS[0], on_pos, rx=1.5))
        o.append(r(cx - CW / 2.0, EMB[0], CW, EMB[1] - EMB[0], False, rx=1.5))
        o.append(r(cx - CW / 2.0, TOK[0], CW, TOK[1] - TOK[0], False, rx=2))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" '
            'role="img" aria-label="Mini-mappa dell\'architettura: la parte trattata in questa '
            'slide e evidenziata">%s</svg>' % (W, H, W, H, "".join(o)))

for name in ("pos", "fc", "somma", "attn", "testa", "corsie"):
    fn = os.path.join(OUT, "minimap-%s.svg" % name)
    open(fn, "w").write(build(name))
    print(os.path.basename(fn))
