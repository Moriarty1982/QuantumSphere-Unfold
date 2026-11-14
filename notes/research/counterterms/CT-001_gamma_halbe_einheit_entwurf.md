# Entwurf CT-001: Phaseneinheit des Flusses ΔΦ = γ_M/2

**Stand:** 14. November 2026, Entwurf. Autorenwahl: „Einheit bei γ/2“ als erster echter Platzhalter der
Counterterm-Registry. Der Eintrag wird registriert, sobald Phase 1 (Schema, Validator, Weitergabe) gemergt ist. Bis
dahin ist dies nur eine Beschreibung. Feldnamen folgen der Arbeitsanweisung und werden an das tatsächliche Schema
angepasst.

## Was gesetzt ist
Der Fluss vom Qubit-Oktanten zu den geladenen Leptonen ist ΔΦ = π/4 − 3θ_e. Nach dem Scan vom 13.11. gilt
ΔΦ ≈ γ_M/2, mit γ_M = 0,237533 aus der Zählregel des Materie-Frames (alle Spins, Gewicht 2).

In der Holonomie-Fluss-Paarung ist der Flusseigenwert γ·m in einer Flächeneinheit. Als Phase gelesen braucht er eine
Phase pro Einheitsfluss κ:

ΔΦ = κ · γ_M · s,

wobei s der Spinwert und κ die Phase pro Flächeneinheit ist. **γ/2 entsteht nur mit einer bestimmten Konventionswahl**
(`op3_flux_two_thirds_2026_11_13.md`, Nachtrag Holonomie-Fluss-Paarung):

| Flächeneinheit | Spinwert s | Phase | gegen γ/2 |
|---|---|---|---|
| 8πGħ = 1 | \|m\| = 1/2 | 0,11877 | **= γ/2 (gewählt)** |
| 8πGħ = 1 | √(j(j+1)) | 0,2057 | 1,73-fach |
| Għ = 1 | √(j(j+1)) (Konvention r10) | 5,170 | 43,5-fach |

## Vorgesehene Felder
- **id / version / status:** CT-001, 1.0.0, `phenomenological_placeholder`.
- **target_sector:** Lepton-Fluss (Koide-Phase), Frame M (Materie).
- **Basisgröße:** der Fluss ΔΦ zwischen Qubit-Oktant und geladenen Leptonen. Es ist kein Lagrange-Term, sondern eine
  Auslesegröße; im Schema als Auslese-Gegenterm führen.
- **Kompensationsfunktion:** δ_1 = κ · γ_M · s mit κ = 1 rad pro 8πGħ und s = |m| = 1/2.
- **Parameter:** diskrete Konventionswahl (Flächeneinheit, Spinwert), keine stetige Anpassung. Rolle: Auswahl aus
  einer endlichen Menge.
- **Herkunft (`fitted_on`):** ausgewählt durch einen Scan mit 154 Versuchen (ein Treffer, 0,34 zufällig erwartet).
  Ziel war 3θ_e = 2/3 rad gegen die bekannten Massen m_e = 0,51099895, m_μ = 105,6583755 und m_τ = 1776,93 ± 0,09 MeV
  (PDG 2024).
- **Abhängige Aussagen:** H102 (m_τ = 1777,134 MeV) und die Lesart „Fluss 2/3 rad = π/4 − γ/2“ im Auswahlprinzip.
- **Blindheit:** H102 ist nur gegen PDG-Ausgaben nach dem 13.11.2026 blind. Ein unveränderter Mittelwert wäre
  derselbe Datenpunkt wie in `fitted_on` und dürfte nicht als Bestätigung zählen. Das ist mit der Vorab-Notiz von H102
  zu klären, sobald neue Daten vorliegen.
- **Offene Guards:**
  - GUARD-CT001-EINHEIT-FREI: Die Einheit κ ist nicht hergeleitet.
  - GUARD-CT001-KONVENTION-R10: Die eigene Flächenkonvention des Companion (r10) gibt 43,5 · γ/2.
  - GUARD-CT001-NACHTRAEGLICH: Die Beziehung ist ein Scan-Treffer mit bekanntem m_τ.
