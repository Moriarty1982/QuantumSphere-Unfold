# OP5: sechs 9x9-Schnitte einschließlich orientierter Flächen

29.10.2026. Gespeicherte Koeffizienten des kausal kontrollierten Zweimodenfelds, keine Neuanpassung. Schnitte tx,ty,tz,xy,xz,yz mit jeweils9 Positionen pro Achse und Abweichung ±.01 um (1,.6,0,0); die anderen Koordinaten bleiben fest. 486 Auswertungen mit Überschneidungen, keine486 verschiedenen Punkte und kein vollständiges9^4-Raster.

Berechnet: vollständige Spinorrestnorm, g^{00}, normierter gemischter Metrikanteil g_ij/sqrt(abs(g_ii g_jj)), Lorentz-Flächenbetrag sqrt(abs(g_ii g_jj-g_ij²)), alle sechs Komponenten des orientierten Bivektors E_i wedge E_j, räumliches Kreuzprodukt der räumlichen Projektionen E_spatial_i cross E_spatial_j. Die Projektionskreuzprodukte ersetzen nicht die Zeit-Raum-Komponenten des Bivektors. Gram-Identität area²=-sum(B_0a²)+sum(B_ab²) an allen Punkten numerisch unter1e-8 geprüft, ebenso die räumliche Kreuzproduktidentität. Keine neue Dynamik aus Kreuzprodukten postuliert.

Maximale Restnormen pro Schnitt: tx .03066, ty .03655, tz .03668, xy .03215, xz .03354, yz .03868. Sämtliche geprüften Coframes invertierbar, minimale absolute Determinante9.6991. Größter inverser Zeitmetrikw ert g^{00}=-.46613, also an allen geprüften Punkten negative Werte. Alle geprüften Flächendeterminanten nichtnull. Dies sind Stichprobenaussagen, keine garantierten Gebietsschranken. Der gemischte Metrikanteil misst Schiefstellung/Kopplung der Koordinatenrichtungen, nicht allein Riemann-Krümmung. Der Flächenbetrag allein verliert das Vorzeichen, das in den JSON-Daten separat gespeichert ist.

Darstellung: OP5_Slices_9x9.svg sowie HTML. Gleiche Farbskala pro Messgröße über alle sechs Schnitte; Zahlen unter Karten geben lokale Minima/Maxima. Lokale Koordinaten sind Vergleichseinheiten, keine physikalisch kalibrierten Längen/Zeiten.

Artefakte: OP5_Slices_9x9_Check.py/.json. Reproduktion durch python im lokalen Forschungsordner, gespeicherte Koeffizienten und bestehende Torch-Auswertung erforderlich. Lokal gespeichert, nicht committed. Feld bleibt Näherung, OP5 offen.
