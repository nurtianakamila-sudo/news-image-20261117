"""News-image entry (Python 3.13, standard library only): copies the bundled
front-page image to /output/entry.png. Deterministic: the same bytes every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import hashlib
import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(_OUT, exist_ok=True)
_src = os.path.join(_HERE, "entry.png")
_dst = os.path.join(_OUT, "entry.png")
shutil.copyfile(_src, _dst)
# Guard the deterministic-output requirement: the written file must be
# byte-identical to the bundled image, never a truncated copy.
with open(_src, "rb") as _f:
    _want = hashlib.sha256(_f.read()).hexdigest()
with open(_dst, "rb") as _f:
    _got = hashlib.sha256(_f.read()).hexdigest()
if _want != _got:
    raise SystemExit("entry.png copy mismatch: output differs from bundled image")
