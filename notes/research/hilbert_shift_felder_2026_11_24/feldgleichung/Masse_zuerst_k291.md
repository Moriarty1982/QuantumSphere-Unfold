# Keine Masse auf HS(0) und HS(1): wo sie im Ansatz zuerst entsteht (Erkundung k291, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Der Ansatz k290 kommt auf HS(0) und HS(1) ohne Massenterm aus, wenn ω als Wellenfrequenz (ω = |k|) statt als Masse gelesen wird. Eine
Ruhemasse im strengen Sinn, also die Ruheenergie einer gebundenen, ortsfesten Lösung, kann in drei Raumdimensionen erst bei HS(2) entstehen: Der Flächenterm K₁ verschwindet
auf dem Kreis S¹ identisch und ist auf S³ genau der Skyrme-Term, und nur S³ trägt Knoten mit Windungszahl. HS(1) hat dagegen zwei Arten von **Protomasse**, die
nicht gebunden sind. Welche Lesart gilt (Urknall bei HS(1) oder HS(2)), hängt an einer einzigen Größe: ob die Norm f des Felds schon bei HS(1) festliegt.

Auftrag des Autors (25.11.2026): „aus HS(0) und HS(1) dürfte es Masse erstmal nicht im strengeren Sinne geben“, danach: HS(1) könnte „quasi schon eine Protomasse“
sein, je nachdem, ob der Urknall bei HS(1) oder HS(2) angesetzt wird; das Licht oder eine Vorform könnte dort schon eine Idee von Masse haben, es braucht aber den nächsten
Schritt. **Erkundung, nicht blind:** Derrick-Skalierung, Skyrme-Igel, Stückelberg-Masse und die elektroschwache Massenmatrix sind Standard. Neu ist nur die Zuordnung zum
Turm, und die ist eine Lesart. Keine H-Nummer, keine Runde. Vergeben: Skripte **k291, k291b**. Nachtrag zu k290 (`README.md`), das dort Geschriebene bleibt stehen.

Werkzeuge: Python mit sympy (exakt) und scipy (Igel-Profil durch Minimierung). Wolfram Language unabhängig mit Quaternionen als 2×2-Matrizen und einem
Schießverfahren für das Igel-Profil (k291b). Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
k253 (HS(0) als Linie ohne Zeitrichtung, HS(1) als Ellipse mit Ladung ω(a² − b²), HS(2) mit erster Holonomie, „Urknall bei HS(2)“; lineare Polarisation am Äquator,
Kreisanteile an den Polen), k246 (Holonomie braucht mindestens drei Dimensionen), k250, k251 (Λ und Drehrate), k272 (Amplitude, Frequenz, Phase frei), k274 (Duffing),
`licht_vermittler_zeit_2026_11_24/`, k290. Der HC als Normalisierer ab dem ersten Shift steht in `v470/07_qam_infrastructure.tex` (gesetzt).

## Anpassung des Ansatzes
- **L₀ und L₁ ohne Massenterm:** μ₀ = μ₁ = 0. Die Regel ψ̈ = −ω²ψ gilt weiter an jedem Ort, jetzt als Gleichung einer Welle mit ω = |k| (k291 A). Die Ellipse
  a·e^{i(ωt − kx)} + b·e^{−i(ωt − kx)} löst □ψ = 0. Für a = b ist sie eine reelle Welle (HS(0), lineare Polarisation), die Ladungsdichte ω(a² − b²) misst den Drehsinn.
- **Was in k290 „Vorzeichen von μ²“ hieß**, ist auf HS(0) und HS(1) dann kein Parameter mehr. Es wird zur Frage, ob das Feld eine feste Norm f hat (Variante B unten).

## Ergebnisse
1. **K₁ auf fester Norm (k291 B, k291b V1–V5):** Auf S¹ ist K₁ ≡ 0, weil der Zielraum eindimensional ist. Auf S³ ist K₁ nicht null, und 4·K₁ ist genau der
   Kommutator der Ströme, also der Skyrme-Term (symbolischer Nullrest der Differenz). Der Term, der bei HS(1) eingeführt wird, wirkt bei fester Norm also erst bei HS(2).
2. **Derrick (C, V6):** In drei Raumdimensionen verlangt eine ruhende lokalisierte Lösung E₄ = E₂ + 3E₀. Ohne Term vierter Ordnung in den Ableitungen gibt es keine.
   Auf HS(0) (kein K-Term) und auf S¹ (K₁ = 0) zerläuft jede Anhäufung.
