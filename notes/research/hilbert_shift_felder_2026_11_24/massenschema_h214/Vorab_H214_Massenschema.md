# Vorab-Notiz H214 (k427): Welches Massenschema gilt für x_lepton — Pol- oder laufende Massen?

**Datum:** 2026-11-27 (vor der Rechnung committet). **Strang:** 3 (Lepton-Massen/Mischung), Fortsetzung nach H213.
**Anlass:** Autor 27.11., 19:32: „dann nimm das massenschema“. H213c zeigte: laufende Massen bei M_Z verschieben x_lepton um +0,6σ(x_ν)
(Abstand zu x_ν 1,22σ statt 1,78σ). Welches Schema meint der Rahmen?
**Nummern:** H214, k427 (gegen `main` geprüft).

## Frage
Lässt sich aus dem Rahmen begründen, ob x_lepton aus Polmassen oder aus laufenden Massen zu bilden ist? Und kann irgendein zulässiges
Schema den 1,78σ-Abstand zu x_ν schließen?

## Vorwissen geprüft
- `generationszahl_h138/Ergebnis_H154_Unteralgebra_und_Abweichung.md`: **Koide gilt für Polmassen** (K = 0,666664, 0,43σ unter ⅔, ganz aus σ(m_τ));
  an einer gemeinsamen Skala verschiebt QED K um ≈ +1,2·10⁻³ (≈ 225σ), fast skalenunabhängig; mit jeweils eigener Skala fällt der gemeinsame Faktor heraus.
- H1/k14 (über H172): laufende Massen bei M_Z geben K = 0,6678.
- `delta_h166/Ergebnis_H166_...`: unter Postulat J (K = ⅔) ist δ* = 0,2222220471; „für welche Massendefinition die Beziehung gilt, verschiebt mehr“.
- `versatz_spannung_h213/`: x_lepton(Pol) = 0,0395746, x_lepton(M_Z) = 0,040762 (mit freier Amplitude a = 1,41689 ≠ √2), x_ν = 0,043359 ± 0,00213.
- `analysis/Coupling_Physical_Origin_Diagnosis.md`: einschleifige QED-Beziehung Pol/laufend (Sumino), δ(m_i/m_τ)/(m_i/m_τ) = (3α/2π) ln(m_τ/m_i) an gemeinsamer Skala.
- Memory/Bilanz: K_ν = K_e = ⅔ im Rahmen geschützt (H178–H182, Postulat J / Zählregel).

## Nicht blind (offen gesagt)
**Teil a ist nicht blind:** Dass nur Polmassen K = ⅔ erfüllen, steht in H154. Er wird hier als Auswahlkriterium des Rahmens festgehalten und nachgerechnet.
**Teile b, c, d sind blind.**

## Teile und Entscheidungskriterien
**a (nicht blind) — Kriterium des Rahmens.** Der Rahmen setzt K = ⅔ exakt (Amplitude a = √2 in √m_k = μ(1 + a cos(δ + 2πk/3))); x ist nur in einem
Schema definiert, in dem diese Form gilt. Zulässig ist ein Schema, wenn |K − ⅔| ≤ 2σ_K (σ_K aus den Massenfehlern).
Geprüft: Pol, laufend an gemeinsamer Skala μ = M_Z (Xing–Zhang–Zhou 2008), laufend an gemeinsamer Skala μ = m_τ (einschleifige QED aus Pol).

**b (blind) — laufend, je eigene Skala m̄(m̄).** Einschleifige QED-Umrechnung M = m̄(M)(1 + α(M)/π) mit dem laufenden α am jeweiligen Massenwert.
Ist das Schema zulässig (Kriterium a), und wie weit verschiebt es x_lepton gegenüber Pol (in σ(x_ν))?

**c (blind) — Rückwärtssuche.** Welche Massenverhältnisse verlangt x = x_ν bei K = ⅔? Relative Änderung von m_e/m_μ und m_μ/m_τ gegenüber Pol.
Vergleich mit der größten Verschiebung, die ein **zulässiges** Schema (a, b) erzeugt.
Kriterium: Ist die verlangte Änderung mehr als zehnmal größer als jede zulässige Schema-Verschiebung ⇒ „kein zulässiges Schema schließt den Abstand“.

**d (blind) — Neutrino-Seite.** Wie stark hängt R (und damit x_ν) vom Schema/von der Skala ab? Einschleifiges SM-Laufen des Weinberg-Operators
(nicht-universeller Anteil ∝ C y_τ², C = −3/2) zwischen M_Z und niedriger Skala. Kriterium: |Δx_ν| < 0,1 σ(x_ν) ⇒ R ist schemafest, die
Neutrino-Seite liefert „physikalische“ (polartige) Massenverhältnisse; der gleichartige Vergleich verlangt dann Polmassen auch bei den Leptonen.

## Gesamturteil (vorab festgelegt)
- **trägt (Pol ist das Schema des Rahmens):** a lässt nur Pol (und gegebenenfalls b) zu, b verschiebt x um < 0,3σ(x_ν), d bestätigt Schemafestigkeit von R.
  Dann ist H213c (M_Z) keine zulässige Lesart, der maßgebliche Abstand bleibt 1,78σ, und nur bessere R-Daten (JUNO) entscheiden.
- **trägt teilweise:** a lässt mehr als ein Schema zu und diese unterscheiden sich in x um ≥ 0,3σ(x_ν), oder d zeigt Schemaabhängigkeit von R.
- **widerlegt:** Polmassen verfehlen das Kriterium a.

## Werkzeuge
Python (`k427_test_h214.py` → `k427_out.txt`); Wolfram unabhängig (`k427b_gegenprobe.wl` → `k427b_out.txt`): K und δ je Schema exakt aus den
Massen, Rückwärtssuche (Massenverhältnisse bei x = x_ν). Qiskit nicht einschlägig.

## Grenzen
Einschleifige QED (zweischleifige und hadronische Beiträge nur abgeschätzt); M_Z-Werte aus der Literatur. Neutrino-Laufen nur einschleifig im SM.
Alles unter H99/Postulat J. Kein Guard berührt; OP3/OP4 offen.
