# Vorab-Notiz H176: Ein-Zahl-Kandidat für die Leptonmischung, festgeschrieben für künftige Daten

**Stand:** 26.11.2026. Anlass: Autor, 26.11.2026, „ja, festschreiben“. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3. Vergeben: H176 (geprüft: frei).
**Nicht blind gegenüber den heutigen Daten:** Der Kandidat ist in k373 nachträglich aus acht Varianten ausgewählt und an R, θ₁₃, θ₁₂ (JUNO 2026), θ₂₃ angepasst
(χ² = 2,86, vier Messgrößen, eine Zahl). Diese Notiz schreibt ihn fest, damit er an **künftigen** Daten geprüft werden kann. Ab jetzt wird nichts mehr angepasst.

## Vorwissen geprüft
H173, k369, H174, H175, k372, k373 (`../mischung_h173/`, `../mischung_h174/`, `../mischung_h175/`); H99/H100 (Neutrino-Verhältnis R, `../../predictions/`),
H125 (Erwartung sin δ_PMNS < 0), H168 (gemeinsamer Versatz; steht mit diesem Kandidaten in Spannung, siehe unten).

## Der Kandidat (festgeschrieben)
- Platzbasis, T und A wie k262b. Neutrinos: Ein-Feld-Form N̂ mit Brannen-Spektrum (K = ⅔) bei δ_ν = π/6 − x.
- Geladene Leptonen: M_e ∝ Ĉ(ρ, δ) + i·tan x·(K₁ + K₂)/√2 mit K₁ = E₁₃ − E₃₁, K₂ = (−E₁₂ + E₂₁ + E₂₃ − E₃₂)/√2; ρ, δ aus den drei Polmassen
  (Zweig mit dem Elektron auf dem T-Eigenwert 1).
- **x = 0,04478** (Unsicherheit aus der Anpassung ± 0,00091). Rechenweg: `../mischung_h175/k371_test_h175.py`, `k373_nachtrag_gemeinsam.py`.

## Vorhersagen (Band für x ± 0,00091)
| Größe | Wert | Band |
|---|---|---|
| sin²θ₁₂ | 0,3019 | 0,3012 bis 0,3025 |
| sin²θ₁₃ | 0,0223 | 0,0218 bis 0,0228 |
| sin²θ₂₃ | 0,4954 | 0,4952 bis 0,4955 |
| δ_CP | ±77,7° (sin δ = ±0,977, cos δ = +0,213) | ±77,6° bis ±77,8° |
| Δm²₂₁/Δm²₃₁ | 0,02971 | 0,02952 bis 0,02991 |
| Massen (normale Ordnung, mit Δm²₂₁ = 7,53·10⁻⁵ eV²) | 0,36 / 8,69 / 50,3 meV, Summe 59,4 meV | Summe 59,2 bis 59,6 meV |

Das Vorzeichen von δ_CP wird nicht gesetzt (beide Zweige, komplex konjugiert). Mit der Erwartung aus H125 (sin δ < 0) wäre es δ_CP ≈ −78° (282°).
Ein Vergleich mit heutigen δ_CP-Anpassungen ist nicht gemacht (keine Werte im Repo).

## Kriterien (an der jeweils nächsten Datenausgabe: JUNO für θ₁₂, NuFIT für alle Winkel und R, später DUNE/T2HK/Hyper-K für δ_CP und den Oktanten)
- **Widerlegt**, wenn eine der Größen sin²θ₁₂, sin²θ₁₃, sin²θ₂₃, R um mehr als 3σ (Messfehler plus Band quadratisch) vom festgeschriebenen Wert abweicht,
  oder wenn |sin δ_CP| < 0,8 mit 3σ gemessen wird, oder wenn die inverse Ordnung mit 3σ festgestellt wird.
- **Besteht**, solange alle Größen innerhalb 2σ liegen. Dazwischen: **in Spannung**.
- Schärfste Stellen: sin²θ₂₃ = 0,495 (erster Oktant knapp unter ½; ein gemessenes 0,45 oder 0,55 mit Fehler 0,01 widerlegt) und sin²θ₁₂ = 0,302 (JUNO-Ziel: Fehler ≈ 0,002).

## Grenzen
- Richtung (K₁ + K₂)/√2, Stärke tan x und der Wert von x sind angepasst, nicht hergeleitet. Ein-Feld-Form, K = ⅔ für Neutrinos und die gleiche Normierung sind Setzungen.
- x = 0,04478 liegt 5,7σ neben dem Versatz der geladenen Leptonen (0,039577). Der gemeinsame Versatz aus H168 gilt in diesem Kandidaten nicht.
- Keine Übertragung in den Materie-Frame (Maske); mit dem postulierten ε ist sie nach H173c weit weg. Der Kandidat steht damit außerhalb der Maskenregel aus H45/H134;
  das ist offen und wird nicht als gelöst dargestellt.
- OP3 und OP4 bleiben offen.
