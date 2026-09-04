# -*- coding: utf-8 -*-
"""Sezione 2 — le due figure dei loop (slide 8 e 9b).

NON fa parte di `regen.py`, che copre solo la Sezione 3. Si lancia a mano:

    python3 presentation/svg-src/gen_sez2.py

Esiste perche' queste due figure hanno un layout calcolato (righe di payload di
lunghezza variabile, riquadri che crescono, graffe centrate sul contenuto) e
rifarle a mano dopo ogni ritocco e' come riscriverle. Le altre figure delle
Sezioni 1-2 (slide 2, 4, 7) sono piccole e restano scritte a mano nell'SVG.

Alfabeto proprio, NON quello della Sezione 3: qui i vettori non c'entrano, le
righe sono messaggi di una conversazione. I ruoli sono codificati dal colore:
grigio = storia gia' spedita, nero = input nuovo dell'utente, burgundy = output
appena generato dal modello, teal = risultato appeso da fuori (non dal modello).
"""
import io, os

MONO = "'SFMono-Regular', Menlo, Monaco, Consolas, monospace"
POP  = "Poppins, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
BUR, BUR_T, BLACK, BODY, GREY, LINE, GREYF, F6 = (
    "#a1245a", "#ecd3de", "#161719", "#212529", "#838383", "#dee2e6", "#9aa0a6", "#f6f6f6")
TEAL, TEAL_F, TEAL_D = "#1ab197", "#d1efea", "#0e7c6a"
OUT  = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "svg")
W, H = 1140, 356
CH   = 6.9          # larghezza carattere del mono a 11.5px
C2   = 7.82         # ... e a 13px, usata dalla pila della generazione
LH   = 16

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def txt(x, y, t, fs, fill, anchor="start", weight="400", fam=POP, ls=None):
    a = ' text-anchor="%s"' % anchor if anchor != "start" else ""
    l = ' letter-spacing="%s"' % ls if ls else ""
    return ('<text x="%g" y="%g"%s font-family="%s" font-size="%g" font-weight="%s" fill="%s"%s>%s</text>'
            % (x, y, a, fam, fs, weight, fill, l, esc(t)))

def rect(x, y, w, h, fill, stroke=None, rx=7, sw=1, dash=None):
    s = '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"' % (x, y, w, h, rx, fill)
    if stroke:
        s += ' stroke="%s" stroke-width="%g"' % (stroke, sw)
        if dash: s += ' stroke-dasharray="%s"' % dash
    return s + "/>"

def brace(x, y0, y1, label, lx):
    """Graffa verticale aperta a sinistra, con l'etichetta ruotata accanto."""
    ym = (y0 + y1) / 2.0
    d = ("M %g %g C %g %g %g %g %g %g L %g %g C %g %g %g %g %g %g "
         "C %g %g %g %g %g %g L %g %g C %g %g %g %g %g %g") % (
        x - 6, y0, x, y0, x - 2, y0 + 6, x - 2, y0 + 6, x - 2, ym - 6,
        x - 2, ym, x, ym - 2, x + 4, ym, x, ym + 2, x - 2, ym, x - 2, ym + 6,
        x - 2, y1 - 6, x - 2, y1 - 6, x, y1, x - 6, y1)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="1.5" stroke-linecap="round" '
            'stroke-linejoin="round"/>' % (d, GREY)
            + '<text transform="rotate(90 %g %g)" x="%g" y="%g" text-anchor="middle" '
              'font-family="%s" font-size="12.5" font-weight="500" fill="%s">%s</text>'
              % (lx, ym, lx, ym, POP, BODY, esc(label)))

