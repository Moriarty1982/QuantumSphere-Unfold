# Übergabe: Stand der letzten Sitzung

**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.** Sie ist der Einstiegspunkt für die nächste Sitzung, egal mit welchem Modell. Die Geschichte steht in `AGENTS.md` (Rundentabelle), in der Kernkarte und in den Runden.

## Stand vom 4. November 2026, 22:30 (Claude, Sitzung zu OP5)
- **Gemergt:**
  - r77: PR #60, 1be5dc1;
  - r78: PR #61, 9e7c3d6;
  - r79: PR #63, 1d8c9b1.
- **Zuletzt vergebene Hypothese:** H67. Die nächste freie Nummer ist H68.
- **Laufende Branches auf GitHub:**
  - `rechnen/hintergrund` (29b69ad): Erkundung Fierz/polare Größen des Hintergrunds (`k168_fierz.py`, `Erkundung_Fierz_Hintergrund.md`); noch in keiner Runde;
  - `rechnen/h59`, `rechnen/h65`, `rechnen/h67`: erledigt und in r77–r79 eingegangen. Sie können weg; das Löschen über den Proxy ist gesperrt.
- **Offene PRs:** keine.

## Nächster Schritt
**H68 vorab festlegen**, mit dem Abschnitt „Vorwissen geprüft“, **und rechnen.** Gefragt ist, ob der vorgegebene Hintergrund kovariante Feldgleichungen erfüllt, deren Quellen die drei Spinorblöcke sind:
- Yang–Mills für A = M(t) dφ, Farbtyp λ₄, λ₆, mit dem Farbstrom Ψ̄γ^μ(T⊗1)Ψ als Quelle;
- Yukawa bzw. Klein–Gordon für h(t, r) mit der Quelle Ψ̄(Y⊗β)Ψ;
- jeweils mit einer einzigen Kopplungskonstanten.

Grundlage ist die Fierz-Erkundung: β ≈ 0, Hubble-Strömung v = ±x/t, Spins entlang φ̂ = e_y. Werkzeuge: k127 (R punktweise), k130 (Fortsetzung zu anderen Punkten), k164 (Rb mit Hintergrund als Eingabe).

## Danach
- Runde r80 mit H68 und der Fierz-Erkundung, dazu Wiki und PR. Merge nur nach Freigabe.
- Offen bleiben die Lorentz-Wirkung auf die 6 Moden und ein zweiter Grundpunkt.

## Pflichten in jeder Sitzung
- Zuerst `AGENTS.md` lesen, dann die einschlägige Anleitung mit dem Abschnitt „Bereits beantwortet“, dann diese Datei.
- Vorwissen-Pflicht und Vorab-Notizen beachten. Merges nur nach „PR NN mergen“.
- Wiki im selben PR mitziehen.
- Am Ende diese Datei aktualisieren.
