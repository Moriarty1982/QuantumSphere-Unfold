# Bilanz: Wie die allgemeine Feldgleichung jetzt aussieht (Stand 27.11.2026)

Zusammenfassung des Standes nach den Tests H183–H197 (Skripte k387–k406), auf Wunsch des Autors („zurück zur
Hauptrechnung: was haben wir gelernt, wie sieht die Feldgleichung aus"). Knapp und verständlich; die Einzelnachweise
stehen in den jeweiligen Test-Ordnern unter `notes/research/hilbert_shift_felder_2026_11_24/`.

---

## 1. Die Feldgleichung in ihrer jetzigen Form

**Bühne.** Ein einziges Feld Ψ in der komplexifizierten Albert-Algebra **ℂ ⊗ H₃(𝕆)** (3×3-hermitesche Matrizen über den
Oktonionen, die ausnahmehafte Jordan-Algebra; Automorphismengruppe F₄, mit der Ladung die Untergruppe). Ein Feld, N = 1.

**Vakuum.** Ein ruhendes, zirkulantes **Leptonvakuum W₀** mit den drei Diagonal-Eigenwerten
l = [0,04035, 0,58021, 2,37944] (aus δ = 2/9, so dass Tr W₀ = 3 und K = Σl²/(Σl)² = 2/3). Die **Leptonen** sitzen auf den
Diagonalrichtungen, die **Quarks** sind die Off-Diagonal-Oktonionmoden X in Position (i, j) — jede Mode gehört zu einem Paar
(l_i, l_j), der dritte Eigenwert heißt l_k.

**Potential.** F₄-invariant, ein Polynom in den Jordan-Invarianten (Tr, e₂ = Σl_il_j, e₃ = det). Grad bis **mindestens 5**:
Das in den Quarkmassen gebrauchte l_k²-Glied erscheint in der Krümmung **erst ab Potentialgrad 5** (unter Grad 5 nur
linear in l_k). Welche Invarianten mit welchen Koeffizienten — **frei**.

**Kinetischer Term.** Eine W²-gewichtete kinetische Norm. Über die Peirce-Zerlegung gilt exakt W₀∘X = ½(l_i+l_j)·X, also
N₂ = ¼(l_i+l_j)²·N₀ — das liefert den **Nenner (l_i+l_j)²** der Massenformel ohne Einsetzen von Hand.

**Ladungsterm.** Die komplexe Konjugation / der Frame-Tausch J bildet den Ladungsoperator Q₀ auf 1−Q₀ ab. Im Farbblock
lässt J **genau eine** ladungsungerade hermitesche Form zu: **h = Ψ†(Q₀−½)Ψ**. Up (Ladung ⅔) und Down (Ladung ⅓)
unterscheiden sich dadurch nur im **Vorzeichen** s = ±1 dieses Terms.

**Massenformel der Quarks** (Krümmung / kinetische Norm, je Generation k, Ladung s = ±1):

> **m_s(k) = [ A·l_k + B·l_k² + s·(C·l_k + D·l_k²) ] / (l_i + l_j)²**

A, B ladungsgerade, C, D ladungsungerade (die „s·"-Terme). Für die **Leptonen** liefert dieselbe Struktur K_ν = K_e = ⅔
und den Fixpunkt 45°, bis Grad 4 unabhängig von den Koeffizienten.

---

## 2. Was davon hergeleitet ist (unter den Setzungen)

- **Das Muster der vier Sektoren** (H178, H182): zwei Lepton-Sektoren mit demselben K = ⅔; zwei Quark-Sektoren, deren Winkel
  frei und verschieden sein dürfen. J erzwingt die Gleichheit bei den Leptonen (farblose Ebene, J² = +1) und erlaubt den
  Unterschied bei den Quarks (Farbrichtungen, J² = −1). Dafür reicht HS(3) mit der Ladung; die Sedenionen werden nicht gebraucht.
- **Der Nenner (l_i + l_j)²** (H195): aus Peirce-Eigenwert ½(l_i+l_j) und der W²-gewichteten kinetischen Norm. Exakt verifiziert.
- **Der Ort des Up/Down-Unterschieds** (H182, H196): im Vorzeichen s eines ladungsungeraden Terms — nicht in getrennten Feldern
  oder Skalen.
- **Dass l_k² ein Potential vom Grad ≥ 5 braucht** (H195), und dass das ladungsungerade l_k² (D) schon bei Grad 4 existiert,
  unabhängig vom ladungsgeraden (H197).
- **Dass die H188-Form spezifisch an die geladenen Leptonen bindet** (H194): zufällige Eigenwert-Tripel reproduzieren beide
  Sektoren in 0,0 % — die leptonischen l_k sind ausgezeichnet, kein beliebiger Fit.

## 3. Was gesetzt oder angepasst ist

- **Das Vakuum** (K = ⅔, δ = 2/9, die drei l) ist eine Eingabe aus den Leptonen, keine Lösung der Quark-Dynamik.
- **Die Funktionsform** der H188-Massenformel wurde nachträglich gewählt (H194), nicht aus der Dynamik abgeleitet.
- **Alle Zähler-Koeffizienten A, B, C, D** (bzw. b/a je Sektor) sind freie Zahlen. Vier Parameter für sechs Massen treffen
  (χ² ≈ 8), sind aber eine Umparametrisierung von H194.
- **D ≈ B** („Down linear, Up quadratisch") ist **gefittet, nicht erzwungen** (H197): keine Symmetrie des Rahmens liefert es.
- Die Zuordnung Paar→Generation (Permutation B) ist gesetzt; δ je Quarksektor nicht behandelt.

---

## 4. Was die Tests gezeigt haben

**Strang A — „Quarks als Farbschwingungen um das Leptonvakuum" (H183–H190): als Massenquelle erschöpfend widerlegt.**
- **H183:** Lepton- und Quarkzustand sind nie zugleich Vakua eines Grad-4-Potentials (konvexes Programm, Grund: Vorzeichen b₂).
  → Der Autor wählte die Lesart „ein Vakuum, Sektoren schwingen".
- **H184/H185:** Zahl und Form der Farbschwingungen stimmen (drei Frequenzen je sechsfach; zwei Ladungssätze ⅓, ⅔), aber in
  F₄-invarianten Potentialen sind sie masselos; Up ≠ Down verlangt einen Term mit dem Ladungsoperator (H185d: Jordan-Spuren allein
  reichen nicht).
- **H186/H187:** Elf Ladungsterme bis Grad 4 spannen den Unterschied auf (keine Vorhersage), kein einzelner trifft die Daten;
  Adjunkte/Kreuzprodukt geben l_k, l_k², l_i l_j, aber keine Funktion trifft die sechs Massen (Down nie).
- **H188/H189/H190:** Ableitungsterme (ruhend null; bei bewegtem/drehendem Vakuum nur Ausbreitung, Ruhefrequenzen gleich für
  beide Ladungen); Generationsdrehung macht eine Frequenz klein, trifft aber Up nie (7,1σ). **Bilanz: Zahl und Form folgen, die
  Massen nicht.**

**Strang B — „Lesart wechseln: Quarks auf eigener HS-Stufe" (H192, H193): beide Gabeln geprüft.**
- **H192** (gemeinsame Geometrie, Bänder = HS-Stufen auf einer Sphäre): die Oktant-Struktur kommt (𝕆–𝕊 = 89,5°, stabil), die
  kleinen Winkel nicht (ℂ–ℍ läuft mit Gewicht/Gesetz). Teilweise.
- **H193** (getrennte Felder je Stufe): widerlegt — stufenfeste Verhältnisse Faktor 1–2 gegen beobachtet 20–589; freie Skala je
  Feld = sechs Zahlen für sechs Massen (inhaltsleer).

**Strang C — „gemeinsame Form aus der Feldgleichung" (H194–H197): der weiteste Stand.**
- **H194:** Die H188-Form bindet die Quarks spezifisch an die geladenen Leptonen (erste Quark-Lesart mit mehr als reinem Fit),
  aber die Form ist nachträglich gewählt.
- **H195:** Der **Nenner** folgt aus der kinetischen Struktur; der **Zähler** ist feldgleichungs-fähig (ab Grad 5), aber mit
  freien Koeffizienten, nicht vorhergesagt.
- **H196:** Der Ladungsterm verschiebt das l_k²-Glied wirklich (Up quadratisch, Down linear), aber als Umparametrisierung von
  H194 (vier freie Zahlen).
- **H197:** **Keine Symmetrie erzwingt D = B.** Das ladungsgerade l_k² (Grad 5) und das ladungsungerade (Grad 4) sind
  unabhängig; die einzige J-ausgezeichnete Ladungsform (Q₀−½) gäbe ein antisymmetrisches Glied (D/B = −1), nicht „Down aus". Die
  nötige Kopplung ist der Up-Typ-Projektor **P_up = 3(Q₀−⅓)**, und der ist nicht J-kovariant. Die Daten verlangen scharf
  D/B = 1,009 ± 0,001, fern von jedem symmetrienahen Wert.

**Nebenstränge (OP1 / Maschine, nicht die Quark-Feldgleichung).** k394–k396: Stellgrößen-Übersicht, selbstjustierende
HC-Schleife (Fixpunkt ½, nicht β_sym), Bandwechsel qualitativ. H191/k398/k399: Schleife über Spin-Bänder erzeugt die
Casimir-Fläche √(j(j+1)) nicht (Clebsch-Gordan-Abfall 1/k statt 1/k²); Primzahl-Rauschen wie Zufall; Geometrie-Erkundungen
(Möbius = Spinor-Vorzeichen, Clifford-Torus, Hopf-Faserungen). Ein paralleler Thread erkundet HS(−1) (k405).

---

## 5. Die eine offene Stelle

Der Rahmen liefert **Zahl, Form und Ort** der Sektoren, aber **nicht die Stärke** der Up/Down-Asymmetrie im quadratischen Glied.
Diese Stärke ist genau ein **Up-Typ-Projektor P_up = 3(Q₀−⅓)**: ein konkretes, benanntes Objekt, das der F₄/Ladungs-Baukasten
nicht aus einer Symmetrie erzeugt. H197 schließt die Baustein-Suche in diesem Rahmen ab: ein weiterer Term desselben Baukastens
lässt D/B nur weiter frei. Nötig ist eine **neue Eingabe**.

## 6. Offene Weggabelung (bleibt beim Autor)

- **(1a) P_up ↔ bekannte Projektgröße:** Hängt der Up-Typ-Projektor mit einer Projektion im HS-Turm oder der Oktantstruktur
  zusammen (etwas, das anderswo im Projekt schon trägt)?
- **(1b) Dynamik / Lauf der Kopplungen:** Entsteht D ≈ B erst aus dem Lauf von M_Z zu einer höheren Skala, statt an einem
  festen Punkt?
- **(ruhen)** Den Quark-Strang ruhen lassen und einen anderen Punkt der Liste vorziehen (Maschine, Rauschgenerator,
  Möbius/Sphäre).

**Status der offenen Probleme ehrlich:** OP3 und OP4 (Quarkzahlen K, δ; Massenquelle) bleiben offen. Kein Guard geschlossen.
