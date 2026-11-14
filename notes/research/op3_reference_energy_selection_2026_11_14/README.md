# OP3: Auswahl des Bezugszustands durch zwei Energieterme

14. November 2026, Codex. Analytische und exakt symbolische **Erkundung,
nicht blind**. Der Zielzustand, 2/3 und pi/4 waren vorher bekannt.
Einordnung T8/T13, OP3. Kein natives Gesetz, Hypothesentest, neuer
MMA-Beleg oder neuer CT-Eintrag; keine Änderung offener Guards.

## Vorwissen geprüft und geänderte Suchrichtung

Geprüft: Gesamtbild nach r13, aktuelle Übergabe,
`../op3_koide_potential_2026_11_13.md`,
`../op3_selection_principle_2026_11_13.md`,
`../op3_slot_fourier_2t_2026_11_14.md`,
`../op3_fourier_native_gate_2026_11_14.md`,
`../op3_triality_slot_phases_2026_11_14/README.md`,
`../op3_two_probe_fourier_bridge_2026_11_14.md` sowie die Platzhalterbilanz.
Suche nach Grundzustand, Projektorsummen, Selbstdualität und Lokalisierung
in Forschungsnotizen, predictions und analysis: Die früheren Potential-
und Auswahlnotizen benennen bereits die offene Bezugsauswahl und
abgestimmte Kopplungen; sie begründen den folgenden Hamiltonoperator nicht.
OP5-Geometrie-/Projektorbefunde werden nicht als neuer Auswahlbeleg übernommen.

Die aktive Fourier-Herkunftsroute bleibt wie festgehalten ruhend.
Hier wird eine **andere, schwächere Frage** untersucht: Lässt sich der
benötigte Bezug variational auswählen, ohne F als aktive Operation zu
postulieren? Das ist ein neuer begrenzter Vergleich, kein weiterer Fit
der freien T_12-Einträge und keine native Massenrechnung.

QAM-Leseserver nicht verfügbar. Lokale read-only-Abfragen nach `ground`
und `Fourier` endeten mit Code 0 ohne Treffer. Indexvollständigkeit nicht
bestätigt, keine Beleg-/Prämissenhashes als Nachweis. Remote-main bleibt
bei 31e689e. Kein neuer Datenvergleich; H100/H102 nicht ausgewertet.

## 1. Bereits benennbare Projektoren, zusätzlich gesetzte Energie

Wir arbeiten ausschließlich auf dem ausgewählten skalaren C³ mit
positiver Hermitemetrik. In der bisherigen Schreibweise sind

$$e=(1,0,0)^T,\quad s=(1,1,1)^T/\sqrt3,\quad
Q=ee^\dagger,\quad R=ss^\dagger.$$

Mit tau(x,y,z)=(y,z,x), D=diag(1,omega,omega²) und omega=exp(2 pi i/3)
gilt dort

$$Q=(I+D+D^2)/3,\qquad R=(I+\tau+\tau^2)/3.$$

Q und R sind also die normierten Spektralprojektoren auf die jeweils
ausgewählte Eigenlinie zum Eigenwert eins. Die feste Wahl der D-Linie
zeichnet bereits einen Slot aus. Andere Slots liefern umnummerierte
Vergleiche, keine zusätzliche Vorhersage.

**Sektorgrenze:** D hat auf dem neutralen Raum Ordnung drei, seine volle
Trialitätshebung aber Ordnung neun. Die obige Projektorformel wird
nicht ungeprüft auf alle farbigen Zustände übertragen. Auf dem
Q_8=0-Mehrfachraum ist auch die konjugierte neutrale D-Wirkung verfügbar;
sie hat dieselbe Eigenlinie zum Eigenwert eins. Ein selektiver Einsatz
nur im Majorana-Sektor wäre eine weitere physikalische Bedingung.

Als **zusätzlichen Vergleichs-Hamiltonoperator** setzen wir

$$H=-(aQ+bR),\qquad a,b>0.$$

Er belohnt einerseits einen bestimmten Slot, andererseits kohärente
Gleichverteilung über die Slots. Beide Projektoren haben Rang und Norm
eins; diese gemeinsame Normierung erzwingt aber nicht a=b.
Die Summe vorhandener Operatoren ist nicht schon ein aus der Wirkung
hergeleiteter Energieterm. Zeitnormierung, physische Koeffizienten und
Präparation bleiben offen. H muss die ursprüngliche Trialitätsform
nicht erhalten; die frühere Symmetriesperre wird nicht zurückgenommen.

