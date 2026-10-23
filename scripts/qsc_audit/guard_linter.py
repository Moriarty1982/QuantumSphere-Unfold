"""Guard-Linter fuer Quantum-Sphaera-Texte (LaTeX oder Klartext, Deutsch/Englisch).

Findet Stellen, die eine der fuenf verbotenen Aussagen behaupten koennten, und alles, was RH als
bewiesen darstellt. Ein Treffer wird unterdrueckt, wenn im Umfeld (gleicher Satz) eine Verneinung steht
("not", "nicht", "kein", "does not imply", "verboten", "forbidden", "widerlegt", ...).

Aufruf:
  python guard_linter.py datei.tex [--start N --end M]
  python guard_linter.py daten.jsonl --jsonl        # prueft nur die Assistenten-Antworten
Rueckgabe-Code 1, wenn Treffer gefunden wurden.
"""
import json
import re
import sys

PATTERNS = [
    ("C5 = 0 (exakte C5-Null-Schliessung)",
     r"C_?\{?5\}?\s*=\s*0(?![.,]\d)|C5\s*=\s*0|exact(e)?\s+(finite\s+)?C5[- ]?(zero|null)[- ]?(closure|schlie)"),
    ("0_termdata => 0_all (exakte All-Readout-Terminalitaet)",
     r"0_?\{?(\\mathrm\{)?termdata\}?\}?\s*(\\Rightarrow|=>|⇒|\\implies)\s*0_?\{?(\\mathrm\{)?all|exact(e)?\s+all-?readout[- ]terminal"),
    ("C6/T2-Schliessung",
     r"(C6|T2)\s*(is|ist|wird)?\s*(closed|geschlossen|discharged|bewiesen|proved)|(closure|schliessung|schließung)\s+(of\s+)?(C6|T2)\b"),
    ("W_gamma^glob (globales Photon-Clock-/RH-Theorem)",
     r"W_?\{?\\gamma\}?\^?\{?(\\rm\s*|\\mathrm\{)?glob|W_γ\^glob|global(es)?\s+(photon[- ]clock|RH)[- ]?(theorem|satz)"),
    ("W_all (globale All-Readout-Schliessung)",
     r"W_?\{?(\\rm\s*|\\mathrm\{)?all\}?(?![a-z])|global(e)?\s+all-?readout[- ](closure|schlie)"),
    ("RH als bewiesen",
     r"(Riemann[- ]Hypothes[ie]s?|Riemannsche Vermutung|\bRH\b)[^.;\n]{0,60}\b(is|ist|wird|wurde)\s+(\w+\s+){0,2}(proved|proven|bewiesen|gel[oö]st|established|closed)"
     r"|(proof|Beweis)\s+(of|der|von)\s+(the\s+)?(Riemann|RH)[^.;\n]{0,40}(complete|vollst|geschlossen)"),
]
NEG = re.compile(r"\b(not|no|never|nicht|kein\w*|nie|forbid\w*|verbiet\w*|verboten|withdrawn|zur[uü]ckgezogen|"
                 r"widerlegt|refuted|false|falsch|does not imply|impliziert nicht|unless|ausser|"
                 r"remains blocked|bleibt gesperrt|open|offen|conjecture|vermutung)\b", re.I)

def sentences(text):
    # Satzende = . ! ? gefolgt von Leerraum oder Textende, oder eine Leerzeile (LaTeX-Absatz).
    for m in re.finditer(r"(?s).*?(?:[.!?](?=\s|$)|\n\s*\n|$)", text):
        if m.group(0).strip():
            yield m.start(), m.group(0)

def lint(text, offset_line=1):
    hits = []
    line_starts = [0] + [i + 1 for i, c in enumerate(text) if c == "\n"]
    def line_of(pos):
        lo, hi = 0, len(line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1)//2
            if line_starts[mid] <= pos: lo = mid
            else: hi = mid - 1
        return lo + offset_line
    for pos, sent in sentences(text):
        for name, pat in PATTERNS:
            for m in re.finditer(pat, sent, re.I):
                if NEG.search(sent):
                    continue
                hits.append((line_of(pos + m.start()), name, sent.strip()[:160]))
    return hits

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return 2
    path = args[0]
    if "--jsonl" in args:
        total = 0
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                rec = json.loads(line)
                for msg in rec["messages"]:
                    if msg["role"] == "assistant":
                        for _, name, s in lint(msg["content"]):
                            total += 1
                            print(f"Eintrag {i}: {name}\n   {s}")
        print(f"{total} Treffer in Assistenten-Antworten.")
        return 1 if total else 0
    text = open(path, encoding="utf-8", errors="replace").read()
    start = int(args[args.index("--start") + 1]) if "--start" in args else 1
    end = int(args[args.index("--end") + 1]) if "--end" in args else None
    lines = text.split("\n")
    chunk = "\n".join(lines[start - 1:end])
    hits = lint(chunk, offset_line=start)
    for ln, name, s in hits:
        print(f"Zeile {ln}: {name}\n   {s}")
    print(f"{len(hits)} Treffer.")
    return 1 if hits else 0

if __name__ == "__main__":
    sys.exit(main())
