"""Erzeugt das Ollama-Modelfile mit der aktuellen Kernkarte als Systemkontext.

Aufruf:  python make_modelfile.py [basismodell] [--kurz]   (Standard: qwen2.5:3b)
  --kurz  nur Abschnitte 0-6 der Kernkarte (mit Kurzregister, ohne Arbeitsergebnisse K1 ff.),
          fuer kleine Grafikkarten wie die RTX 2060
num_ctx wird aus der Laenge des Systemkontexts berechnet (naechste Zweierpotenz, mit mindestens
2048 Tokens Platz fuer Frage und Antwort), damit der Anfang mit den Guard-Regeln nie abgeschnitten wird.
Danach:  ollama create sphaera -f Modelfile
"""
import os, sys

here = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
kurz = "--kurz" in sys.argv
base = args[0] if args else "qwen2.5:3b"
karte = open(os.path.join(here, "..", "Kernkarte_Quantum_Sphaera_v1.md"), encoding="utf-8").read()
if kurz:
    karte = karte.split("\n## 7.")[0]
spec = __import__("importlib.util").util.spec_from_file_location("bd", os.path.join(here, "build_dataset.py"))
bd = __import__("importlib.util").util.module_from_spec(spec); spec.loader.exec_module(bd)
system = bd.SYSTEM + "\n\nWissensgrundlage (Kernkarte):\n\n" + karte
tokens = int(len(system) / 3.2)            # grobe Schaetzung fuer deutschen Text mit Formeln
ctx = 8192
while ctx < tokens + 2048:
    ctx *= 2
with open(os.path.join(here, "Modelfile"), "w", encoding="utf-8") as f:
    f.write(f"FROM {base}\nPARAMETER num_ctx {ctx}\nPARAMETER temperature 0.2\n")
    f.write('SYSTEM """' + system.replace('"""', "'''") + '"""\n')
print(f"Modelfile geschrieben (Basis {base}, {len(system)} Zeichen = ca. {tokens // 1000}k Tokens Systemkontext, "
      f"num_ctx {ctx}).")
if ctx > 16384:
    print("Hinweis: num_ctx ueber 16384 braucht viel Grafikspeicher. Auf einer 6-GB-Karte (RTX 2060) besser --kurz.")