def box(bx, by, bw, righe, etichetta):
    """Un payload spedito all'API: una riga per messaggio, e cresce coi messaggi."""
    bh = 8 + len(righe) * LH + 4
    o = [rect(bx, by, bw, bh, F6, LINE),
         txt(bx - 12, by + 20, etichetta, 12.5, GREY, "end", "600")]
    for j, (tag, body, kind) in enumerate(righe):
        ry  = by + 8 + j * LH
        bxx = bx + 16 + (len(tag) * CH + 7 if tag else 62)
        if kind == "pill":                                   # generato adesso dal modello
            o.append(rect(bx + 8, ry, bw - 16, LH, BUR, rx=5))
            o.append(txt(bx + 16, ry + 11.5, tag, 11.5, BUR_T, fam=MONO))
            o.append(txt(bxx, ry + 11.5, body, 11.5, "#ffffff", fam=MONO))
        elif kind == "tool":                                 # appeso da fuori, non dal modello
            o.append(rect(bx + 8, ry, bw - 16, LH, TEAL_F, TEAL, rx=5))
            o.append(txt(bx + 16, ry + 11.5, tag, 11.5, TEAL_D, fam=MONO, weight="600"))
            o.append(txt(bxx, ry + 11.5, body, 11.5, BODY, fam=MONO))
        else:
            fade  = kind == "old"
            c_tag = GREYF if fade else (BLACK if tag == "[user]" else GREY)
            o.append(txt(bx + 16, ry + 11.5, tag, 11.5, c_tag, fam=MONO))
            o.append(txt(bxx, ry + 11.5, body, 11.5, GREYF if fade else BODY, fam=MONO))
    return "".join(o), by + bh

def head(x, titolo, sub):
    return txt(x, 26, titolo, 13, BUR, weight="700", ls="1.6") + txt(x, 47, sub, 13, GREY)

def wrap(body, alt, comment):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img">\n  <title>%s</title>\n\n  <!-- %s -->\n\n  %s\n</svg>\n'
            % (W, H, W, H, esc(alt), comment, body))

SYS  = ("[system]", "Sei un assistente utile.", "old")
CONV = [
    [SYS, ("[user]", "Ciao, chi sei?", "user"), ("[assistant]", "Sono un assistente AI.", "pill")],
    [SYS, ("[user]", "Ciao, chi sei?", "old"), ("[assistant]", "Sono un assistente AI.", "old"),
     ("[user]", "Spiegami cosa sono i transformer", "user"),
     ("[assistant]", "Un'architettura del 2017…", "pill")],
    [SYS, ("[user]", "Ciao, chi sei?", "old"), ("[assistant]", "Sono un assistente AI.", "old"),
     ("[user]", "Spiegami cosa sono i transformer", "old"),
     ("[assistant]", "Un'architettura del 2017…", "old"),
     ("[user]", "E l'attention come funziona?", "user"),
     ("[assistant]", "È il meccanismo che pesa i token…", "pill")],
]

def colonna_conversazione(bx, bw, y0=62, gap=6):
    o, y = [], y0
    for t, righe in enumerate(CONV):
        s, y = box(bx, y, bw, righe, "turno %d" % (t + 1))
        o.append(s); y += gap
    return "".join(o), y - gap

