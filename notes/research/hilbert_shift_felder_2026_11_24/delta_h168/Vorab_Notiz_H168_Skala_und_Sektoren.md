# Vorab-Notiz H168: Hängt die Skala mit den Sektoren zusammen? Ladungsmischung je Sektor, gemeinsamer Versatz, Neutrino-Daten

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Überwiegend nicht blind:** a und b stehen analytisch fest, c ist überschlagen (R(π/6) ≈ 0,041), und H99 ist
bekannt. Blind sind d und e. Anlass: Autor, 26.11.2026, 18:28 UTC: „prüfe ob die skale mit den sektoren zusammenhängt, es könnte nämlich beides sein.“
Meine Lesart von „Sektoren“: die Fermionsektoren (geladene Leptonen, Neutrinos), unterschieden durch die Ladung; ihre Massenskalen unterscheiden sich um
viele Größenordnungen. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4. Vergeben: H168, k363 (geprüft: frei).

## Vorwissen geprüft
- **H167** (`../delta_h167/`, PR #343): Konjugationsterm cos 2δ, Spin-1-Term cos 2(δ − χ), χ = arctan c; c = 1 gibt den Oktanten; zwei Wege zur Elektronmasse
  (α/α′ = 0,0793204 dimensionslos, oder Ordnung 6 mit β₃v₀²/(α′Λ²) = −0,0852479).
- **H99** (`../../predictions/Ergebnis_H99_Neutrino_Phase_Bogenrand.md`): θ_ν = θ_e + π/12 bei K = ⅔ gibt R = Δm²₂₁/Δm²₃₁ = 0,030839; NuFIT 6.0 +1,31σ, NuFIT 6.1
  +1,80σ; θ_e − π/12 gibt 0,0003. Beziehung aus der Literatur (Brannen), „keine Herleitung der Verschiebung π/12“.
- **H102** (`../../predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`): π/4 − 3θ_e = γ_M/2, m_τ +2,3σ.
- **k282, k278:** für c = 0 fallen Konjugations- und Spin-1-Term zusammen; c ist die Ladungsmischung.
- **H1:** δ = 2/9 gilt nicht für Quarks; Quarks werden hier nicht gerechnet.
- **H144:** „Sektor“ als C-Faktor der Frames ist eine andere Lesart; hier nicht benutzt.
- Suche nach „c = 0“ zusammen mit „Neutrino“ und „π/12“ unter `notes/`, `wiki/`: kein Vorbefund, dass π/12 der Abstand der Minima für c = 0 und c = 1 ist.

**Suchrichtung:** rückwärts von H99: gesucht ist, was die zwei Sektoren unterscheidet und was sie gemeinsam haben. **Werkzeugwahl:** Python (mpmath, numpy),
Wolfram unabhängig. Qiskit nicht geeignet.

## Aufbau (k363, `k363_test_h168.py`; Gegenprobe `k363b_gegenprobe.wl`)
Ein Term je Sektor, der Spin-1-Term mit der Ladungsmischung c des Sektors: V_δ ∝ −cos 2(δ − χ), Minima δ = χ + {0, π/2} (beide Vorzeichen des Koeffizienten).
Gefaltet auf [0, π/3] (δ → −δ, δ → δ + 2π/3). Neutrino-Auslese wie H99: K = ⅔, Wurzeln 1 + √2 cos(δ + 2πk/3), m = Wurzel², R = (m₂² − m₁²)/(m₃² − m₁²), normale
Ordnung. Daten: NuFIT 6.1 wie H99b, Δm²₂₁ = 7,537 ± 0,097 ·10⁻⁵ eV², Δm²₃₁ = 2,511 ± 0,0205 ·10⁻³ eV². x = π/12 − δ* = 0,0395773 (δ* aus H166).

## Hypothesen und Kriterien
- **H168a (nicht blind, exakt):** Für c = 0 (neutraler Sektor) liegen die Minima gefaltet bei 0 und π/6, für c = 1 bei π/12 und π/4. Der Abstand der Minima
  mit drei verschiedenen, nichtnegativen Wurzeln nahe der Leptonform, π/6 − π/12, ist π/12: die Verschiebung aus H99. Kriterium: symbolisch, Python und Wolfram.
- **H168b (nicht blind):** Gilt H99, so haben beide Sektoren denselben Versatz x gegen ihr Minimum: δ_e = π/12 − x, δ_ν = π/6 − x; in der Sprache einer
  Mischung χ_e = π/4 − x, χ_ν = −x. Kriterium: Identität auf 10⁻¹².
- **H168c (nicht blind, überschlagen): Der Versatz ist keine Wirkung einer gemeinsamen Skala.** Mit gemeinsamem Λ ist der Versatz aus Ordnung 6 proportional
  zu v₀², im Neutrinosektor also um (Σ√m_ν/Σ√m_ℓ)² < 10⁻¹⁰ kleiner; dann wäre δ_ν = π/6 und R = R(π/6) ≈ 0,041. Kriterium: |R(π/6) − R_obs| > 5σ.
  Folge, falls bestätigt: Entweder ist der Versatz dimensionslos (Konjugationsweg oder Mischung), oder die Skala wächst mit dem Sektor, Λ_s ∝ v_s.
- **H168d (blind): Unter den acht Kandidaten δ_ν ∈ {0, π/12, π/6, π/4} ± x liegt genau einer innerhalb 3σ von R_obs, nämlich π/6 − x.** (Bekannt aus H99 sind nur
  π/6 − x und θ_e − π/12; die übrigen sechs sind nicht gerechnet.) Zusätzlich berichtet: der Versatz x_ν, den die Daten verlangen, mit Fehler, gegen x.
- **H168e (blind): Keine native Zahl trifft den Versatz.** Konstanten β_sym, β_sym², 1 − β_sym², ε₀, γ_L = 1,8646997646, 1/γ_L, γ_L − 1, γ_M = 0,237533,
  κ = (γ_L + 1/γ_L)/2, mal Faktoren 1, 1/2, 1/3, 1/4, 1/6, 1/12, 1/(2π), 1/(4π), gegen die Ziele x, 2x, 3x, tan x, tan 2x (360 Vergleiche). Treffer, wenn relativ
  näher als 10⁻⁴. Vorhersage: kein Treffer. Bekannt und kein Treffer in diesem Sinn: 3x gegen γ_M/2 (H102, relativ etwa 3·10⁻⁴).

## Folge, vorab festgelegt
- a und b bestätigt: Die Sektoren unterscheiden sich in dieser Lesart durch die Ladungsmischung (0 neutral, 1 geladen); π/12 aus H99 ist dann hergeleitet,
  bedingt auf c = 1 und auf die Brannen-Form für Neutrinos. Gemeinsam ist ein Versatz x, der nicht hergeleitet ist.
- c bestätigt: Antwort auf die Frage des Autors: Eine feste gemeinsame Skala scheidet als Quelle des Versatzes aus; „beides“ ist möglich, wenn die Skala am
  Sektor hängt (Λ_s ∝ v_s), und dann ist der Versatz wieder eine dimensionslose Zahl. Das gilt nur, soweit H99 gilt (heute +1,8σ, JUNO an der 2σ-Grenze).
- d widerlegt (mehrere oder kein Kandidat): Die Zuordnung der Sektoren zu c ist nicht eindeutig oder falsch; dann kein Schluss auf c.
- Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen. Keine neue Vorhersage für Daten; H99 und H102 bleiben, wie sie sind.
