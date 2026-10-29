# OP5: Unschärfe, Auslesung und zentrale Krümmung

29.10.2026. Neuer begrenzter Test, keine Änderung des Manuskripts.

## Vertrag und Methode

Feste interne Matrizen aus OP5_Sector_Transport_Result.md, positive gewöhnliche Hilbertraumstruktur. R=[[-cos(2theta),sin(2theta),0],[sin(2theta),cos(2theta),0],[0,0,-1]], S_AB=S_BA=1/2, Y_AB=-i,Y_BA=i. Der vollständige Sektoroperator ist J=R tensor gamma5; R allein ist nur der interne Faktor. Keine native Quantisierung vorausgesetzt. Exakte symbolische Identitäten mit SymPy 1.14.0 unter Python 3.12.10, unabhängige analytische Gegenprüfung durch uncertainty_review. 16 symbolische Checks bestanden, Manifest validiert, run.status=completed. Keine numerische Stichprobenverallgemeinerung.

## 1. Sektor und Auslesung

Mit C=cos(2theta), T=sin(2theta), Z=diag(1,-1,0) gelten [R,S]=-i C Y und [S,Y]=i Z.

Im normierten Referenzzustand n=(cos(theta),-sin(theta),0) gilt Rn=-n, Var(R)=0, Var(S)=C²/4, Var(Y)=1, <Y>=0. Beide symmetrischen Kovarianzen für R/S und S/Y sind null. Robertson und Schrödinger liefern für R/S nur 0>=0. Ein nichtverschwindender Matrixkommutator erzwingt nicht in jedem Zustand eine positive Produktuntergrenze.

Dieser Referenzzustand ist nicht die bisherige Feldfamilie Psi=(c u,d u,w). Für jene Familie, mit q=||u||²/(||u||²+||w||²), 0<=q<=1, ergeben sich exakt:

- <R>=-1+2q T², <S>=q T/2, <[R,S]>=0.
- Var(R)=4q T²(1-q T²), Var(S)=q(1-q T²)/4.
- Cov(R,S)=q T(1-q T²).
- Var(R)Var(S)=Cov(R,S)²: die stärkere Schrödinger-Grenze wird gesättigt, während der Robertson-Kommutatorterm null bleibt.

Kohärenzen mit C ändern diese Momente nicht, weil alle betreffenden Operatorprodukte blockdiagonal sind. Die Sättigung folgt auch aus der zustandsbezogenen Identität R Psi=(4T S-I)Psi. Sie ist keine Operatoridentität auf dem gesamten Raum. Für J gegen S tensor I ist der Kommutatorerwartungswert in derselben proportionalen Familie ebenfalls null; die übrigen R-Momente dürfen nicht ungeprüft auf J übertragen werden.

## 2. Echte Auslese-/Mischungsgrenze und Verbindung zum Transport

Im Referenzzustand n gilt DeltaS DeltaY=|C|/2, exakt gleich der Robertson-Untergrenze. Für theta=pi/12 ist das sqrt(3)/4. Das ist dimensionslos und zustandsabhängig, keine neue Naturkonstante.

Es gilt dn/dtheta=iYn und d<S>/dtheta=-C. Die Unschärferelation liest sich damit auch als Empfindlichkeitsgrenze |d<S>/dtheta|<=2 DeltaS DeltaY, hier gesättigt. Derselbe Mischgenerator, der den Zustand dreht, ändert also die Auslesung.

Die ältere Transportobstruktion d Tr(SR)=2C dtheta hat damit einen gemeinsamen algebraischen Ursprung. Sie ist aber nicht identisch mit einer positiven R/S-Unschärfe: letztere ist im Referenzzustand null, während die Transportobstruktion bestehen kann. Auch im tatsächlichen Feldzustand ist der Kommutatorterm null. Fluktuationen heben widersprüchliche deterministische Gleichungen nicht automatisch auf.

## 3. Warum dies die zentrale OP5-Krümmung noch nicht erklärt

Ein zusätzlicher zentraler Anteil c_mu I kommutiert mit R,S,Y. Er ändert weder ihre internen Kommutatoren noch ihren adjungierten Transport. Beliebige verschiedene zentrale Curls dc sind deshalb mit denselben internen Unschärfedaten vereinbar. Aus diesen Daten allein kann die konkret erforderliche Quelle F(V,W) nicht folgen.

Eine Gegenkontrolle verhindert den falschen Schluss, zentrale Krümmung sei generell unsichtbar: Für D_x=partial_x, D_y=partial_y+i x gilt [D_x,D_y]psi=i psi. Skalare Potentiale kommutieren, ihre kovarianten Ableitungen nicht.

Allgemein gilt für D=partial+iA: [D_mu,D_nu]=i F_mu_nu. Unter zusätzlichen Operator-/Hilbertraumannahmen hätten Pi_mu=-i hbar D_mu deshalb eine Robertson-Grenze DeltaPi_mu DeltaPi_nu >= hbar² |<F_mu_nu>|/2. Diese Aussage ist hier nur konditional: positive Zustandsnorm, geeignete gemeinsame Definitionsbereiche, Randbedingungen, physikalische Bedeutung und Skalierung von A sind noch festzulegen. Für die bisherige Zeit-Raum-Komponente darf ein selbstadjungierter Zeitimpuls nicht automatisch vorausgesetzt werden. Punktwerte von F ersetzen zudem keine Erwartungswerte in einer normalisierten Wellenfunktion.

Für die ortsabhängigen Richtungen V,W lautet die geometrische Identität [D_V,D_W]-D_[V,W]=i F(V,W). Das zusätzliche Lie-Klammerglied darf in einer möglichen Unschärferechnung nicht unterschlagen werden.

Selbst eine solche Impulsunschärfe würde bei gegebener Krümmung eine Streuungsgrenze liefern; sie wählt allein weder die Krümmung noch die frühere OP5-Quelle aus. F=0 bleibt mit einer Unschärfe-Ungleichung grundsätzlich vereinbar.

## Ergebnis und nächste Trennung

Verifiziert: interne Auslese-/Generatorunschärfe und ihr Zusammenhang mit der Empfindlichkeit unter Mischungsrotation. Nicht verifiziert: eine Unschärfeursache der zentralen Krümmungsquelle, native physikalische Quantisierung, regionales Lösungsfeld oder Abschluss von OP5. Die identifizierte Unsicherheit existiert bereits auf gewöhnlicher Operatorenebene; eine neue höhere Unschärferelation wurde nicht hergeleitet.

Nächster trennscharfer Schritt wäre eine begründete Zustandsraum-/Transportobservablen-Definition aus der nativen Wirkung. Erst dann lassen sich Transportkrümmung und Streuungen im gleichen physikalischen Modell vergleichen. Keine Wirkung allein zum Erzwingen der gewünschten Schranke einsetzen.

## Reproduktion

Im Repository: `python analysis/OP5_Uncertainty_Check.py` erzeugt OP5_Uncertainty_Check.json neben dem Skript. Ein optionales erstes Argument legt einen anderen Ergebnispfad fest. Benötigt Python 3.12 und SymPy 1.14.0; der Vertrag liegt in OP5_Uncertainty_Contract.json.

Der ursprüngliche lokale Lauf verwendete den computation-audit-Runner und ein erfolgreich validiertes Manifest. Bei der Repository-Übernahme wurde lediglich die Ausgabepfadwahl portabel gemacht und die Rechnung erneut ausgeführt. Das ursprüngliche lokale Manifest wird nicht als unveränderte Provenienz dieser angepassten Skriptdatei ausgegeben. Die Ergebnisse und der begrenzte mathematische Geltungsbereich bleiben gleich.
