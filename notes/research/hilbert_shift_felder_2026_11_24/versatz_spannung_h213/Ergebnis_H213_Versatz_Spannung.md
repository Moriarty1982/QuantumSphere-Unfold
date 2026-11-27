# Ergebnis H213 (k426): Der „4,2σ-Abstand“ zwischen Neutrino- und Lepton-Versatz war ein Fehler im Nenner — es sind 1,8σ

**Datum:** 2026-11-27. **Vorab:** `Vorab_H213_Versatz_Spannung.md` (Commit eae4b6d, vor der Rechnung). **Urteil: trägt** (Abstand nicht signifikant).
**Werkzeuge:** Python (`k426_test_h213.py` → `k426_out.txt`), Wolfram unabhängig (`k426b_gegenprobe.wl` → `k426b_out.txt`); alle
gemeinsamen Zahlen stimmen überein. Qiskit nicht einschlägig. Teil a nicht blind (aus H168 absehbar), Teile b–d blind.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| a (nicht blind) | x_ν = 0,043359 ± 0,002128 (aus R allein); x_lepton = 0,0395746 ± 0,0000063 (Polmassen); Differenz 0,003784 → **1,78σ**. Mit dem H207-Nenner 0,00091 käme 4,16σ heraus | T < 2 | **4,2σ war ein Nenner-Fehler** |
| b (blind) | Monte Carlo 10⁶: x_ν = 0,043358 (−0,00211/+0,00212); Anteil x_ν ≤ x_lepton 3,68 % → **1,79σ** | Abweichung > 0,3σ? | nein, linear reicht |
| c (blind) | Laufende Massen bei M_Z: K = 0,66793, x_lepton(M_Z) = 0,040762; Verschiebung +0,00119 = +0,56σ(x_ν); Abstand **1,22σ** | ≤ 1σ / < 0,3σ / dazwischen | **teilweise** (Schema verkleinert den Abstand, erklärt ihn nicht ganz) |
| d (blind) | Normale Ordnung: nur der H168-Zweig (δ_ν = 0,4802) und sein Spiegelbild (gleiches Spektrum). Invertierte Ordnung: Zweig bei δ_ν ≈ π/3 mit Versatz 0,0053, also −16σ von x_lepton | Liste | kein näherer Konkurrent |

**Gesamturteil: trägt.** Der maßgebliche Abstand ist 1,78σ (linear und Monte Carlo gleich). Zwischen dem Versatz, den R verlangt, und dem
Versatz der geladenen Leptonen besteht **keine signifikante Spannung**. Ein gemeinsamer Versatz x für beide Sektoren (H168) ist mit den Daten
verträglich.

## Was falsch war (Korrektur zu H207, append-only)
H207 (`staerke_h168_h207/k417_test_h207.py`, Zeile 75) teilte die Differenz x_ν − x_lepton durch σ = 0,00091. Diese Zahl ist die
Anpassungs-Unsicherheit des gemeinsamen Vier-Größen-Fits (R, θ₁₃, θ₁₂, θ₂₃) aus H175/H176. x_ν kommt aber allein aus R und hat
σ = 0,00213, wie schon H168d festhielt (−1,78σ). Die Unsicherheit von x_lepton ist wegen der genauen Lepton-Massen vernachlässigbar.
H207 bleibt unverändert stehen; seine Aussage „Rest-Spannung 4,2σ zwischen den Sektor-Versätzen“ gilt mit dieser Runde als berichtigt.
Die übrigen H207-Befunde (x\* = 0,0409 für θ₁₃, θ₁₃/θ₂₃/δ null-parametrig ~1,5σ) sind davon nicht berührt, denn dort ist der Fit-Nenner richtig.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** die korrekte Fehlerfortpflanzung für x_ν (linear und MC), die Schema-Empfindlichkeit von x_lepton, die Zweig-Liste.
- **Gesetzt:** Brannen-Form mit K = ⅔ für Neutrinos (H99); Datenstand NuFIT wie H99b/H168; laufende Massen aus der Literatur (Xing–Zhang–Zhou 2008);
  für IO in Teil d |Δm²₃₂| = 2,498·10⁻³ eV² als Näherungswert (nur für die Zweigliste, ohne Einfluss auf das Urteil).
- **Nachträglich bemerkt:** Die einzelnen Massen ziehen x_lepton(M_Z) in verschiedene Richtungen (nur m_μ laufend: 0,0432; nur m_τ: 0,0374;
  nur m_e: 0,0392). Das Schema ist also eine echte Zusatzwahl mit ≈0,6σ(x_ν) Spielraum. Welches Schema der Rahmen meint, ist offen; Koide (K = ⅔)
  gilt empirisch für Polmassen (K_Pol = 0,666664, K_MZ = 0,667929).
- **Kleinigkeit:** Mit freier Amplitude a statt a = √2 ist x_lepton = 0,0395746 statt 0,0395773 (Repo-Wert); Unterschied 2,7·10⁻⁶, belanglos.

## Folgen für den Stand
- Offene Stelle (ii) aus H207/H208 („4,2σ Neutrino-R-Versatz gegen Lepton-Versatz“) entfällt als Spannung; es bleibt ein 1,8σ-Abstand, der
  mit JUNO-Genauigkeit für Δm²₂₁ schärfer wird (σ(x_ν) skaliert im Wesentlichen mit σ(R)).
- **Vorhersage, die daraus folgt (bereits in H99/H168 enthalten, hier bestätigt):** Gilt ein gemeinsamer Versatz, muss R zu x_lepton passen:
  R(π/6 − x_lepton) = 0,030839 (H168c, +1,8σ zum heutigen Wert). JUNO kann das prüfen.
- Verbleibend offen im Mischungsstrang: die θ₁₂↔CP-Korrelation (H208). OP3/OP4 offen; kein Guard berührt.

## Dateien
- `Vorab_H213_Versatz_Spannung.md` — Vorab-Notiz (vor der Rechnung committet).
- `k426_test_h213.py`, `k426_out.txt` — Python-Rechnung und Ausgabe.
- `k426b_gegenprobe.wl`, `k426b_out.txt` — Wolfram-Gegenprobe und Ausgabe (mit Warnungen).

Vergeben: H213, k426. Nächste frei: H214, k427 (vor Vergabe gegen `main` prüfen).
