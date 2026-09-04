# -*- coding: utf-8 -*-
"""Lotto A: le tre slide che INSEGNANO l'alfabeto (10, 12, 14)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alfa import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

# ================= SLIDE 10 — a ogni parola il suo vettore =================
def slide10():
    W, H = 1060, 215
    o = []
    cols = [330, 610, 890]
    words = [("gatto",  ["0.8", "-1.3", "2.1", "0.4"]),
             ("cane",   ["0.7", "-1.1", "1.9", "0.5"]),
             ("Parigi", ["-2.4", "0.6", "-0.3", "1.8"])]
    for cx, (w, vals) in zip(cols, words):
        o.append(vec(cx, 28, 4, 56, TEAL, TEAL_F, values=vals, fs=17))
        o.append(arrow(cx, 118, cx, 92))
        o.append(tile(cx, 126, 230, 44, w, 20))
    o.append(txt(cols[0] - 115, 200, "quattro celle nel disegno, migliaia di numeri nella realtà — "
                 "e l'associazione è appresa durante l'addestramento, non scritta a mano",
                 12, GREYD))
    o.append(txt(cols[0] - 130, 56, "vettore", 12, TEAL_D, "end", "700"))
    o.append(txt(cols[0] - 130, 70, "l'embedding", 9.5, GREYD, "end"))
    o.append(txt(cols[0] - 130, 154, "parola", 12, GREYD, "end", "700"))
    return svg(W, H, "".join(o),
               "Tre parole e i loro vettori: la tessera-token in basso, il vettore di quattro celle sopra")

# ================= SLIDE 10b — che cos'e' un vettore =================
def slide10b():
    W, H = 700, 340
    CX = [118, 350, 582]
    o = [txt(350, 24, "una cella per dimensione — e la freccia vive in quello spazio",
             11.5, GREYD, "middle")]
    for cx, lab in zip(CX, ("NEL PIANO", "NELLO SPAZIO", "SULLA SFERA")):
        o.append(txt(cx, 56, lab, 11, BUR, "middle", "700", ls="0.16em"))
        o.append(rect(cx - 80, 72, 160, 160, "#fbfbfc", LINE, rx=6))

    # --- 1. nel piano: due numeri
    cx, U, OY = CX[0], 62, 152
    o.append(line(cx - 68, OY, cx + 68, OY, "#e9ecef", 1))
    o.append(line(cx, 84, cx, 220, "#e9ecef", 1))
    o.append(arrow(cx, OY, cx + 0.8 * U, OY - 0.6 * U, TEAL, 2.6, marker="at"))
    o.append(line(cx + 0.8 * U, OY - 0.6 * U, cx + 0.8 * U, OY, "#c3c8cd", 1, dash="3 3"))
    o.append(line(cx, OY - 0.6 * U, cx + 0.8 * U, OY - 0.6 * U, "#c3c8cd", 1, dash="3 3"))
    o.append(txt(cx + 0.4 * U, OY + 14, "0.8", 9.5, GREYD, "middle", "400", MONO))
    o.append(txt(cx - 12, OY - 0.3 * U, "0.6", 9.5, GREYD, "middle", "400", MONO))
    o.append(vec(cx, 268, 2, 26, TEAL, TEAL_F, values=["0.8", "0.6"], fs=10))
    o.append(txt(cx, 322, "due numeri: una direzione nel piano", 10, GREYD, "middle"))

    # --- 2. nello spazio: tre numeri
    cx = CX[1]
    ox, oy = cx - 34, 186
    XD, YD, ZD = (72, 0), (38, -42), (0, -74)          # i tre assi, in assonometria
    for d, nome in ((XD, "x"), (YD, "y"), (ZD, "z")):
        o.append(arrow(ox, oy, ox + d[0], oy + d[1], "#ced4da", 1.4))
        o.append(txt(ox + d[0] + 8, oy + d[1] + 4, nome, 9, GREYD, "middle"))
    px = ox + 0.8 * XD[0] + 0.6 * YD[0]
    py = oy + 0.8 * XD[1] + 0.6 * YD[1]
    qx, qy = px + 0.5 * ZD[0], py + 0.5 * ZD[1]
    o.append(line(ox, oy, px, py, "#c3c8cd", 1, dash="3 3"))
    o.append(line(px, py, qx, qy, "#c3c8cd", 1, dash="3 3"))
    o.append(arrow(ox, oy, qx, qy, TEAL, 2.6, marker="at"))
    o.append(vec(cx, 268, 3, 26, TEAL, TEAL_F, values=["0.8", "0.6", "0.5"], fs=10))
    o.append(txt(cx, 322, "tre numeri: una direzione nello spazio", 10, GREYD, "middle"))

    # --- 3. sulla sfera: lunghezza 1
    cx, R = CX[2], 62
    o.append('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.4"/>'
             % (cx, OY, R, "#ced4da"))
    o.append('<ellipse cx="%s" cy="%s" rx="%s" ry="19" fill="none" stroke="#e3e6ea" '
             'stroke-width="1.2"/>' % (cx, OY, R))
    o.append('<ellipse cx="%s" cy="%s" rx="19" ry="%s" fill="none" stroke="#e3e6ea" '
             'stroke-width="1.2"/>' % (cx, OY, R))
    for ang, hot in ((53, True), (128, False), (205, False), (315, False)):
        a = math.radians(ang)
        ex, ey = cx + R * math.cos(a), OY - R * math.sin(a)
        o.append(arrow(cx, OY, ex, ey, TEAL if hot else "#a8ded2", 2.6 if hot else 1.8,
                       marker="at"))
        o.append('<circle cx="%s" cy="%s" r="3.4" fill="%s"/>' % (ex, ey, TEAL_D if hot else "#a8ded2"))
    o.append(txt(cx, 246, "ogni punta cade sulla superficie", 9, GREYD, "middle"))
    o.append(vec(cx, 268, 3, 26, TEAL, TEAL_F, values=["0.6", "0", "0.8"], fs=10))
    o.append(txt(cx, 322, "lunghezza 1: resta solo la direzione", 10, GREYD, "middle"))

    return svg(W, H, "".join(o),
               "Tre pannelli: un vettore nel piano con due numeri, nello spazio con tre, e i vettori di lunghezza 1 che cadono sulla superficie di una sfera")

# ================= SLIDE 11 — vettori e prodotto scalare =================
B_F, B_S = "#a8ded2", TEAL_D           # il secondo vettore: stesso teal, tono piu' fondo

def _colvec(cx, y_top, vals, cell, stroke, fill):
    o = []
    for i, v in enumerate(vals):
        o.append(rect(cx - cell / 2.0, y_top + i * cell, cell, cell, fill, stroke,
                      rx=cell * 0.13, sw=1.3))
        o.append(txt(cx, y_top + i * cell + cell * 0.68, v, cell * 0.44, BODY, "middle", "500", MONO))
    return "".join(o)

def slide11():
    W, H = 700, 364
    CX = [118, 350, 582]
    U, OY = 62, 152
    CASI = [("AFFINI", (0.8, 0), (1, 0), ["0.8", "0"], ["1", "0"], "0.8",
             "stessa direzione: si sovrappongono del tutto"),
            ("ESTRANEI", (1, 0), (0, 1), ["1", "0"], ["0", "1"], "0",
             "perpendicolari: non hanno nulla in comune"),
            ("OPPOSTI", (0.1, -1), (0, 1), ["0.1", "\u22121"], ["0", "1"], "\u22121",
             "versi opposti: si annullano a vicenda")]
    o = ['<defs><marker id="ad" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
         'markerHeight="5" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" '
         'fill="%s"/></marker></defs>' % B_S,
         txt(350, 24, "sopra la direzione, sotto gli stessi numeri: sono lo stesso oggetto",
             11.5, GREYD, "middle")]

    for cx, (lab, a, b, av, bv, res, note) in zip(CX, CASI):
        o.append(txt(cx, 56, lab, 11, BUR, "middle", "700", ls="0.16em"))
        o.append(rect(cx - 80, 72, 160, 160, "#fbfbfc", LINE, rx=6))
        o.append(line(cx - 68, OY, cx + 68, OY, "#e9ecef", 1))
        o.append(line(cx, 84, cx, 220, "#e9ecef", 1))
        off = 5 if (a[1] == 0 and b[1] == 0) else 0
        o.append(arrow(cx, OY - off, cx + a[0] * U, OY - a[1] * U - off, TEAL, 2.6, marker="at"))
        o.append(arrow(cx, OY + off, cx + b[0] * U, OY - b[1] * U + off, B_S, 2.6, marker="ad"))
        o.append(txt(cx + a[0] * U + 10, OY - a[1] * U - off + (18 if a[1] <= 0 else -8),
                     "a", 13, TEAL_D, "middle", "700"))
        o.append(txt(cx + b[0] * U + 12, OY - b[1] * U + off - 10, "b", 13, B_S, "middle", "700"))
        o.append(vec(cx - 64, 276, 2, 22, TEAL, TEAL_F, values=av, fs=11))
        o.append(txt(cx - 30, 294, "\u00b7", 18, GREYD, "middle", "600"))
        o.append(_colvec(cx - 12, 265, bv, 22, B_S, B_F))
        o.append(txt(cx + 12, 294, "=", 15, GREYD, "middle"))
        o.append(rect(cx + 26, 272, 60, 30, "#ffffff", BUR, rx=4, sw=1.4))
        o.append(txt(cx + 56, 293, res, 14, BUR, "middle", "700", MONO))
        o.append(txt(cx, 328, note, 10, GREYD, "middle"))
    o.append(txt(350, 354, "il prodotto scalare: una riga per una colonna, e ne esce un numero solo",
                 11.5, BODY, "middle", "600"))
    return svg(W, H, "".join(o),
               "Tre casi del prodotto scalare: affini, estranei, opposti; in ognuno le due frecce e gli stessi due vettori come riga e colonna")

# ================= SLIDE 11b — la somma fra vettori =================
def slide11b():
    W, H = 700, 364
    CX = [118, 350, 582]
    U, OY, OXD = 42, 152, -30          # unita', quota dell'origine, scarto dell'origine
    CASI = [("CONCORDI", (1, 0), (0.8, 0), ["1", "0"], ["0.8", "0"], ["1.8", "0"],
             "stessa direzione: lo spostamento si allunga"),
            ("DIVERSI", (1, 0), (0, 1), ["1", "0"], ["0", "1"], ["1", "1"],
             "direzioni diverse: ci si sposta di lato"),
            ("OPPOSTI", (1, 0), (-0.8, 0), ["1", "0"], ["\u22120.8", "0"], ["0.2", "0"],
             "versi opposti: lo spostamento quasi si annulla")]
    o = ['<defs><marker id="ad" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
         'markerHeight="5" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" '
         'fill="%s"/></marker></defs>' % B_S,
         txt(350, 24, "sopra lo spostamento, sotto gli stessi numeri: sono lo stesso oggetto",
             11.5, GREYD, "middle")]

    for cx, (lab, a, b, av, bv, sv, note) in zip(CX, CASI):
        ox = cx + OXD
        indietro = (a[1] == 0 and b[1] == 0 and a[0] * b[0] < 0)   # b torna sui suoi passi
        boff = -11 if indietro else 0
        soff = 12 if (a[1] + b[1]) == 0 else 0                     # somma orizzontale: sfalsata
        o.append(txt(cx, 56, lab, 11, BUR, "middle", "700", ls="0.16em"))
        o.append(rect(cx - 80, 72, 160, 160, "#fbfbfc", LINE, rx=6))
        o.append(line(cx - 72, OY, cx + 72, OY, "#e9ecef", 1))
        o.append(line(ox, 84, ox, 220, "#e9ecef", 1))
        ax, ay = ox + a[0] * U, OY - a[1] * U
        bx, by = ax + b[0] * U, ay - b[1] * U
        o.append(arrow(ox, OY, ax, ay, TEAL, 2.4, marker="at"))
        o.append(arrow(ax, ay + boff, bx, by + boff, B_S, 2.4, marker="ad"))
        o.append(arrow(ox, OY + soff, bx, by + soff, BUR, 2.8, marker="ab"))
        o.append(txt((ox + ax) / 2.0, OY - 9, "a", 12, TEAL_D, "middle", "700"))
        if b[1]:
            o.append(txt(bx + 13, (ay + by) / 2.0 + 4, "b", 12, B_S, "middle", "700"))
        else:
            o.append(txt((ax + bx) / 2.0, ay + boff - 9, "b", 12, B_S, "middle", "700"))
        o.append(txt(ox + 4, OY + 34, "a + b", 11, BUR, "start", "700"))
        o.append(vec(cx - 58, 274, 2, 26, TEAL, TEAL_F, values=av, fs=9.5))
        o.append(txt(cx - 22, 293, "+", 15, GREYD, "middle", "600"))
        o.append(vec(cx + 14, 274, 2, 26, B_S, B_F, values=bv, fs=9.5))
        o.append(txt(cx + 50, 293, "=", 15, GREYD, "middle"))
        o.append(vec(cx + 86, 274, 2, 26, BUR, TEAL_F, values=sv, fs=9.5))
        o.append(txt(cx, 330, note, 10, GREYD, "middle"))
    o.append(txt(350, 354, "due righe, e ne esce un'altra riga: un punto nuovo nello spazio",
                 11.5, BODY, "middle", "600"))
    return svg(W, H, "".join(o),
               "Tre casi della somma fra vettori: concordi, diversi, opposti; in ognuno le frecce in fila e gli stessi vettori come righe di celle")

# ================= SLIDE 12 — la scala del calcolo =================
# Unica slide della sezione che si legge DALL'ALTO IN BASSO: e' una lista
# numerata di tre passi, non un flusso di dati.
def slide12():
    W, H = 1060, 482
    C, TXT = 22, 560
    o = []

    # ---- LIVELLO 1 (in alto): riga . colonna = numero
    o.append(eyebrow(0, 22, "LIVELLO 1"))
    o.append(txt(82, 22, "vettore · vettore = numero", 12.5, BODY, "start", "600", MONO))
    o.append(vec(112, 69, 4, C, TEAL, TEAL_F))
    o.append(txt(178, 86, "·", 20, GREYD, "middle", "600"))
    o.append(vvec(218, 32, 4, C, TEAL, TEAL_F))
    o.append(txt(262, 86, "=", 17, GREYD, "middle"))
    o.append(rect(294, 69, 78, C, "#ffffff", BUR, rx=4, sw=1.4))
    o.append(txt(333, 85, "0,83", 14, BUR, "middle", "700", MONO))
    o.append(txt(112, 136, "una riga", 10, GREYD, "middle"))
    o.append(txt(218, 136, "per una colonna", 10, GREYD, "middle"))
    o.append(txt(TXT, 78, "Una riga per una colonna: in uscita un solo numero,",
                 12, BODY, "start", "600"))
    o.append(txt(TXT, 92, "quanto i due vettori sono allineati.", 11.5, GREYD))

    # ---- LIVELLO 2 (al centro): il gradino focale
    o.append(eyebrow(0, 168, "LIVELLO 2"))
    o.append(txt(82, 168, "vettore × matrice = vettore", 12.5, BUR, "start", "600", MONO))
    my0 = 184
    ymid = my0 + 2 * C - C / 2.0
    o.append(vec(112, ymid, 4, C, TEAL, TEAL_F))
    o.append(txt(178, ymid + 16, "×", 17, GREYD, "middle"))
    o.append(matrix(206, my0, 4, 3, C, GREYD, SOFT))
    o.append(txt(298, ymid + 16, "=", 17, GREYD, "middle"))
    o.append(vec(362, ymid, 3, C, TEAL, TEAL_F))
    ybot = my0 + 4 * C
    for j in range(3):
        xin = 206 + j * C + C / 2.0
        xout = 362 - (3 * C) / 2.0 + j * C + C / 2.0
        o.append(curve(xout, ymid + C, xout, ymid + C + 22, xin, ybot + 22, xin, ybot + 5,
                       BUR, 1.0, marker="ab", op=0.75))
    o.append(txt(206, ybot + 34, "ogni colonna della matrice è una colonna come quella del livello 1:",
                 11, GREYD))
    o.append(txt(206, ybot + 46, "lo stesso prodotto scalare, fatto 3 volte in un colpo solo", 11, GREYD))
    o.append(txt(TXT, ymid - 6, "Moltiplicare per una matrice significa interrogare",
                 12, BODY, "start", "600"))
    o.append(txt(TXT, ymid + 8, "una batteria di rilevatori, tutti insieme.", 12, BODY, "start", "600"))
    o.append(txt(TXT, ymid + 28, "Ogni cella in uscita è l'allineamento con un rilevatore:", 11.5, BUR))
    o.append(txt(TXT, ymid + 42, "è la stessa forma delle matrici Q, K e V dell'attention.", 11.5, GREYD))

    # ---- LIVELLO 3 (in basso)
    o.append(eyebrow(0, 348, "LIVELLO 3"))
    o.append(txt(82, 348, "matrice × matrice = matrice", 12.5, BODY, "start", "600", MONO))
    ty0 = 364
    tin = ty0 + (4 * C - 3 * C) / 2.0
    for i in range(3):
        o.append(vec(112, tin + i * C, 4, C, TEAL, TEAL_F))
    o.append(txt(178, ty0 + 2 * C - 4, "×", 17, GREYD, "middle"))
    o.append(matrix(206, ty0, 4, 3, C, GREYD, SOFT))
    o.append(txt(298, ty0 + 2 * C - 4, "=", 17, GREYD, "middle"))
    for i in range(3):
        o.append(vec(362, tin + i * C, 3, C, TEAL, TEAL_F))
    o.append(txt(60, ty0 + 4 * C + 20, "molti vettori insieme — per esempio tutti i token della frase",
                 11, GREYD))
    o.append(txt(TXT, ty0 + 2 * C - 10, "La stessa batteria, interrogata da ogni vettore.",
                 12, BODY, "start", "600"))
    o.append(txt(TXT, ty0 + 2 * C + 4, "È quello che succede a ogni strato, per ogni token.", 11.5, GREYD))

    o.append(line(0, 150, W, 150, "#eef0f2", 1))
    o.append(line(0, 332, W, 332, "#eef0f2", 1))
    return svg(W, H, "".join(o),
               "Tre gradini dall'alto: riga per colonna, vettore per matrice, matrice per matrice")

# ================= SLIDE 14 — la tokenizzazione =================
def slide14():
    G, DY = 84, 46                          # gutter dell'etichetta; di quanto scende la parte bassa
    W, H = 700 + G, 322 + DY
    RAW = "Il gatto ha un elettroencefalogramma"
    X0, CW = 30, 640 / 36.0                 # 36 caratteri, allineati al pixel
    TOKENS = [(0, 2, "243", False), (3, 5, "28741", False), (9, 2, "1274", False),
              (12, 2, "553", False), (15, 7, "11621", True), (22, 7, "45093", True),
              (29, 7, "30818", True)]
    VY, VC = 44, 18                         # riga dei vettori
    TY0, TY1 = 104, 156                     # riga delle tessere
    LK0, LKH = 178, 30                      # riga di lookup: un troncone del vocabolario
    LK1, LKM = LK0 + LKH, LK0 + LKH / 2.0
    RY = 184 + DY                           # il testo grezzo, spinto in basso per far posto
    PITCH = 640 / 7.0
    FS_C, FS_I = 11, 10                     # dentro la cella: la voce, e sotto il suo id
    o = []

    o.append(txt(X0, 30, "ogni tessera diventa un vettore, sempre di 4 celle", 11, TEAL_D,
                 "start", "600"))

    # --- le celle del lookup: larghe quanto il loro contenuto, tenute il piu' possibile
    #     sotto il token che le pesca, con un gioco minimo fra l'una e l'altra
    GAP, LB, RB = 22, X0 + 22, X0 + 610
    cells = []
    for start, ln, tid, rara in TOKENS:
        cells.append({"w": round(max(ln * FS_C, len(tid) * FS_I) * 0.6 + 16, 1),
                      "cxt": X0 + (start + ln / 2.0) * CW, "id": tid, "rara": rara,
                      "s": RAW[start:start + ln]})
    prev = LB - GAP
    for c in cells:                                     # da sinistra: rispetta il gioco minimo
        c["x"] = max(c["cxt"] - c["w"] / 2.0, prev + GAP)
        prev = c["x"] + c["w"]
    lim = RB
    for c in reversed(cells):                           # da destra: non sfondare il bordo
        c["x"] = min(c["x"], lim - c["w"])
        lim = c["x"] - GAP
    for c in cells:
        c["x"] = round(c["x"], 1)
        c["cx"] = round(c["x"] + c["w"] / 2.0, 1)

    # --- la fascia: un troncone di tabella, tagliato di netto ai due estremi
    o.append(rect(X0, LK0, 640, LKH, SOFT, "none"))
    o.append(line(X0, LK0, X0 + 640, LK0, LINE, 1))
    o.append(line(X0, LK1, X0 + 640, LK1, LINE, 1))
    bordi = [X0] + [v for c in cells for v in (c["x"], c["x"] + c["w"])] + [X0 + 640]
    for a, b in zip(bordi[0::2], bordi[1::2]):           # nei vuoti: le voci che non vediamo
        for k in (-5, 0, 5):
            o.append('<circle cx="%.1f" cy="%s" r="1.15" fill="%s"/>'
                     % ((a + b) / 2.0 + k, LKM, ARROW))
    for c in cells:
        o.append(rect(c["x"], LK0 + 1, c["w"], LKH - 2, BUR_F if c["rara"] else "#ffffff",
                      BUR if c["rara"] else OFF_T, rx=3, sw=1.1))
        o.append(txt(c["cx"], LK0 + 12, c["s"], FS_C, BUR if c["rara"] else BODY,
                     "middle", "500", MONO))
        o.append(txt(c["cx"], LK0 + 25, c["id"], FS_I, BUR if c["rara"] else GREYD,
                     "middle", "400", MONO))

    for i, ((start, ln, tid, rara), c) in enumerate(zip(TOKENS, cells)):
        x = X0 + start * CW
        w = ln * CW
        cxt = x + w / 2.0                                  # centro della tessera
        cxv = X0 + PITCH / 2.0 + i * PITCH                 # centro del vettore
        st, mk = (BUR, "ab") if rara else ("#c3c8cd", "a")
        o.append(vec(cxv, VY, 4, VC, TEAL, TEAL_F))
        o.append(curve(cxt, TY0 - 4, cxt, TY0 - 22, cxv, VY + VC + 20, cxv, VY + VC + 4,
                       "#c3c8cd", 1.2))
        o.append(rect(x + 1, TY0, w - 2, TY1 - TY0, BUR_F if rara else "#ffffff",
                      BUR if rara else LINE, rx=5, sw=1.6 if rara else 1.2))
        o.append(txt(cxt, TY0 + 30, RAW[start:start + ln], 22,
                     BUR if rara else BODY, "middle", "500", MONO))
        o.append(txt(cxt, TY0 + 46, tid, 9.5, BUR if rara else GREYD, "middle", "400", MONO))
        # dalla voce del vocabolario alla tessera che porta quell'id
        o.append(curve(c["cx"], LK0 - 1, c["cx"], LK0 - 9, cxt, TY1 + 11, cxt, TY1 + 3,
                       st, 1.2, marker=mk))
        # dalla porzione di testo grezzo alla sua voce nel vocabolario
        o.append(curve(cxt, RY - 2, cxt, RY - 10, c["cx"], LK1 + 10, c["cx"], LK1 + 2,
                       st, 1.2, marker=mk))

    o.append('<text x="%s" y="%s" textLength="640" lengthAdjust="spacingAndGlyphs" '
             'font-family="%s" font-size="27" fill="%s">%s</text>'
             % (X0, RY + 22, MONO, BODY, RAW))
    for cut in (22, 29):
        o.append(line(X0 + cut * CW, RY, X0 + cut * CW, RY + 28, BUR, 1.8))

    # --- la nota, in fondo: il glifo e il testo insieme
    NY = 226 + DY
    o.append(rect(20, NY, 660, 82, BLACK, "none", rx=8))
    o.append(txt(44, NY + 36, "11621", 19, YEL, "start", "700", MONO))
    o.append(txt(118, NY + 35, "e non", 11, "#c9ccd1", "start"))
    o.append(txt(158, NY + 36, "e l e t t r o", 15, "#8a8f96", "start", "400", MONO))
    o.append(line(156, NY + 31, 272, NY + 31, "#8a8f96", 1.4))
    o.append(txt(44, NY + 62, "dentro la tessera le lettere spariscono", 10, "#8a8f96", "start"))
    o.append(txt(316, NY + 24, "È per questo che a un modello riesce difficile contare le",
                 11.5, "#ffffff", "start"))
    o.append(txt(316, NY + 41, "lettere di una parola: le lettere, lui, non le ha mai viste.",
                 11.5, "#ffffff", "start"))
    o.append(txt(316, NY + 64, "D'ora in poi diremo: token.", 11.5, YEL, "start", "700"))

    # --- l'etichetta della fascia, nel gutter: fuori dalla traslazione del disegno
    gut = (txt(G + X0 - 14, LK0 + 12, "encoding", 12, BODY, "end", "700") +
           txt(G + X0 - 14, LK0 + 26, "~100.000 voci", 10, GREYD, "end"))
    return svg(W, H, gut + '<g transform="translate(%s 0)">%s</g>' % (G, "".join(o)),
               "Dal basso: la frase grezza, la riga di encoding del vocabolario che trasforma "
               "ogni porzione di testo nel suo id, le tessere-token e infine i vettori di quattro "
               "celle; la parola rara pesca tre voci diverse del vocabolario")

for fn, body in (("slide10-parola-vettore.svg", slide10()),
                 ("slide10b-che-cos-e-un-vettore.svg", slide10b()),
                 ("slide11-vettori-prodotto-scalare.svg", slide11()),
                 ("slide11b-somma-vettori.svg", slide11b()),
                 ("slide12-scala-del-calcolo.svg", slide12()),
                 ("slide14-tokenizzazione.svg", slide14())):
    open(os.path.join(OUT, fn), "w").write(body)
    print(fn)
