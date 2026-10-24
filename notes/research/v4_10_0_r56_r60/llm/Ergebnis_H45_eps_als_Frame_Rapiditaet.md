# Ergebnis H45: ε = Rapidität des Materie-Frames ist verträglich und legt θ₂₃ scharf fest, δ nicht

Vorab-Notiz: `Vorab_Notiz_H45_eps_als_Frame_Rapiditaet.md`, Commit bfde03d (2026-10-24 22:53 MESZ), vor der Rechnung bei diesen Werten. **Nicht blind:** die Trefferfenster
(ε ≈ 0.62–0.64) waren aus r59 bekannt. Skript `k100_test_h45.py`, Ausgabe `k100_out.txt`.

## Herleitungsidee

D = exp(εW) ist eine hyperbolische (boost-artige) Abbildung der Generationen-Plätze; ihr natürlicher Parameter ist eine Rapidität. Die einzige Rapidität der Theorie ist die
des Materie-Frames, β_sym = tanh η, γ_L = cosh 2η (Konvention F). Lesart: ε = η.

## Ergebnisse

| | ε | Treffer | sin²θ₂₃ | \|sin δ\| |
|---|---|---|---|---|
| Variante A | artanh(β_sym) = 0.6174 | 120 | [0.4913, 0.4975] | [0.169, 0.998] |
| Variante B | artanh(β_sym) = 0.6174 | 1 104 | [0.4913, 0.4975] | [0.167, 0.998] |
| A und B | artanh(1/√3) = 0.6585 (Hopf) | 0 | – | – |

- **H45a bestätigt** (Treffer beim gemessenen β_sym; nur Verträglichkeit, weil nicht blind).
- **H45b widerlegt**: θ₂₃ ist scharf (Spannweite 0.006), δ nicht (Spannweite 0.83). Das Kriterium verlangte beides.
- **H45c:** beim Hopf-Wert keine Treffer.

## Einordnung

1. **Erstmals eine Lesart, in der ε aus der Struktur kommt** und die Daten trifft: Die Maske ist die Abweichung der triality-kovarianten Chiralität, mit der Stärke der
   Frame-Rapidität. Dass das gemessene β_sym passt und der Hopf-Wert nicht, ist ein Unterschied, den die Daten treffen.
2. **Neu und vorher unbekannt:** Bei festem ε = artanh(β_sym) liegt sin²θ₂₃ in [0.491, 0.498], also nahe maximaler Mischung, knapp im unteren Oktanten, in beiden Varianten
   gleich. Das ist eine scharfe Aussage über künftige Daten und schärfer als H42 (≤ 0.54). Nach dem Kriterium von H45 entsteht daraus keine Vorhersage H46, weil δ frei
   bleibt; eine Vorhersage nur für θ₂₃ müsste eigens festgelegt werden (Vorschlag).
3. **Einschränkungen:** nicht blind (Fenster bekannt); β_sym selbst ist eingesetzt (aus γ_BI/γ_string, OP1 offen); die Lesart ε = η ist eine Idee, keine Herleitung aus einer
   Wirkung.
