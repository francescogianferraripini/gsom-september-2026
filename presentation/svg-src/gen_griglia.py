# -*- coding: utf-8 -*-
"""Griglia-calcolo dell'attention, dal basso verso l'alto.
Slide 18-19-20: i tre stadi sulla frase del portiere.
Slide 20b: la stessa griglia su due frasi, in due fotogrammi."""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")

W, H = 700, 440

TEAL, TEAL_F, TEAL_D = "#1ab197", "#d1efea", "#0e7c6a"
BUR,  BUR_F, BUR_M   = "#a1245a", "#ecd3de", "#d9a3bb"
GRA,  GRA_F          = "#161719", "#e6e6e8"
BLU,  BLU_F, BLU_D   = "#4da0d7", "#dbeaf6", "#2b6f9c"
LINE, GREYD, BODY    = "#dee2e6", "#838383", "#212529"
OFF_F, OFF_S, OFF_T  = "#fbfbfc", "#ececef", "#c8ccd0"
FEED, ARROW          = "#d3d7db", "#b0b6bc"
BLACK_BG             = "#161719"

FONT = "Poppins, system-ui, -apple-system, 'Segoe UI', sans-serif"
MONO = "'SFMono-Regular', Menlo, Monaco, Consolas, monospace"

GUT, FEED_X = 106, 116
COLS = [170, 287, 404, 521, 637]
ACT = 4

R_TOK = (406, 430)
R_EMB = (380, 396)
W_Q_Y = 366
R_Q   = (336, 352)
W_K_Y = 322
R_K   = (292, 308)
R_QK  = (258, 280)
R_SM  = (224, 246)
W_V_Y = 210
R_V   = (178, 194)
R_VW  = (144, 166)
R_SUM = (112, 130)

SENT1 = {"tokens": ["Il", "portiere", "diede", "un", "calcio"],
         "qk": ["0.1", "3.1", "1.4", "0.2", "1.9"],
         "pct": [3, 63, 12, 3, 19],
         "cloud": ("SPORT", ["pallone", "rigore", "partita"])}
SENT2 = {"tokens": ["ossa", "forti", "con", "il", "calcio"],
         "qk": ["2.9", "2.2", "0.2", "0.1", "1.7"],
         "pct": [52, 26, 3, 3, 16],
         "cloud": ("MINERALI · SALUTE", ["ferro", "vitamina D", "latte"])}

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def txt(x, y, s, size=10, fill=BODY, anchor="start", weight="400", font=None, ls=None):
    a = ['x="%s" y="%s"' % (x, y), 'font-family="%s"' % (font or FONT), 'font-size="%s"' % size,
         'fill="%s"' % fill, 'text-anchor="%s"' % anchor, 'font-weight="%s"' % weight]
    if ls is not None: a.append('letter-spacing="%s"' % ls)
    return '<text %s>%s</text>' % (" ".join(a), esc(s))

def rect(x, y, w, h, fill="none", stroke="none", rx=0, sw=1.0, op=None):
    a = ['x="%s" y="%s" width="%s" height="%s" rx="%s"' % (x, y, w, h, rx),
         'fill="%s"' % fill, 'stroke="%s"' % stroke, 'stroke-width="%s"' % sw]
    if op is not None: a.append('opacity="%s"' % op)
    return '<rect %s/>' % " ".join(a)

def line(x1, y1, x2, y2, stroke=FEED, sw=1.0):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>'
            % (x1, y1, x2, y2, stroke, sw))

def cells(cx, y, n, h, stroke, fill, on, op=None):
    if not on: stroke, fill = OFF_S, OFF_F
    x0 = cx - (n * h) / 2.0
    return "".join(rect(x0 + i * h, y, h, h, fill, stroke, rx=2.5, sw=1.3, op=op) for i in range(n))

def rowlabel(y, label, sub, col, on, cur):
    o = []
    if cur:
        o.append(rect(0, y - 11, 3, 22, fill=BUR, rx=1.5))
    o.append(txt(GUT - 8, y, label, 10.5, (col if on else OFF_T), "end", "700" if cur else "600"))
    if sub:
        o.append(txt(GUT - 8, y + 11, sub, 8, (GREYD if on else OFF_T), "end"))
    return "".join(o)

def wmatrix(ycent, stroke, fill, sup, cols_out, y_out, on=True):
    """4 celle in ingresso, 3 in uscita: la moltiplicazione della slide 12."""
    if not on:
        stroke, fill = OFF_S, OFF_F
    o, c, x0 = [], 4.5, 110
    y0 = ycent - 9
    for r in range(4):
        for cc in range(3):
            o.append(rect(x0 + cc * c, y0 + r * c, c, c, fill, stroke, rx=0.6, sw=0.5))
    o.append(rect(x0 - 2, y0 - 2, 3 * c + 4, 4 * c + 4, "none", stroke, rx=1.5, sw=1.1))
    o.append('<text x="132" y="%s" font-family="%s" font-size="9.5" fill="%s" '
             'text-anchor="start" font-weight="700">&#215; W'
             '<tspan font-size="6.5" dy="-4">%s</tspan></text>' % (ycent + 3, FONT, stroke, sup))
    o.append('<path d="M %s %s V %s" stroke="#c3c8cd" stroke-width="1.2" marker-end="url(#a3)"/>'
             % (FEED_X, ycent + 15, ycent + 10))
    o.append(line(162, ycent, cols_out[-1], ycent, OFF_S if not on else FEED, 1.0))
    for cx in cols_out:
        o.append('<path d="M %s %s V %s" stroke="%s" stroke-width="1.1" marker-end="url(#a)"/>'
                 % (cx, ycent - 3, y_out + 3, OFF_S if not on else ARROW))
    return "".join(o)

