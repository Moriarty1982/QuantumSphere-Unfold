"""Bewertet ein lokales Modell (Ollama) auf eval.jsonl.

Voraussetzung: Ollama laeuft (http://localhost:11434), Modell ist geladen, z. B. 'sphaera' aus dem Modelfile.
Aufruf:  python eval_ollama.py sphaera  [--data eval.jsonl]

Pro Frage drei Kennzahlen:
  tags     - Antwort enthaelt mindestens einen Ebenen-Tag [V]/[M]/[S]/[P]
  guard    - Guard-Linter findet keinen Treffer (verbotene Aussage ohne Verneinung)
  stichw   - Anteil der Schluesselzahlen/-begriffe der Referenzantwort, die in der Modellantwort vorkommen
Guard-Treffer sind das wichtigste Kriterium: jeder einzelne ist ein Fehler.
"""
import json
import re
import sys
import urllib.request
import importlib.util
import os

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gl", os.path.join(here, "guard_linter.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)

def ask(model, messages):
    body = json.dumps({"model": model, "messages": messages, "stream": False,
                       "options": {"temperature": 0.2}}).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())["message"]["content"]

def keys(text):
    nums = set(re.findall(r"\d+,\d+|\d+\.\d+|\b\d{2,}\b", text))
    words = set(w.lower() for w in re.findall(r"\b[A-Za-z_]{2,}[\w\^/+-]*\b", text)
                if any(c in w for c in "_^") or w in ("Lesart", "SO", "CP", "GUE", "GOE", "Poisson"))
    return nums | words

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    model = sys.argv[1]
    data = sys.argv[sys.argv.index("--data") + 1] if "--data" in sys.argv else os.path.join(here, "eval.jsonl")
    n = tags = guard_ok = 0; cover = 0.0
    for line in open(data, encoding="utf-8"):
        rec = json.loads(line); msgs = rec["messages"]
        ref = msgs[-1]["content"]
        ans = ask(model, msgs[:-1])
        n += 1
        t = bool(re.search(r"\[(V|M|S|P)\]", ans)); tags += t
        hits = gl.lint(ans); guard_ok += not hits
        k = keys(ref); c = (len([x for x in k if x.lower() in ans.lower()])/len(k)) if k else 1.0; cover += c
        print(f"--- {msgs[-2]['content']}\n{ans}\n    tags={t} guard={'OK' if not hits else 'VERSTOSS'} stichw={c:.0%}")
    print(f"\n{n} Fragen | Tags {tags}/{n} | Guard sauber {guard_ok}/{n} | Stichwort-Abdeckung {cover/n:.0%}")

if __name__ == "__main__":
    sys.exit(main())
