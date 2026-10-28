# OP5: Abhängigkeiten zurück zur kosmologischen Konstante

Datum: 25. Oktober 2026. Geprüfte Revision: `f2de387d66d6ab2da00ef28a14305729910d7ef1`.
Begrenzter Quellen- und Folgerungsaudit. Keine Änderung am Paper, keine Veröffentlichung,
kein neuer physikalischer Abschluss. Koordinationsauftrag: die historische OP5-Kette bis
zur behaupteten Lambda-Zuordnung zurückverfolgen und prüfen, welche Rolle ein aus zwei
Frames konstruierter neutraler Bezug übernehmen könnte.

## Primärer Befund

Die früheste noch fehlende Verbindung liegt vor der Wahl eines neutralen Frames:
Der spektrale Ausdruck ist nicht als wohldefinierte metrikabhängige Wirkung gegeben.
Seine drei Bestandteile sind daher nicht bereits hergeleitete Beiträge zu
Einstein-Tensor, Materiestress und kosmologischer Konstante. Ein anderer Frame kann
diese fehlende Wirkungs- und Variationsdefinition nicht allein liefern.

Der später eingeführte Ausdruck `beta_sym^2 <f,f>` ist ein formulierter Frame-Term.
Sein Nullwert bei `beta_sym=0` folgt aus der gewählten Parametrisierung. Er ist kein
Beweis, dass die gesamte Vakuumwirkung oder die gravitative kosmologische Konstante
verschwindet. Die aktuelle r24-Konvention identifiziert den betreffenden alten
„Photon-Frame“ mit Referenzframe R, nicht mit dem Photonenzustand P.

## 1. Die tatsächliche Kette und ihre getrennten Pfeile

| Schritt | Rohquelle, genaue Fundstelle | Befund und Evidenzlabel |
| --- | --- | --- |
| Dilationoperator `L0=-i(x d/dx+1/2)` -> spektrale Spur `Sigma(t)=Tr exp(-itL0)` | `sources/research/parts/v470/10_sphaera_and_physics.tex:1460–1493`, `thm:einstein` | Spektrale Modellzuordnung; Domain, Volumen-/Spurregularisierung und ein vierdimensionaler metrikabhängiger Operator fehlen hier. **Unvollständig** für die physikalische Anwendung. |
| Spur -> `S=int_0^infty Sigma(t)dt` | dieselbe Quelle, `:1462–1467`; Korrektur `sources/research/parts/v480-post-release-layers.tex:640–661`, r05.2 | Unregulierte Wirkung nicht definiert; kein Testfunktionspaar mit ausgewiesener Metrikabhängigkeit. Die unitäre Spur wird zudem als Wärmekern behandelt. **Unvollständig**, im aktuellen Projekt selbst zurückgestuft. |
| `Sigma=1-Theta+R` -> Zuordnung der drei Variationen zu Lambda, Materie, Einstein-Tensor | `10_sphaera_and_physics.tex:1468–1491`; r05.1/r05.2 in `v480-post-release-layers.tex:605–661` | Alte Zerlegung korrigiert. Die neue Zerlegung als Identität zwischen Distributionen beweist die gravitative Zuordnung nicht. **Strukturelle Vermutung**, keine hergeleitete Einstein-Gleichung. |
| Konstanter Spuranteil -> `Lambda_bare~gamma_1^2~200 mP^4` | `23_physical_readouts.tex:388–391`, `prop:bare-lambda`; r05 in `v480-post-release-layers.tex:663–668` | Als Herleitung zurückgezogen. Der korrigierte Polterm `exp(t/2)` enthält keine erste Nullstelle; der Faktor `gamma_1²` wird daraus nicht erzeugt. **Zurückgezogener/ungestützter Ansatz**. |
| `tau_n²=t_n²-beta²` -> dunkle Energiedichte `~beta² rhoP` | `10_sphaera_and_physics.tex:1203–1229`, `thm:dark-offset` | Ein konstanter dimensionsloser Term ist zunächst ein Offset. Eine Ableitung einer gravitativen Energiedichte bzw. ihres Zustands benötigt zusätzliche Dynamik und Einheiten. **Unvollständige physikalische Identifikation**. |
| Modellterm `L_frame=beta²<f,f>` -> kosmologischer Stress `beta² g_mu_nu` | `10_sphaera_and_physics.tex:1627–1645`, `def:lagrangian`; `:1685–1694`, `prop:lambda-from-frame` | Der Term ist **definiert**. Sein Variationsergebnis braucht eine Raumzeit-Wirkung mit Volumenform, normiertem Zustandsfaktor, Feldern und deren Metrikabhängigkeit. Diese Angaben stehen dort nicht. **Bedingt/unvollständig**. |
| `beta=0` im alten Photon-Frame -> kein Frame-Term | `23_physical_readouts.tex:396–426`, `thm:lambda-zero(i)` | `beta²<f,f>=0` ist **korrekt als Definitionsfolge**, sofern der Zustandsfaktor endlich definiert bleibt. Es schließt keine anderen konstanten Wirkungsterme aus. |
| Markov-Abgangswahrscheinlichkeiten -> `Omega_M=beta²`, `Omega_Lambda=1-beta²` | `10_sphaera_and_physics.tex:1364–1399`, `thm:dark-energy` | Wahrscheinlichkeiten sind dimensionslos. Ihre Identifikation mit kosmologischen Energiedichteanteilen ist eine eigene **Modellannahme**, keine Folgerung aus dem Markov-Status. Der Text unterscheidet heute Flussfraktionen und stationäre Zustandsverteilungen. |
| `Lambda_obs=beta²/ellP²` -> beobachteter Wert | `23_physical_readouts.tex:409–444`; F3/F4/F8 in `v480-post-release-layers.tex:89–123,191–202` | Richtige Krümmungseinheit, aber falscher Zahlenmaßstab nach dem vorhandenen Audit; kein bloßer Einheitenfehler. **Als quantitative Identifikation widerlegt** in der dokumentierten Auswertung. |
| Zwei Frames / neuer neutraler Bezug -> alle vorigen Pfeile | kein entsprechender nativer Satz gefunden | Kann einen Bezug, eine Vergleichskarte oder einen zusätzlichen Zustand definieren. Er liefert nicht automatisch Wirkung, Metrikvariation, Vakuumstress, physikalische Einheiten oder absolute Skala. **Offene Brückenpflicht**. |

