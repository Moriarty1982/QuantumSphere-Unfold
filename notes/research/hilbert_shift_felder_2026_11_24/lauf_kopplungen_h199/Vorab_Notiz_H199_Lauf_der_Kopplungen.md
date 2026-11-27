# Vorab-Notiz H199 (1b): Entsteht D ≈ B aus dem Lauf der Kopplungen?

**Datum:** 27.11.2026. **Nummern:** H199 (Test), k409 (Rechnung). **Strang:** Quarkmassen; offene Stelle aus H197.
**Anlass:** „probiere beides" des Autors (27.11., 10:55), Richtung 1b: Lauf der Kopplungen.

## Worum es geht
H197 fand D/B = 1,009 ± 0,001 **bei M_Z**, und keine Symmetrie bei M_Z erzwingt das. Frage hier: Ist D ≈ B vielleicht kein
Zustand bei M_Z, sondern das Ergebnis des **Laufs** von einer höheren Skala? Dann wäre an einer hohen Skala μ* ein
symmetrieausgezeichneter Wert (D/B ∈ {0, ⅓, −1}) erreicht, und das Herunterlaufen zu M_Z erzeugte D ≈ B.

## Modell
Die Massenformel m_s(k) = [A l_k + B l_k² + s(C l_k + D l_k²)]/(l_i+l_j)² bindet A,B,C,D an die **sechs Quarkmassen** bei einer
Skala. Die Quarkmassen (Yukawa-Kopplungen y_i = m_i/v) laufen mit den SM-Renormierungsgruppengleichungen (1-Schleife). Ich
laufe die sechs y_i von M_Z aufwärts, fitte an jeder Skala μ die vier Koeffizienten (A,B,C,D) neu und verfolge **D/B(μ)**.

Wichtig: Innerhalb eines Sektors sind die Massen**verhältnisse** bei 1-Schleife fast skaleninvariant — der gemeinsame
QCD-Faktor kürzt sich. Beweglich ist vor allem das Up-Sektor-Verhältnis über die **Top-Yukawa** (3/2)y_t²; die leichten
Quarks und der Down-Sektor laufen fast nur über die universellen (kürzenden) Terme. D/B(μ) kann sich also bewegen, aber
voraussichtlich schwach.

## Teile und Kriterien
- **H199a (nicht blind).** 1-Schleifen-SM-RGEs für g₁,g₂,g₃ und die sechs Yukawas (mit Top-Dominanz) von M_Z bis zur
  Planck-Skala integrieren; Kontrolle: Massenverhältnisse innerhalb eines Sektors bei 1-Schleife bis auf den Top-Term stabil.
- **H199b (Test — läuft D/B zu einem Symmetriewert?).** D/B(μ) für μ von M_Z bis 10¹⁹ GeV.
  - **„ja, Lauf erklärt D=B":** D/B(μ) erreicht an einer endlichen Skala μ* ≤ M_Planck einen symmetrieausgezeichneten Wert
    (0, ⅓ oder −1) **innerhalb 2σ**, und die restlichen Koeffizienten sind dort einfacher (z. B. C = 0 oder D = 0). Dann ist
    D ≈ B bei M_Z der heruntergelaufene Rand eines symmetrischen Hochskalen-Zustands.
  - **„teilweise":** D/B(μ) bewegt sich merklich (> 10 %) in Richtung eines Symmetriewerts, erreicht ihn aber nicht bis zur
    Planck-Skala.
  - **„nein":** D/B(μ) bleibt über alle Skalen nahe 1 (Bewegung < 10 %); der Lauf ist nicht die Quelle.
- **H199c (Bericht).** Welche Skala käme einem Symmetriewert am nächsten, und wie weit ist sie von bekannten Skalen (GUT
  ~10¹⁶, Planck ~10¹⁹) entfernt?

## Erwartung (offen gelegt)
Ich erwarte **„nein"**: Massenverhältnisse laufen bei 1-Schleife schwach, der Haupteffekt (Top-Yukawa) verschiebt nur das
Up-Sektor-Verhältnis um wenige Prozent über 17 Dekaden; D/B bliebe nahe 1, fern von 0, ⅓, −1. Ein echter Gegenbefund wäre,
wenn D/B an einer physikalisch bedeutsamen Skala exakt einen Symmetriewert träfe — das wäre ein starker Hinweis auf eine
Hochskalen-Symmetrie. Darum lohnt die Rechnung trotz der Erwartung.

## Werkzeuge
Python (numpy, scipy.integrate für die RGEs, Fit wie in k406); Wolfram Language zur Gegenprobe der RGE-Koeffizienten /
eines Laufpunkts. Qiskit nicht nötig.

## Vorwissen geprüft
- `.../symmetrie_db_h197/` (H197, k406): D/B = 1,009 ± 0,001 bei M_Z; Fit-Code und Daten (M_Z-Yukawa, k376).
- `.../ladung_zaehler_h196/` (H196): Modell und Parameter.
- Memory: Nachrechnung k358 — Empfindlichkeiten bei M_Z; kein Lauf bisher geprüft für die Quarks.
- Bilanz_Feldgleichung_2026_11_27.md: Gesamtstand (Koeffizienten frei).

## Grenzen (vorab)
1-Schleifen-SM-RGEs (2-Schleife nur falls 1-Schleife knapp an einem Symmetriewert vorbeiläuft). Keine Schwellen-Feinheiten
(grobe Flavour-Schwellen). Die Zuordnung Paar→Generation (Permutation B) und das Vakuum bleiben fest; nur die sechs Massen
laufen. OP3/OP4 bleiben offen; kein Guard berührt.
