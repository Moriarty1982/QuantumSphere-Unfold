# Vorab-Notiz H3: Triolen-Vorzeichen als Majorana-CP-Parität

Festgelegt am 2026-10-20, **vor** der Berechnung von m_ββ aus diesem Ansatz. Baut auf H2 auf
(`Vorab_Notiz_H2_Neutrino_Triole.md`, Commit 434c5a8; Ergebnis K14) und auf K14.4.

## Herkunft

K14.4: Alle geladenen Dreiergruppen liegen im positiven Bogen (e₃ > 0), die Neutrinos jenseits der Grenze π/12
(e₃ < 0). Die Neutrinos sind die einzigen Fermionen, die Majorana-Teilchen sein können. Das Vorzeichen von √m ist
in der Standardphysik nicht beobachtbar (m = v²). H3 gibt ihm deshalb **per Ansatz** eine physikalische Rolle.

## Hypothese

**H3 (V):**
(a) e₃ < 0 ⇔ Majorana. Die Neutrinos sind Majorana-Teilchen, die geladenen Fermionen Dirac-Teilchen (für Letztere
durch Ladungserhaltung ohnehin erzwungen, also kein Beleg).
(b) Die CP-Paritäten der Majorana-Massen sind die Triolen-Vorzeichen: m_k^phys = sign(v_k) · v_k². Aus H2 (NO):
η₁ = −1, η₂ = η₃ = +1. Weitere Majorana-Phasen gibt es nicht.

## Offenlegung vor der Festlegung

Grobe Kopfrechnung vor dieser Notiz mit den H2-Massen: Die drei Beiträge zu m_ββ sind etwa 0,24 meV (m₁),
2,6 meV (m₂) und 1,1 meV (m₃). m_ββ liegt also im Bereich weniger meV, unterhalb der Reichweite aller geplanten
Experimente. Das Vorzeichen η₁ ändert m_ββ nur um etwa 0,5 meV. H3 wird trotzdem so festgelegt; das Ergebnis
ist eine Vorhersage für die ferne Zukunft, kein heutiger Test.

## Daten (verbindlich)

NuFIT 6.0 (arXiv:2410.05380), Tabelle 1, „IC24 with SK atmospheric data“, normale Ordnung:
sin²θ₁₂ = 0,308 (+0,012/−0,011), sin²θ₁₃ = 0,02215 (+0,00056/−0,00058), δ_CP = 212° (+26/−41).
Massen aus H2 mit den Δm²-Werten der H2-Notiz.

## Verfahren (verbindlich)

m_ββ = | η₁ c₁₂² c₁₃² m₁ + η₂ s₁₂² c₁₃² m₂ + η₃ s₁₃² m₃ e^{−2iδ_CP} |, PDG-Konvention.
- Zentralwert mit δ_CP = 212°.
- Monte Carlo (10⁵, Gauß, asymmetrische Fehler gemittelt) über Δm², sin²θ₁₂, sin²θ₁₃, δ_CP.
- Zusätzlich der volle Bereich über δ_CP ∈ [0°, 360°).
- Vergleich: dasselbe mit η₁ = +1 (zeigt, was das Vorzeichen ausmacht).
- Zusätzlich m_β = (Σ |U_ek|² m_k²)^{1/2} (vom Vorzeichen unabhängig, folgt aus H2).

## Entscheidungskriterium (verbindlich)

- Heute: verträglich, wenn m_ββ unter der KamLAND-Zen-Grenze (28–122 meV, 90 %) liegt.
- **Widerlegung von H3** (bei Zutreffen von H2 und Austausch leichter Neutrinos): (i) Nachweis, dass Neutrinos
  Dirac-Teilchen sind; oder (ii) ein bestätigtes 0νββ-Signal mit m_ββ über der oberen 95 %-Grenze der
  Vorhersage über den vollen δ_CP-Bereich, unter Berücksichtigung der Kernmatrixelement-Spanne.
- **Kein Test des Vorzeichens selbst**, solange m_ββ nicht auf besser als den Unterschied η₁ = ±1 gemessen
  werden kann. Das wird ausdrücklich so festgehalten.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
