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