3. **Ruhemasse bei HS(2) (D, V7):** Der Igel auf S³ hat die Ruheenergie M ≈ 103,2·f·√c₁. Das Verhältnis zur Schranke 6√2π² ist 1,2325 (Python, Gitter) und 1,2298
   (Wolfram, Schießverfahren), der Literaturwert des Skyrme-Igels ist 1,2315. Die Masse entsteht aus der Amplitude f und dem Koeffizienten c₁, ohne Massenterm.
   Standard-Homotopie (nicht gerechnet): π₃ ist null für S⁰, S¹ und S⁷ und ℤ für S³. Knoten mit Windungszahl gibt es in drei Raumdimensionen nur bei HS(2).
4. **Protomasse 1, ohne feste Norm (G, V9):** Eine einzelne laufende Welle ist lichtartig (E² − P² = 0). Zwei Laufrichtungen geben E² − P² = 4A²B²k⁴ > 0. Das ist eine
   invariante Masse aus Licht, aber nicht gebunden (Punkt 2).
5. **Protomasse 2, feste Norm f bei HS(1) (E):** Wird die U(1) geeicht, bekommt das Eichfeld die Masse m_A = e·f, und es bleibt kein masseloses übrig.
6. **Der nächste Schritt (H, V8):** Auf HS(2) mit fester Norm f, SU(2) links und U(1) rechts geeicht, sind die Massenquadrate g²f²/4 (zweimal), (g² + g′²)f²/4 und **0**.
   Die masselose Mischung ist g′W₃ + gB. Erst hier gibt es wieder masseloses Licht neben massiven Eichfeldern, mit m_W²/m_Z² = g²/(g² + g′²). Das ist die
   bekannte elektroschwache Massenmatrix. Dass sie herauskommt, liegt an der so(4)-Symmetrie von L₂ ohne K₂ (k290, Zeile „kinetisch, V(N), K₁“ bei n = 2).

## Die zwei Lesarten
| | A: Urknall bei HS(2) | B: Urknall bei HS(1), Protomasse |
|---|---|---|
| Norm bei HS(1) | frei, Vakuum ψ = 0 | fest, N(ψ) = f² |
| Licht bei HS(1) | masselos | massiv, m_A = e·f (wenn die U(1) geeicht ist) |
| Protomasse | nur E² − P² gekreuzter Wellen | m_A und dieselbe Skala f |
| Skala f | entsteht erst bei HS(2) | wird von HS(1) geerbt |
| Ruhemasse bei HS(2) | M ≈ 103,2·f·√c₁ | dieselbe Formel, dazu M/m_A = 103,2·√c₁/e ohne freie Skala |
| masseloses Licht bei HS(2) | ja | ja, als Mischung g′W₃ + gB |

**Was sie unterscheidet:** In B liegen zwischen der Protomasse von HS(1) und den Massen von HS(2) nur reine Zahlen (e, g, g′, c₁), in A ist f eine neue Größe des
zweiten Schritts. B trifft die Beschreibung des Autors genau in einem Punkt: Das Licht von HS(1) hat schon eine Masse, und erst der nächste Schritt stellt den beobachteten
Zustand her (masseloses Licht, massive Partner). B verlangt aber, dass die U(1) von HS(1) nicht die spätere elektromagnetische ist, sondern in sie eingeht (wie die Hyperladung).
Ob der HC, der ab HS(1) dazukommt, mit der festen Norm zu tun hat (er ist als Normalisierer gesetzt), ist eine naheliegende Frage und hier nicht geprüft.

## Grenzen
- Lesart, keine Herleitung. Die elektroschwache Struktur ist nicht vorhergesagt, sie ist mit der Wahl „SU(2) links, U(1) rechts, feste Norm“ hineingesteckt. Hergeleitet ist nur,
  dass der Ansatz sie zulässt und dass die so(4) dafür aus k290 stammt.
- Die feste Norm f ist eine Setzung (in B bei HS(1), in A bei HS(2)). Woher f kommt, ist offen. k272 ließ die Amplitude frei.
- Der Igel ist nur im Kugelansatz gerechnet. Stabilität gegen andere Verformungen, Quantisierung und die Zuordnung zu Teilchen sind nicht geprüft.
- Mit K₂ (c₂ ≠ 0, gebaut aus D_μψ) fällt die so(4) auf die diagonale SU(2), und Punkt 6 gilt nicht mehr. Die Bauart der Zusatzterme (k290) entscheidet also mit.
- Mischungswinkel, Kopplungen und f sind freie Parameter. OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **HC und feste Norm:** prüfen, ob die Normalisierer-Rolle des HC (QAM, erster Randschritt) die Bedingung N(ψ) = f² liefert. Das würde zwischen A und B entscheiden.
- **HS(3):** Auf S⁷ gibt es keine Knoten (π₃ = 0). Was mit dem Igel beim Schritt ℍ → 𝕆 geschieht, ist die nächste Rechnung.

## Dateien
`k291_masse_zuerst.py` (`k291_out.txt`, Laufzeit etwa eine Minute), `k291b_gegenprobe.wl` (`k291b_out.txt`).
