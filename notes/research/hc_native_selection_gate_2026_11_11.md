# Native Auswahl nach der Zeta-/Unschärfe-Erkundung

11. November 2026, Codex. Analytische Erkundung, nicht blind. Fortsetzung
nach Merge von PR #93 als e0e25fc18c078294933341a3e291f373f43245b7.
Keine neue H-Nummer, keine Simulation, keine Änderung historischer Runden.

## Vorwissen und Rückwärtssuche

Gesucht ist ein nativer zweiter Operator, der HC-Sektoren verbindet und
normalisierbare Auswahlzustände besitzt. Die Multiplikatorroute aus
`zeta_prime_operator_uncertainty_2026_11_11.md` besitzt solche exakten
Eigenzustände nicht. Der Vergleich bleibt auf positiver komplexifizierter
Hilbertmetrik mit komplex-linearer Erweiterung des reellen J. Er löst
keine native antiunitäre Konvention und identifiziert keine M/T/P-Frames.

Gelesen und eingeordnet:

- `generation-coupling.tex`, `v480:generation-closed-seeds`, Absatz
  „The spectral restriction is not the new coupling“ und
  `v480:generation-defect-gram`: ein nur auf H_- wirkendes A kann
  nicht zugleich nichtnullig sein und mit J antikommutieren.
- `native-operator-link.tex`, `v480:native-penalty-identity`,
  `v480:native-closure-transfer`, `v480:native-isospectral-freedom`:
  der minimale positive Penalty ist closure-blockdiagonal; ein Spektrum
  allein bestimmt die Übergangsmatrix relativ zu Closure und Seeds nicht.
- `hc-dynamics-and-geometry.tex`, `v480:hc-root-domain` und
  `v480:hc-projected-autonomy`: positive Wurzelzulässigkeit und projizierte
  Dynamik benötigen eigene Voraussetzungen; der formale Mastergenerator
  ist noch kein selbstadjungierter Hamiltonoperator auf geklärter Domäne.
- `analysis/Generation_Closure_Coupling.md`,
  `analysis/Native_Operator_Link_Audit.md`, `analysis/HC_Root_Readout.md`:
  native Tupel (P,R_beta,Seeds), Eingriffsregel und Auslesung sind offen.
- QAM-Suche `generation-defect`: kein Treffer; keine MMA-Belege beansprucht.

Rückwärtssuche: Erst den erforderlichen J-wechselnden Block isolieren und
die Wurzelauslesung gegen die vorgeschlagenen Zustände prüfen. Keine
weiteren Zeta-Profile oder numerischen Eigenvektoren auf freien Gittern.
Die Auslöser der zurückgestellten Ideen wurden geprüft; kein neuer
Auslöser durch diesen Vergleich innerhalb eines gemeinsamen Trägers.

## 1. Zwei verschiedene Zerlegungen nicht verwechseln

J ist die selbstadjungierte HC-Involution; E_±=(I±J)/2 sind ihre
orthogonalen Sektorprojektoren. P ist dagegen der orthogonale
Closure-Projektor. Im angegebenen Vergleich gilt [P,J]=0, aber P ist
nicht mit E_+ gleichgesetzt. Sei R_beta beschränkt, mit geklärten
Einheiten wie in der bestehenden Konstruktion. Die folgende Darstellung
verwendet seine dortige dimensionslose Normierung R_tilde.

Definiere den J-ungeraden Anteil und den Closure-Defekt

$$
R_o=\tfrac12(\widetilde R-J\widetilde R J),\qquad
D=(I-P)\widetilde R P.
$$

Wegen [P,J]=0 folgt exakt

$$
D_o=\tfrac12(D-JDJ)=(I-P)R_oP.
$$

Eine mögliche selbstadjungierte Vergleichskopplung wäre A=D_o+D_o*.
Sie erfüllt AJ=-JA. Wegen D_o=(I-P)D_oP sind die beiden Summanden
verschiedene Closure-Blöcke: A=0 genau dann, wenn D_o=0.
Insbesondere [R_tilde,J]=0 impliziert D_o=A=0, selbst wenn D nicht null
ist. Closure-Leckage ist also nicht automatisch ein HC-Sektorwechsel.
Der Ausdruck für A ist eine zusätzliche Operation, kein aus der Wirkung
abgelesener Hamiltonoperator. Die Quelle liefert R_o nicht ausgewertet.

Die minimale Penalty H aus `native-penalty-identity` kommutiert mit P.
Daraus allein folgt keine Aussage zu [H,J]. Eine Identifikation beider
Zerlegungen wäre ein unbelegter zusätzlicher Schritt.

## 2. Was ein vorhandener ungerader Block leisten könnte

Jede beschränkte selbstadjungierte J-ungerade Kopplung hat auf H_+⊕H_-
die Form A=((0,L),(L*,0)), mit L:H_-→H_+. Für ein normalisiertes
Singularpaar Lv=su, L*u=sv, s>0, sind

