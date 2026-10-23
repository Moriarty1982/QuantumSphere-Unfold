# Ergebnis H29: Massenterme sind Frame-Kopplungen mit Higgs-Quantenzahlen; Massenaufspaltung verlangt die Brechung der Frame-Spiegelung, Mischung die der Triality

Vorab-Notiz: `Vorab_Notiz_H29_Brechung_Massen_Mischung.md`, Commit 85d065a (2026-10-23 20:55 MESZ), vor der Rechnung. Offengelegt waren dort die
bekannten Teile (Higgs-Quantenzahlen der Yukawa-Kopplungen, Brannen-Form ℤ₃-zirkulanter Matrizen, gleichzeitige Diagonalisierung). Skript
`k85_test_h29.py`, Ausgabe `k85_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H29a Räume | **bestätigt** | Verbinder, die mit Farbe und Lorentz-Drehungen vertauschen: 24 Dimensionen, linear wie antilinear |
| H29b antilinear, Higgs | **bestätigt** | Block Bild ← Kern: 8 Dimensionen (Lepton 4, Quark 4), genau Dubletts mit Y/2 = +½ (Q_em 1, 0) und Y/2 = −½ (Q_em 0, −1): H und H̃ |
| H29c linear | **bestätigt** | Block Bild ← Kern: 4 Dimensionen, nur Lepton-Sektor (Quark 0), Hyperladungen −½ und −3/2 (Q_em bis −2): keine Higgs-Quantenzahlen |
| H29d eichinvariant | **bestätigt** | Kein eichinvarianter Verbinder Bild ← Kern; im Block Kern ← Kern genau einer, und er wirkt nur auf ν^c |
| H29e Massen, Mischung | **bestätigt** | (i) S₃-symmetrisch: entartetes Paar; (ii) ℤ₃ allein: drei verschiedene Massen, genau Brannen-Form, Koide 2/3 bei \|b\| = a/√2; (iii) up und down beide ℤ₃-symmetrisch: \|V\| ist eine Permutation, keine Mischung |

## Einordnung

1. **Massenterme sind Frame-Kopplungen.** In der Operatorsprache der MM-Matrix ist jeder Massenterm **antilinear**, er enthält den
   Frame-Wechsel T:
   - Lineare Nebendiagonal-Blöcke einer farbverträglichen MM-Matrix liefern keine Massen. Sie fehlen bei den Quarks ganz und tragen bei den
     Leptonen falsche Ladungen.
   - Masse ist im Modell damit eine **Kopplung zwischen Materie- und Tachyon-Frame**. Das entspricht der Federkopplung Materie–Tachyon
     in `thm:spring` der Originalarbeit, aus der dort die träge Masse kommt.
   - Die Kopplungen, die das leisten, tragen genau die Quantenzahlen des Higgs-Dubletts (H und H̃), bei Leptonen und Quarks.
2. **Symmetriebrechung:** Eichinvariant ist keiner dieser Massenterme. Er wird erst durch einen Erwartungswert des Dubletts zu einer Masse.
   - Die Struktur liefert also, **welche** Brechung nötig ist (ein Dublett mit Y/2 = ½, also die elektroschwache Brechung), aber nicht,
     **warum** sie eintritt.
   - Eichinvariant ist nur ein Majorana-Term für ν^c. Er braucht keinen Higgs. Das erlaubt im Modell den See-Saw-Mechanismus für kleine
     Neutrinomassen (Lesart, nicht gerechnet).
3. **Massen über die drei Plätze:**
   - Mit voller Triolen-Symmetrie (τ und ρ) gibt es höchstens zwei verschiedene Massen. Das ist der Grund für die Widerlegungen von H11 und
     H16 bis H18.
   - Bricht man nur die Spiegelung ρ, also die Frame-Triole (r38), und behält die Triality τ, so gibt es drei verschiedene Massen, und zwar
     genau in der **Brannen-Form** a + 2|b|cos(θ + 2πk/3). Koide K = 2/3 entspricht |b| = a/√2.
   - Die Koide-Form aus v4.8.0-r10 ist damit die Massenform einer ℤ₃-symmetrischen, ρ-gebrochenen Kopplung. Nicht erklärt sind das
     Verhältnis |b|/a und die Phase θ (die alte Phasenformel ist widerlegt, r09).
4. **Mischung:** Sind die Kopplungen für up und down beide τ-symmetrisch, werden sie von derselben Fourier-Matrix diagonalisiert, und es
   gibt keine Mischung. Mischung verlangt, dass die Triality selbst gebrochen ist, und zwar für up und down verschieden.
5. **Zusammengefasst:** Im Modell hat jede beobachtete Eigenschaft ihre Brechungsstufe.
   - Masse braucht die Frame-Kopplung (Higgs).
   - Die Massenaufspaltung braucht die Brechung der Frame-Spiegelung ρ.
   - Die Mischung braucht die Brechung der Triality τ.

   Woher diese Brechungen kommen, sagt die Struktur nicht. Sie ordnet sie aber in eine Reihenfolge, die zu den Ebenen des Companion passt:
   Frames, Spiegelung, Triality.
