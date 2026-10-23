# Vorab-Notiz H18: Massen aus links-invarianten Etiketten an den Minima der geprüften Potentiale

Festgelegt am 2026-10-23, **vor** der numerischen Prüfung und vor jedem Vergleich mit Massen. Bezug: K77.10
(`k72_links_invariant.py`, `formal/QSFormal/Lesarten.lean`), H11 (K32), H17 (K76).

## Rahmen

Tripel (x₁, x₂, x₃) ∈ 𝕆³, abgelegt als (Im ℍ) ⊗ 𝕆 (Zeile b = Platz). Lorentz wirkt von links. Links-invariante Etiketten
(K77.10): μ_k = 2(|x_i|²|x_j|² − ⟨x_i, x_j⟩²) mit {i, j, k} = {1, 2, 3}, also der doppelte Flächeninhalt der beiden anderen
Plätze. μ ist G₂-invariant und invariant unter der Linkswirkung.

**Massen-Lesart (verbindlich):** m_k ∝ √μ_k. Das ist die gradgleiche Entsprechung zu m ∝ n² aus H11 (μ hat Grad 4).
Also √m_k ∝ μ_k^{1/4} und K = Σ√μ_k / (Σ μ_k^{1/4})². Zuordnung zu den Generationen nach Größe: Die drei Werte werden
sortiert verglichen, es gibt keine freie Zuordnung.

**Auswahlprinzip (verbindlich):** Das Tripel ist das globale Minimum eines der bereits geprüften Potentiale. Die
Potentiale werden nicht verändert.
- Familie A (H11): V₄ = −S + βS² + γQ − κt, Gitter wie k30 (β ∈ {0,25; 0,5; 1; 2; 4}, γ ∈ {−0,2; −0,1; 0; 0,1; 0,5; 1; 3},
  κ ∈ {0; 0,1; 0,5; 1; 2; 5}), ohne die flachen Fälle γ = κ = 0.
- Familie B (H17): V_R = −S + βS² + γQ − κt − μL − νR₂ − λL², Verteilung wie k69, aber N = 500, Seed 18.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

- Bei paarweise orthogonalen Plätzen ist √(μ_k/2) = n_i n_j = P/n_k. Die Reihenfolge kehrt sich gegenüber den Normen um.
- An den Minima von A und B sind die Normen höchstens zweierlei (H11, H17). Unterschiede in μ können dann nur aus den
  Winkeln ⟨x_i, x_j⟩ kommen. An S₃-symmetrischen Konfigurationen sind alle μ gleich.
- Minima können ganze Mannigfaltigkeiten sein. G₂ und die Linkswirkung ändern μ nicht, andere flache Richtungen
  vielleicht doch. Dann wären die μ unbestimmt.
- Erwartung: Entweder gleiche μ oder unbestimmte μ; drei bestimmte, verschiedene μ eher nicht. Das ist nicht gerechnet.

## Hypothesen (V)

- **H18a:** Für mindestens einen Parameterpunkt aus A oder B hat das globale Minimum **bestimmte** und **drei
  verschiedene** μ.
- **H18b:** Unter diesen Punkten gibt es einen, dessen Massen (Lesart oben) die Lepton-Verhältnisse treffen:
  √m_e/√m_τ = 0,016959 und √m_μ/√m_τ = 0,243848, je auf 1 % relativ.

## Verfahren (verbindlich)

- Minimierung über alle 24 Koordinaten, BFGS mit analytischem Gradienten (wie k30/k69), 20 Startpunkte je
  Parameterpunkt.
- „Bestimmt“: Alle Startpunkte, deren Endwert höchstens 10⁻⁹·|V_min| über dem besten liegt (mindestens 3 solche), haben
  dieselben sortierten μ bis auf relativ 10⁻³. Sonst „unbestimmt“. Weniger als 3 solche Startpunkte: „nicht entschieden“.
- „Verschieden“: relative Abstände der sortierten μ über 10⁻³; „≠ 0“: μ > 10⁻⁶·max μ.
- Berichtet: Anzahl je Muster (gleich / zwei verschieden / drei verschieden; bestimmt / unbestimmt / nicht entschieden),
  bei drei verschiedenen und bestimmten die Werte, K und der Abstand zu den Lepton-Verhältnissen.

## Entscheidungskriterium (verbindlich)

- H18a **bestätigt**, wenn mindestens ein Parameterpunkt bestimmte, drei verschiedene, von null verschiedene μ hat;
  sonst **widerlegt**.
- H18b **bestätigt**, wenn ein solcher Punkt beide Lepton-Verhältnisse auf 1 % trifft; sonst **widerlegt**. Ein Treffer
  wäre wegen der vielen Parameterpunkte nur ein Hinweis, keine Vorhersage. Als Vorhersage zählt er erst, wenn er auf einem
  zusammenhängenden Gebiet mit höchstens einem freien Parameter auftritt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
