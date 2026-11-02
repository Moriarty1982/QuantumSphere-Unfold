# OP5: analytischer Vollsystem-Test des zentralen Krümmungsanteils
29.10.2026. Unabhängige Kontrolle des zuvor projizierten Differenzentests.

## Verfahren
Die vollständige Spinorgleichung ist M(x)a(x)+r(x)=0 mit 24 reellen Gleichungen und 20 sektorerhaltenden hermiteschen Verbindungskoeffizienten.
M und r wurden symbolisch differenziert, einschließlich der ortsabhängigen Basis und der Spinor-Ableitungen. Anschließend wurden Werte mit NumPy ausgewertet; keine finiten Differenzen und keine differenzierte Pseudoinverse.

Gemeinsames System:
M a=-r,
(d_k M)a+M d_k a=-d_k r, k=0..3.
Das sind 120 Zeilen und 100 Unbekannte (20 Werte,80 Ableitungen).
Der zentrale Kovektor ist c_mu=Tr(C_mu)/3. Da die fünf Basismatrizen konstante Spuren (1,1,1,0,0) besitzen, ist seine Ableitung durch die entsprechenden Koeffizientenableitungen korrekt gegeben. Sechs zusätzliche Bedingungen d_i c_j-d_j c_i=0 wurden über einen vollständigen Nullraum erzwungen. Alle spurfreien Werte UND Ableitungen bleiben frei.

Felder, Geometrie, kanonischer Sektortransport und die torsionsbehaftete Null-Spinverbindung sind wie im bisherigen Vergleich festgehalten. Die kanonische Verbindung ist spurfrei; ihr Beitrag verändert den zentralen Kovektor nicht.

## Ergebnis
P1=(1,.6,0,0):
- freies System Rang90, Restnorm6.35e-14.
- geschlossener zentraler Anteil Rang89 auf reduziertem Variablenraum, Restnorm2.404639847.

P2=(1,.4,.2,.2):
- freies System Rang90, Restnorm6.41e-14.
- geschlossener zentraler Anteil Rang89, Restnorm2.912654430.

Relative Rangschwelle1e-10. Alle Singulärwerte gespeichert. Die Restnormen unterscheiden sich erwartbar von denen des projizierten Systems, weil die Gleichungsgewichtung eine andere ist. Beide Verfahren stimmen in der Unverträglichkeit der Geschlossenheitsforderung überein.

## Welche Krümmung ist erzwungen?
Sei N der vollständige Kern der 120x100-Matrix, T die Abbildung auf die sechs Komponenten des zentralen Curls. T N hat an beiden Punkten Rang5. Somit können fünf Kombinationen der sechs Komponenten durch homogene Lösungen verändert werden; eine Kombination bleibt fest und ungleich null.

In der Reihenfolge (tx,ty,tz,xy,xz,yz) ergibt die euklidisch normierte linke Bedingung:
P1: ungefähr .857492926 F_tz-.514495755 F_xz=-1.844006778.
P2: ungefähr -.327912918 F_tx-.163956459 F_ty+.819782295 F_tz-.393495501 F_xz-.196747751 F_yz=-2.201560878.

Vorzeichen hängen von der SVD-Basiswahl ab; Bedingung und rechte Seite wechseln gemeinsam. Euklidisch minimale Curlnormen sind1.844006778 und2.201560878. Dies sind keine Lorentz-invarianten physikalischen Feldstärken und keine Naturkonstanten. Sie quantifizieren die Nichtnull-Bedingung im festgelegten Koordinaten-/Normierungssystem.

Die kleinsten nichtverschwindenden Singulärwerte von T N sind etwa .0439 und .0450; der letzte ist unter4e-16. Damit ist die eine fehlende Curlrichtung numerisch deutlich getrennt. Direkte Rückeinsetzung der minimalen Curl-Lösung erhält die vollständigen Feld-/Ableitungsgleichungen bis unter1e-9.

## Interpretation und Grenzen
Der Test bestätigt unabhängig und ohne Finite-Differenzen: In der festgehaltenen Vergleichsfamilie ist eine reine lokale skalare Phase als zentraler Verbindungsanteil mit den ersten differenzierten Bedingungen numerisch unvereinbar. Nicht nur ein Minimum-Norm-Repräsentant wurde getestet; die volle homogene Lösungsfreiheit wurde berücksichtigt.

Analytische Ableitungen bedeuten hier nicht exakte symbolische Linearalgebra: Rang und Konsistenz wurden in Gleitkomma ausgewertet. Ein formaler oder intervallzertifizierter Nichtexistenzsatz fehlt.
Keine regionale Lösung, keine eigenen Verbindungsfeldgleichungen, keine native M16/C7-Herleitung, keine elektromagnetische Identifikation und kein Lambda-Ergebnis sind bewiesen. Andere gemeinsam veränderte Spinorfamilien können andere Bedingungen besitzen.

Nächster sinnvoller Schritt: die eine verbleibende Curlbedingung geometrisch auf die vorhandenen Ströme/Projektoren zurückführen, dann prüfen, ob eine erklärte native Verbindungsgleichung sie zulässt. Bloß neue freie Krümmung anzusetzen würde die physikalische Herleitung nicht ersetzen.

Artefakte: OP5_Central_Phase_Analytic_Full_Jet_Check.py/.json. Lokal gesichert, nicht committed; OP5 offen.
