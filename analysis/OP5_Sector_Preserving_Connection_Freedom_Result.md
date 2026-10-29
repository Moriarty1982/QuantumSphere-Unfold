# OP5: verbleibende sektorerhaltende Verbindung
29.10.2026. Zwei-Punkt-Diagnostik im Vergleichsmodell. Keine native OP5-Schließung.

## Nachtrag zum letzten, unterbrochenen Arbeitsschritt
OP5_Sector_Transport_Full_Equation_Check.py/.json wurden am 28.10 erfolgreich ausgeführt. Die abschließende Textdatei und zusätzliche Restvektor-Assertion konnten wegen eines Fehlers der automatischen Freigabeprüfung (Nutzungslimit) nicht mehr gespeichert werden.
Ergebnis: Kanonische Ergänzung A0=-Y theta_t erzeugt E0=2dt, Ei=dxi+vi dt. Ohne Lorentz-Spinverbindung bleiben die vollständigen quadratischen Restnormen 102.2777778 und 157.3617634. Analytisch erklärt dies die Homogenität (partial_t+v·grad)u,w=0 und Y Psi=i partial_theta Psi.
Die Levi-Civita-Ergänzung H=-1/(2t) liefert den kontrahierten Spinbeitrag -3i/(4t), erhöht die Reste um 9 und verändert die Coframe-Auslese um delta E0=-sum xi Ei/(2t), delta Ei=-Ei/2. Deshalb ist sie auf diesen unveränderten Feldern kein Fixpunkt der Auslese.

## Aktueller mathematischer Vertrag
Fest: ursprüngliche Spinorfeldwerte UND Ableitungen an P1/P2; E0=2dt, Ei=dxi+vi dt; kanonische interne Verbindung; Massenterm; Lorentz-Spinverbindung null.
Letzteres ist eine explizite torsionsbehaftete Vergleichswahl, keine Levi-Civita-Verbindung und keine aus einer Wirkung hergeleitete Quelle.

Frei: zusätzliche hermitesche interne C_mu mit [C_mu,R]=0. Damit bleibt D R=0 bestehen. Jeder interne Kommutant hat fünf reelle Dimensionen: R besitzt einen eindimensionalen Plus- und zweidimensionalen Minusraum.
Basis: m m^T, n n^T, z z^T, (n z^T+z n^T)/sqrt2, i(n z^T-z n^T)/sqrt2,
n=(c,-d,0), m=(d,c,0), z=(0,0,1).
Vier Koordinatenrichtungen liefern 20 reelle freie Koeffizienten. Keine Spur- oder zusätzliche native Projektionsbedingung wurde vorausgesetzt.

## Elimination und vollständige Restkontrolle
Zunächst wurde die 16x20 lineare Änderung der reellen Coframe gebildet, dann ihr Nullraum vollständig bestimmt. An beiden Punkten hat sie numerischen Rang null: Alle getesteten sektorerhaltenden Verbindungsrichtungen lassen die Coframe auf DIESEN Spinorfeldwerten unverändert. Größte Singulärwerte unter 6e-17, absoluter Rangcutoff 1e-11. Das ist keine allgemeine Aussage für beliebige Spinoren.

Die vollständige reell gepackte Spinorgleichung liefert eine 24x20-Matrix mit Rang 18. Ihre zwei kleinsten Singulärwerte liegen unter 4e-16, der kleinste nichtverschwindende bei etwa .64 bzw. .67. Relative Least-Squares-Schwelle 1e-12.
Der ursprüngliche Rest liegt an beiden Punkten numerisch im Bild dieser Matrix.

Mit Coframe-Bedingung:
P1: quadratische Restnorm 6.52e-27 oder kleiner, Coframe-Änderungsnorm unter 2e-16.
P2: quadratische Restnorm 2.92e-28 oder kleiner, Coframe-Änderungsnorm unter 2e-16.
Die rekonstruierten 3x3-Verbindungen wurden direkt in die vollständigen komplexen Gleichungen eingesetzt. Nicht bloß eine Stromprojektion wurde angepasst. Normalgleichungsorthogonalität und Kommutation mit R wurden kontrolliert.

## Was damit erreicht ist
In der zugelassenen Vergleichsklasse sind an beiden Punkten Spinorgleichung, interne Sektorerhaltung und unveränderte kanonische Coframe miteinander verträglich. Die kanonische Verbindung allein war unzureichend; ihr Kommutant bietet eine bisher nicht geprüfte Reparaturmöglichkeit.

## Was ausdrücklich offen bleibt
Dies ist eine inverse Bestimmung der Verbindung aus den gewünschten Feldern, keine dynamische Herleitung.
- Eigene Verbindungs-/Eichfeldgleichungen und gemeinsame Wirkung fehlen.
- Native M16/C7-Projektionen und zulässige Verbindungsalgebra sind nicht überprüft.
- Die Verbindung wurde separat an zwei Punkten bestimmt. Glatte regionale Fortsetzung, Rangstabilität und höhere Bedingungen fehlen.
- Die geometrische Verbindung mit Torsion wurde nicht aus einer Quelle hergeleitet.
- Die zwei freien Nullrichtungen sind keine identifizierten Eichfreiheiten; ihre Bedeutung ist offen.
- Keine Lösung der Vakuumenergiefrage oder Herleitung eines physikalischen Primwerts.

Nächster Test: zusätzliche native Zulässigkeitsbedingungen (z.B. Spur) als eigene Kontrollen prüfen und erst dann regionale Verbindungsrekonstruktion bzw. Wirkungsgleichungen verfolgen. Nicht aus einem erfolgreichen Potentialfit auf OP5-Abschluss schließen.

Reproduktion: OP5_Sector_Preserving_Connection_Freedom_Check.py/.json; benötigt den benachbarten bisherigen Evaluator. Forschungsarbeitsstand; keine OP5-Schließung.