- **structural_replacement:** Ziel ist eine Herleitung von κ und s aus dem Companion. Der Rest ist
  Δ_1 = F_1^struct − δ_1. **Bekannte Spannung:** Die Konvention von r10 entspricht heute Δ_1 = 42,5 · γ/2, also einer
  Abweichung weit über jeder Toleranz. Eine strukturelle Ersetzung muss erklären, warum die Einheit beim Fluss eine
  andere sein soll als bei der Fläche.

## Offen
- Ob die Registry diskrete Konventionswahlen mit Versuchszahl (154) als Parameterart führen kann, wird mit Phase 1
  abgestimmt.

## Schritt 1 nach der Platzhalter-Methode (14.11.2026, Erkundung, nicht blind)
Skript `../ct001_shrink_2026_11_14.py`, Ausgabe `..._out.txt`. Autor: „kannst du es mal versuchen jetzt mit der neuen
methode?“

**(a) Was genau gesetzt ist.** Rückwärts aus den Massen (PDG 2024) folgen ΔΦ = π/4 − 3θ_e = 0,118724 und
κ·s = ΔΦ/γ_M = **0,49982**. Das 1σ-Band aus m_τ ist [0,49974; 0,49990]. Gesetzt ist also die Zahl 1/2. Sie liegt
2,3σ neben dem Datenwert; das ist dieselbe Spannung wie bei H102, keine neue Information.

**(b) Die Phase kommt nicht aus dem Qubit selbst.** Die Bargmann-Phase eines gleichseitigen Qubit-Tripels ist Ω/2.
Bei ρ² = 0,499997 weicht sie nur um 10⁻⁵ von π/4 ab. Das Tripel kann ΔΦ = 0,119 also nicht selbst erzeugen. ΔΦ ist
ein **äußerer Fluss**, passend zu „nur ein Fluss erhält Koide“ (Auswahlprinzip).

**(c) Herleitungsbaustein für die 1/2.** Liest man den äußeren Fluss als Aharonov-Bohm- bzw. Dirac-Phase eines
Monopolfelds, ist die Phase q·g·Ω_ext mit q·g ∈ ℤ/2. Der kleinste Wert q·g = 1/2 gibt **κ·s = 1/2 pro Steradiant**.
Das ist dieselbe 1/2 wie bei der Berry-Phase eines Spin-1/2 (m = 1/2), und es braucht keine Flächeneinheit. Die drei
Konventionen der Tabelle oben spielen dann keine Rolle mehr.

**Aufteilung des Platzhalters**
- **CT-001 (Einheit κ·s):** Status `partially_constrained`. Die 1/2 folgt aus der minimalen Dirac-Quantisierung,
  unter der neuen Annahme, dass ΔΦ eine Monopolphase ist. Neuer Guard: GUARD-CT001-MONOPOL (Existenz des Monopolflusses
  nicht hergeleitet). Δ = 0,5 − 0,49982 = 1,8·10⁻⁴, also 2,3σ. Nach der Methode wird das **nicht still übernommen**,
  sondern bleibt als Spannung stehen.
- **Neuer Restplatzhalter CT-002 (Raumwinkel):** Ω_ext = 2ΔΦ = 0,237448 sr gegen γ_M = 0,237533. Die Frage ist
  jetzt eng: Warum ist der äußere Raumwinkel gleich der Barbero-Immirzi-Zahl der Zählregel? `fitted_on` wie bei
  CT-001: Scan mit 154 Versuchen, m_τ PDG 2024.
- **Spannung zu r10 verschoben:** Dort ist γ ein Flächenverhältnis (43,5-fach), hier wäre γ ein Winkel. Die Spannung
  wird nicht aufgelöst, aber anders gestellt: Ist γ_M im Companion auch als Winkel lesbar?

**Bewertung.** Die Methode hat den Platzhalter **verkleinert, nicht beseitigt**. Aus „Einheit frei unter drei
Konventionen“ wurde „minimale Dirac-Phase (Annahme) und Raumwinkel = γ_M (offen)“. Hergeleitet ist nichts. Jeder
Schritt ist nachträglich, mit bekanntem m_τ. OP3/OP4 bleiben offen, H102 ist unberührt.

