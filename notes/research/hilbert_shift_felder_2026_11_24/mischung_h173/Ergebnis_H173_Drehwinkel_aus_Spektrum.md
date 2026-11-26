# Ergebnis H173: Mit der Ein-Feld-Form ist der Drehwinkel nicht mehr frei, aber die Zahl stimmt nicht

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H173_Drehwinkel_aus_Spektrum.md` (Commit 93bdc7f, vor der Rechnung). a nicht blind, b mit vorab notierter
Erwartung „widerlegt“, c und d blind. Skripte k368 (Python; Maskenfunktionen unverändert aus k263) und k368b (Wolfram, exakt für a). Übereinstimmung in a und
im Wert von b; c bis e nur in Python. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Verlangt man für das neutrale Feld die Ein-Feld-Form (gleiche Diagonale), dann folgt der Drehwinkel der Mischung aus dem Spektrum:
am Baumwert δ_ν = π/6 ist die Mischung exakt tribimaximal (θ₁₃ = 0), und derselbe Versatz x, der das Massenverhältnis einstellt, erzeugt θ₁₃; mit x aus den
Leptonen kommt aber sin²θ₁₃ = 0,0143 statt 0,0225 heraus (−14,7σ), und weder die Maske noch ein freies x bringen Übereinstimmung.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H173a | N = {{a, b, c}, {b, a, −b}, {c, −b, a}}: a = 1, c = −√2 sin(δ_ν + π/6), b² = cos δ_ν (cos δ_ν − √3 sin δ_ν)/2. tan² 2φ = 3 tan²(δ_ν + 2π/3) − 1; sin²θ₁₃ = sin²φ/3; sin²θ₁₂ = 1 − 4/(5 + cos 2φ); θ₂₃ = 45°, \|sin δ_CP\| = 1. Bei δ_ν = π/6: b = 0, θ₁₃ = 0, sin²θ₁₂ = ⅓. Für δ_ν > π/6 ist b² < 0 (keine reelle Lösung) | Nullreste; Zahlenprobe 10⁻¹² | **bestätigt** (Reste ≤ 7·10⁻¹⁶) |
| H173b | x = 0,0395773 (Leptonen): sin²θ₁₃ = 0,014263 gegen 0,02248 ± 0,00056: **−14,7σ**. sin²θ₁₂ = 0,32369 (NuFIT +2,2σ, JUNO +3,1σ). Mit x_ν aus den Neutrino-Daten: 0,01553 ± 0,00071, −7,7σ | \|z\| > 3 | **widerlegt** (wie erwartet) |
| H173c | Maske, Variante A, ε = artanh β_sym: 288 Fälle (24 Zweige × 12), keiner mit sin²θ₁₃ innerhalb 3σ; nächster 0,0097 (−22,8σ). Kontrolle ε = 0 trifft b auf 10⁻¹⁸ | kein Fall innerhalb 3σ | **widerlegt** |
| H173d | χ²_min = 57,6 bei x = 0,0568: R = 0,02725 (−6,1σ), sin²θ₁₃ = 0,01992 (−4,6σ) | χ² < 3,84 | **nicht verträglich** |
| H173e | Feldebene, feste Spalte ν₂: 0,163; ν₃: keine reelle Lösung. Massenebene: ν₁ 0,088, ν₂ 0,130, ν₃ keine Lösung | Bericht | keine Variante nahe 0,0225 |

Rückwärts: sin²θ₁₃ = 0,02248 verlangt x = 0,0649; dort wäre R = 0,0257 (−9,5σ). Variante B ohne Nachanpassung (Bericht): die Maske zerstört das
Massenverhältnis (R zwischen 4·10⁻⁵ und 0,096), kein Fall innerhalb 3σ; mit Nachanpassung der Massen ist die Regel nicht definiert und nicht gerechnet.

## Lesart
- **Antwort auf die Frage des Strangs.** Die Gruppe allein legt den Winkel nicht fest (k262). Mit einer zusätzlichen, im Projekt schon benutzten Forderung, der
  Ein-Feld-Form mit gleicher Diagonale (k278, H158), ist er festgelegt: Er ist eine Funktion der Phase δ_ν. Das ist eine Setzung, keine Herleitung.
- **Was daran trägt (Struktur).** Der Baumwert des neutralen Sektors, δ_ν = π/6 (H168), gibt exakt tribimaximale Mischung. θ₁₃ ≠ 0 entsteht erst durch den Versatz
  x, und nur für den Versatz nach unten (δ_ν < π/6), also in der Richtung, die auch R verlangt. Für kleine x gilt sin²θ₁₃ ≈ 2x/(3√3) mit Korrekturen.
  Ein Parameter steuert damit das Massenverhältnis und θ₁₃ zugleich, und die Größenordnung stimmt (0,014 gegen 0,022).
- **Was nicht trägt (Zahl).** Mit dem gemeinsamen Versatz aus H168 liegt θ₁₃ fünfzehn Standardabweichungen daneben, und kein einzelnes x passt zu R und θ₁₃
  zugleich (χ² = 58). Die Frame-Übertragung mit der Maske, die nach der Regel des Autors vor einem Urteil zu prüfen ist, wurde in Variante A gerechnet und
  verschlechtert die Lage. θ₂₃ = 45° und |sin δ_CP| = 1 gelten wie in k262; sin²θ₁₂ liegt wie bei TM1 zu hoch gegen JUNO (+3,1σ).
- **Folgerung.** In dieser Form ist die Verbindung „ein Versatz für Massen und Mischung“ quantitativ widerlegt. Entweder ist die Ein-Feld-Form für das neutrale
  Feld falsch, oder das Brannen-Spektrum der Neutrinos (H99), oder es fehlt ein Beitrag der geladenen Leptonen jenseits der Maske.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k262 | Träger s, ℤ₃, ungerade ℤ₂, Majorana | TM1, θ₂₃ = 45°, \|sin δ\| = 1 | ein freier Winkel (θ₁₃) |
| H134 | Maske ε = artanh β_sym | verträglich nur mit freiem φ in Variante B | φ bleibt frei |
| H173 | Ein-Feld-Form (gleiche Diagonale), Brannen-Spektrum (H99) | Winkel aus δ_ν; Baumwert tribimaximal | keine Wahl mehr frei, aber von den Daten widerlegt |

## Grenzen
- Daten: NuFIT 6.1 (NO) und JUNO 2026 mit den Werten aus dem Repo (k235, H134); nicht neu recherchiert.
- Maske nur in Variante A nach Kriterium; Variante B ohne Nachanpassung als Bericht. Zuordnung der Spalten fest (nach |λ|).
- Alles unter H99 und den Setzungen von k262. Kein Vorzeichen gesetzt (beide Vorzeichen von b gerechnet); kein Guard berührt; OP3 und OP4 offen.
- Vergeben: H173, k368. Nächste frei: H174, k369.
