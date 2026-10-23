# Ergebnis H31: Readouts aus den Verschiebungen brechen τ nie; erst Masken, die Generationen unterscheiden, erzeugen Mischung

Vorab-Notiz: `Vorab_Notiz_H31_Tau_Brechung_Readouts.md`, Commit ea74447 (2026-10-23 21:41 MESZ), vor der Rechnung. Offengelegt: H31a folgt aus der
Kommutativität von ℂ[ℤ₃], H31c ist allgemeine Störungstheorie. Skript `k87_test_h31.py`, Ausgabe `k87_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H31a Verbot | **bestätigt** | 200 Verschiebungs-Readouts (Produkte, Untergruppen-Mittel, Selektor-Kontraktionen): alle vertauschen mit τ; \|V\| bleibt eine Permutation (Abstand ≤ 8·10⁻¹⁴) |
| H31b Art-Masken | **bestätigt** | Masken auf einzelne Generationen vertauschen nicht mit τ; mit δ = 0,3 entsteht Mischung, auch bei gleicher Maske für up und down (kleinster Abstand zur Permutation 0,028) |
| H31c Skalierung | **bestätigt** | Die Mischung wächst linear in δ (Verhältnis 0,998–1,001 zwischen δ = 10⁻³ und 10⁻⁴) und ist durch δ·(1/Lücke_u + 1/Lücke_d)/3 beschränkt |
| H31d Frames | **bestätigt** | Art-Masken sind reell, die τ-Brechung ist frame-frei |

Der Faktor 1/3 in der Schranke ist die Größe der Einträge einer Ein-Platz-Maske in der Fourier-Basis der Generationen.

## Einordnung

1. **Die gemischten Readouts, so wie sie aus dem Hilbert-Shift gebildet sind, erzeugen keine Mischung.** Alle Readouts, die nur aus den
   Generations-Verschiebungen gebaut sind (Summe, Vereinigung, Selektor-Kontraktion), liegen im kommutativen Gruppenring von ℤ₃ und
   vertauschen mit τ. Das ist ein echtes Verbot.
2. **Erst ein Readout, der Generationen als eigene Auslesearten unterscheidet, bricht τ.** Das sind Bits der Masken-Registrierung, die einzelne
   Plätze auswählen. Dann gilt:
   - Mischung entsteht, und zwar schon bei gleicher Maske für up und down, weil die beiden Kopplungen verschieden sind.
   - Sie ist **klein**, wenn die Maske schwach gewichtet ist (∝ δ), und umso kleiner, je weiter die Massen auseinanderliegen. Das passt
     qualitativ zu den kleinen CKM-Winkeln bei starker Massenhierarchie. Große Mischung wäre dort zu erwarten, wo die Massen dicht liegen,
     etwa bei den Neutrinos.
   - Zahlenwerte folgen daraus nicht.
3. **Spannung, offen benannt:** In der Physik ist die Mischung messbar und kein Artefakt des Beobachters. „Mischung durch Auslesen“ kann daher
   nur heißen, dass die generationen-selektive Maske ein **Teil der Kopplungen** ist, also der Struktur, in der ausgelesen wird. Eine
   Abhängigkeit vom Messenden darf es nicht bedeuten. Woher eine solche Maske in der Struktur kommt, ist offen.
4. **Stand der Brechungen:**

   | Brechung | Quelle |
   |---|---|
   | Frame-Kopplung | Higgs (Typ festgelegt) |
   | ρ | Chiralität, aus der Struktur begründet |
   | τ | generationen-selektive Maske, nicht aus den Verschiebungen; nur als Bedingung gezeigt |
