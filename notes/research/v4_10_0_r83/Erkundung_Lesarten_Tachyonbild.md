# Erkundung: Zwei Lesarten des Tachyonbilds einer Wirkung, I4 und Geist-Kondensation (5. November 2026)

**Status: Erkundung, analytisch, ohne Kriterium.** Anlass: Nach H76 braucht die Stabilität einen ausgezeichneten Rahmen mit Cutoff; der Auslöser von I4 hat getroffen. Frage: Erzeugt die Struktur selbst Rahmen und Skala?

## Vorwissen geprüft
- Repo: keine frühere Behandlung von Geist-Kondensation, P(X) oder Einstein-Äther. r09 (Lesart V) schließt aus, dass die Rapidität des Beobachters gegenüber einem bevorzugten Rahmen direkt in η eingeht (Faktor 10¹³ zu groß); ein Rahmen darf nur schwach an Beobachtbares koppeln. r22 (Konvention F, F3): Umrechnung des Gewichts k nach T mit Phase (−1)^k aus γ ↦ −γ. r82.1(b) und `Wirkung_W2_Higgs.md`: „gesamter Energie-Impuls-Tensor des Bildes wechselt das Vorzeichen“. H71: Partner negativer Norm, über die Masse gekoppelt, macht die Mode tachyonisch.
- Literatur: Arkani-Hamed, Cheng, Luty, Mukohyama, *Ghost condensation* (hep-th/0312099): ⟨φ̇⟩ = M², Zustandsgleichung ρ = −p, Lorentz-Brechung, veränderte Gravitation ab M_P/M². Furukawa u. a., *Ghost dark matter* (1001.4634): Anregungen um das Kondensat verhalten sich wie dunkle Materie; Schranken M ≳ 10 eV (Strukturbildung), M ≲ 100 GeV (phänomenologisch).

## 1. I4 allein liefert keinen Rahmen
Ein Kondensat ⟨χ⟩ = konstant (I4: tachyonische Moden rollen in ein Minimum) ist Lorentz-invariant. Es zeichnet keinen Rahmen aus. Die Anregungen um das Minimum haben im Bild mit F3 weiter negative Energie (Masse √2·m), der Zerfall aus H76 bleibt erlaubt und divergiert über die Boosts. I4 heilt H76 nicht. I4 bleibt als Quelle einer Skala (Kondensat, meV-Abschätzung) möglich, nicht als Quelle des Rahmens.

## 2. Zwei Lesarten des Tachyonbilds einer Wirkung
- **Lesart A (Energieparität, so in r82.1 verwendet):** L_T = −L_M. Der gesamte Energie-Impuls-Tensor wechselt das Vorzeichen (F3 auf die Energie als Größe vom Gewicht 1). Folge: Geist-Kopie mit normaler Dispersion, Vakuumenergie hebt sich bei Photon-Gewichten auf (r82.1), Vakuumzerfall braucht einen Lorentz-brechenden Cutoff (H76).
- **Lesart B (Fortsetzung der Impulse):** η ↦ η + iπ/2 macht p ↦ i·p, also X = (∂φ)² ↦ −X, X² ↦ X², Potentialterme ohne Ableitungen bleiben. Das ist F3 Term für Term mit k = Zahl der Ableitungspaare. Folge: Massenterm wird tachyonisch (wie H71), Potential V und damit V_min **wechseln das Vorzeichen nicht**, die Aufhebung aus r82.1 **entfällt**.
- Masselos und ohne Potential stimmen A und B überein (Kinetik s_T = −1, so in r81 benutzt). r81 ist davon nicht berührt; r82.1(b) hängt an Lesart A.

## 3. Lesart B liefert eine Geist-Kondensation (sympy)
Eine gesunde Materie-Seite mit P_M(X) = X/2 + c·X², c > 0 (Positivität), geht unter B über in P_T(X) = −X/2 + c·X². Das ist genau die Form der Geist-Kondensation:
- Minimum bei X₀ = 1/(4c) > 0 (zeitartig, also ⟨χ̇⟩ ≠ 0), P_XX = 2c > 0: Anregungen stabil, **keine Geist-Quanten, kein Vakuumzerfall wie in H76**;
- ρ = 1/(16c) > 0, p = −1/(16c), **w = −1**: ein Λ-artiger Beitrag positiver Energie;
- ⟨χ̇⟩ ≠ 0 zeichnet einen Rahmen aus, den mitbewegten (Kandidat: der Rahmen aus H70, Versatz in konformer Zeit fest; χ ∝ t ist eine Uhr);
- die Anregungen um das Kondensat sind nach der Literatur dunkle-Materie-artig. Das passt zur Autor-Umdeutung I3 (Λ und dunkle Materie aus derselben Rechnung) – nachträglich bemerkt, nicht geprüft.
Unter Lesart A gibt es dagegen nur ein Extremum bei X = −1/(4c) < 0 (raumartig) mit P_XX = −2c < 0: keine Geist-Kondensation.

## Grenzen
- Der Term c·X² ist in W1/W2 nicht enthalten; er wäre eine neue Eingabe (wie jeder Term höherer Ordnung einer effektiven Theorie).
- Die Höhe von Λ ist nicht festgelegt (P kann eine Konstante enthalten; ρ hängt an c). Für ρ_Λ müsste M = X₀^{1/4} im meV-Bereich liegen, die Schranke M ≳ 10 eV aus der Strukturbildung gilt aber nur, wenn die Anregungen die dunkle Materie sind.
- Lesart B gibt die Aufhebung der Higgs-Vakuumenergie (r82.1) auf; das Λ-Problem von 10⁵⁵ kehrt zurück, falls nichts anderes es löst.
- Welche Lesart die Struktur verlangt, entscheidet diese Erkundung nicht: F3 ist in r22 für Auslesegrößen formuliert, nicht für Terme einer Wirkung.

## Entscheidung für den Autor
Welche Lesart des Tachyonbilds gilt für Wirkungen: A (Energieparität, Aufhebung von V_min, Stabilität nur mit äußerem Cutoff) oder B (Fortsetzung der Impulse, Geist-Kondensation mit eigenem Rahmen und Λ-artigem Term, aber ohne Aufhebung von V_min)? Oder soll zuerst geprüft werden, welche Lesart mit r20/r22 und H71 verträglich ist?
