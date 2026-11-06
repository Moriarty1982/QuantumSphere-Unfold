# Erkundung: Dorau–Much, semiklassische Einstein-Gleichungen aus relativer Entropie

**6. November 2026. Status: Erkundung (Literaturauswertung), keine Rechnung, kein Kriterium.** Anlass: Hinweis des Autors auf die
Pressemeldung phys.org (Oktober 2026, „Gravity and quantum linked …“). Ausgewertet nach Lesen von arXiv:2510.24491v3 (HTML-Fassung
und erste PDF-Seite). Die Formeln unten folgen dieser Fassung; eine Nachrechnung hat nicht stattgefunden.

## Quelle
P. Dorau, A. Much (Institut für Theoretische Physik, Universität Leipzig), *From Quantum Relative Entropy to the Semiclassical Einstein
Equations*, Phys. Rev. Lett. **136**, 091602 (2. März 2026), DOI 10.1103/lmq8-nsty, arXiv:2510.24491 (v1 Oktober 2025 unter dem Titel
„Quantum Relative Entropy implies the Semiclassical Einstein Equations“, v3 3. März 2026). Lokale Kopie, nicht versioniert (`*.pdf`
ignoriert): `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf`.

## Was das Paper zeigt
1. **Lokale Geometrie.** Kleine Umgebung eines Punktes, Metrik ≈ Minkowski (Äquivalenzprinzip, führende Ordnung). Boost-Killingfeld ξ,
   null und tangential auf zwei Nullflächen: lokaler Rindler-Horizont (Jacobson 1995).
2. **Feld und Zustände.** Reelles, minimal gekoppeltes Klein–Gordon-Feld der Masse m (CCR-Algebra). Referenzzustand ω₀ quasifrei,
   boost-invariant, Hadamard (Rindler: Minkowski-Vakuum). Nur **kohärente** Anregungen ω_φ.
3. **Relative Entropie (Araki–Uhlmann).** Die Modulargruppe wirkt geometrisch als Boost (Δ^{it} = Boost um 2πt, Bisognano–Wichmann bzw.
   Summers–Verch; KMS bei β = 2π/κ). Damit
   S_rel(ω₀‖ω_φ) = −2π ∫ U ⟨:T_ab:⟩_φ ξ^a ξ^b dU dS,
   also der Energiefluss über den Horizont. Das ist der eigentliche Beitrag; er ersetzt Jacobsons heuristisches δQ.
4. **Geometrie.** Raychaudhuri mit verschwindender Expansion, Scherung und Rotation am Horizont: δA = −∫ U R_ab ξ^a ξ^b dU dS.
5. **Gesetzt, nicht hergeleitet:** S_rel = δA/4 (Bekenstein–Hawking). Daraus α = 8π (Einheiten G = 1); G kommt also über diese Annahme.
6. **Ergebnis.** Für alle Nullrichtungen α⟨T_ab⟩ = R_ab + N g_ab; Erhaltung von ⟨T⟩ und kontrahierte Bianchi-Identität geben
   N = −R/2 + Λ, also G_ab + Λ g_ab = 8π ⟨:T_ab:⟩. **Λ ist Integrationskonstante, ausdrücklich beliebig.**

Grenzen nach den Autoren: „arguments indicating“, führende Ordnung, nur kohärente Zustände, nur Skalarfeld; höhere Ordnungen
(Riemann-Normalkoordinaten) und nicht-kohärente Zustände offen. Ausblick: Verbindung zur Quanten-Null-Energie-Bedingung über
halbseitige modulare Inklusionen.

## Einordnung
Seriöse Arbeit, kein „wildes Zeug“. Die Pressemeldung („aus der Vakuumenergie“) verkürzt: Das Vakuum ist **Bezugszustand** der relativen
Entropie, keine Energiequelle. Erklärt werden weder G (steckt im Flächengesetz) noch Λ (frei).

