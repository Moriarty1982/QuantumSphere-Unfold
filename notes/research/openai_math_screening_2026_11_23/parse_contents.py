"""Zerlegt openai/math CONTENTS.md in Familien (Nummer, Titel, Beschreibung, Manuskripte mit Abstract).

Aufruf: python -I parse_contents.py <ordner_mit_CONTENTS.md> <anzahl_teile>
Schreibt families.json und slice_K.md (K = 1..n) in denselben Ordner.
"""
import json
import os
import re
import sys

src_dir = sys.argv[1]
n_slices = int(sys.argv[2])
text = open(os.path.join(src_dir, "CONTENTS.md"), encoding="utf-8").read()

cells = re.findall(r"<td>\s*(.*?)\s*</td>", text, flags=re.S)
families = []
fam_re = re.compile(r"^\*\*(\d{3})\.\s*(.*?)\*\*\s*(.*)$", re.S)
man_re = re.compile(r"^&emsp;\[(.*?)\]\((.*?)\)\s*(.*)$", re.S)


def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("$`", "$").replace("`$", "$")
    return re.sub(r"\s+", " ", s).strip()


for c in cells:
    m = fam_re.match(c)
    if m:
        families.append({"nr": m.group(1), "title": clean(m.group(2)), "desc": clean(m.group(3)), "papers": []})
        continue
    m = man_re.match(c)
    if m and families:
        families[-1]["papers"].append({"title": clean(m.group(1)), "path": m.group(2), "abstract": clean(m.group(3))})

json.dump(families, open(os.path.join(src_dir, "families.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
n_papers = sum(len(f["papers"]) for f in families)
print("Familien:", len(families), "Manuskripte:", n_papers)

size = -(-len(families) // n_slices)
for k in range(n_slices):
    part = families[k * size:(k + 1) * size]
    if not part:
        continue
    with open(os.path.join(src_dir, f"slice_{k + 1}.md"), "w", encoding="utf-8") as fh:
        for f in part:
            fh.write(f"## {f['nr']}. {f['title']}\n{f['desc']}\n")
            for p in f["papers"]:
                fh.write(f"- **{p['title']}** ({p['path']}): {p['abstract']}\n")
            fh.write("\n")
    print(f"slice_{k + 1}.md: Familien {part[0]['nr']}–{part[-1]['nr']}, {sum(len(f['papers']) for f in part)} Manuskripte")