Die entscheidende Graphstruktur ist:

```text
Spektrum + Operatorbereich + metrikabhängige Realisierung
    -> regulierte Wirkung Gamma[g, fields; reference data]
    -> vollständige Metrikvariation bei festgelegten unabhängigen Größen
    -> geometrischer Koeffizient A und konstante Dichte rho
    -> Lambda_cos = rho/(2A)  [unter der unten festgelegten Konvention]
    -> physikalische Newton-/Planck-Kalibrierung und kosmologische Lösung.

Separater Ast:
Framezustände -> relativer Parameter / Mischzustand / Referenzkarte
    -> Einfluss auf Gamma  [zu definieren, nicht aus dem Namen ableitbar].
```

## 2. Was Lambda hier genau heißen müsste

Mit Signatur `(-,+,+,+)` und der ausdrücklich gewählten Vergleichswirkung

\[
S=\int d^4x\sqrt{|g|}\,[A R-\rho+\mathcal L_m],
\qquad
T_{\mu\nu}=-\frac2{\sqrt{|g|}}\frac{\delta S_m}{\delta g^{\mu\nu}},
\]

bei konstanten A und rho und geeigneten Randbedingungen ergibt die Variation

\[
A G_{\mu\nu}+\frac\rho2g_{\mu\nu}-\frac12T_{\mu\nu}=0,
\qquad
\Lambda_{\rm cos}=\frac\rho{2A}.
\]

Das ist eine direkte bedingte Rechnung, keine Herleitung dieser Wirkung aus
dem Framework. Sie zeigt die fehlenden Normalisierungen: rho ist eine Dichte,
Lambda_cos hat Krümmungsdimension, A trägt die gravitative Normierung.
Eine dimensionslose Zahl beta² ist noch keines von beiden.

Falls `rho` eine physikalische Energiedichte ist und die gewöhnliche Einstein-
Normierung benutzt wird, lautet die Zuordnung `Lambda=8 pi G rho/c^4`.
Bei Massendichte statt Energiedichte wäre der c-Faktor anders. Die Rohquelle
vermischt diese Lesarten; eine neue Einordnung muss sich ausdrücklich entscheiden.

Ebenso gilt: Ein additiver Term in einer Definition von `tau²` bestimmt für
sich noch keine vierdimensionale Metrik samt Ableitungen und daher keine
Krümmung. Insbesondere folgt aus einem konstanten Zahlenoffset nicht allein
eine Friedmann-/de-Sitter-Dynamik.

## 3. Definition von Nullpunkt und physikalischer Nullwert

