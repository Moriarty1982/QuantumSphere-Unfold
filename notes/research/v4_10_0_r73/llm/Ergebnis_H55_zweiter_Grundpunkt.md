# Ergebnis H55: Vier versteckte Bedingungen an 6-Jets auch an einem zweiten Grundpunkt

Vorab-Notiz: `Vorab_Notiz_H55_zweiter_Grundpunkt.md`, lokaler Commit 04a3950 (3. November 2026), vor der Rechnung.
Rechnung: `k143_h55.py`, Protokoll `k143_log_H55.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Der Punkt

Neuer 4-Jet c₄' = c₄(rep) + α·z₄ aus dem Kern von F³₅ (Seed 55), Abstand 50 % von c₄(rep). Er ist fortsetzbar:
ε_ref' = κ(F⁴₅) = 5,0e-14. Positivkontrolle (Störung 1e-3, Seed 56): κ = 5,3e-4, also 1e10-fach darüber.

## Messwerte

| Größe | Vorhersage / Schranke | Messwert |
|---|---|---|
| κ(F₇) | ≤ 100·ε_ref' = 5,0e-12 | 3,9e-12 |
| P₅₆(F₇) | 852 | 852 (Lücken 6e7, 1e10) |
| P₅₆(F₈) | 848 | **848** (Lücken 5e5, 4e4) |
| kleinster Nicht-Null-Wert F₈ / η | ≥ 100 | 2,72e-6 / 3,8e-9 = 710 |
| kleinster gezählter Wert F₈ ohne c₅, c₆ / η_red | ≥ 100 | 1,0e-9 / 7,2e-13 = 1390 |

## Ergebnis: bestätigt

Am zweiten Grundpunkt gilt dasselbe wie am ersten: Mit den Gleichungen bis Grad 6 hat die Faser der 6-Jets die
Dimension des Symbols, mit den Gleichungen vom Grad 7 kommen genau 4 Bedingungen an 6-Jets hinzu.

## Lesart und Einschränkung

- Die 4 versteckten Bedingungen sind nicht an den reparierten Punkt gebunden. Zusammen mit H^{5,2}(g') = 4 heißt das:
  Das geeichte System ist bei Ordnung 6 nicht formal integrabel. Die vier Spencer-Klassen werden tatsächlich
  angenommen, nicht nur an einem Sonderpunkt.
- **Einschränkung, nachträglich bemerkt:** Die Matrix F₈ ohne die Spalten von c₅ und c₆ hängt nur vom Jet bis Grad 2 ab.
  Sie ist an beiden Punkten identisch (gleiche Werte 1,93e-7, 1,11e-7, 1,0e-9). Neue Information trägt nur der Rang des
  vollen F₈ (7957 bei geändertem c₄). Der Test prüft also, ob die Bedingungen bei geändertem 4-Jet bestehen bleiben,
  nicht bei geändertem Jet bis Grad 3.
- Bestimmt sind die vier Bedingungen damit nicht. Das ist der nächste Schritt; danach Cartan-Test des erweiterten
  Systems.
