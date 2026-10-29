# OP5: gemeinsames Mehrmodenfeld mit variablen Amplituden

29.10.2026. Numerische lokale Näherung, keine exakte PDE-Lösung.

## Ansatz und feste Modellwahl

Chi_j(x)=sum_{m=1,2}(a_jm+sum_mu b_jm_mu (x-center)_mu/radius) exp(i k_m dot(x-center)); beide Moden tragen unabhängige affine komplexe vierkomponentige Amplituden für alle drei Spezies. Frequenzen k1=(1,1,0,0), k2=(-1,0,1,1). Center=(1,.6,0,0), radius=.01 in Vergleichskoordinaten. Die Frequenzen werden nicht physikalisch identifiziert oder optimiert.

Q=Chi†(Z tensor beta)Chi. Setze Psi=sqrt(8/(h Q)) Chi für positives Q. Damit gilt h Psi†ZbetaPsi=8 exakt als Funktionsidentität, nicht nur an Trainingspunkten. Es handelt sich um eine aus der vorhandenen Vergleichsgleichung abgeleitete notwendige Zustandsbedingung. Ihre Erfüllung ersetzt die übrigen Gleichungen nicht.

Originale ortsabhängige interne Kopplungen und Massenterm unverändert, Lorentz-Spinverbindung weiterhin null wie im Vergleich. Coframe und inverse Coframe aus dem gesamten Feld samt Amplituden-/Normierungsableitungen neu berechnet. Keine neue zentrale Verbindung. Feldwerte und räumliche Daten bleiben beim Fit nicht auf den alten Ausgangswerten fixiert. Daher ist dies die Suche nach einem neuen gemeinsamen Feld, nicht die Entwicklung der früheren Anfangsdaten.

## Optimierung und Kontrollen

PyTorch double/complex128, ein CPU-Thread, L-BFGS mit starker Wolfe-Liniensuche. 9 Trainingspunkte: Zentrum und die acht positiven/negativen Achsenpunkte. Vier zuvor nicht verwendete Diagonalpunkte als erste Kontrolle. Der erste Lauf ohne Forderung raumartiger t-Schnitte verbessert den Fehler, endet aber bei g^{00}>0; dieses Vergleichsergebnis bleibt im separaten Skript/JSON erhalten.

Zweiter Lauf: zusätzlich weiche Strafe100*mean(max(g^{00}+.05,0)^2) an Trainingspunkten, 600 L-BFGS-Iterationen/615 Closure-Aufrufe. Dies ist eine überwachte numerische Nebenbedingung, keine globale Garantie.

Vorher: Trainings-RMS der vollständigen Spinorgleichung .46142, Kontroll-RMS .52484. Danach: Training .02040, Kontrolle .02025. Maximalreste .02769 und .02276. Kein relativer physikalischer Fehlermaßstab; diese Normen gelten in der Vergleichsnormierung. Ein exakter Lösungsrest wurde nicht erreicht.

Zusätzliche Prüfung am gespeicherten/erneut deterministisch berechneten Feld auf81 Punkten im kleineren Hyperwürfel mit Koordinatenabweichungen -.0075,0,.0075: RMS .02711, maximaler Rest .04058, minimale absolute Coframe-Determinante9.8118, größtes g^{00}=-.45799, kleinstes Q5.4677. Das Zentrum ist auch Trainingspunkt; die übrigen80 Rasterpunkte sind nicht die Trainingspunkte. Die Stichprobe ist keine Aussage für jeden Punkt des Würfels.

Unabhängige Ableitungskontrolle: Feldwerte bei drei Rasterpunkten durch zentrale Differenzen mit Schritten1e-5 und1e-6 differenziert, anschließend vorhandenen NumPy-Residual-Evaluator verwendet. Abweichung zur analytisch kodierten Torch-Auswertung unter9e-10. Das prüft die Amplituden-/Normierungsableitungen und Operatororientierung auf diesem Testumfang, nicht die gesamte physikalische Modellwahl.

## Bedeutung

Anders als frühere unabhängige Punktjets ist dies eine einzige explizite glatte Feldfunktion auf ihrem regulären Gebiet Q>0, t!=0, rho>0 und den bisherigen reellen Wurzelbereichen. Gemischte Ableitungen vertauschen dort automatisch. Der nichtverschwindende PDE-Rest bedeutet dennoch, dass das frühere Integrabilitätsproblem nicht als gelöst gelten darf. Statt unvereinbarer exakter Punktdaten liegt jetzt ein gemeinsames approximatives Feld vor.

Die einfache affine Amplitudenfamilie und zwei fest gewählte Frequenzen liefern eine brauchbare numerische Näherung. Ob der Rest durch Anreicherung der Familie kontrolliert sinkt oder eine strukturelle Grenze anzeigt, ist offen. Der nächste aussagekräftige Test ist ein Ansatzvergleich mit quadratischen Amplituden und zusätzlicher Kontrollabdeckung bei gleicher Gebietsgröße; kein bloßes Verkleinern des Gebiets als scheinbarer Lösungsfortschritt.

Keine regionale exakte Existenz, kein nativer Wirkungsnachweis, keine abgeleitete Levi-Civita-Dynamik, keine physikalische Unschärfequelle und keine OP5-Schließung. Keine Optimierung oder Identifikation von Lambda.

Artefakte: OP5_Multimode_Amplitude_Field_Check.py/.json (ohne kausale Strafe), OP5_Multimode_Causal_Field_Check.py/.json, OP5_Multimode_Field_Validation.py/.json. Ausführen mit python im lokalen Ordner; benötigen gespeicherte Vorgängerdaten, vorhandenen Repository-Evaluator, PyTorch, NumPy und SymPy. Koeffizienten sind in JSON gespeichert. Validierungsskript führt vor der Kontrolle den deterministischen Fit erneut aus. Lokal gesichert, nicht committed.
