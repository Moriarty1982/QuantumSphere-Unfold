# Dixon-Kommutant in Abschnitt 2.4

Wolfram Language 15.0.1 über den Wolfram-Connector. `dixon.wl` rekonstruiert die Hamilton- und Cayley–Dickson-Multiplikation aus der Konvention des Companion bei Commit `f2a4e687273f2ec7f4124d490e696e07c00f387a`, Pfad `notes/research/op3_frame_bridge_2026_11_15/frame_bridge_commutant.py`. Alle Koeffizienten sind exakt. Die sechs Lorentz-Generatoren umfassen die drei Quaternion-Linksmultiplikationen und die zugehörigen imaginären Boost-Generatoren. Die schwachen und Farb-Generatoren sowie der Hyperladungsoperator werden wie in der Quelle konstruiert.

Ein komplex-linearer mit den Lorentz-Linksmultiplikationen kommutierender Operator ist durch seine Wirkung auf `1 ⊗ v` bestimmt. Ist `X(1 ⊗ v) = Σ e_j ⊗ M_j v`, so folgt `X(q ⊗ v) = Σ q e_j ⊗ M_j v`. Damit spannen die Quaternion-Rechtsmultiplikationen mit den vier noch freien 8×8-Faktoren alle Kandidaten auf. Farbinvarianz beschränkt jeden der vier Faktoren auf einen sechsdimensionalen Raum. Wolfram berechnet den Rang der verbleibenden linearen Gleichungen auf diesem 24-dimensionalen Raum zu 18. Die sechs Hyperladungs-Spektralprojektoren liegen paarweise orthogonal im Kommutanten und summieren sich zur Identität. Sie liefern sechs unabhängige Elemente und damit die behauptete Algebra `C^6`.

Ein antilinearer Operator ist `X K` mit Konjugation `K`. Für einen reellen invertierbaren Rotationsgenerator `A` folgt aus der Kommutation `AX = XA`, aus dem zugehörigen Generator `iA` folgt zugleich `AX = −XA`. Das ergibt `X = 0`. Wolfram bestätigt Reellheit, die Konjugation des Boosts und den vollen Matrixrang von `A`.

Damit ist die konkrete Generatorrechnung reproduziert. Die Zuordnung der deklarierten Darstellung zu einem nativen Materiesektor des Ansatzes bleibt eine Modellvoraussetzung. Der separate Rückgabewert `Null` ist die Rückgabe des letzten `Print`, die Befunde stehen in der tatsächlichen Ausgabe `dixon.txt`.

Reproduktion: `wolframscript -file dixon.wl` oder Auswertung des Skripts als Ganzes mit dem Wolfram-Connector.