Die Quelle sagt im Beweis zu `thm:lambda-zero` ausdrücklich: beta sei im
betreffenden Frame per Definition null. Daraus folgt das Verschwinden des
so definierten Frame-Terms. Eine stärkere Aussage benötigt unabhängig:

1. dass dieser Term die gesamte konstante Dichte der vollständigen Wirkung ist;
2. dass seine Metrikvariation wirklich den Vakuumstress und keine zusätzliche
   Feldgleichung, Metrikabhängigkeit oder anisotrope Antwort enthält;
3. dass das Setzen auf null eine physikalische Eigenschaft und nicht eine
   Wahl der Referenz/Subtraktion ist;
4. dass quantenmechanische Fluktuationen und weitere Sektoren diesen Nullwert
   erhalten oder ihre Beiträge durch eine berechnete Symmetrie kompensieren.

Die schon vorhandene Analyse `HC_Induced_Gravity_Heat_Kernel.md:309` trifft
diese Unterscheidung explizit: `Gamma[g]-Gamma[g0]` bei festem g0 verändert die
Variation nach g nicht. Ein Abzug `rho0 int sqrt|g|` verändert sie, ist aber ein
lokaler kosmologischer Gegenterm. Der neue Name „neutral“ entscheidet nicht,
welche dieser Operationen gemeint ist.

## 4. Was eine Kombination von zwei Frames leisten kann

Die Idee ist mathematisch zulässig, wenn die Kombination definiert wird:
zum Beispiel ein gemeinsamer Ruhe-/Energieframe, ein symmetrischer Rapidi-
tätsmittelpunkt oder ein gemischter Zustand. Diese drei Objekte sind nicht
ohne weitere Brücken gleichzusetzen.

Ein einfacher Gegencheck verhindert eine falsche Schließung. Zwei reale
Offsetwerte +z und -z sind im Mittel neutral, aber

\[
\tfrac12(+z)+\tfrac12(-z)=0,
\qquad
\tfrac12 z^2+\tfrac12(-z)^2=z^2.
\]

Allgemein: `E[z²]=(E[z])²+Var(z)`. Ein neutraler erster Moment beseitigt einen
quadratischen Energiekandidaten also nicht. Energie des gemittelten Zustands
und gemittelte Energie sind verschiedene Operationen. Dies ist ein exakter
algebraischer Gegencheck; es wird damit keine spezifische QAM-Energie definiert.

Eine stärker relationale Formulierung wäre etwa ein eigener Modellterm
`V=mu^4 F(eta1-eta2)` auf einer gemeinsamen reellen Rapidi­tätslinie. Er wäre
gegen einen gemeinsamen Shift beider eta invariant und könnte am Mittelpunkt
nicht ohne Weiteres verschwinden. Das ist nur ein Formbeispiel. Weder mu noch F
noch die Kopplung an g sind dadurch aus QAM oder den Frame-Bezeichnungen
abgeleitet. Eine native Tachyonrelation darf nicht stillschweigend als zweiter
gewöhnlicher zeitartiger Lorentz-Beobachter behandelt werden.

Für einen echten Vakuumterm `T_vac=-rho g` ist seine Koeffizient rho bei
gewöhnlichen Lorentz-Beobachterwechseln unverändert. Die gemessene Vakuum-
energiedichte `T_vac(u,u)=rho` für normierte zeitartige u zeigt dies direkt.
Ein anderer gemeinsamer Ruheframe kann einen Energiefluss entfernen, aber
keinen vorhandenen skalaren Vakuumterm allein durch Beobachterwahl löschen.
Aktive Zustandsänderung, Mischung oder Coarse-Graining ist eine andere Frage.

## 5. Anschluss an bereits vorhandene Forschungsmechanismen

`HC_Induced_Gravity_Heat_Kernel.md:11–31,48–109` besitzt eine deutlich präzisere
bedingte Kette: zusätzlicher metrikabhängiger elliptischer Dirac-Operator,
reguliertes Determinantenmaß ds/s, Krümmungskoeffizient A, Vakuumdichte rho.
Dies ist eine Vergleichstheorie mit zusätzlichen Voraussetzungen, nicht die
Wiederherstellung des alten Trace-Theorems. Ihr rein fermionischer Beitrag
erzeugt gerade eine ununterdrückte Dichte (`:164–184`).