CALLOUT = {
 18: ("Il match si fa su q · k.",
      "Ma ciò su cui fai match non è ciò che ricevi: manca ancora una riga."),
 19: ("Le stesse affinità, ora come budget.",
      "I divari si allargano: 3.1 contro 1.9 diventa 63% contro 19%."),
 20: ("Il contesto ha consegnato.",
      "L'embedding di «calcio» non è più quello del vocabolario: è quello di questa frase."),
}

def band_callout(stage):
    a, b = CALLOUT[stage]
    return (rect(58, 20, 584, 56, BLACK_BG, "none", rx=8)
            + txt(78, 42, a, 12, "#ffffff", "start", "600")
            + txt(78, 60, b, 10.5, "#c9ccd1"))

def band_cloud(sent):
    title, words = sent["cloud"]
    o = [txt(0, 12, "DOVE FINISCE «CALCIO»", 8.5, GREYD, "start", "700", ls="0.13em")]
    px, py = 150, 55
    o.append('<circle cx="%s" cy="%s" r="5.5" fill="%s"/>' % (px, py, BUR))
    o.append(txt(px, py + 22, "calcio", 11, BUR, "middle", "600", MONO))
    o.append(txt(px, py + 34, "(dal vocabolario)", 8.5, GREYD, "middle"))
    o.append('<path d="M %s %s H %s" stroke="%s" stroke-width="2" marker-end="url(#a2)"/>'
             % (px + 13, py, 312, BUR))
    o.append('<ellipse cx="490" cy="%s" rx="166" ry="26" fill="#f6f6f6"/>' % py)
    o.append(txt(490, py - 8, title, 8.5, BUR, "middle", "700", ls="0.1em"))
    for j, w in enumerate(words):
        wx = 380 + j * 110
        o.append('<circle cx="%s" cy="%s" r="2.4" fill="%s"/>' % (wx, py + 4, BODY))
        o.append(txt(wx, py + 19, w, 9.5, BODY, "middle"))
    return "".join(o)

