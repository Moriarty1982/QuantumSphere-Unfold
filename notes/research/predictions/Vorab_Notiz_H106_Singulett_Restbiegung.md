# Vorab-Notiz H106: Schließt die vierte Dixon-Kopie (Singulett) den Rest der Biegung?

Festgelegt am 2026-11-16, **vor** der Rechnung. Auftrag des Autors: „weiter mit OP3“. Einordnung OP3, v4.10.0-r25. Skript
`k228_test_h106.py` (wird nach dieser Notiz geschrieben und ausgeführt).

## Anlass
Das Spin-1-Dreieck (r15.3, im Triplett von HS(8) nach r25.3) hat bei Überlappung ½ die Bargmann-Phase 0,679042. Die geladenen
Leptonen liegen bei φ = 2/3 (r14); es fehlen 0,012376 rad. Die Spin-1-Notiz vom 15.11. legt fest: Diesen Rest zu deuten, geht nur mit
Vorab-Notiz und einem Mechanismus, der die Größe **vor** der Rechnung festlegt. r25 hat mit dem Singulett der vier Dixon-Kopien eine
neue Struktur geliefert. Hier werden zwei Mechanismen geprüft, die das Singulett ohne freien Parameter einbeziehen.

## Vorwissen geprüft
- `../op3_spin1_triangle_2026_11_15/README.md`: Spin-1-Dreieck, Phase 0,679042, Rest 0,012376, Deutungsregel.
- `../op3_dixon_copies_2026_11_16/README.md` (r25): HS(8) = Triplett ⊕ Singulett; Spatprodukt im Singulett, |det V|² = det G.
- `../op3_guarded_core_flux_2026_11_15/README.md`: Lesart A, φ = π/4 − γ_M/2 = 0,666632 (Kern als Fluss); nicht blind.
- `../op3_horizon_shadow_2026_11_15/README.md`: Sektorschatten γ/2 wäre fast zehnmal zu groß.
- `Vorab_Notiz_H102_*`, `Ergebnis_H102_*` (offen): m_τ aus dem Fluss Φ_e = π/4 − γ_M/2.
- Suche nach „Beimischung“, „Singulett“, „admixture“ in den OP3-Notizen: keine Singulett-Beimischung zu Generationszuständen geprüft.

## Festgelegte Konstruktion
Drei Einheitsrichtungen n_k auf einem Kegel mit halbem Öffnungswinkel ψ um die z-Achse, Azimut 2πk/3 (k = 0, 1, 2). |n⟩ ist der
kohärente Spin-½-Zustand zu n; der Kopienindex ist C² ⊗ C² (zwei Kopien-Qubits, HS(8)); ε = (|01⟩ − |10⟩)/√2 ist das Singulett.
Für jeden Mechanismus wird ψ allein durch die Überlappung festgelegt, |⟨g_j|g_k⟩|² = ½ für j ≠ k (also K = 2/3). Die Bargmann-Phase
φ = |arg(⟨g₀|g₁⟩⟨g₁|g₂⟩⟨g₂|g₀⟩)| ist dann die **Vorhersage**.

- **M1 (Dimensionsanteil):** g_k = √(3/4) |n_k⟩|n_k⟩ + √(1/4) ε. Das Gewicht ¼ ist der Anteil des Singuletts an der Dimension von C² ⊗ C²;
  die Phase des Singulettanteils ist für alle k gleich (das Singulett ist unter dem Zyklus invariant).
- **M2 (Normalen-Paare, Idee des Autors aus r25):** g_k = |n_k⟩ ⊗ |n_{k+1}⟩ (Indizes mod 3). Jede Generation ist ein Paar benachbarter
  Richtungen; ihr Singulettanteil ist durch die Geometrie festgelegt (er gehört zur „Normale“ des Paares).

Gibt es für einen Mechanismus kein ψ mit Überlappung ½, scheidet er aus. Gibt es mehrere, zählt jede Lösung als eigener Versuch.

## Entscheidungskriterium (vor der Rechnung festgelegt)
- **bestätigt**, wenn für mindestens einen Mechanismus eine Lösung |φ − 2/3| ≤ 0,001 rad erfüllt (das schließt mindestens 92 % des Rests
  0,012376).
- **widerlegt**, wenn keine Lösung das erfüllt.
- Offenlegung: zwei Mechanismen, also bis zu zwei (bei mehreren Lösungen mehr) Versuche; das Ergebnis wird mit dieser Zahl genannt. Der
  Zielwert 2/3 war bekannt; blind ist die Prüfung nur darin, dass M1 und M2 vor jeder Rechnung festgelegt sind. Ein Treffer wäre eine
  Lesart des Rests, keine Herleitung der Überlappung ½.

## Ablauf
1. Diese Notiz committen.
2. `k228_test_h106.py` schreiben und ausführen (Ausgabe `k228_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H106_Singulett_Restbiegung.md`.