Eine dort untersuchte echte sektorielle Kompensation kann den flachen
Vakuumkoeffizienten aufheben, ohne den Einstein-Koeffizienten zu löschen
(`:208–299`). Dafür werden passende zusätzliche skalare Moden und Massen
explizit gewählt. Das ist eine Änderung des Feldinhalts/eine dynamische
Kompensationsbedingung, keine Wahl eines neutralen Beobachters. Die native
Identifikation und Stabilität dieser Paarung bleiben offen (`:301–311`).

`HC_Two_Frame_Action_Bridge.md:50–78` zeigt zugleich: Bloßes lineares Mitteln
entfernt den dortigen gemeinsamen Spurobstruktionsterm nicht. Eine gemeinsame
Wirkung mit Multiplikator liefert Nebenbedingungen und Rückwirkung; sie
erzwingt nicht automatisch die separate Einstein-Gleichung. Das erklärt,
welche Zusatzarbeit eine Zwei-Frame-Deutung tatsächlich benötigt.

Die spätere Zähl-Lesart in
`notes/research/v4_10_0_r63_r64/llm/Pruefung_Gravitation_Frames.md:3–20`
verschärft die Typfrage: Beide Zählungen benutzen dort dieselbe Fläche und
dasselbe G/ellP. Die früheren Umrechnungsgewichte von hbar und G sind durch das
Zählverhältnis allein nicht gestützt. Ein dimensionsloses Zählverhältnis darf
also nicht nochmals unbemerkt eine physikalische Planckskala erzeugen.

## 6. Stärkste vertretbare Neueinordnung

Eine sinnvolle Arbeitsfassung trennt künftig:

- **Frame-Geometrie:** Ein relational konstruierter neutraler Bezug braucht
  mindestens die verglichenen Zustände und eine definierte Symmetrie-/Gewichts-
  regel. Er darf als eigenständiges Vergleichsobjekt geführt werden.
- **Dimensionsloser Readout:** beta² oder eine neue relationale Funktion kann
  einen Kontrast, ein Gewicht oder eine angenommene Flussfraktion parametrisieren.
  Das ist nicht automatisch die beobachtete kosmologische Krümmung.
- **Vakuum-/Gravitationsdynamik:** Der gemeinsame Wirkungskoeffizient rho und
  sein Verhältnis zu A müssen separat abgeleitet und kalibriert werden.

Die schon in r03 angebotene Lesart `Omega_Lambda=1-beta²` vermeidet die
Einheitenvermischung. Mit gemessenem H0 liefert sie
`Lambda=3 Omega_Lambda H0²/c²`. Damit wird die absolute Skala aber ausdrücklich
aus H0 übernommen und die Hierarchie nicht erklärt
(`v480-post-release-layers.tex:212–235`). Sie ist ein möglicher phänomenologischer
Ansatz, keine abgeschlossene OP5-Lösung und im Projekt nicht als neue Definition
adoptiert.

Die kosmologische Neueinordnung ist deshalb offen, aber enger bestimmt:
Ein neutraler Zwei-Frame-Bezug könnte die Bedeutung des relativen Readouts
verbessern. Er repariert die älteren Lücken bei Wirkung, Variation, Dichte-
Krümmungs-Konversion und absoluter Skala nicht durch seine Konstruktion allein.

## Prüfprovenienz

Gelesene Rohquellen und vorhandene Forschungsnotizen; algebraische direkte
Kontrollen zu Variation und Mittelung. Kein neuer numerischer Lauf, kein
externes Theorem als hier neu verifiziert ausgegeben. Quellenstatusangaben
sind zum Teil bereits vorhandene Autorenkorrekturen und wurden als solche
ausgewiesen; keine externe unabhängige Begutachtung.

SHA256 der Hauptquellen bei diesem Audit:

```text
v470/10_sphaera_and_physics.tex 7D72C58B1159F5462C6BE395961FCD8882028FC3E8C8495E7F2A3B10055C1A32
v470/23_physical_readouts.tex   55F6FBD55EB4290D523BE9C214190C6F91F62838E5718099B1EC20082E726242
v480-post-release-layers.tex  B2EB049956E3761440CD7DC3A7562A5BE32571013C3E14726169781040A072BB
v490-post-release-layers.tex  232BDD631BAC34259BE48B6D326FBF6EAF38F084EE4BEC1A621658B3C964424E
HC_Induced_Gravity_Heat_Kernel.md 3910A1FEE31AD4B27FAC0445FDC2BB53ED5FF6C8442D52556C76651426C1A340
HC_Two_Frame_Action_Bridge.md BD5649A5D5BC219B7F2878085A059B5D5344F5705BEDB3EA63C59F874355725D
```
