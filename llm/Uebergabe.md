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
Alle fünf Entscheidungen sind getroffen (Bestandsaufnahme, Abschnitt „Entscheidungen des Autors“). Die Wirkung W1 steht in `llm/Wirkung_W1_Dixon_U1.md`. Erster Befund (k170, Erkundung): Die K-Lesart ist bei symmetrischer Kinetik leer. Nicht symmetrisiert erzwingt sie mit unabhängiger Verbindung j^a = 0, also Ψ = 0 in einem Frame. Die Schließung kommt damit nicht dynamisch, die Chiralität bleibt Eingabe.

Als Nächstes:
1. die Euler–Lagrange-Gleichungen der reellen W1 symbolisch aufstellen (Einstein–Cartan mit algebraischer Torsion, Maxwell mit Quelle, Weyl je Sektor), dazu Bianchi- und Ward-Identität prüfen;
2. der kleine Test: Erfüllt C_ch die Bedingung Tr(M₁₆ P_C7) ≡ 0 mod HC?
3. Autorfrage offen: die M–T-Lücke in k170 (Komponenten mit negativer Dichte), nur nach Konvention F.

Die neuen lokalen Commits ab c741b00 sind noch nicht auf GitHub. Sie kommen mit der nächsten Runde (r81) per ours-Merge nach.

## Danach
- Wirkung auf einen einfachen symmetrischen Ansatz (homogen, isotrop) reduzieren und prüfen, ob der Vakuumterm frei bleibt (W7).
- Offene Vorhersagen H15, H42, H46 warten auf Daten.

## Pflichten in jeder Sitzung
- Auslöser in `llm/Zurueckgestellte_Ideen.md` prüfen (beim Start und wenn ein Ansatz scheitert).
- Zuerst `AGENTS.md` lesen, dann die einschlägige Anleitung mit dem Abschnitt „Bereits beantwortet“, dann diese Datei.
- Vorwissen-Pflicht und Vorab-Notizen beachten. Merges nur nach „PR NN mergen“.
- Wiki im selben PR mitziehen.
- Am Ende diese Datei aktualisieren.