def build(stage, sent, band):
    on_sm, on_v = stage >= 19, stage >= 20
    tokens, QK, PCT = sent["tokens"], sent["qk"], sent["pct"]
    imax = PCT.index(max(PCT))
    o = ['<rect width="%s" height="%s" fill="#ffffff"/>' % (W, H),
         '<defs>'
         '<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
         'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>'
         '<marker id="a2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
         'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>'
         '<marker id="a3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.5" '
         'markerHeight="4.5" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" '
         'fill="#c3c8cd"/></marker>'
         '</defs>' % (ARROW, BUR)]

    o.append(line(146, 388, FEED_X, 388, "#c3c8cd", 1.2))
    o.append(line(FEED_X, 388, FEED_X, (W_V_Y if on_v else W_K_Y), "#c3c8cd", 1.2))
    o.append('<circle cx="146" cy="388" r="2" fill="#c3c8cd"/>')

    for i, cx in enumerate(COLS):
        act = (i == ACT)
        o.append(rect(cx - 50, R_TOK[0], 100, R_TOK[1] - R_TOK[0], "#ffffff",
                      BUR if act else LINE, rx=4, sw=1.6 if act else 1.2))
        o.append(txt(cx, R_TOK[0] + 17, tokens[i], 12.5, BUR if act else BODY, "middle", "500", MONO))
    o.append(rowlabel(R_TOK[0] + 14, "token", "la frase", GREYD, True, False))

    for i, cx in enumerate(COLS):
        o.append(cells(cx, R_EMB[0], 4, 16, TEAL, TEAL_F, True))
        if i == ACT:
            o.append(cells(cx, R_Q[0], 3, 16, BUR, BUR_F, True))
        else:
            o.append(txt(cx, R_Q[0] + 12, "—", 11, OFF_T, "middle"))
        o.append(cells(cx, R_K[0], 3, 16, GRA, GRA_F, True))
    o.append(wmatrix(W_Q_Y, BUR, BUR_F, "Q", [COLS[ACT]], R_Q[1]))
    o.append(wmatrix(W_K_Y, GRA, GRA_F, "K", COLS, R_K[1]))
    o.append(rowlabel(R_EMB[0] + 11, "embedding", "4 celle, come nella torre", TEAL_D, True, False))
    o.append(rowlabel(R_Q[0] + 11, "q — la domanda", "solo il token che cerca", BUR, True, stage == 18))
    o.append(rowlabel(R_K[0] + 11, "k — la chiave", "una per ogni token", GRA, True, stage == 18))

    for i, cx in enumerate(COLS):
        top = (i == imax)
        o.append(rect(cx - 34, R_QK[0], 68, R_QK[1] - R_QK[0], BUR_F if top else "#f6f6f6",
                      BUR if top else LINE, rx=4, sw=1.4 if top else 1.0))
        o.append(txt(cx, R_QK[0] + 15, QK[i], 12.5, BUR if top else BODY, "middle",
                     "700" if top else "500", MONO))
    o.append(rowlabel(R_QK[0] + 15, "q · k", "affinità grezza", BODY, True, stage == 18))

    for i, cx in enumerate(COLS):
        top = (i == imax)
        o.append(rect(cx - 34, R_SM[0], 68, R_SM[1] - R_SM[0], "#ffffff" if on_sm else OFF_F,
                      (BUR if top else LINE) if on_sm else OFF_S, rx=4,
                      sw=1.4 if (on_sm and top) else 1.0))
        if on_sm:
            o.append(rect(cx - 30, R_SM[1] - 7, 60 * PCT[i] / 100.0, 4, BUR if top else BUR_M,
                          "none", rx=2))
            o.append(txt(cx, R_SM[0] + 13, "%d%%" % PCT[i], 12, BUR if top else BODY, "middle",
                         "700" if top else "500", MONO))
    o.append(rowlabel(R_SM[0] + 15, "softmax", "il budget: somma a 100", BUR, on_sm, stage == 19))

    mx = float(max(PCT))
    for i, cx in enumerate(COLS):
        o.append(cells(cx, R_V[0], 3, 16, BLU, BLU_F, on_v))
        o.append(cells(cx, R_VW[0] + 3, 3, 16, BLU, BLU_F, on_v,
                       op=(0.16 + 0.84 * (PCT[i] / mx)) if on_v else None))
    o.append(wmatrix(W_V_Y, BLU, BLU_F, "V", COLS, R_V[1], on=on_v))
    o.append(rowlabel(R_V[0] + 11, "v — il contenuto", "ciò che il token consegna", BLU_D, on_v, stage == 20))
    o.append(rowlabel(R_VW[0] + 14, "v × peso", "consegna proporzionata", BLU_D, on_v, stage == 20))

    if on_v:
        for cx in COLS:
            o.append('<path d="M %s %s C %s %s %s %s %s %s" fill="none" stroke="%s" '
                     'stroke-width="1.1" opacity="0.55" marker-end="url(#a)"/>'
                     % (cx, R_VW[0] - 2, cx, R_VW[0] - 12, COLS[ACT], R_SUM[1] + 12,
                        COLS[ACT], R_SUM[1] + 4, ARROW))
        o.append(cells(COLS[ACT], R_SUM[0], 4, 18, BUR, TEAL_F, True))
        o.append(txt(COLS[ACT] - 62, R_SUM[0] + 8, "il nuovo embedding di «calcio»", 10, BODY, "end", "600"))
        o.append(txt(COLS[ACT] - 62, R_SUM[0] + 21, "spostato dove il contesto lo porta", 8.5, GREYD, "end"))
    else:
        o.append(cells(COLS[ACT], R_SUM[0], 4, 18, OFF_S, OFF_F, False))
    o.append(rowlabel(R_SUM[0] + 12, "somma", "l'uscita dell'attention", TEAL_D, on_v, stage == 20))
    o.append(band)
    return "".join(o)

def svg(body, alt):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" '
            'role="img" aria-label="%s">%s</svg>' % (W, H, W, H, esc(alt), body))

FILES = [
 ("slide18-griglia-qk.svg", build(18, SENT1, band_callout(18)),
  "Griglia dell'attention dal basso: dall'embedding, tramite W Q e W K, si calcolano domanda e chiavi; il prodotto scalare da l'affinita"),
 ("slide19-griglia-softmax.svg", build(19, SENT1, band_callout(19)),
  "Griglia dell'attention dal basso: la softmax trasforma le affinita grezze nel budget di ascolto"),
 ("slide20-griglia-v.svg", build(20, SENT1, band_callout(20)),
  "Griglia dell'attention dal basso: W V produce i value, che pesati si sommano nel nuovo embedding di calcio"),
 ("slide20b-contesto-frase1.svg", build(20, SENT1, band_cloud(SENT1)),
  "Attention completa sulla frase il portiere diede un calcio: il budget va a portiere e calcio finisce nell'area dello sport"),
 ("slide20b-contesto-frase2.svg", build(20, SENT2, band_cloud(SENT2)),
  "Attention completa sulla frase ossa forti con il calcio: il budget va a ossa e forti e calcio finisce nell'area dei minerali"),
]
for fn, body, alt in FILES:
    open(os.path.join(OUT, fn), "w").write(svg(body, alt))
    print(fn)
