# Vorab-Notiz H112: β² aus dem solaren Mischungswinkel und aus Ω_m ist dieselbe Zahl (Überbestimmung)

**Stand:** 17. November 2026, vor jeder Prüfung festgelegt. Blind gegenüber den künftigen Prüfdaten, **nicht blind** gegenüber dem heutigen
Datenstand (Vorschau unten; zählt nicht). Auftrag des Autors vom 17.11.2026: „H112 Überbestimmung“ (offener Vorschlag 1 der Übergabe).

## Worum es geht
Der Companion liest dieselbe Zahl β_sym² an zwei Stellen ab: als |U_e2|² im Leptonmischen (H9) und als heutigen Materieanteil Ω_M (H96).
H9 und H96 prüfen jede Stelle gegen den **Wert** β_sym² = 0,30185 aus der Zählregel (U(1)-Zählung, Gewicht 2, OP1 offen). H112 prüft nur,
ob beide Stellen **dieselbe** Zahl zeigen, gleich welche. Damit trennt H112 die These „eine Zahl“ (T6, r29) vom Wert der Zählregel:
- Fallen H9 oder H96, H112 aber nicht, ist die Zählregel belastet, die Gleichsetzung der beiden Stellen nicht.
- Fällt H112, fällt mindestens eine der beiden Lesarten (|U_e2|² = β² oder Ω_M = β²), unabhängig von OP1.

## Vorwissen geprüft
- `Vorab_Notiz_H96_Omega_M_beta2.md` (6.11.2026): Ω_M = β_sym² = 0,30185 gegen das erste flache-ΛCDM-Ω_m aus DESI DR3 (BAO allein) oder
  Euclid nach dem 6.11.2026, 2σ-Kriterium. Offen. H112 übernimmt diese Datenwahl unverändert.
- `../v4_8_0_r03_r12/llm/Vorab_Notiz_H9_Solarwinkel_beta_sym.md` (20.10.2026): sin²θ₁₂ = β_sym²/cos²θ₁₃ gegen die nächste JUNO-Messung mit
  σ ≤ 0,004; |z| < 2 verträglich, ≥ 3 widerlegt. Nachträglich gefunden. Offen. H112 übernimmt diese Datenwahl unverändert.
