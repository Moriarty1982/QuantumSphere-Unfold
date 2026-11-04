# Übergabe: Stand der letzten Sitzung

**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.** Sie ist der Einstiegspunkt für die nächste Sitzung, egal mit welchem Modell. Die Geschichte steht in `AGENTS.md` (Rundentabelle), in der Kernkarte und in den Runden.

## Stand vom 4. November 2026, 23:20 (Claude, Sitzung zu OP5)
- **Gemergt:** r77 (PR #60, 1be5dc1), r78 (PR #61, 9e7c3d6), r79 (PR #63, 1d8c9b1). Inzwischen auch PR #62 (Lean MMA/QAM, c3e2652, vom Autor).
- **PR #64 gemergt als 42d8397** (vormals offen, (`research/v4.10-r80-hintergrund`): Runde r80 = Fierz-Erkundung (k168), **H68 widerlegt** (k169: Hintergrund A, h nicht aus Yang–Mills/Klein–Gordon mit Spinorquellen), **Abschluss des Vergleichsmodell-Zweigs r71–r80** (Autorentscheidung 4.11.); dazu die Bestandsaufnahme der Wirkungsansätze. Wiki im PR. Lokal eingebaut (3d72d40): 1315 Seiten, 3947 Labels, Overfull 45, harte Werte 0, Guard-Linter 0. AGENTS-Zeile und Kernkarte nachgezogen.)
- **Weitere offene PRs (nicht OP5, nicht angefasst):** #59 (Short paper draft), #51 (AGENTS.md).
- **Zuletzt vergebene Hypothese:** H68. Nächste freie Nummer H69.
- **Branches, die weg können** (Löschen über den Proxy gesperrt): `rechnen/h59`, `rechnen/h65`, `rechnen/h67`, `rechnen/hintergrund` (in r80 aufgegangen).

## Richtungswechsel (Autorentscheidung 4.11.)
Der OP5-Vergleichsmodell-Zweig ist geschlossen. Keine weiteren Feinheiten daran (Lorentz-Wirkung auf die 6 Moden, zweiter Grundpunkt) ohne eigene Dynamik. Es geht eine Ebene höher: zur gemeinsamen Wirkung, die OP1–OP5 gleichermaßen fehlt.

## Nächster Schritt
**Stand der Entscheidungen:** 1 entschieden (Variante B: Koframe eigenes Feld, E ≈ C[Ψ] später als Test); 2 entschieden (R im Frame M als Hauptlinie, K = R + Gleichungen aus Im S parallel mitrechnen, Prüfung auf exakte Schließung); 3 entschieden (Einstein–Cartan ohne Λ, vorerst ein System; Idee I1 zurückgestellt); 4 entschieden (Dixon-Ablage mit U(1) aus L_{e₇}, sektorweise nach r48, Buchführung in QAM); 5 offen, werden einzeln mit dem Autor durchgegangen.

`llm/Bestandsaufnahme_Wirkungsansaetze.md` mit dem Autor durchgehen und die fünf offenen Entscheidungen in Abschnitt 5 klären (Koframe eigenes Feld oder Funktion von Ψ; komplexe/reelle Wirkung; Gravitationsterm; Eichgruppe; P_C7 exakt oder dynamisch). Erst danach die kleinste Wirkung nach (W1)–(W8) aufschreiben und ihre Euler–Lagrange-Gleichungen sowie Bianchi- und Ward-Identitäten symbolisch prüfen. Tests mit Kriterium nur mit Vorab-Notiz.

## Danach
- Wirkung auf einen einfachen symmetrischen Ansatz (homogen, isotrop) reduzieren und prüfen, ob der Vakuumterm frei bleibt (W7).
- Offene Vorhersagen H15, H42, H46 warten auf Daten.

## Pflichten in jeder Sitzung
- Auslöser in `llm/Zurueckgestellte_Ideen.md` prüfen (beim Start und wenn ein Ansatz scheitert).
- Zuerst `AGENTS.md` lesen, dann die einschlägige Anleitung mit dem Abschnitt „Bereits beantwortet“, dann diese Datei.
- Vorwissen-Pflicht und Vorab-Notizen beachten. Merges nur nach „PR NN mergen“.
- Wiki im selben PR mitziehen.
- Am Ende diese Datei aktualisieren.
