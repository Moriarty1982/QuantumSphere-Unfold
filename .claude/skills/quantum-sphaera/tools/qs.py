#!/usr/bin/env python3
"""qs -- Werkzeuge fuer den Quantum-Sphaera-Dokumentkomplex.

Unterkommandos:
  outline    Gliederung und Runden eines .tex-Monolithen
  xref       LaTeX-Nummerierung aufloesen (Nummer <-> Label <-> Titel)
  citations  \\cite-Verweise mit Nummer gegen die Quelldatei pruefen
  guards     Kandidaten fuer unbewachte verbotene Claims suchen
  ledger     Guard-/Residual-Vektoren ueber die Runden verfolgen
  manifest   SHA256-Manifest im Format der Release-Begleitdateien

Alle Kommandos lesen nur; nichts wird veraendert.
"""

import argparse
import hashlib
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SECTION_LEVELS = ["section", "subsection", "subsubsection"]


# ---------------------------------------------------------------- Hilfsmittel

def strip_comment(line):
    """Entfernt einen LaTeX-Kommentar, respektiert \\%."""
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def read_lines(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def brace_arg(text, start):
    """Liest ein {...}-Argument ab Position start (muss auf '{' stehen)."""
    if start >= len(text) or text[start] != "{":
        return None, start
    depth = 0
    i = start
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return None, start


# ------------------------------------------------------------- Nummerierung

class Numbering:
    """Bildet die LaTeX-Theoremnummerierung einer Datei nach.

    Beruecksichtigt geteilte Zaehler (\\newtheorem{lemma}[theorem]{Lemma}),
    Reset durch [section] und den Unterschied zwischen \\section und \\section*.
    """

    RE_NEWTHM = re.compile(
        r"\\newtheorem(?P<star>\*)?\{(?P<env>[^}]+)\}"
        r"(?:\[(?P<shared>[^\]]+)\])?"
        r"\{(?P<label>[^}]*)\}"
        r"(?:\[(?P<within>[^\]]+)\])?"
    )
    RE_SECTION = re.compile(r"\\(sub)*section(?P<star>\*)?\s*[\{\[]")
    RE_BEGIN = re.compile(r"\\begin\{(?P<env>[a-zA-Z*]+)\}")
    RE_LABEL = re.compile(r"\\label\{(?P<lbl>[^}]+)\}")

    def __init__(self, path):
        self.path = path
        self.lines = read_lines(path)
        self.counter_of = {}     # env -> Zaehlername
        self.within = {}         # Zaehlername -> "section" o.ae.
        self.unnumbered = set()
        self.caveats = []
        self._scan_preamble()
        self.entries = self._walk()

    def _scan_preamble(self):
        for raw in self.lines:
            line = strip_comment(raw)
            for m in self.RE_NEWTHM.finditer(line):
                env = m.group("env")
                if m.group("star"):
                    self.unnumbered.add(env)
                    continue
                shared = m.group("shared")
                if shared:
                    self.counter_of[env] = self.counter_of.get(shared, shared)
                else:
                    self.counter_of[env] = env
                    if m.group("within"):
                        self.within[env] = m.group("within")
            if "\\numberwithin" in line:
                self.caveats.append("\\numberwithin gefunden: " + line.strip())
            if re.search(r"\\setcounter\{(section|theorem)\}", line):
                self.caveats.append("\\setcounter gefunden: " + line.strip())

    def _walk(self):
        sec = 0
        counters = {}
        entries = []
        in_appendix = False
        pending = None       # (env, number, line_no, titel)

        for idx, raw in enumerate(self.lines, start=1):
            line = strip_comment(raw)

            if "\\appendix" in line and "\\renewcommand" not in line \
                    and "newcommand" not in line:
                in_appendix = True
                self.caveats.append(
                    "\\appendix in Zeile %d: Nummerierung ab hier pruefen" % idx)

            m = self.RE_SECTION.search(line)
            if m and m.group(1) is None:      # nur \section, nicht \subsection
                if not m.group("star"):
                    sec += 1
                    for cname, w in self.within.items():
                        if w == "section":
                            counters[cname] = 0
                # Gliederungsknoten als eigener Eintrag, damit --label auch
                # Abschnittsmarken findet und nicht faelschlich "fehlt" meldet.
                titel, _ = brace_arg(line, line.index("{")) if "{" in line else (None, 0)
                pending = {"env": "section", "number": str(sec) if not m.group("star") else "*",
                           "line": idx, "title": (titel or "").strip()[:60],
                           "label": None, "section": sec}
                entries.append(pending)

            for mb in self.RE_BEGIN.finditer(line):
                env = mb.group("env")
                if env in self.unnumbered or env not in self.counter_of:
                    continue
                cname = self.counter_of[env]
                counters[cname] = counters.get(cname, 0) + 1
                if self.within.get(cname) == "section":
                    num = "%s%d.%d" % ("A." if in_appendix else "",
                                       sec, counters[cname])
                else:
                    num = str(counters[cname])
                title = None
                rest = line[mb.end():]
                if rest.startswith("["):
                    close = rest.find("]")
                    if close != -1:
                        title = rest[1:close]
                pending = {"env": env, "number": num, "line": idx,
                           "title": title, "label": None, "section": sec}
                entries.append(pending)

            if pending is not None and pending["label"] is None:
                ml = self.RE_LABEL.search(line)
                if ml and idx - pending["line"] <= 3:
                    pending["label"] = ml.group("lbl")

        return entries

    def by_number(self, number):
        return [e for e in self.entries if e["number"] == number]

    def by_label(self, label):
        return [e for e in self.entries if e["label"] == label]


def fmt_entry(e):
    title = (" [%s]" % e["title"]) if e["title"] else ""
    label = ("  \\label{%s}" % e["label"]) if e["label"] else ""
    return "%-11s %-8s Zeile %-7d %s%s" % (
        e["env"].capitalize(), e["number"], e["line"], title, label)


# -------------------------------------------------------------------- outline

RE_ROUND = re.compile(r"v?4\.7\.0-r(\d+)|(?:^|\s)r(\d{2})\b")


def cmd_outline(args):
    lines = read_lines(args.tex)
    pat = re.compile(r"^\\(?P<lvl>sub)*section(?P<star>\*)?\{")
    shown = 0
    for idx, raw in enumerate(lines, start=1):
        m = pat.match(raw)
        if not m:
            continue
        depth = len(m.group("lvl") or "") // 3
        if depth > args.depth:
            continue
        title, _ = brace_arg(raw, raw.index("{"))
        title = (title or "").strip()
        if args.rounds:
            mr = RE_ROUND.search(title)
            if not mr:
                continue
        if args.grep and args.grep.lower() not in title.lower():
            continue
        print("%7d  %s%s" % (idx, "  " * depth, title))
        shown += 1
    print("\n%d Eintraege, Datei hat %d Zeilen." % (shown, len(lines)))


# ----------------------------------------------------------------------- xref

def cmd_xref(args):
    nb = Numbering(args.tex)
    if nb.caveats:
        print("Hinweise zur Nummerierung:")
        for c in dict.fromkeys(nb.caveats):
            print("  ! " + c)
        print()

    if args.number:
        hits = nb.by_number(args.number)
        if not hits:
            print("Keine Umgebung mit Nummer %s." % args.number)
            return 1
        for e in hits:
            print(fmt_entry(e))
        return 0

    if args.label:
        hits = nb.by_label(args.label)
        if not hits:
            print("Kein \\label{%s} gefunden." % args.label)
            return 1
        for e in hits:
            print(fmt_entry(e))
        return 0

    entries = nb.entries
    if args.section:
        entries = [e for e in entries if e["section"] == args.section]
    for e in entries:
        print(fmt_entry(e))
    print("\n%d nummerierte Umgebungen." % len(entries))
    return 0


# ------------------------------------------------------------------ citations

CITE_TYPES = "Theorem|Lemma|Proposition|Corollary|Definition|Axiom|Assumption"
RE_CITE = re.compile(r"\\cite\{(?P<keys>[^}]+)\}")
RE_NUMREF = re.compile(
    r"(?P<type>" + CITE_TYPES + r")[~\s]*(?P<num>\d+\.\d+)")
RE_SYMREF = re.compile(
    r"(?P<type>" + CITE_TYPES + r")[~\s]*(?P<sym>T\d+(?:\+T\d+)?)")


STOPWORDS = set("""the and for with from into over under a an of on in to as by
via des der die das und fuer mit""".split())


def content_words(text):
    """Inhaltstragende Woerter (>=4 Buchstaben, keine Stoppwoerter)."""
    words = re.findall(r"[A-Za-zaeoeuess]{4,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def clean_tex(text):
    text = re.sub(r"\\cite\{[^}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[{}$~\\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def cmd_citations(args):
    sources = {}
    for spec in args.source:
        if "=" not in spec:
            print("--source erwartet KEY=pfad.tex, bekam: %s" % spec)
            return 2
        key, path = spec.split("=", 1)
        if not os.path.exists(path):
            print("Quelldatei fehlt: %s" % path)
            return 2
        sources[key] = Numbering(path)
        print("Quelle %-20s %s (%d Umgebungen)"
              % (key, os.path.basename(path), len(sources[key].entries)))
    print()

    lines = read_lines(args.tex)

    # Zusammenhaengender Text mit Zeilenzuordnung: Verweise wie
    # "Lemma~13.2, Step~3\nof~\cite{...}" laufen ueber Zeilengrenzen und
    # wuerden bei zeilenweiser Suche verlorengehen.
    stripped = [strip_comment(l) for l in lines]
    text = "\n".join(stripped)
    starts = []
    pos = 0
    for l in stripped:
        starts.append(pos)
        pos += len(l) + 1

    def line_of(offset):
        import bisect
        return bisect.bisect_right(starts, offset)

    ok = bad = sym = flagged = 0
    for mc in RE_CITE.finditer(text):
            idx = line_of(mc.start())
            keys = [k.strip() for k in mc.group("keys").split(",")]
            keys = [k for k in keys if k in sources]
            if not keys:
                continue
            lo = max(0, mc.start() - args.window)
            hi = min(len(text), mc.end() + args.window)
            window = text[lo:hi]

            for ms in RE_SYMREF.finditer(window):
                sym += 1
                if args.verbose:
                    print("~ Zeile %-7d symbolisch %s %s -> %s (nicht pruefbar)"
                          % (idx, ms.group("type"), ms.group("sym"), keys[0]))

            for mn in RE_NUMREF.finditer(window):
                typ, num = mn.group("type"), mn.group("num")
                for key in keys:
                    hits = sources[key].by_number(num)
                    if not hits:
                        bad += 1
                        print("FEHLT  Zeile %-7d %s %s -> %s: Nummer existiert nicht\n"
                              % (idx, typ, num, key))
                        continue
                    target = hits[0]
                    typ_ok = target["env"].lower() == typ.lower()

                    # Kontext: umliegende Zeilen, nicht nur das Zeichenfenster.
                    c_lo = max(0, idx - 1 - args.context)
                    c_hi = min(len(lines), idx + args.context)
                    context = clean_tex(" ".join(lines[c_lo:c_hi]))
                    title = target["title"] or ""
                    overlap = content_words(title) & content_words(context)

                    status = "ok    "
                    if not typ_ok:
                        status = "TYP   "
                        bad += 1
                    elif title and not overlap:
                        status = "PRUEF "
                        flagged += 1
                    else:
                        ok += 1

                    if status != "ok    " or args.verbose:
                        print("%s Zeile %-7d zitiert %s %s aus %s"
                              % (status, idx, typ, num, key))
                        print("       Ziel:    %s %s%s (Zeile %d)"
                              % (target["env"].capitalize(), target["number"],
                                 (" [%s]" % title) if title else "",
                                 target["line"]))
                        snippet = context
                        if len(snippet) > 150:
                            mid = snippet.lower().find(typ.lower())
                            s = max(0, mid - 60) if mid > 0 else 0
                            snippet = ("..." if s else "") + snippet[s:s + 150]
                        print("       Kontext: %s" % snippet)
                        if status == "PRUEF ":
                            print("       -> kein gemeinsames Stichwort zwischen "
                                  "Zieltitel und Kontext")
                        print()

    print("%d unauffaellig, %d zu pruefen, %d Typfehler, %d symbolisch."
          % (ok, flagged, bad, sym))
    print("PRUEF ist eine Heuristik (Stichwortabgleich), kein Urteil.")
    return 1 if bad else 0


# --------------------------------------------------------------------- guards

FORBIDDEN = [
    ("C5 exakt null", re.compile(r"C_?5(?:\^?\{?\}?)?\s*=\s*0")),
    ("all-readout Terminalitaet",
     re.compile(r"0_\{?\\(?:rm|mathrm)\s*\{?termdata\}?\}?[^\n]{0,40}"
                r"\\Rightarrow[^\n]{0,40}0_\{?\\(?:rm|mathrm)\s*\{?all\}?")),
    ("C6/T2 Schliessung",
     re.compile(r"(?:C6\s*/\s*T2|T2)[^\n]{0,30}"
                r"(?:closure|closed|geschlossen)", re.I)),
    ("globaler Photon-Clock/RH",
     re.compile(r"W_\{?\\gamma\}?\^?\{?\\?(?:rm\s*)?glob")),
    ("globale all-readout Schliessung",
     re.compile(r"W_\{?\\(?:rm|mathrm)\s*\{?all\}?")),
]

NEGATORS = re.compile(
    r"\\not|\\neg|\\nRightarrow|\bnot\b|\bno\b|forbidden|remains open|"
    r"does not|cannot|unclaimed|nicht|kein|verboten|\bopen\b|guard",
    re.I)


def cmd_guards(args):
    lines = read_lines(args.tex)
    lo = args.start or 1
    hi = args.end or len(lines)
    flagged = 0
    for idx in range(lo, min(hi, len(lines)) + 1):
        raw = lines[idx - 1]
        line = strip_comment(raw)
        if not line.strip():
            continue
        ctx_lo = max(0, idx - 1 - args.context)
        ctx_hi = min(len(lines), idx + args.context)
        context = " ".join(lines[ctx_lo:ctx_hi])
        for name, pat in FORBIDDEN:
            if pat.search(line) and not NEGATORS.search(context):
                flagged += 1
                print("Zeile %-7d [%s]" % (idx, name))
                print("    " + line.strip()[:150])
    print("\n%d Kandidat(en) in Zeilen %d-%d." % (flagged, lo, hi))
    print("Heuristik: markiert Treffer ohne erkennbare Verneinung im Umfeld.")
    print("Jeder Treffer ist von Hand zu pruefen, nicht automatisch ein Fehler.")
    return 0


# --------------------------------------------------------------------- ledger

RE_LEDGER = re.compile(
    r"(?P<name>R_\{?\\(?:rm|mathrm)\s*\{?(?:glob|eff/local|exact/global)\}?\}?"
    r"|\\Gamma_\{?\\(?:rm|mathrm)\s*\{?guard\}?\}?)"
    r"\^?\{?\(?r(?P<round>\d+)[,+)]*\}?\s*=\s*\((?P<vec>[01,\s]+)\)")


def cmd_ledger(args):
    lines = read_lines(args.tex)
    rows = []
    for idx, raw in enumerate(lines, start=1):
        line = strip_comment(raw)
        for m in RE_LEDGER.finditer(line):
            name = re.sub(r"\s+", "",
                          re.sub(r"[\\{}]|rm|mathrm", "", m.group("name")))
            vec = "(" + re.sub(r"\s+", "", m.group("vec")) + ")"
            rows.append((int(m.group("round")), name, vec, idx))
    if not rows:
        print("Keine Ledger-Vektoren gefunden.")
        return 1
    rows.sort()
    print("%-6s %-16s %-14s %s" % ("Runde", "Groesse", "Wert", "Zeile"))
    prev = {}
    for rnd, name, vec, idx in rows:
        mark = ""
        if name in prev and prev[name] != vec:
            mark = "  <-- geaendert (vorher %s)" % prev[name]
        prev[name] = vec
        print("r%-5d %-16s %-14s %-7d%s" % (rnd, name, vec, idx, mark))
    return 0


# ---------------------------------------------------------------------- audit

# Sollwerte aus dem RC19-Compile-Audit (siehe CLAUDE.md).
BASELINE = {
    "pages": 1014,
    "undefined_refs": 0,
    "undefined_cites": 0,
    "duplicate_labels": 0,
    "rerun": 0,
    "overfull": 45,
    "labels": 3290,
}


AUDIT_KEYS = ["pages", "undefined_refs", "undefined_cites",
              "duplicate_labels", "rerun", "overfull", "labels"]

# Diese drei duerfen sich durch eine Textaenderung bewegen; die uebrigen nicht.
AUDIT_SOFT = {"pages", "overfull", "labels"}


def scan_build(logpath, auxpath=None):
    with open(logpath, "r", encoding="utf-8", errors="replace") as fh:
        log = fh.read()
    mp = re.search(r"Output written on .*?\((\d+) pages", log)
    found = {
        "pages": int(mp.group(1)) if mp else None,
        "undefined_refs": len(re.findall(
            r"Reference `[^']*' on page \d+ undefined", log)),
        "undefined_cites": len(re.findall(
            r"Citation `[^']*' on page \d+ undefined", log)),
        "duplicate_labels": len(re.findall(r"Label `[^']*' multiply defined", log)),
        "rerun": len(re.findall(r"Rerun to get|Label\(s\) may have changed", log)),
        "overfull": len(re.findall(r"Overfull \\hbox", log)),
        "labels": None,
    }
    aux = auxpath or re.sub(r"\.log$", ".aux", logpath)
    if os.path.exists(aux):
        with open(aux, "r", encoding="utf-8", errors="replace") as fh:
            found["labels"] = len(re.findall(r"\\newlabel\{", fh.read()))
    found["_errors"] = re.findall(r"^! (.+)$", log, re.M)
    return found


def cmd_audit(args):
    if not os.path.exists(args.log):
        print("Log-Datei fehlt: %s" % args.log)
        return 2
    found = scan_build(args.log, args.aux)

    ref = None
    if args.compare:
        if not os.path.exists(args.compare):
            print("Vergleichs-Log fehlt: %s" % args.compare)
            return 2
        ref = scan_build(args.compare)
        head = ("Pruefung", "Referenz", "Ist", "Status")
        note = ("Referenz = derselbe Build-Lauf ohne die Aenderung. Das ist der "
                "aussagekraeftigere\nMassstab als die feste Baseline, weil "
                "Overfull-Zahlen von der TeX-Version abhaengen.")
    else:
        head = ("Pruefung", "Soll", "Ist", "Status")
        note = ("Feste RC19-Baseline. Overfull-Zahlen sind toolchain-abhaengig - "
                "fuer eine belastbare\nAussage denselben Stand ohne die Aenderung "
                "bauen und mit --compare gegenpruefen.")

    print("%-20s %10s %10s   %s" % head)
    print("-" * 58)
    hard = soft = 0
    for key in AUDIT_KEYS:
        want = ref[key] if ref else BASELINE[key]
        got = found[key]
        if got is None or want is None:
            status = "nicht ermittelt"
        elif got == want:
            status = "unveraendert" if ref else "ok"
        elif key in AUDIT_SOFT:
            status = "%+d" % (got - want)
            soft += 1
        else:
            status = "ABWEICHUNG (%+d)" % (got - want)
            hard += 1
        print("%-20s %10s %10s   %s"
              % (key, "?" if want is None else want,
                 "?" if got is None else got, status))

    if found["_errors"]:
        print("\n%d LaTeX-Fehler:" % len(found["_errors"]))
        for e in found["_errors"][:15]:
            print("  ! " + e.strip()[:120])
        if len(found["_errors"]) > 15:
            print("  ... und %d weitere" % (len(found["_errors"]) - 15))

    print("\n%d harte Abweichung(en), %d erwartbare Verschiebung(en)."
          % (hard, soft))
    print(note)
    return 1 if (found["_errors"] or hard) else 0


# ------------------------------------------------------------------------ doi

DOI_ROLES = [
    ("Version DOI (v4.8.0)", "10.5281/zenodo.23365244"),
    ("Concept DOI", "10.5281/zenodo.19210728"),
    ("Previous DOI (v4.7.0)", "10.5281/zenodo.20232911"),
    ("Previous/baseline DOI (v4.6.0)", "10.5281/zenodo.20117361"),
    ("ABGELAUFEN - darf nicht vorkommen", "10.5281/zenodo.20181842"),
]


def cmd_doi(args):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf fehlt.  Installation:  python -m pip install --user pypdf")
        return 2
    if not os.path.exists(args.pdf):
        print("PDF fehlt: %s" % args.pdf)
        return 2

    reader = PdfReader(args.pdf)
    pages = [p.extract_text() or "" for p in reader.pages]
    full = "\n".join(pages)
    title = pages[0] if pages else ""

    def count(needle, hay):
        # Zeilenumbrueche im PDF-Text koennen die DOI zerreissen.
        flat = re.sub(r"\s+", "", hay)
        return flat.count(re.sub(r"\s+", "", needle))

    print("PDF: %s (%d Seiten)\n" % (os.path.basename(args.pdf), len(pages)))
    print("%-34s %-26s %8s %10s" % ("Rolle", "DOI", "gesamt", "Titelseite"))
    print("-" * 82)
    bad = 0
    for role, doi in DOI_ROLES:
        total = count(doi, full)
        on_title = count(doi, title)
        flag = ""
        if "ABGELAUFEN" in role and total:
            flag = "  <-- FEHLER"
            bad += 1
        if role.startswith("Previous") and on_title:
            flag = "  <-- Vorgaenger-DOI gehoert nicht auf die Titelseite"
            bad += 1
        if role.startswith(("Version", "Concept")) and on_title != 1:
            flag = "  <-- Titelseite soll genau 1 Zeile haben"
            bad += 1
        print("%-34s %-26s %8d %10d%s" % (role, doi, total, on_title, flag))

    print("\n%s" % ("%d Beanstandung(en)." % bad if bad
                    else "Compact-Titlepage-Regel und DOI-Trennung eingehalten."))
    return 1 if bad else 0


# ------------------------------------------------------------------- manifest

def cmd_manifest(args):
    root = args.dir
    names = sorted(n for n in os.listdir(root)
                   if os.path.isfile(os.path.join(root, n))
                   and not n.startswith("."))
    if args.only:
        wanted = set(args.only)
        names = [n for n in names if n in wanted]
    print("file,sha256,bytes")
    for name in names:
        path = os.path.join(root, name)
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        print("%s,%s,%d" % (name, h.hexdigest(), os.path.getsize(path)))
    return 0


# ----------------------------------------------------------------------- main

def main():
    p = argparse.ArgumentParser(prog="qs", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("outline", help="Gliederung / Runden")
    o.add_argument("tex")
    o.add_argument("--depth", type=int, default=0, help="0=section, 1=+subsection")
    o.add_argument("--rounds", action="store_true", help="nur rNN-Abschnitte")
    o.add_argument("--grep", help="Titel-Filter")
    o.set_defaults(func=cmd_outline)

    x = sub.add_parser("xref", help="Nummerierung aufloesen")
    x.add_argument("tex")
    x.add_argument("--number", help="z.B. 3.2")
    x.add_argument("--label", help="z.B. thm:FE")
    x.add_argument("--section", type=int, help="nur diese Section")
    x.set_defaults(func=cmd_xref)

    c = sub.add_parser("citations", help="\\cite-Nummern gegen Quellen pruefen")
    c.add_argument("tex")
    c.add_argument("--source", action="append", required=True,
                   metavar="KEY=PFAD", help="Bibkey und zugehoerige .tex-Datei")
    c.add_argument("--window", type=int, default=140)
    c.add_argument("--context", type=int, default=2)
    c.add_argument("--verbose", "-v", action="store_true")
    c.set_defaults(func=cmd_citations)

    g = sub.add_parser("guards", help="unbewachte verbotene Claims suchen")
    g.add_argument("tex")
    g.add_argument("--start", type=int)
    g.add_argument("--end", type=int)
    g.add_argument("--context", type=int, default=8)
    g.set_defaults(func=cmd_guards)

    l = sub.add_parser("ledger", help="Guard-/Residual-Vektoren je Runde")
    l.add_argument("tex")
    l.set_defaults(func=cmd_ledger)

    a = sub.add_parser("audit", help="Compile-Log gegen die RC19-Baseline")
    a.add_argument("log", help="Pfad zur .log-Datei des Builds")
    a.add_argument("--aux", help="zugehoerige .aux (Default: log mit .aux)")
    a.add_argument("--compare", metavar="REF.log",
                   help="Referenz-Build statt fester Baseline")
    a.set_defaults(func=cmd_audit)

    d = sub.add_parser("doi", help="DOI-Vorkommen und Titelseiten-Regel im PDF")
    d.add_argument("pdf")
    d.set_defaults(func=cmd_doi)

    m = sub.add_parser("manifest", help="SHA256-Manifest erzeugen")
    m.add_argument("dir")
    m.add_argument("--only", nargs="*", help="nur diese Dateinamen")
    m.set_defaults(func=cmd_manifest)

    args = p.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
