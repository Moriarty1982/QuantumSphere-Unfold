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

Stand 4.11., ca. 23:55: W1 korrigiert. Ψ ist der ganze Raum C⊗ℍ⊗𝕆 mit 16 Weyl-Zuständen, C_ch steckt in den Kopplungen, U(1)_J ist anomaliefrei (k171). Die Weyl-Form des K-Befunds gilt (k172). Die Torsion gibt −(3/16)κ j² mit dem Gesamtstrom (k173, Kontrolle Hehl–Datta). Die Feldgleichungen 1–3 stehen in der W1-Notiz. W1 erzeugt keinen Vakuumterm (W7 braucht den Skalarsektor).

Als Nächstes:
1. die Feldgleichungen symbolisch mit sympy aus der Wirkung ableiten und die Bianchi- und Ward-Identität explizit prüfen;
2. den Skalar- bzw. Higgs-Sektor nach r44 dazunehmen; erst dort kann ein Vakuumterm entstehen;
3. P_C7 bleibt vorerst offen (Autor, 5.11.). C_ch ist der HC (`llm/Notiz_mod_HC_und_P_C7.md`). Die Lesart „mod HC = chinesischer Restsatz über Primzahl-Plätze“ steht als I2 in `llm/Zurueckgestellte_Ideen.md`; sie wird geprüft, sobald P_C7 gebraucht wird.
4. M–T-Lücke (k174, `llm/Erkundung_MT_Luecke.md`): Mit Tachyon-Anteil nach Konvention F verlangt K nur j_M + j_T = 0, also keinen Querstrom zur M–T-Achse, und die Torsion verschwindet. Offen: Ist T ein eigenes Feld? Was bedeutet das umgekehrte Kinetikvorzeichen (Energie)? Folgt eine Vorhersage? Autor (5.11.): Frames müssen nicht synchron sein (Versatz δ, Querstrom dann antiperiodisch, Periode 2δ), und δ könnte durch die kosmische Expansion festgelegt sein; das ist der Ursprung von OP5 (`thm:expansion`). **H69 bestätigt (k175):** Ein versetztes M–T-Paar (Δω·δ = π) löst W1 mit Re- und Im-Gleichungen im flachen Raum ohne Nettostrom und ohne Nettoenergie-Impuls (Residuen 1e-15). **H70 (k176):** Nur ein in konformer Zeit fester Versatz (C2, kosmisch δ ∝ a) erhält das Paar; δ = 1/H und die Form aus `thm:expansion` verletzen die Weyl-Gleichung des T-Bildes und erzeugen einen homogenen, nicht Λ-artigen Rest (H70a bestätigt, H70b widerlegt). Im konsistenten Fall kein Vakuumterm. Zuletzt vergebene Hypothese: H70. **Nachtrag k177:** Die neutrale Paarung ist die Photon-Mischung P (½, ½); mit Materie-Gewichten bleibt ein homogener, spurfreier, strahlungsartiger Rest ∝ |b| = 1/γ. Masselose Felder können nie Λ-artig beitragen (spurfrei). **Kandidat H71** (massives M–T-Paar, gekoppelt über die Massenterme aus r44) ist **zurückgestellt**: Die r44-Lesart „Masse koppelt M und T“ verwechselt die Zeitumkehr T mit der Tachyon-Abbildung; r51 hat das für r41–r49 korrigiert, aber r44 nicht genannt (Nachtrag 4 in `llm/Erkundung_MT_Luecke.md`, Kandidat für eine Korrektur in r81). **Zuerst eine Frame-Prüfung** auf dem Dublett: Welche der Involutionen R = σ_y, T = σ_z, J_B = σ_x macht γ → −γ, tauscht p₊ ↔ p₋ bzw. steckt im Massenterm? **H71 (k179):** Massive Partner: Antiteilchen bzw. gekoppelter Spiegelpartner (s = +1) normal massiv, Tachyonbild (s = −1) tachyonisch (ω² = k² − m², raumartiger Strom); keine Variante erfüllt die K-Bilanz; kein Λ-artiger Beitrag aus einzelnen Moden. Ungekoppelter Spiegelsektor (Autoridee Spiegelteilchen) wäre dunkle-Materie-artig. Zuletzt vergebene Hypothese: H71. **Offene Frage für H72:** Kann eine Überlagerung tachyonischer Moden (V2) T ∝ η erzeugen (Druck = −Dichte, isotrop)? Das wäre ein Vakuumterm aus der Struktur. **H72 (k180):** Ein Λ-artiger Term (p = −ρ, isotrop) entsteht klassisch aus einem Gas tachyonischer Moden beider Normvorzeichen auf mindestens zwei Impulsschalen; Höhe und Vorzeichen frei (Gewichtsverhältnis), durch Frame-Gewichte bei einem Impuls nicht festgelegt (a, b bestätigt; c widerlegt). Zuletzt vergebene Hypothese: H72. **H73 widerlegt (k181):** Bezugszustände (M in Ruhe, T an der Schwelle) mit Materie-Gewichten geben w = −β_sym²/3 = −0,10 (parameterfrei, normierungsunabhängig). Nachträglich, nicht vorregistriert: Im Tachyon-Frame gelesen w = −1/(3x) = −1,105; exakt −1 für β = 1/√3. Nur als Anlass für eine neue Vorab-Notiz mit Begründung der Frame-Wahl. Zuletzt vergebene Hypothese: H73. **k182 (Autorhinweis Grenzwert):** Bei gemeinsamer Rapidität η für Moden und Gewichte ist die Mischung im Materie-Frame exakt druckloser Staub (w = 0, ρ = m/cosh η) für jedes η; im Tachyon-Frame ρ = 0, reine Spannung; Summe w = −⅓. Kein Λ; H73 war ein Artefakt inkonsistenter Rapiditäten (`llm/Erkundung_Rapiditaetsfamilie.md`). **Autor-Umdeutung I3:** Λ nicht als eigener Gegenstand, sondern als Folge der Dunkle-Materie-Rechnung (`llm/Zurueckgestellte_Ideen.md`, I3); Kandidat H74 dort beschrieben. **Weitere Fragen:** Rückwirkung (Paar als Quelle der FRW-Gleichungen, nicht nur Testfeld), Zulässigkeit von s_T = −1 (Energie, Stabilität), und was die Amplituden bzw. Δω festlegt.

Auf GitHub: PR #65 (`research/v4.10-w1-wirkung`) mit allen Notizen bis b1a9f3c, offen, Merge nur nach Freigabe.

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