## Bezug zum Companion
(a) **Λ frei.** Deckt sich mit v4.10.0-r03 und r05 (unter G2 kein Λ aus der Dynamik, Λ = a·V_min frei; Λ als Auslesung). Auch die
Standardherleitung legt Λ nicht fest. Das bestätigt die Einordnung „Λ nicht Teil der Dynamik“, ist aber kein Treffer des Companion.

(b) **Vorzeichen der Gravitation.** Bei Dorau–Much folgt α > 0 aus S_rel ≥ 0 und dem positiven Flächengesetz; das Vorzeichen ist nicht
frei. In v4.10.0-r01 musste das Vorzeichen von W1 von Hand korrigiert werden (W1 wie notiert stieß ab). Eine Herleitung nach diesem Muster
würde das Vorzeichen aus einer Positivität begründen statt aus einer Autorentscheidung. Nur Beobachtung, nicht geprüft.

(c) **Flächengesetz = Horizontzählung.** Genau die gesetzte Annahme S_rel = δA/4 ist die Stelle, an der r63–r68 ansetzen (Zählregeln
ABCK j = ½ für T, DL/Meissner für M; γ_ABCK = 0,127384, γ_DL/M = 0,237533; Literatur bevorzugt SU(2), γ ≈ 0,274; Nachrechnung
`llm/Nachrechnung_r63_r67.md`). Eine frame-abhängige Zählung änderte α, also den Vorfaktor, nicht G selbst; das passt zu r64
(Frame-Unterschied in γ, nicht in ħ, G).

(d) **Referenzzustand und Frames.** ω₀ muss boost-invariant und Hadamard sein; im Companion hat R (r24 Bezugsframe, r29 Vakuum als Quelle
des Tachyon-Bezugszustands) diese Rolle. Offen: Unter der Tachyon-Abbildung z → iz wird die Rapidität imaginär, aus dem Boost eine
Drehung. Dann ist der Modularfluss keine reelle Einparametergruppe von Boosts mehr, und die KMS-Struktur bei β = 2π/κ ist fraglich.
Vermutung: Die Herleitung gilt im M-Frame (und in R), nicht ohne Weiteres im T-Frame. Das wäre der eigentliche Prüfpunkt.
**Nachtrag (7.11.):** „Drehung, also keine Thermik“ ist zu schnell. Die KMS-Periode β = 2π ist im euklidischen Bild gerade der volle
Drehwinkel 2π (Unruh über Wick-Rotation). Der Companion hat diese Brücke selbst: thm:artqft (Wick-Rotation t ↦ iτ_E am Biquaternion).
Ob z → iz mit dieser Wick-Rotation zusammenfällt, ist offen; wenn ja, ist der T-Frame die euklidische Seite derselben KMS-Struktur, nicht
ihr Verlust.

(e) **Torsion.** Die Herleitung gibt Riemann-Geometrie (Levi-Civita, Skalarfeld ohne Spin). W1 ist Einstein–Cartan mit Torsion
+(3/16)κ j² aus dem Spinorstrom (v4.10.0-r01). Für einen Vergleich bräuchte es die Erweiterung auf Dirac-Felder; die Autoren behandeln sie
nicht.

## Frames (Konvention F, sinngemäß)
- Materie M: Herleitung gilt wie im Paper (reelle Boosts, KMS).
- Tachyon T: offen, siehe (d).
- Photon P: entarteter Fixpunkt; kein eigener Befund.
Frame-frei ist die Aussage damit nicht.

## Mögliche nächste Schritte (nicht begonnen)
1. Prüfen, ob unter z → iz eine KMS-Bedingung für den Tachyon-Bezugszustand existiert (Erkundung oder, mit Kriterium, Test mit
   Vorab-Notiz).
2. Positivitätsargument (b) auf W1 übertragen: Folgt das in v4.10.0-r01 korrigierte Vorzeichen aus S_rel ≥ 0?
3. Bei Interesse als Runde v4.10.0-rNN einbauen (Literaturbezug plus Statusvermerk-Kandidat zu Λ).
