# Ergebnis H76: Quanten-Zerfall des Vakuums der M–T-Paarung über die Gravitation

Vorab-Notiz: `Vorab_Notiz_H76_Vakuumzerfall.md`, Commit `2b47e7f` (nicht blind). Skripte `k191_vakuumzerfall.py` (Lauf 1), `k191b_lauf2.py` (Lauf 2, nicht verwertbar), `k191c_boostvolumen.py` (Lauf 3, halbanalytisch); Ausgaben `k191_out.json`, `k191b_out.json`, `k191c_out.json`.

## Ergebnisse
- **H76a bestätigt:** Der Zerfall 0 → φφ (Materie, E > 0) + χχ (Tachyonbild, E < 0) über ein Graviton ist kinematisch erlaubt. Mit nur einem Lorentz-invarianten Cutoff P² < Λ² wächst die Rate mit dem Rahmen-Cutoff L ohne Grenze. Die Verhältnisse Γ(L)/Γ(L/2) sind 7,06; 4,77; 4,23; 4,07; 4,02; 4,006; 4,002 für L = 2 … 128 (Lauf 3, Fehler < 0,1 %). Das sind alle ≥ 2, und sie laufen gegen 4: Γ ∝ L², das Volumen der Boosts auf dem Hyperboloid. Das ist die Divergenz über die Boosts von Cline, Jeon und Moore.
- **H76b bestätigt:** Mit einem Cutoff |k| < Λ in einem ausgezeichneten Rahmen ist Γ/V = c·Λ⁸/M_P⁴ mit Exponent 8,000 bzw. 7,997 und **c = 2,25·10⁻⁵** (relativer Fehler 0,12 %), für masselose Skalare als Stellvertreter.
- **H76c bestätigt:** Übertragen auf die Abschätzung von Cline et al. (deren Λ ≲ 3 MeV mit c ~ 1) verschiebt unser kleines c die Schranke um c^{−1/7} = 4,6 auf **Λ ≲ 14 MeV** (grob; Skalare statt Photonen, Faktoren der Ordnung 1 offen). Das liegt weit unter der Higgs-Skala. Ein T-Sektor, der als Lorentz-invariante Kopie bis zur Higgs-Skala reicht und nur über die Gravitation koppelt, widerspricht dem Gammastrahlen-Hintergrund.
- **H76d (Lesart, nicht geprüft):** Der nötige ausgezeichnete Rahmen kann der mitbewegte Rahmen aus H70 sein, in dem der M–T-Versatz in konformer Zeit fest ist. W2 erzeugt einen Cutoff in diesem Rahmen aber nicht selbst.

## Offenlegung
- Lauf 1 (direkte Monte-Carlo-Stichprobe) war für H76b genau, für H76a bei großem L aber zu ungenau (L = 16: 35 % Fehler, Verhältnis 2,3).
- Lauf 2 mit zehnmal mehr Stichproben half nicht: Die Gewichte sind schwer verteilt, die Fehler schrumpfen nicht (Verhältnisse 5,2 ± 1,6 und 0,96 ± 0,43). Er ist nicht verwertbar.
- Lauf 3 rechnet dieselbe Größe mit der Lorentz-Invarianz: Konfiguration im Ruhesystem des Materie-Paares, Boost-Volumen mit allen |k| < L exakt pro Richtung. Er trifft Lauf 1 bei L = 1, 2, 4 auf unter 1 % (5,773 / 5,751; 4,077 / 4,050; 1,943 / 1,940 ·10⁻⁸…⁻⁷). Das Entscheidungskriterium ist unverändert. Der Methodenwechsel kam nach Ansicht der Daten.

## Einordnung
- Die Aufhebung der Vakuumenergie in r82.1 ist klassisch (Kondensate). Ausgeschlossen ist hier nicht das Kondensat, sondern ein T-Sektor mit Lorentz-invarianten Anregungen oberhalb von etwa 10 MeV. Die Stabilität verlangt also einen **Cutoff im T-Sektor oder in der Gravitation, der einen Rahmen auszeichnet**.
- Damit taucht zum ersten Mal eine Skala auf, die nicht die Planck-Skala ist, aber nur als **Obergrenze**: Daten ≲ 14 MeV; die Natürlichkeit bei Kaplan und Sundrum ≲ 2 meV (Bruch der Gravitation unter etwa 0,1 mm). Die meV-Zahl stimmt größenordnungsmäßig mit der Abschätzung in I4 überein (Kondensat mit λ ~ 1, m ≈ 2–3 meV). Diese Übereinstimmung ist nachträglich bemerkt und nicht geprüft.
- Bei Λ = 2 meV ist Γ/V ≈ 3·10⁻¹⁷⁵ GeV⁴, praktisch null.
- Nicht erfasst: Spin-1-Photonen, die massiven Tachyonmoden aus H71 (deren Moden mit k < m sind schon ohne Gravitation tachyonisch instabil, siehe I4), Zerfälle über andere Kopplungen.

## Folgerung
Das Vakuum der M–T-Paarung ist quantenmechanisch nur stabil, wenn ein Rahmen ausgezeichnet ist und der T-Sektor (oder die Gravitation) dort bei höchstens etwa 10 MeV abgeschnitten wird. Das Modell hat mit H70 einen Kandidaten für den Rahmen, aber keinen Wert für den Cutoff. OP5 bleibt offen.