## 2. Ein eindeutiges Minimum mit analytisch berechenbarem Bezug

Die Ebene span(e,s) ist dieselbe gerade Ebene span(e,u) mit
u=(0,1,1)/sqrt2. Die ungerade Richtung (0,1,-1)/sqrt2 hat Energie null.
Definiere

$$\Delta=\sqrt{a^2+b^2-2ab/3},\qquad
z=\frac{a-b/3}{\Delta},\qquad p=\frac{1+z}{2}.$$

Die drei Eigenwerte von H sind

$$-\frac{a+b+\Delta}{2},\qquad
-\frac{a+b-\Delta}{2},\qquad0.$$

Da a,b>0 gilt 0<Delta<a+b. Der Grundzustand ist somit eindeutig,
mit Lücke Delta zum ersten angeregten Zustand und normierter Richtung

$$\psi=\left(\sqrt p,\sqrt{(1-p)/2},\sqrt{(1-p)/2}\right)^T.$$

Für a=b wird daraus

$$\psi_* =\frac{(1+\sqrt3,1,1)^T}{\sqrt{6+2\sqrt3}}.
\qquad \Delta=2a/\sqrt3.$$

Genau dieser Bezug wurde in der Fourier-Erkundung vorausgesetzt. Hier
ist er Grundzustand eines ausgeschriebenen Vergleichsoperators. Für
die Variationsrechnung muss kein Fourier-Puls erzeugt werden.

## 3. Die Zahl 2/3 verlangt genau die Koeffizientenbalance

Betrachte wie zuvor die drei normierten Zustände psi_j=S^j psi mit
S=diag(1,omega,omega). Alle zyklischen Überlappungen lauten
d=p+(1-p)omega, also

$$f=|d|^2=\frac{1+3z^2}{4},\qquad
K_{\rm orb}:=\frac{1+2f}{3}=\frac{1+z^2}{2}.$$

Hier ist K_orb zunächst ein **Bahndiagnostikum**, keine identifizierte
physische Massenformel. Es gilt exakt

$$K_{\rm orb}-\frac23=
\frac{(3a+b)(a-b)}{9\Delta^2}.$$

Bei positiven Koeffizienten folgt daher

$$K_{\rm orb}=2/3\quad\Longleftrightarrow\quad a=b.$$

Bei dieser Balance ist d³=(1+i)/4: Die Bargmann-Phase der festgelegten
S-Orientierung ist +pi/4; bei S^-1 konjugiert sie. Für a/b=1+epsilon
beträgt die Abweichung K_orb-2/3=epsilon/3+O(epsilon²).
Die Auswahl ist also nicht gegenüber einer kleinen relativen
Koeffizientenabweichung geschützt.

F vertauscht Q und R. Die Gleichgewichtung könnte daher durch ein
**zusätzliches Austauschprinzip dieser beiden Projektoren** gesichert
werden; ein solches Prinzip ist im vorhandenen Energieterm nicht
hergeleitet. Die Austauschbedingung verlangt nicht eindeutig F auf dem
ganzen Raum, ist aber die verbleibende neue Voraussetzung des Vergleichs.
Aus zwei freien Zahlen bleibt nach gemeinsamer Energieskalierung genau
ein freies Verhältnis; die bekannte Zielzahl setzt es auf eins.

## 4. Drei Kontrollen gegen eine überstarke Deutung

### Das feste H erhält den S-Zyklus nicht

Der ausgewählte Bezug ist ein einziger Grundzustand. Seine S-Bilder
sind keine drei gleichenergetischen Grundzustände desselben H. Bei a=b
lauten ihre **Energieerwartungswerte**

$$\langle H\rangle_{\psi_*}=-a(1+1/\sqrt3),\qquad
\langle H\rangle_{S\psi_*}=\langle H\rangle_{S^2\psi_*}=-a.$$

Zur Kontrolle erzwingen wir S-Invarianz durch Mittelung:

$$\bar H=\frac13\sum_{j=0}^2 S^j H S^{-j}
=-(a+b/3)Q-(2b/3)uu^\dagger.$$

Für a>b/3 ist der Grundzustand e, für a<b/3 ist er u. Beide sind
S-Eigenzustände; ihre projektive Bahn ist trivial und K_orb=1.
Bei a=b/3 ist die Grundebene entartet und der Bezug nicht ausgewählt.
Insbesondere verliert die S-symmetrisierte Version bei a=b den Oktanten.

