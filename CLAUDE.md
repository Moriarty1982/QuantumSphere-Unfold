# CLAUDE.md

@AGENTS.md

Alle Arbeitsregeln, der Rundenstand und die Abläufe stehen in `AGENTS.md` und `llm/anleitungen/`. Sie gelten für jedes
Modell. Änderungen an Regeln oder am Stand gehören dorthin, nicht hierher.

## Nur für Claude
- Die Projekt-Skills unter `.claude/skills/` (`weitermachen`, `qs-sitzung-uebergeben`, `qs-hypothese-testen`,
  `qs-wiki-nachziehen`, `qsc-runde-einbauen`, `op5-vergleichsmodell-rechnen`, `quantum-sphaera`, `zenodo-release`) sind
  nur Hüllen: sie verweisen auf die gleichnamige Anleitung in `llm/anleitungen/`. Abläufe dort ändern, nicht im Skill.
  Der Skill `quantum-sphaera` stellt `qs.py` bereit.
- Merges auf GitHub nur nach ausdrücklicher Freigabe im Chat.
