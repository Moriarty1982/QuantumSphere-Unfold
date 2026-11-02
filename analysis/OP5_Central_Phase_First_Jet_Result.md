# OP5: erster Ableitungstest des zentralen Phasenanteils
29.10.2026. Numerische endliche-Jet-Diagnostik; kein zertifizierter Nichtexistenzsatz.

## Vertrag
Aus dem letzten Test: Nach Eliminieren der spurfreien sektorerhaltenden Verbindung erfüllt der zentrale Kovektor c_mu die projizierte Bedingung F(x)c(x)=b(x).
F=P Mcentral, b=-P residual, P=I-Mtraceless Mtraceless^+.
Der vollständige orthogonale Projektor wird differenziert, nicht eine willkürlich wechselnde linke Nullraumbasis.

Feste Daten: ursprüngliche Spinorfamilie und Ableitungen, kanonische Coframe, interner Sektortransport, nullgesetzte Lorentz-Spinverbindung. Freie Daten: ALLE vier zentralen Werte und ihre ersten Ableitungen. Es wird nicht nur der Minimum-Norm-Repräsentant des vorigen Tests untersucht.

Untersuchte Bedingungen:
F c=b,
(d_k F)c+F d_k c=d_k b.
Kontrolle: 16 unabhängige Ableitungen d_k c_mu.
Phasenfall: c=dphi, deshalb zehn symmetrische zweite Ableitungen d_k c_mu=d_mu c_k.
Jeweils werden die zentralen Werte und Ableitungen gemeinsam gelöst.

## Ergebnis
Zentrale Differenzen h=.001,.0005,.00025; analytische Ausgangsfelder werden mit gecachten Lambdas ausgewertet. Lineares System 120 Zeilen, 20 bzw.14 Spalten.

Mit relativer Rangschwelle 1e-5:
- freie Ableitungen: Rang10 an beiden Punkten und allen Schritten.
- symmetrische Ableitungen: Rang9 an beiden Punkten und allen Schritten.

Restnormen (keine quadrierten Normen):
P1 frei: 5.1281e-6 ->1.2820e-6 ->3.2050e-7.
P1 symmetrisch: 2.6125591 ->2.6125577 ->2.6125574.
P2 frei: 8.2343e-6 ->2.0586e-6 ->5.1464e-7.
P2 symmetrisch: 3.2199517 ->3.2199510 ->3.2199509.

Die freien Kontrollen konvergieren quadratisch mit der Differenzschrittweite. Die Phasenfälle zeigen einen stabilen großen Rest.

## Rangempfindlichkeit
Ein erster Lauf mit rcond=1e-7 nahm bei gröberen Schritten zusätzliche kleine numerische Richtungen auf; Rang wechselte mit h. Dieser Lauf darf nicht als stabiler Rangnachweis verwendet werden. Die endgültigen Daten verwenden 1e-5 und speichern alle Singulärwerte. Die große Diskrepanz zwischen freiem und symmetrischem Fall bleibt bestehen. Kein exakter symbolischer Rang oder Intervallbeweis liegt vor.

## Bedeutung
Dies ist stärkere Evidenz als die Nichtgeschlossenheit eines einzelnen Minimum-Norm-Feldes: Die zwei zuvor freien zentralen Richtungen werden hier mitoptimiert. In dieser festgehaltenen Vergleichsfamilie scheint kein geschlossener zentraler Kovektor bereits den ersten differenzierten Bedingungen zu genügen. Ein allgemeines Verbindungsfeld mit antisymmetrischem Ableitungsanteil besteht die Kontrolle dagegen bis zur beobachteten Diskretisierungsgenauigkeit.

Das ist keine Identifikation mit Elektromagnetismus und kein Beweis einer neuen Naturkonstante. Auch eine native Wirkung oder Verbindungsgleichung fehlt. Gemeinsame Änderungen der Ausgangsfelder und Geometrie könnten die Bedingungen ändern. Die nullgesetzte Lorentzverbindung bleibt eine torsionsbehaftete Vergleichswahl.

Nächster Schritt: F,b analytisch differenzieren oder den Test unabhängig gegen das nichteliminierte vollständige System prüfen; dann die unvermeidbare antisymmetrische Ableitung präzise bestimmen. Erst daraus können belastbare Aussagen über einen erforderlichen Krümmungsanteil folgen.

Artefakte: OP5_Central_Phase_First_Jet_Check.py/.json. Numerische Recherche lokal gesichert, nicht committed. OP5 offen.
