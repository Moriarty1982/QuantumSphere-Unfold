# Quark-No-go, xyz als kubische Albert-Norm und Vakuumausrichtung (Erkundung k277, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Solange A₄ exakt gilt, spüren die Quarks die Ladungsbrechung auf keinem SO(3)-verträglichen Weg (No-go). Der
kubische A₄-Term xyz, den Flavon-Modelle von Hand ansetzen, ist in der Albert-Algebra die **kubische Norm nach der Ladungsdrehung**,
N(C·X(v)) = −2 v₁v₂v₃. Ein Potential nur aus dieser Größe erzwingt die Ausrichtung (1,1,1) mit Restgruppe ℤ₃. Gemischte Terme bringen
Σvᵢ⁴ mit freiem Koeffizienten, und dann entscheidet das bekannte Phasendiagramm zwischen ℤ₃ und ℤ₂.

Auftrag: Autor (24.11.2026, Karte „Als Erkundung k277 mit PR“) nach H127 (#291) und der Vorüberlegung zu H128. **Nicht blind:** Alle drei
Aussagen standen vor der Rechnung analytisch fest. Deshalb gibt es keinen Test H128, die Nummer bleibt frei. Skripte **k277, k277b**.

Werkzeuge: Python (numpy, scipy) mit der Albert-Algebra aus k276 (Dimensionen, Stichproben, Minimierung; k277). Wolfram Language exakt für
det(CX), die Spuren und die Extrema von xyz (k277b). Qiskit nicht eingesetzt.

## Vorwissen geprüft
k275 (Familien-SO(3), Tripletts alle Spin 1, Rest A₄), H127/k276 (C auf H₃(ℂ) reiner Spin 3; Stufe B offen), H39 (ℤ₃ für Dirac-Sektoren, ℤ₂ für
Neutrinos, H39d: V_CKM = 𝟙 in führender Ordnung), k256 (K∘S₀, TM1), H8, H37, k274 (nichtlineares Feld). Literatur: A₄-Flavon-Potential und
Vakuumausrichtung (Altarelli–Feruglio 2005), A₄-invariante Masse eines Tripletts ∝ 𝟙.

## Ergebnisse
1. **No-go (k277 A).** Auf den Farbtripletts (18) haben die A₄-invarianten und die SO(3)-invarianten Operatoren dieselbe Dimension 36, und jede
   A₄-invariante kommutiert mit so(3) (Rest 10⁻¹⁵). Grund: Spin 1 ⊗ Spin 1 = l 0, 1, 2, und A₄ hat in l = 1, 2 kein Invariantes. C ist A₄-invariant
   (exakt), also ist jede SO(3)-äquivariante Konstruktion aus C, gleich welcher Ordnung, auf den Quarks SO(3)-invariant. Stufe B von H127 war
   damit nicht nur für die gewählte Kopplung leer, sondern für jede.
2. **xyz als kubische Norm (k277 B, k277b).** Flavon v in den e₇-Anteilen (Spin 1): det X = 0, Tr X² = 2|v|². Y = C·X(v) ist reell symmetrisch mit
   Nulldiagonale und Einträgen −vₖ, **det Y = −2 v₁v₂v₃** (exakt), Tr Y = 0, Tr Y² = 2|v|².
3. **Invarianten (k277 C, k277b).** Aus Y allein: nur |v|² und xyz (Tr((Y²)²) = 2|v|⁴). Gemischt: Tr((X∘Y)²) = 2Σ_{i<j}vᵢ²vⱼ², Tr(X²∘Y²) = 2Σvᵢ⁴.
4. **Ausrichtung (k277 D, k277b).** Die Extrema von xyz auf der Sphäre liegen genau bei |vᵢ| = 1/√3 (8 Lösungen). Potentiale nur aus Y: alle Minima
   (1,1,1)-Typ, Restgruppe ℤ₃, für κ = ±0,5 und 0,05. Allgemeines Potential mit λ′Σv⁴: λ′ = +0,3 gibt ℤ₃, λ′ = −0,15 gibt (1,0,0) mit Restgruppe ℤ₂.

## Bewertung
- **Für die Quarks ist eine Suchrichtung ehrlich geschlossen.** Mit exakter A₄ tragen sie die Familien-SO(3) effektiv exakt: entartete Massen,
  V_CKM = 𝟙. H39d ist damit hergeleitet und nicht mehr nur gelesen. Mischung verlangt, dass A₄ selbst bricht.
- **Neu ist die Herkunft des kubischen Terms.** In A₄-Modellen ist xyz eine Eingabe. Hier ist er die Jordan-Norm des ladungsgedrehten Flavons, und
  die Ladung ist dieselbe Struktur, die r42/r43 für die Chiralität verwenden.
- **Die Ausrichtung ist nicht vorhergesagt.** Ein Potential nur aus der kubischen Norm gibt ℤ₃, also die Lesart der Dirac-Sektoren (H39). Für ℤ₂
  (Neutrinos) braucht es gemischte Terme mit einem freien Koeffizienten. Ein blinder Test bräuchte ein Prinzip, das diese Koeffizienten festlegt,
  etwa eine Wirkung aus dem Turm. Das ist offen.
- Vorausgesetzt bleibt, dass die drei Plätze Generationen sind und der Flavon in den e₇-Anteilen sitzt (Lesart). OP3 bleibt offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- Ein Prinzip für die Koeffizienten suchen: Lässt sich das Potential aus der Dynamik des Turms ableiten (k274, nichtlineares Feld, mit der kubischen Norm als
  natürlichem Term dritter Ordnung)?
- Ein zweiter Flavon im Spin-2-Teil (Realteile, 5 → 1′ ⊕ 1″ ⊕ 3 unter A₄) als Neutrino-Kandidat: Welche Invarianten liefert dort die Algebra?

## Dateien
`k277_quark_nogo_xyz.py` (`k277_out.txt`; benutzt `../h127/k276_test_h127.py`), `k277b_xyz_exakt.wl` (`k277b_out.txt`, Wolfram).
