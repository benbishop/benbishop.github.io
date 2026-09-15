#!/usr/bin/env python3
"""Inline every image in index.html to produce a single self-contained file.

Run it from the Portfolio-Site folder:

    python3 build.py

index.html stays the file you edit. index-standalone.html is the output, for when
you want to email or drop the whole portfolio as one file with nothing alongside it.
Deploying the folder does not need it.
"""
import base64, mimetypes, pathlib, re, sys

here = pathlib.Path(__file__).parent
src  = here / "index.html"
out  = here / "index-standalone.html"

if not src.exists():
    sys.exit("index.html not found next to build.py")

html = src.read_text(encoding="utf-8")
missing, inlined = [], 0

def repl(match):
    global inlined
    rel = match.group(1)
    if rel.startswith("data:") or "://" in rel:
        return match.group(0)
    path = here / rel
    if not path.exists():
        missing.append(rel)
        return match.group(0)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode()
    inlined += 1
    return 'src="data:%s;base64,%s"' % (mime, b64)

html = re.sub(r'src="([^"]+)"', repl, html)
out.write_text(html, encoding="utf-8")

print("inlined %d image(s) -> %s (%.0f KB)" % (inlined, out.name, out.stat().st_size / 1024))
for m in missing:
    print("  missing, left as a link:", m)
