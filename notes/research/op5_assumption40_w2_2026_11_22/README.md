# Annahme (40) aus W2: nur der skalare Kanal, ohne gerichteten Kontrast (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Die Gleichsetzung δJ_OP5 = δ𝒥_h folgt aus W2 genau dann, wenn das skalare OP5-Vergleichsfeld der Radialmodus η
des Higgs-Dubletts ist; dann ist sie für den skalaren Kanal exakt (Quelle 𝒥_h, Normierung durch den kinetischen Faktor), verlangt aber
c_h = 1 statt der gesetzten 1/2 und lässt im minimalen W2 weder einen Einstein-Kanal (g₀ = 0) noch den gerichteten massiven Vermittler
(g_m = 0) zu. Der gerichtete Kontrast des OP5-Falls hat in W2 kein Gegenstück. **Nach dem vorab festgelegten Raster: teilweise herleitbar.**

Auftrag des Autors: „lass uns annahme 40 untersuchen“. Verfahren vorab: `Methoden_Notiz.md` (Commit a9b61787). Skript `assumption40_w2.wl`,
Ausgabe `run/assumption40_w2.txt`, Wolfram exakt. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) Radialmodus in W2 | h_W = v + η mit |Φ| = h_W: 2(∂_t² − Δ)η + 4μ²η = 𝒥_h, also m_H² = 2μ², kinetischer Faktor Z_W = 2. Die Higgsquelle 𝒥_h ist die Quelle von η mit festem Koeffizienten. |
| (2) Mischungen | minimal: keine lineare η–Metrik-Mischung im Vakuum (V′(v) = 0); mit ξR|Φ|²: Mischung ∝ ξv. Kopplung an das Z-Boson quadratisch in Z: keine lineare Mischung mit einem massiven Vektor. |
| (3) Koeffizientenvergleich | OP5-Skalar = W2-Modus ⇔ c_h² = 1, Z = 2 − 3g₀²/2, Ω² = 2m_H²/Z; minimal g₀ = 0, Z = 2, Ω = m_H. Die gesetzten Daten (Z = 1, c_h² = 1/2, g₀² = 3/100) geben ungleiche Koeffizienten von q (109/200) und −x (209/200), also keinen Lorentz-invarianten Skalar. |
| (4) Gerichteter Kanal | Der Kontrast lebt im Vermittler-Sektor g_m²N_m/d_m mit r_m = 1/2. W2 hat keinen linear an η gekoppelten massiven Vermittler (g_m = 0), und ein Lorentz-invariantes Feld hätte r_m = 1. |

## Lesart
- Was an die Stelle von (40) tritt: Die Gleichsetzung selbst ist in W2 begründet, sobald das Vergleichsfeld der Higgs-Radialmodus ist. Die
  tragende Annahme des gerichteten Kontrasts ist dann eine andere: **ein unterluminaler, gerichtet gekoppelter massiver Vermittler mit
  Kopplung g_m an den Higgsradius**, den W2 nicht enthält, sowie die nicht Lorentz-invarianten Geschwindigkeiten c_h² = r_m = 1/2.
- Der gewöhnliche Teil des OP5-Falls (kompakter Außenbeitrag, r32.3) bleibt unberührt; er braucht (40) nicht.
- Ein Einstein-Kanal g₀ ≠ 0 entstünde in W2 nur mit einer nichtminimalen Kopplung ξR|Φ|², die W2 nicht hat.
- OP5 und H96 bleiben offen.
