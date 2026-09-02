#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rigenera tutti gli SVG della Sezione 3 in ../svg.

    python3 presentation/svg-src/regen.py

Dopo averlo lanciato, `git status` deve essere pulito: se qualcosa cambia
senza che tu abbia toccato i generatori, gli SVG erano stati modificati a mano
e le due fonti hanno divergito."""
import os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = ["gen_a.py", "gen15.py", "gen_b.py", "gen_griglia.py", "gen_minimap.py"]

for name in SCRIPTS:
    print("\n· %s" % name)
    sys.path.insert(0, HERE)
    runpy.run_path(os.path.join(HERE, name), run_name="__main__")