- `../v4_8_0_r03_r12/llm/Nachpruefung_JUNO_2026.md`: JUNO 2026 sin²θ₁₂ = 0,3036 ± 0,0064 (arXiv:2609.37895).
- `../op4_status_audit_2026_11_17/README.md` mit Nachtrag „Vorschau“ (PR #176): H9 gegen NuFIT 6.1 0,00σ, gegen JUNO 2026 +0,81σ; kein Test.
- `../op1_one_number_2026_11_17/README.md` (PR #172): γ_L = γ_M/γ_T = D_M = cosh 2η = 1/b_M als eine Zahl; v4.10.0-r29 (Zählregel von M als eine
  Zahl). Dort keine Gleichsetzung der beiden Messstellen als eigener Test.
- `Vorhersagen-und-Tests.md` (Wiki), Abhängigkeitsabsatz (r08, r10, r11): H9-artige und H96 ruhen auf demselben Kern; Ω_M = β² ist eine zusätzliche
  Gleichsetzung von Registerverhältnis und Dichteanteil (r11). Eine wertfreie Gegenprüfung beider Stellen gibt es bisher nicht.
- `wiki/Gesamtbild.md`: berührt T6 (β_sym als Strukturgröße, OP1) und T8 (Mischungswinkel, OP4); kosmologische Lesart über OP5 (Λ-Auslesung).
- Suche nach `H112`, `k234`: nur als „frei“ vermerkt (Übergabe, Ergebnis H111, Notizen zu Flusslinien und H6 C, Wiki „Forschungsstand“).

## Aufbau
- Neutrino-Seite: b_ν = sin²θ₁₂ · cos²θ₁₃ = |U_e2|². sin²θ₁₂ aus der **Prüfmessung von H9** (nächste JUNO-Veröffentlichung mit 1σ ≤ 0,004, ersatzweise
  ein globaler Fit, der diese Daten enthält); cos²θ₁₃ aus derselben Veröffentlichung, sonst aus der dann neuesten NuFIT-Version (normale Ordnung).
  Der Fehler aus θ₁₃ wird vernachlässigt (unter 2 % von σ_ν).
- Kosmologie-Seite: b_cos = Ω_m aus der **Prüfmessung von H96** (erstes flaches-ΛCDM-Ω_m nach dem 6.11.2026 aus DESI DR3 BAO allein oder Euclid,
  je nachdem was zuerst erscheint; keine CMB-Kombination, keine Reanalyse).
- Pull z = (b_ν − b_cos)/√(σ_ν² + σ_cos²); bei asymmetrischen Fehlern jeweils die zur anderen Größe weisende Seite. Die beiden Messungen sind
  unabhängig (Reaktorneutrinos gegen Galaxienverteilung).
- Skript `k234_test_h112.py`: mit sieben Argumenten der Test, ohne Argumente die Vorschau.

## Hypothese und Kriterium
- **H112:** b_ν und b_cos sind innerhalb der gemeinsamen Fehler gleich.
  - |z| < 2: **verträglich** (bestätigt im Sinn der Überbestimmung);
  - 2 ≤ |z| < 3: **Spannung**, nicht entschieden;
  - |z| ≥ 3: **widerlegt**.
- Ausgewertet wird, sobald **beide** Prüfmessungen vorliegen. Liegt bis zum **31.12.2029** eine davon nicht vor, entfällt H112 ohne Urteil.
- Der Wert 0,30185 geht in H112 nicht ein. H9 und H96 werden mit denselben Daten nach ihren eigenen Kriterien getrennt ausgewertet.

## Trennschärfe (vor der Prüfung offen gesagt)
Bei σ(sin²θ₁₂) = 0,004 und σ(Ω_m) = 0,006 (0,0086 wie DESI DR2) ist das gemeinsame σ ≈ 0,0072 (0,0094). Widerlegt wird H112 also erst bei einem
Unterschied |Δβ²| ≥ 0,022 (0,028). Das ist ein schwacher Test:
- Er unterscheidet die Hopf-Variante Ω_M = 1/3 von einem Neutrinowert um 0,30 (Δ ≈ 0,03).
- Er unterscheidet **nicht** TM1 (b_ν = 0,311) von β_sym² = 0,302; das bleibt Sache von H9.
- Ein verträgliches Ergebnis heißt nur: Die beiden Stellen widersprechen der Gleichsetzung nicht. Es ist kein Beleg für die Zählregel und keiner
  für einen Zusammenhang zwischen Mischung und Kosmologie; zwei Zahlen um 0,30 stimmen bei dieser Genauigkeit auch zufällig überein. Ob das als
  Zufall gelten muss, beantwortet die getrennte Zufallsabschätzung (offener Vorschlag 3), nicht H112.

## Offenlegung (vor dem Festschreiben bekannt; zählt nicht)
Vorschau mit `k234_test_h112.py` ohne Argumente (β = √b):

| Neutrino-Seite | Kosmologie-Seite | b_ν | b_cos | z |
|---|---|---|---|---|
| NuFIT 6.1 (0,3088, θ₁₃ 0,02248) | DESI DR2 BAO 0,2975 ± 0,0086 | 0,3019 (β 0,5494) | 0,2975 (β 0,5454) | +0,41 |
| NuFIT 6.1 | Planck 2018 0,3153 ± 0,0073 | 0,3019 | 0,3153 (β 0,5615) | −1,37 |
| JUNO 2026 (0,3036 ± 0,0064) | DESI DR2 BAO | 0,2968 (β 0,5448) | 0,2975 | −0,07 |
| JUNO 2026 | Planck 2018 | 0,2968 | 0,3153 | −1,93 |

Heute verträglich in allen vier Paarungen; gegen Planck am Rand. Die Kosmologie-Daten streuen untereinander um etwa 2,5σ (H96); deshalb ist die
Quelle fest vorgegeben.

## Folge, vorab festgelegt
- **Verträglich:** Die Gleichsetzung |U_e2|² = Ω_M bleibt stehen; T6 erhält keinen neuen Beleg, nur keine neue Belastung. Der gemeinsame Wert
  (gewichtetes Mittel) wird als Messwert von β² notiert, nicht als Bestätigung von 0,30185.
- **Widerlegt:** Mindestens eine der Lesarten |U_e2|² = β² (H9-Linie, OP4) oder Ω_M = β² (H96-Linie, OP5) fällt; „eine Zahl“ gilt dann nicht für
  beide Stellen. Welche fällt, sagen H9 und H96 mit ihren eigenen Kriterien.
- **Spannung oder entfallen:** keine Aussage.
- Nach dem Commit dieser Notiz wird an Datenwahl und Kriterium nichts mehr geändert.