## Schritt 2: Fläche gegen Winkel am Kreissektor (14.11.2026, Erkundung, nicht blind)
Hinweis des Autors: „Es könnte was damit zu tun haben, dass wir einmal eine Kreisfläche im Verhältnis zur Bogenlänge
und einmal den eingeschlossenen Winkel messen.“ Skript `../ct001_sector_reading_2026_11_14.py`, Ausgabe `..._out.txt`.

**Geometrie.** Ein Kreissektor mit Öffnungswinkel θ und Radius r hat die Fläche A = r²θ/2 und den Bogen s = rθ. Also
gilt A/s = r/2 und A/r² = θ/2. Die **½ ist die Sektorformel**, keine Konvention.

**Lesart.** Der Flächenbeitrag einer Punktierung aus r10, A_j = 8πγ a(j) ℓ_P², ist die Fläche eines Sektors mit
Öffnungswinkel γ. Sein Radius ist r_j² = 2A_j/γ = 16π a(j) ℓ_P², **unabhängig von γ**. Dieselbe Fläche lässt sich
dreimal messen:

| Messweise | Wert (j = 1/2) | Abhängig von |
|---|---|---|
| (i) relativ zum eigenen Kreis, A/r² | γ/2 = 0,118766 | nichts (gleich für alle j) |
| (ii) in Einheiten 8πGħ | γ a(j) = 0,2057 (√3-fach) | j |
| (iii) in Einheiten Għ (r10) | 8πγ a(j) = 5,170 (43,5-fach) | j und Einheiten |

Damit sind alle drei Zeilen der Konventionstabelle **ein und derselbe Sektor, verschieden gemessen**. Die Faktoren
1,73 = 2a(½) = √3 und 43,5 = 16π a(½) = 8π√3 sind die Umrechnungen. Ehrlich gesagt ist diese Übereinstimmung teilweise
Konstruktion: Die Tabelle ist aus denselben Formeln entstanden. Neu ist die Ordnung, nicht die Zahlen.

**Was das für CT-001 bedeutet.**
- Nur die Messweise (i) ist frei von Einheit und Spin. Für eine **Phase**, also eine dimensionslose Größe, ist sie die
  natürliche Wahl. Es ist dieselbe Regel wie bei der Bargmann-/Berry-Phase (Raumwinkel Ω = A/R²), die im Projekt
  schon π/4 liefert.
- Die ½ braucht damit weder die Wahl |m| = 1/2 noch eine minimale Dirac-Ladung (Schritt 1). Sie folgt aus der
  Sektorgeometrie, für jedes j.
- **CT-001 (Einheit):** Vorschlag `structurally_matched` unter dem Guard „Phase = normierte Sektorfläche“
  (GUARD-CT001-SEKTORNORM), der als Regel im Projekt schon gilt. Δ_struct = 0 in der Lesart. Die 2,3σ-Datenspannung
  (verlangt 0,49982) betrifft H102, nicht die Einheit.
- **CT-002 (Rest) geschärft:** γ_M ist der **Öffnungswinkel des Punktierungssektors**. Warum gerade γ_M (Zählregel M)
  und warum dieser Sektor den Lepton-Fluss trägt, bleibt offen.
- **Spannung zu r10, jetzt benannt:** Die Zählregel von r10.1 (Unruh, E·β = 2πγ a(j)) misst die Fläche in der Weise
  (ii), also γ a(j) pro Radiant. Der Lepton-Fluss verlangt die Weise (i). Beide messen denselben Sektor, offen ist,
  welche Messweise für welche Größe gilt.

**Bewertung.** Der Hinweis trägt. Der Konventionsstreit „½, 1,73 oder 43,5“ löst sich als drei Messweisen eines
Sektors auf, und die einheitenfreie liefert γ/2. Hergeleitet ist damit die **Messweise** (unter dem genannten Guard),
nicht die Identifikation des Winkels mit γ_M. Alles ist nachträglich. OP3/OP4 bleiben offen, H102 ist unberührt.
