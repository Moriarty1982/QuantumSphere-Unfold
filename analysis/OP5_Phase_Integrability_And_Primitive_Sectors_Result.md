# OP5: Phasenintegrabilität und mögliche unzerlegbare Teilbereiche
28.10.2026. Nutzerfrage: Könnte der gefundene Beitrag ein „physikalischer Primwert“ sein, im Sinne nicht weiter teilbarer Teilbereiche oder eines Primzahlbezugs?

## 1. Der lokale Phasenfit ist noch kein Phasenfeld
Für die vorgeschriebene Reparatur ist p=l/(cd) die relative Phasen-Einform. Notwendig für eine gewöhnliche glatte lokale skalare Phase ist d_ext p=0.
An den ursprünglichen Vergleichsfeldern wurde l an benachbarten Punkten jeweils neu aus der transversalen Gleichung bestimmt. Zentrale Differenzen mit vier Schrittweiten und unabhängig analytisch differenzierte Normalgleichungen ergeben:

P1: (d_ext p)_tz=3.5843829212, (d_ext p)_xz=-0.8419691426.
P2: (d_ext p)_tx=-1.2784248059, (d_ext p)_xz=8.0719842845, weitere Komponenten ebenfalls nicht null.
Dritter Kontrollpunkt (.9,.3,.2,.1): maximaler Absolutwert etwa 14.1203 (Schrittweitenvergleich).
Die analytischen Ableitungen stimmen an P1/P2 mit den feinsten zentralen Differenzen bis unter 2e-6 überein. Die Zahlen haben die Koordinaten-/Normierungseinheiten des Vergleichsmodells.

Damit ist diese punktweise vorgeschriebene Phasenreparatur nicht der Gradient einer gewöhnlichen Phasenfunktion auf einer Umgebung. Dies ist ein Kompatibilitätsbefund auf der eingefrorenen Startfamilie, kein Ausschluss einer gemeinsam entwickelten nichtlinearen Feldlösung. Überall alte Feldwerte und neue Ableitungen einzusetzen beschreibt selbst noch kein konsistentes Feld.

Die einzelnen vorgeschriebenen Phasen-Einformen sind p_A=-d²p und p_B=c²p. Ihre gemeinsame Integrabilität würde zusätzlich d_ext theta wedge p=0 verlangen, sofern cd ungleich null. Der Ansatz hat die gewichtete gemeinsame Phasen-Einform auf null gesetzt; ihre Freigabe ist eine weitere echte Erweiterung, die den gemeinsamen A/B-Rest verändert.

## 2. Was bedeutet „nicht weiter teilbar“ hier?
Eine präzise mögliche Übersetzung ist ein gemeinsamer invarianter Teilraum der relevanten Operatoren. Eine orthogonale Zerlegung in voneinander getrennte Sektoren verlangt einen nichttrivialen Projektor, der mit den betrachteten hermiteschen Operatoren kommutiert.

Für die internen drei Spezies:
[S,X]=[Y,X]=0 erzwingt X=diag(a,a,b).
Zusätzlich [G,X]=0 verlangt (a-b)p=(a-b)q=0.
Bei nichtverschwindender Verbindung zwischen C und A/B folgt a=b. Der gemeinsame Kommutant der Familie {S,Y,G} enthält also nur skalare Matrizen; keine nichttrivialen gemeinsamen orthogonalen Sektorprojektoren.

Das wurde exakt mit SymPy für S/Y und einen nichtverschwindenden G-Test geprüft und durch die allgemeine Bedingung für p,q begründet. Es bedeutet: Die drei Spezies zerfallen unter DIESER Operatorfamilie nicht in getrennte interne Blöcke. Es bedeutet nicht, dass eine physikalische Urgröße oder ein elementares Teilchen gefunden wurde.

Wichtige Grenze: S ist der gewählte Ausleseoperator. Unzerlegbarkeit unter Dynamik UND Auslese ist stärker als eine Aussage über den Hamiltonoperator allein. Der einzelne Hamiltonoperator kann anders zerlegt werden. Native M16/C7-Operatoren, dynamische Superselektionssektoren, globale Topologie oder räumliche Teilgebiete wurden damit nicht klassifiziert. Irreduzibilität ist immer relativ zu einer angegebenen Operatorfamilie.

## 3. Keine Primzahl- oder Konstantenidentifikation
Die Zahl drei der angesetzten Spezies ist eine Modellwahl und kein hergeleiteter Primzahlmechanismus. Irreduzibilität hängt nicht davon ab, dass die Dimension eine Primzahl ist; auch zusammengesetzte Dimensionen können irreduzible Darstellungen tragen.
Die gefundenen Komponenten l/p variieren bereits zwischen den Testpunkten. Sie sind Ableitungsgrößen mit Koordinatenabhängigkeit, keine universellen dimensionslosen Konstanten. Es gibt hier keine nachgewiesene Quantisierung, topologische Ganzzahl, Eichinvarianz eines neuen Observablen oder experimentelle Identifikation.

## 4. Mögliche Verbindung, aber noch keine Physik
Ein nichtgeschlossenes p lässt sich formal als Teil einer Verbindungsbeschreibung untersuchen: p=dphi+B würde dp=dB ergeben. Diese Zerlegung allein ist jedoch beliebig und liefert kein dynamisches Gesetz. Um B physikalisch zu deuten, braucht es Transformationsgesetz, Wirkung, Feldgleichung und messbaren eichinvarianten Inhalt. Insbesondere ist dp hier nicht als elektromagnetische Feldstärke oder Raumzeitkrümmung identifiziert.

Nächster sinnvoller Schritt: Prüfen, ob bereits vorhandene native Kopplungs-/Verbindungsterme die benötigte nichtintegrable Struktur liefern können, statt ad hoc ein neues Feld einzuführen; dabei den gemeinsamen A/B-Rest und den C-Rest mitführen.

## Artefakte und Status
OP5_Relative_Phase_Integrability_Check.py/.json: örtliche Fits und vier Differenzschritte.
OP5_Phase_Analytic_And_Sector_Check.py/.json: analytisch differenzierte Normalgleichungen und exakte interne Kommutantenprüfung.
Die Differentiation ist analytisch, die anschließenden Auswertungen sind Gleitkomma; kein intervallzertifizierter globaler Satz. Lokaler Arbeitsstand, nicht committed. OP5 bleibt offen.
