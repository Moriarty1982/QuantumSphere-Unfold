"""Erzeugt das Ollama-Modelfile mit der aktuellen Kernkarte als Systemkontext.

Aufruf:  python make_modelfile.py [basismodell] [--kurz]   (Standard: qwen2.5:3b)
  --kurz  nur Abschnitte 0-6 der Kernkarte (ohne Arbeitsergebnisse K1-K9) und num_ctx 8192,
          fuer kleine Grafikkarten wie die RTX 2060
Danach:  ollama create sphaera -f Modelfile
"""
import os, sys, json

here = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
kurz = "--kurz" in sys.argv
base = args[0] if args else "qwen2.5:3b"
karte = open(os.path.join(here, "..", "Kernkarte_Quantum_Sphaera_v1.md"), encoding="utf-8").read()
if kurz:
    karte = karte.split("\n## 7.")[0]
ctx = 8192 if kurz else 16384
spec = __import__("importlib.util").util.spec_from_file_location("bd", os.path.join(here, "build_dataset.py"))
bd = __import__("importlib.util").util.module_from_spec(spec); spec.loader.exec_module(bd)
system = bd.SYSTEM + "\n\nWissensgrundlage (Kernkarte):\n\n" + karte
with open(os.path.join(here, "Modelfile"), "w", encoding="utf-8") as f:
    f.write(f"FROM {base}\nPARAMETER num_ctx {ctx}\nPARAMETER temperature 0.2\n")
    f.write('SYSTEM """' + system.replace('"""', "'''") + '"""\n')
print(f"Modelfile geschrieben (Basis {base}, {len(system)} Zeichen = ca. {len(system)//3200}k Tokens Systemkontext, num_ctx {ctx}).")
