# -*- coding: utf-8 -*-
"""Lotto A: le tre slide che INSEGNANO l'alfabeto (10, 12, 14)."""
import sys, os
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
    W, H = 700, 420
    o = []
    # il vocabolario: riferimento, non flusso — collegato con un tratteggio
    vx0, vy0, vw, vh = 40, 16, 620, 80
    o.append(rect(vx0, vy0, vw, vh, SOFT, LINE, rx=6))
    for r in range(5):
        for c in range(20):
            hot = (r, c) in ((1, 4), (2, 11), (3, 17), (0, 8))
            o.append(rect(vx0 + 12 + c * 30, vy0 + 10 + r * 13, 25, 8,
                          BUR_F if hot else "#ffffff", BUR if hot else LINE, rx=1.5, sw=0.7))
    o.append(txt(vx0 + vw / 2.0, vy0 + vh + 20, "vocabolario fisso: ~100.000 token — le tessere sono prese da qui",
                 10, BODY, "middle", "600"))
    o.append(arrow(350, vy0 + vh + 30, 350, 168, GREYD, 1.1))

    def scene(y, toks, ids, text, tw, accent, label):
        s, n = [], len(toks)
        pitch, x0 = tw + 8, 40 + tw / 2.0
        s.append(txt(40, y - 12, label, 10.5, BUR if accent else GREYD, "start", "700", ls="0.1em"))
        for i, (t, d) in enumerate(zip(toks, ids)):
            s.append(tile(x0 + i * pitch, y, tw, 44, t, 15,
                          BUR if accent else LINE, BUR_F if accent else "#ffffff",
                          BUR if accent else BODY, 1.5 if accent else 1.2, sub=d))
        mid = x0 + (n - 1) * pitch / 2.0
        s.append(arrow(mid, y + 76, mid, y + 52))
        s.append(txt(mid, y + 92, text, 13, GREYD, "middle", "400", MONO))
        return "".join(s)

    o.append(scene(184, ["elettro", "encefal", "ogramma"], ["11621", "45093", "30818"],
                   "elettroencefalogramma", 182, True, "PAROLA RARA: SPEZZATA IN FRAMMENTI"))
    o.append(scene(312, ["Il", "gatto", "è", "sul", "tavolo"],
                   ["243", "28741", "1105", "3387", "9152"], "Il gatto è sul tavolo",
                   108, False, "PAROLE COMUNI: UN TOKEN CIASCUNA"))
    return svg(W, H, "".join(o),
               "Dal testo alle tessere-token: parole comuni un token ciascuna, parola rara spezzata in tre")

for fn, body in (("slide10-parola-vettore.svg", slide10()),
                 ("slide12-scala-del-calcolo.svg", slide12()),
                 ("slide14-tokenizzazione.svg", slide14())):
    open(os.path.join(OUT, fn), "w").write(body)
    print(fn)