$$
\chi_\pm=(u\pm v)/\sqrt2,\qquad A\chi_\pm=\pm s\chi_\pm,
$$

und für T=-iJA

$$
\psi_\pm=(u\pm i v)/\sqrt2,\qquad T\psi_\pm=\pm s\psi_\pm.
$$

Alle vier Zustände erfüllen <J>=0. Für psi_± gilt zusätzlich
<A>=0, Delta J=1, Delta A=s und |<JA>|=s: Robertson wird
ausgeschöpft. Für chi_± ist Delta A=0 und die Robertson-Schranke null,
obwohl dieselbe HC-Balance vorliegt. Balance ist daher nicht mit
einem eindeutigen Unschärfemechanismus gleichzusetzen.

Im endlichen Modell liefert jeder nichtnullige L ein Singularpaar;
ein nichtnulliger kompakter L ebenfalls. Ein allgemeiner beschränkter
L muss dagegen keine normalisierbaren Singularvektoren besitzen.
Genau diese Differenz trat beim arithmetischen Multiplikator auf.
Eine finite Projektion ohne native Auswahl würde das fehlende Spektrum
nur zusätzlich einsetzen.

Auch Existenz ist noch keine Präparation: Eine unitäre Evolution
unter einem mit J kommutierenden selbstadjungierten H erhält <J>.
Im beschränkten Fall folgt das aus d<J>/dt=i<[H,J]>=0. Die Quellen
liefern weder einen nichtnulligen ausgewerteten R_o noch eine Auswahlregel,
welche einen der oben angegebenen Zustände unabhängig präpariert.

## 3. Gegenprobe an der bereits vorhandenen quadratischen Auslesung

Zusätzlicher, ausdrücklich nur vergleichender Anschluss: Identifiziere
eine normierte Zwei-Moden-Koordinate chi=(a,b) mit einer geraden und einer
ungeraden Basisrichtung, also J=diag(1,-1). Das Paper hat diese
Identifikation mit dem oben verwendeten Singularpaar nicht nativ bewiesen.

Die vorhandene quadratische Auslesung definiert
X0=|a|²+|b|², X1=|a|²-|b|², X2=2Re(conj(a)b),
X3=2Im(conj(a)b) und

$$
L_\eta=X_0E_0+\eta X_1E_1+\eta X_2E_2,
\quad E_0=I_3/\sqrt3,\quad E_2=i(U-U^*)/\sqrt6,
\quad \eta\geq0.
$$

U ist der Dreierzyklus; eta bezeichnet hier den im Original zeta
genannten freien Verstärkungsparameter, NICHT die Riemannsche Zeta.
Nur wenn L_eta positiv semidefinit ist, sind seine Eigenwerte zulässige
Hauptwurzeln. Die zitierte Proposition liefert

$$
K=\frac{1+\eta^2[1-(X_3/X_0)^2]}3.
$$

Für die T-Auswahl chi=(1,±i)/sqrt(2) gilt X1=X2=0, |X3|=X0.
Dann ist L_eta=X0 E0 positiv und K=1/3 für jedes eta. Die maximale
J-Streuung wird durch diese konkrete Auslesung nicht zu Koide transportiert.

Stärker: Jeder J-balancierte Zustand hat X1=0. E2 besitzt die Eigenwerte
0,±1/sqrt(2); daher erzwingt L_eta>=0

$$
\eta|X_2|\leq\sqrt{2/3}\,X_0,
\qquad K=\tfrac13\bigl[1+\eta^2(X_2/X_0)^2\bigr]\leq5/9<2/3.
$$

Die Schranke ist scharf innerhalb dieser Vergleichsannahmen: Wähle
X2=X0, X3=0 und eta=sqrt(2/3); dann hat L_eta einen Null-Eigenwert.
Sie ist KEIN allgemeines Koide-No-go und widerspricht nicht der linearen
Abstiegsproposition: Es sind verschiedene Wurzelgesetze. Sie zeigt, dass
die direkte Identifikation dieser Zwei-Moden-Graduierung mit dem HC
zusammen mit genau dieser positiven quadratischen Auslesung nicht reicht.

## Ergebnis und nächster konkret fehlender Input

1. Ausgewertetes R_o und (I-P)R_oP auf einem gemeinsamen nativen Träger.
2. Normalisierbare Singular-/Auswahlzustände oder eine begründete andere
   Zustandsregel, nicht bloß ein postuliertes Spektrum.
3. Eine native Wurzelauslesung, die Balance in positive drei Wurzeln mit
   dem benötigten Verhältnis überträgt. Die oben geprüfte quadratische
   Vergleichsroute schließt diese direkte Übertragung aus.

Validierung: analytische Blockmultiplikation, Singularpaaridentitäten,
Robertson-Erwartungswerte und Eigenwerte des vorhandenen Dreierzyklus
selbst geprüft. Kein numerischer Massenfit, kein Formalbeweis, keine neue
QAM-Beweisfreigabe und keine OP-Schließung.