# ═══════════════ SLIDE 9 — generazione a sinistra, conversazione a destra ═══════════════
def slide9():
    o = [head(12, "IL 1° LOOP — LA GENERAZIONE", "l'unità che si aggiunge è il token"),
         head(575, "IL 2° LOOP — LA CONVERSAZIONE", "l'unità che si aggiunge è il turno"),
         '<line x1="556" y1="12" x2="556" y2="344" stroke="%s" stroke-width="1"/>' % LINE]
    righe = [("", "Il"), ("Il", "gatto"), ("Il gatto", "è"), ("Il gatto è", "sul"),
             ("Il gatto è sul", "tavolo"), ("Il gatto è sul tavolo", "e"),
             ("Il gatto è sul tavolo e", "dorme"), ("Il gatto è sul tavolo e dorme", ".")]
    Y0, PITCH, RH, X0 = 62, 34, 28, 12
    for i, (ctx, tok) in enumerate(righe):
        y = Y0 + i * PITCH
        if ctx:
            cw = round(len(ctx) * C2 + 24)
            o.append(rect(X0, y, cw, RH, F6, LINE))
            o.append(txt(X0 + cw / 2.0, y + 19, ctx, 13, BODY, "middle", fam=MONO))
        else:
            cw = 50
            o.append(rect(X0, y, cw, RH, "none", LINE, dash="4 4"))
            o.append(txt(X0 + cw / 2.0, y + 18.5, "vuoto", 10.5, GREY, "middle"))
        tx, tw = X0 + cw + 4, max(28, round(len(tok) * C2 + 20))
        o.append(rect(tx, y, tw, RH, BUR))
        o.append(txt(tx + tw / 2.0, y + 19, tok, 13, "#ffffff", "middle", fam=MONO))
        if i == len(righe) - 1:                              # il badge STOP
            bx2 = tx + tw + 14
            o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.5"/>'
                     % (tx + tw, y + RH / 2.0, bx2, y + RH / 2.0, GREY))
            o.append(rect(bx2, y, 66, RH, BLACK))
            o.append(rect(bx2, y + 5, 3, 18, "#ffbe0b", rx=0))
            o.append(txt(bx2 + 36, y + 19, "STOP", 12.5, "#ffbe0b", "middle", "700", ls="1"))
    o.append(brace(400, Y0, Y0 + 7 * PITCH + RH, "il contesto cresce di un token per volta", 428))
    o.append(txt(12, 346, "ogni riga è una passata completa del modello: stessi pesi, contesto più lungo",
                 11.5, GREY))
    conv, y_end = colonna_conversazione(630, 460)
    o.append(conv)
    o.append(brace(1096, 62, y_end, "la storia cresce di un turno per volta", 1124))
    return wrap("\n  ".join(o),
        "Comparazione fra il 1° loop (la generazione: un token appeso al contesto) e il 2° loop "
        "(la conversazione: un turno appeso alla storia, rispedita per intero — system prompt "
        "compreso — a ogni chiamata)",
        "La meta sinistra riprende la pila della slide 6. La meta destra e il turno di conversazione,\n"
        "       col system prompt in testa a ogni payload: e' quello il senso di \"rispedita per intero\".")

# ═══════════════ SLIDE 9b — la stessa conversazione, con una tool call ═══════════════
def slide9b():
    DECL = ("", "Tool: cerca_ordine(id_ordine) — stato di un ordine", "old")
    GIRI = [
        [SYS, DECL, ("[user]", "Dov'è il mio ordine 4471?", "user"),
         ("[assistant]", "→ cerca_ordine(\"4471\")", "pill")],
        [SYS, DECL, ("[user]", "Dov'è il mio ordine 4471?", "old"),
         ("[assistant]", "→ cerca_ordine(\"4471\")", "old"),
         ("[tool]", "{ stato: \"in transito\", consegna: \"giovedì\" }", "tool"),
         ("[assistant]", "Il tuo ordine è in transito, arriva giovedì.", "pill")],
    ]
    o = [head(12, "SENZA TOOL", "un giro di generazione per turno"),
         head(575, "CON UNA TOOL CALL", "due giri dentro un solo turno"),
         '<line x1="556" y1="12" x2="556" y2="344" stroke="%s" stroke-width="1"/>' % LINE]
    # niente riga di piede a sinistra: passerebbe sotto il riquadro del turno 3,
    # e la sotto-intestazione dice gia' la stessa cosa.
    conv, _ = colonna_conversazione(68, 460)
    o.append(conv)
    y = 62
    for g, righe in enumerate(GIRI):
        s, y = box(630, y, 460, righe, "giro %d" % (g + 1))
        o.append(s); y += 6
    y_end = y - 6
    o.append(brace(1096, 62, y_end, "un solo turno dell'utente", 1124))
    o.append(txt(575, y_end + 34, "IL GIRO", 11, BUR, weight="700", ls="1.4"))
    for i, t in enumerate(["① il modello chiede un tool, e si ferma.",
                           "② qualcun altro esegue e appende il risultato al contesto.",
                           "③ il modello riparte — e il turno non è ancora finito."]):
        o.append(txt(575, y_end + 54 + i * 17, t, 12, TEAL_D if i == 1 else BODY))
    return wrap("\n  ".join(o),
        "A sinistra una conversazione normale, un giro di generazione per turno. A destra la stessa "
        "meccanica con una tool call: dentro un solo turno il modello genera due volte, perche' in "
        "mezzo qualcun altro esegue il tool e appende il risultato al contesto",
        "La meta sinistra e, identica, la meta destra di slide9-comparazione-loop.svg: e' la\n"
        "       citazione che rende leggibile il confronto. A destra lo stesso payload, con la\n"
        "       dichiarazione del tool dentro il system prompt e il giro di tool call nel flusso.")

