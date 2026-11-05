# Erkundung: Liefert der Shift eine vierte String-Stufe der Konnektoren? (k186, I1)

**5. November 2026. Status: Erkundung. Als H75 geplant; beim präzisen Aufschreiben in Lichtkegelkoordinaten (q² = u·v) wurde das Ergebnis vor der Rechnung analytisch sichtbar, deshalb nicht als blinder Test geführt.**

## Frage
Die drei Konnektoren aus k185 haben q² = −2m² sinh 2η, 0, +2m² sinh 2η, wie die String-Stufen N = 0, 1, 2. Liefert eine Σ-Verkettung (Impulssumme, r39) zweier Konnektoren für jedes η die vierte Stufe q² = +4m² sinh 2η?

## Ergebnis
q²/(m² sinh 2η) aller Σ-Verkettungen bei η ∈ {0,1; 0,3; η_sym; 1; 1,5}:
- c0 + c0 = −8 und c2 + c2 = +8 für alle η; das ist (2q)² = 4q², also derselbe Konnektor mit doppeltem Impuls, keine neue Stufe.
- c1 + c1 (gleiche Sorte) = 0.
- Alle übrigen Verkettungen hängen von η ab, zum Beispiel c1b + c2 = 3,80 … 2,19.
- **Die vierte Stufe +4 kommt in keiner Verkettung für alle η vor.**
- Auffällig: c0 + c2 und c1a + c1b geben exakt q² = 4m², unabhängig von η. Das ist die Paarschwelle (2m)², zwei Teilchen der Masse m in Ruhe.

Frame-Fortsetzung η → η + k·iπ/2: Sie ist **zyklisch der Ordnung 4** (p_M → p_T → −p_M → −p_T → p_M). Die Konnektoren zwischen p_M und seinen Bildern haben nur q² ∈ {0, 4m²}; zusammen mit den Richtungsumkehrungen aus k185 bleibt die Menge endlich: {−2m² sinh 2η, 0, +2m² sinh 2η, 4m²}.

## Lesart
- **Die Parallele zu den String-Stufen besteht diese Prüfung nicht.** Mit Σ-Verkettung entsteht keine gleichabständige vierte Stufe. Physikalisch ist das erklärbar: Impulse addieren beschreibt Zwei-Teilchen-Zustände (ein Kontinuum mit Schwelle 4m²), keine höheren Anregungen eines einzelnen Strings.
- **Die Frame-Struktur hat keinen unbeschränkten Turm.** Ihre Fortsetzung ist zyklisch der Ordnung 4, entsprechend den D₄-Frames der Ablage. Ein String-Turm bräuchte einen unbeschränkten Aufsteige-Operator. Der QAM-Hilbert-Shift i → i + 1 wäre ein solcher, er ist aber eine Umbenennung von Tags und wirkt nicht auf Impulse. Eine physikalische Wirkung des QAM-Shifts als Aufsteige-Operator ist nicht gezeigt.
- Was bleibt: die drei Konnektoren (tachyonisch, masselos, massiv) und die Paarschwelle 4m². Ob die Ähnlichkeit zu N = 0, 1, 2 mehr als ein Zufall dreier Zahlen ist, bleibt offen. Mit den vorhandenen Bausteinen lässt sie sich nicht fortsetzen.
- Die Parallele „Tachyon auf dem reservierten Leerplatz“ (QAM, I1) bleibt als Lesart stehen; sie macht keine Vorhersage.

## Nachtrag (5.11., Autor: „der Shift geht ab dem 2. Mal mit 2^k weiter“)
- Der doppelte Hilbert-Shift (Teil 07, `def:v3360-r16-double-hilbert-shift-route-mask-convention`) ist H₀(k) = k + 1, H₁(a) = 2^{a−1}, zusammen H_mask(k) = 2^k. Ab dem zweiten Schritt wächst er geometrisch. Gesucht war oben ein linearer String-Turm; das war für den Shift die falsche Erwartung.
- Mit dieser Lesart passt k186: Die Selbstverkettung verdoppelt den Impuls (c0 + c0 = 4·c0, c2 + c2 = 4·c2 in q², für jedes η). In Massen heißt das μ_k = 2^k·μ₀, also genau H_mask.
- **Einschränkung:** Dieser Turm ist allgemein, denn 2^k gleiche, kollinear laufende Quanten haben bei jedem Teilchen die Masse 2^k·μ. Er ist mit dem Shift verträglich, unterscheidet aber nichts.
- **Unterscheidender Test (Kandidat H75):** gemischte Masken (zum Beispiel 2⁰ + 2² = 5). Die Verkettungen verschiedener Konnektoren sind fast alle η-abhängig; Ausnahme ist c0 + c2 = 4m² (Paarschwelle, η-unabhängig). Vorab festlegen, welcher Konnektor welches Bit trägt, dann prüfen, ob genau die zulässigen gemischten Masken η-unabhängige Werte ergeben.
