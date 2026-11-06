---
name: quantum-sphaera
description: Arbeiten am Quantum-Sphaera-Dokumentkomplex — dem 1014-seitigen Companion-Monolithen und seinen beiden Quellpapieren (Hauptpaper, Riemann-Arbeit). Diesen Skill laden, sobald eine neue Runde rNN angehängt, ein Querverweis oder eine Theoremnummer geprüft, die Guard-/Claim-Disziplin kontrolliert, ein Release-Kandidat (RC) gebaut, ein SHA256-Manifest oder Zenodo-Metadaten erzeugt oder im Companion navigiert werden soll. Auch laden bei den Stichworten Sphaera, Companion, Millennium-Matrix, Heisenberg-Compensator, QAM/MML/MMA, OP1–OP5, C4/C5/C6, T2, Guard-Vektor, Ledger, Concept-DOI.
---

# quantum-sphaera

Dieser Skill ist nur eine Hülle für Claude. **Der Ablauf steht modellunabhängig in `llm/anleitungen/qs-werkzeug.md`**
(auf GitHub `notes/anleitungen/qs-werkzeug.md`); dieselbe Datei nutzen ChatGPT, Codex und andere Modelle.

1. `llm/anleitungen/qs-werkzeug.md` vollständig lesen und danach arbeiten. Bei Abweichungen gilt die Anleitung.
2. Regeln und Stand aus `AGENTS.md` (über `CLAUDE.md` eingebunden); Stand der letzten Sitzung in `llm/Uebergabe.md`.
3. Hier keine eigenen Regeln ergänzen: Änderungen am Ablauf gehören in die Anleitung.

Das Werkzeug liegt in diesem Skill-Ordner: `tools/qs.py` (Rundengerüst `assets/round_template.tex`). Es ist ein
normales Python-Skript und wird von allen Modellen über den Repo-Pfad `.claude/skills/quantum-sphaera/tools/qs.py` benutzt.