# ═══════════════ SLIDE 9c — perche' serve un secondo addestramento ═══════════════
def slide9c():
    """Adattata da slide14-secondo-addestramento del deck gsom-april-2026: stesso
    prompt, due risposte reali. Introduce la mira con un esempio concreto, prima
    che la 9d la generalizzi con la metafora del golfista."""
    W2, H2 = 1140, 380
    BASE = ["Come posso aumentare le vendite?",
            "E quante persone lavorano nella tua azienda?",
            "Il settore è B2B o B2C? In quale mercato",
            "operate? Negli ultimi anni la domanda è",
            "cresciuta o è rimasta stabile?"]
    DOPO = ["Per aumentare le vendite puoi agire su tre leve:",
            "1) acquisire nuovi clienti (marketing, partnership);",
            "2) aumentare il valore medio per cliente (upselling);",
            "3) migliorare la retention (CRM, customer success).",
            "Vuoi approfondire una di queste?"]
    o = [txt(570, 22, "LO STESSO PROMPT", 11, GREY, "middle", "700", ls="1.4"),
         rect(350, 32, 440, 42, F6, LINE),
         txt(570, 59, "Come posso aumentare le vendite?", 15, BODY, "middle", fam=MONO),
         '<path d="M 480 74 L 480 90 Q 480 100 470 100 L 290 100 L 290 118" fill="none" '
         'stroke="%s" stroke-width="1.5" stroke-linecap="round"/>' % LINE,
         '<polygon points="285,116 290,126 295,116" fill="%s"/>' % LINE,
         '<path d="M 660 74 L 660 90 Q 660 100 670 100 L 850 100 L 850 118" fill="none" '
         'stroke="%s" stroke-width="1.5" stroke-linecap="round"/>' % BUR,
         '<polygon points="845,116 850,126 855,116" fill="%s"/>' % BUR,
         '<line x1="570" y1="118" x2="570" y2="368" stroke="%s" stroke-width="1" '
         'stroke-dasharray="4 4"/>' % LINE]

    for x0, titolo, sub, righe, col, mono, spiega in (
        (40, "MODELLO BASE", "solo pretraining", BASE, GREY, True,
         ["Continua la frase come farebbe un testo del web:", "altre domande, non una risposta."]),
        (610, "DOPO IL SECONDO ADDESTRAMENTO", "stesso modello, un addestramento in più", DOPO, BUR, False,
         ["Riconosce una domanda e risponde: utile,", "strutturata, orientata all'azione."])):
        o.append(txt(x0, 138, titolo, 13, col, weight="700", ls="1.2"))
        o.append(txt(x0, 156, sub, 12, GREY))
        o.append(rect(x0, 168, 490, 146, "#ffffff" if col == BUR else F6,
                      col if col == BUR else LINE, sw=1.4 if col == BUR else 1))
        for i, r in enumerate(righe):
            o.append(txt(x0 + 18, 194 + i * 23, r, 12.5, GREYF if mono else BODY,
                         fam=MONO if mono else POP))
        for i, r in enumerate(spiega):
            o.append(txt(x0, 336 + i * 16, r, 12, GREY))

    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img">\n  <title>%s</title>\n\n  <!-- %s -->\n\n  %s\n</svg>\n'
            % (W2, H2, W2, H2,
               esc("Lo stesso prompt dato a due modelli: quello uscito dal solo pretraining continua "
                   "il testo con altre domande, quello dopo il secondo addestramento risponde"),
               "Adattata da slide14-rlhf-comparison.svg del deck gsom-april-2026, riportata alla\n"
               "       palette e ai font di questo deck (quella di aprile era in Arial su fondi grigi).",
               "\n  ".join(o)))

for fn, body in (("slide9-comparazione-loop.svg", slide9()),
                 ("slide9b-tool-call.svg", slide9b()),
                 ("slide9c-secondo-addestramento.svg", slide9c())):
    io.open(os.path.join(OUT, fn), "w", encoding="utf-8").write(body)
    print(fn)