Der Grund ist allgemein: Ein S-invariantes H mit einfachem Grundzustand
hat diesen als S-Eigenzustand. Drei verschiedene S-bezogene Referenzen
erfordern eine Entartung oder weitere transformierende Hintergrunddaten.
Eine Familie verschiedener H_j=S^j H S^-j hätte zwar entsprechende
Grundzustände, würde aber neue, mittransformierende Felder/Daten benötigen.

### Ein Minimum ist keine Präparation

Unter der zeitunabhängigen unitären Entwicklung e^-iHt bleiben die
Besetzungswahrscheinlichkeiten der Energieeigenräume erhalten. Ein
beliebiger Anfangszustand relaxiert deshalb nicht automatisch nach psi_*.
Eine Grundzustandspräparation braucht ein begründetes Reservoir,
Abkühlungs-/Filtergesetz oder passende Anfangsdaten. Keines davon wird
aus dem Wort „Minimum“ gefolgert.

### Der Qubit-Bezug erzeugt noch keine drei positiven Massen

Die ganze S-Bahn liegt in span(e,u). Ihre Gram-Matrix hat daher immer
Rang zwei und Eigenwerte 3p,3(1-p),0. Bei a=b sind dies

$$\frac{3+\sqrt3}{2},\quad\frac{3-\sqrt3}{2},\quad0.$$

Für diese Gram-Matrix G gilt K_orb=Tr(G²)/(Tr G)². Die Lesart als
Koide-Diagnostik physischer Massen würde zusätzlich sqrt(m_i)
proportional zu den Eigenwerten von G setzen. Ein anderes Massengesetz
ist damit nicht gleichgesetzt. Auch mit dieser Wurzellesart bleibt eine
Masse null. Der bekannte Abstand der geladenen Leptonen vom Qubit-Rand
und eine native Massen-/Operatorbrücke sind weiterhin nicht erklärt.
Die nichtorthogonalen Bahnzustände werden nicht zu drei verschiedenen
Eigenzuständen eines selbstadjungierten Massenoperators erklärt.

## Ergebnis und begrenzter nächster Ansatzpunkt

Der Vergleich schließt eine **logische**, keine native physikalische
Lücke: Die Bezugsauswahl verlangt nicht zwingend eine aktive
Fourier-Operation. Ein einfacher hermitescher Energieterm kann denselben
Bezug als eindeutiges Minimum auswählen. Die unabhängige Voraussetzung
verlagert sich auf die physische Herkunft der beiden Terme, ihre exakte
Balance, die Symmetriebehandlung und die Präparation.

Sinnvoll wäre als Nächstes ausschließlich zu prüfen, ob eine vorhandene
Wirkung **diese beiden Projektoren mit gebundener gleicher Kopplung**
liefert und wie die erforderlichen Hintergrunddaten transformieren.
Die gemeinsame Normierung oder ihre formale Vertauschbarkeit allein
leistet das nicht. Ohne eine solche Quelle keine weiteren Gewichtsfits.
Keine neue Registerannahme wurde als CT-004 oder als strukturell
abgeglichen eingetragen.

## Reproduzierbarer Nachweis und Status

`check.py` prüft die ganze positive Verhältnisfamilie symbolisch, nicht
eine endliche Stichprobe. Vertrag: `contract.json`. Gespeicherter
begrenzter Lauf: `run/`, Status `completed`; Manifest und aktuelle
Eingabe-/Ausgabehashes validiert. Direkte Wiederholung aus dem Repo:

```
python notes/research/op3_reference_energy_selection_2026_11_14/check.py --result build/op3-reference-energy-selection-check.json
```

Exakt geprüft: Grundprojektor und charakteristisches Polynom,
Koeffizientenbedingung, erste Sensitivität, Bargmann-Invariante,
Bahnrang, Energieerwartungswerte und S-Symmetriekontrolle. Eine getrennte
analytische Gegenprüfung bestätigte diese Formeln und die Grenzen der
Präparations-/Massenlesart; Zustimmung ersetzt die ausgeschriebenen
Herleitungen nicht.

I1–I5 erneut geprüft: kein neuer Auslöser. Es wird weder ein konkreter
P_C7/M_16 noch ein Higgs-/FRW-Kondensat oder eine Informationsbrücke
eingeführt. CT-001/CT-002 bleiben ruhend; CT-003 gehört zum anderen
Träger. OP1–OP5, C5, C6/T2 und Guards bleiben unverändert offen.
