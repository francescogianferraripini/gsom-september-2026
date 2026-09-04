# -*- coding: utf-8 -*-
"""Alfabeto visivo della Sezione 3. Primitive condivise da tutti i generatori.
Regole: il vettore e' una riga di 4 celle; q/k/v 3 celle; la matrice di proiezione
e' una griglia 4x3; il flusso va SEMPRE dal basso verso l'alto."""

TEAL, TEAL_F, TEAL_D = "#1ab197", "#d1efea", "#0e7c6a"
BUR,  BUR_F, BUR_M   = "#a1245a", "#ecd3de", "#d9a3bb"
YEL,  YEL_F, YEL_D   = "#e0a500", "#fff2ce", "#8a6500"
GRA,  GRA_F          = "#161719", "#e6e6e8"
BLU,  BLU_F, BLU_D   = "#4da0d7", "#dbeaf6", "#2b6f9c"
LINE, GREYD, BODY    = "#dee2e6", "#838383", "#212529"
OFF_F, OFF_S, OFF_T  = "#fbfbfc", "#ececef", "#c8ccd0"
SOFT, ARROW, BLACK   = "#f6f6f6", "#b0b6bc", "#161719"

FONT = "Poppins, system-ui, -apple-system, 'Segoe UI', sans-serif"
MONO = "'SFMono-Regular', Menlo, Monaco, Consolas, monospace"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def txt(x, y, s, size=10, fill=BODY, anchor="start", weight="400", font=None, ls=None, rot=None):
    a = ['x="%s" y="%s"' % (x, y), 'font-family="%s"' % (font or FONT), 'font-size="%s"' % size,
         'fill="%s"' % fill, 'text-anchor="%s"' % anchor, 'font-weight="%s"' % weight]
    if ls is not None:
        a.append('letter-spacing="%s"' % ls)
    t = '<text %s>%s</text>' % (" ".join(a), esc(s))
    if rot is not None:
        t = '<g transform="rotate(%s %s %s)">%s</g>' % (rot, x, y, t)
    return t

def rect(x, y, w, h, fill="none", stroke="none", rx=0, sw=1.0, op=None, dash=None):
    a = ['x="%s" y="%s" width="%s" height="%s" rx="%s"' % (x, y, w, h, rx),
         'fill="%s"' % fill, 'stroke="%s"' % stroke, 'stroke-width="%s"' % sw]
    if op is not None: a.append('opacity="%s"' % op)
    if dash: a.append('stroke-dasharray="%s"' % dash)
    return '<rect %s/>' % " ".join(a)

def line(x1, y1, x2, y2, stroke=LINE, sw=1.2, dash=None, op=None):
    a = ['x1="%s" y1="%s" x2="%s" y2="%s"' % (x1, y1, x2, y2),
         'stroke="%s"' % stroke, 'stroke-width="%s"' % sw]
    if dash: a.append('stroke-dasharray="%s"' % dash)
    if op is not None: a.append('opacity="%s"' % op)
    return '<line %s/>' % " ".join(a)

def arrow(x1, y1, x2, y2, stroke=ARROW, sw=1.3, marker="a"):
    return ('<path d="M %s %s L %s %s" fill="none" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (x1, y1, x2, y2, stroke, sw, marker))

def curve(x1, y1, cx1, cy1, cx2, cy2, x2, y2, stroke=ARROW, sw=1.2, marker="a", op=None):
    a = ['d="M %s %s C %s %s %s %s %s %s"' % (x1, y1, cx1, cy1, cx2, cy2, x2, y2),
         'fill="none"', 'stroke="%s"' % stroke, 'stroke-width="%s"' % sw]
    if marker: a.append('marker-end="url(#%s)"' % marker)
    if op is not None: a.append('opacity="%s"' % op)
    return '<path %s/>' % " ".join(a)

def vec(cx, y, n=4, cell=22, stroke=TEAL, fill=TEAL_F, values=None, fs=None, op=None, sw=1.3):
    """La forma canonica: n celle affiancate, centrate su cx."""
    x0 = cx - (n * cell) / 2.0
    o = []
    for i in range(n):
        o.append(rect(x0 + i * cell, y, cell, cell, fill, stroke, rx=cell * 0.13, sw=sw, op=op))
        if values:
            o.append(txt(x0 + i * cell + cell / 2.0, y + cell * 0.66, values[i],
                         fs or cell * 0.42, BODY, "middle", "500", MONO))
    return "".join(o)

def vvec(cx, y_top, n=4, cell=18, stroke=GREYD, fill=SOFT, op=None):
    """Vettore-colonna: n celle impilate. Serve dove la matrice e' una batteria di vettori."""
    x0 = cx - cell / 2.0
    return "".join(rect(x0, y_top + i * cell, cell, cell, fill, stroke, rx=cell * 0.13,
                        sw=1.1, op=op) for i in range(n))

def matrix(x0, y0, rows=4, cols=3, cell=20, stroke=GREYD, fill=SOFT, box=True, sw=0.7):
    """Matrice di proiezione: righe = celle in ingresso, colonne = celle in uscita."""
    o = []
    for r in range(rows):
        for c in range(cols):
            o.append(rect(x0 + c * cell, y0 + r * cell, cell, cell, fill, stroke,
                          rx=cell * 0.1, sw=sw))
    if box:
        o.append(rect(x0 - 2.5, y0 - 2.5, cols * cell + 5, rows * cell + 5, "none", stroke,
                      rx=3, sw=1.3))
    return "".join(o)

def tile(cx, y, w, h, label, fs=13, stroke=LINE, fill="#ffffff", color=BODY, sw=1.2, sub=None):
    """Tessera-token: testo monospaziato, sempre la stessa specie di oggetto."""
    o = [rect(cx - w / 2.0, y, w, h, fill, stroke, rx=4, sw=sw)]
    o.append(txt(cx, y + (h * 0.60 if not sub else h * 0.47), label, fs, color, "middle", "500", MONO))
    if sub:
        o.append(txt(cx, y + h * 0.82, sub, fs * 0.62, GREYD, "middle", "400", MONO))
    return "".join(o)

def plus(cx, cy, r=8, stroke=BUR, fs=12):
    return ('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
            % (cx, cy, r, stroke)) + txt(cx, cy + fs / 3.0, "+", fs, stroke, "middle", "600")

def eyebrow(x, y, s, fill=BUR):
    return txt(x, y, s, 8.5, fill, "start", "700", ls="0.13em")

DEFS = ('<defs>'
        '<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
        'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>'
        '<marker id="ab" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
        'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>'
        '<marker id="at" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
        'orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>'
        '<pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse">'
        '<circle cx="1.6" cy="1.6" r="1.1" fill="#e4e7ea"/></pattern>'
        '</defs>' % (ARROW, BUR, TEAL))

def svg(w, h, body, alt):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" '
            'role="img" aria-label="%s">%s<rect width="%s" height="%s" fill="#ffffff"/>%s</svg>'
            % (w, h, w, h, esc(alt), DEFS, w, h, body))
