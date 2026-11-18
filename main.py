"""News-image entry (Python 3.13, standard library only): copies the bundled
front-page image to /output/entry.png. Deterministic: the same bytes every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(_OUT, exist_ok=True)
shutil.copyfile(os.path.join(_HERE, "entry.png"),
                os.path.join(_OUT, "entry.png"))
