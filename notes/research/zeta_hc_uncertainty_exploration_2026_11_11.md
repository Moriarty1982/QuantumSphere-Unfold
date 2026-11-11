# Zeta-Profil, HC und Unschärfe: analytische Erkundung

11. November 2026, Codex. Nicht blind; keine neue H-Nummer, keine
numerische Simulation und keine Änderung einer Forschungsrunde.
Die untenstehenden Operatoridentitäten sind direkt hergeleitet.
Die Verbindung zur nativen Physik bleibt eine offene Modellroute.

## Einordnung, Vorwissen und Rückwärtssuche

Im Gesamtbild betrifft dies die Verbindung zwischen Algebra-Kern und
Massen-/Koide-Auslesung sowie die historische Riemann-Spektralroute.
Ziel ist weiterhin h=<v,Jv>=0 für v=B*e, nicht bloß eine symmetrische
Kurve oder das Auftreten der Zahl 1/2. Für Koide bleiben die Voraussetzungen
des HC-Abstiegs und die zulässige dreifache Hauptwurzelauslesung nötig.

Geprüfte Vorbefunde:

- `sources/research/parts/v480-post-release-layers.tex`, r04:
  der eigenständige HC ist C=(I+J)/2 für eine lineare unitäre Involution.
  Genannt sind eine e1-Reflexion und die Parität f(t)→f(-t).
  Die frühere Identifikation eines Operatorspektrums mit Zeta-Nullstellen
  ist ausdrücklich nicht erhalten. Die kinetische Invarianz der genannten
  Paritätsinstanz ist dort offen.
- `analysis/HC_Lepton_Readout_Identification.md` und
  `analysis/HC_Root_Readout.md`: native HC-/Wurzelraum-Identifikation fehlt;
  selbst native Kanalbalance ist ohne geeignete Auslesung kein Koide-Beweis.
- `notes/research/hc_koide_bridge_review_2026_11_11.md`:
  h=0 liefert Koide erst unter zusätzlichem Seed-/Wurzelgesetz.
- Suche in Vorab-Notizen und Forschungsnotizen: keine hier verwendete
  native Herleitung des unten definierten Vorzeichenoperators oder T gefunden.
  Vorhandene Zeta-Bezeichnungen sind nicht automatisch die Riemannsche Zeta.
- QAM-Registersuche nach `uncertainty`: kein Treffer; kein MMA-Beleg beansprucht.
- Zurückgestellte Idee I2 betrifft Primzahl-Kodierung/CRT. Hier wird kein
  arithmetischer Modul identifiziert; ein entsprechender Auslöser ist nicht
  neu nachgewiesen. I1/I3/I4 werden durch die folgenden Operatoridentitäten
  ebenfalls nicht neu aktiviert.

Rückwärtssuche: Ein zweiter selbstadjungierter Operator, der mit J
antikommutiert, könnte eine überprüfbare Auswahlregel liefern. Daher zuerst
diese fehlende Operation untersuchen, keine Nullstellen- oder Massenfits.

## 1. Träger und Profil

Nur für dieses Spielmodell: komplexer Hilbertraum L²(R,dt),
Skalarprodukt <a,b>=Integral conjugate(a)b. Dies erweitert den reellen
Vergleichsrahmen ausdrücklich; die komplexe Phase wird nicht als bereits
native Operation behauptet. t ist zunächst ein dimensionsloser Parameter,
kein identifizierter physikalischer Ort oder Zeitpunkt.

Mit der vervollständigten Zeta-Funktion definiere

$$
\Xi(t)=\xi(1/2+it),\qquad f(t)=N e^{-t^2}\Xi(t),\qquad \|f\|=1.
$$

Die Funktionalgleichung xi(s)=xi(1-s) macht Xi gerade. Die Konjugation
der Zeta-/Gamma-Faktoren zeigt, dass Xi für reelles t reell ist.
Das Fenster erzeugt ein glattes quadratintegrierbares Profil. Es ist
eine frei gewählte Regularisierung, keine aus der Physik bestimmte Skala.
Die folgenden beschränkten Operatoridentitäten brauchen lediglich ein
normiertes gerades f, nicht seine speziellen Zeta-Werte und nicht RH.

Quelle: [NIST DLMF 25.4](https://dlmf.nist.gov/25.4), insbesondere E3/E4.

## 2. Spiegelung und Vorzeichen sind zwei verschiedene Auslesungen

Setze Rf(t)=f(-t) und Sf(t)=sgn(t)f(t); der Wert bei t=0 ist im L²-Raum
unerheblich. Beide sind beschränkt, selbstadjungiert und involutiv.
Direktes Einsetzen ergibt RS=-SR. Für das gerade f gilt

$$
\langle R\rangle_f=1,\qquad \langle S\rangle_f=0,
\qquad (\Delta R)^2_f=0,\quad (\Delta S)^2_f=1.
$$

In der im Paper genannten Paritätsinstanz J=R gilt somit h=1. Die
bedingte Koide-Formel liefert K=1/3. J=S würde h=0 liefern, ist aber
eine andere Identifikation, die das Paper hier nicht nativ bereitstellt.
Die abstrakte HC-Projektorform allein entscheidet diese Wahl nicht.

Ein Basiswechsel repariert dies nicht: Auf den Paaren (f(t),f(-t)), t>0,
diagonalisiert die Hadamard-Matrix die Spiegelung. Dabei geht das gerade
Profil vollständig in den positiven Vorzeichensektor über. Transformiert
man Operator UND Zustand, bleibt der Erwartungswert 1. Man darf nicht
den Operator wechseln und den Zustand still unverändert lassen.

## 3. Eine tatsächliche Robertson-Unschärferelation

Für die beiden beschränkten selbstadjungierten Operatoren gilt auf ganz L²

$$
\Delta R\,\Delta S\geq\tfrac12|\langle[R,S]\rangle|
 =|\langle RS\rangle|.
$$

Für das ursprüngliche gerade f sind beide Seiten null: <RS>=0,
Delta R=0, Delta S=1. Die Unschärferelation ist erfüllt und wählt
keine HC-Balance aus. Ein nichtverschwindender Kommutatoroperator
garantiert keinen nichtverschwindenden Erwartungswert des Kommutators.

Quellenbasis: [Robertson 1929, Originalscan](https://www2.unicamp.br/~chibeni/textosdidaticos/robertson-1929.pdf).
Die konkrete Anwendung und die folgenden Identitäten sind Eigenherleitungen.

## 4. Konkrete zusätzliche Auswahloperation

Definiere T=-iRS. Aus RS=-SR folgt T*=T, T²=I sowie
TR=-RT und TS=-ST. Jeder normierte Eigenzustand von T erfüllt deshalb
<R>=<S>=0. Denn die Antikommutation und Tpsi=±psi geben
<psi,Rpsi>=-<psi,Rpsi>, ebenso für S.

Für das gerade normierte f ist g=Sf ungerade, normiert und orthogonal zu f.
Explizite Eigenzustände sind

$$
\psi_\pm=\frac{f\pm iSf}{\sqrt2},\qquad T\psi_\pm=\pm\psi_\pm.
$$

Direkte Rechnung ergibt

$$
\langle R\rangle_{\psi_\pm}=\langle S\rangle_{\psi_\pm}=0,
\quad \Delta R=\Delta S=1,\quad
\langle RS\rangle_{\psi_\pm}=\pm i.
$$

Damit wird Robertson exakt ausgeschöpft: 1=1. Die HC-Balance für J=R
ist jetzt gegeben, aber sie stammt aus der zusätzlich gewählten
T-Eigenzustandsbedingung beziehungsweise der relativen Phase ±pi/2.
Die Unschärfeungleichung allein fordert diese Auswahl nicht.

Auf span{f,Sf} sind R=diag(1,-1), S=((0,1),(1,0)) und
T=((0,-i),(i,0)): die bekannte zweidimensionale Pauli-Algebra.
Das ist keine zetaspezifische Entdeckung. Die komplexe Phasenoperation
und ihre native Zulässigkeit bleiben ausdrücklich zu begründen.

Die Familie psi_theta=cos(theta)f+i sin(theta)Sf zeigt die verbleibende
Freiheit: <R>=cos(2theta), <S>=0 und |<RS>|=|sin(2theta)|.
Robertson wird für JEDES theta ausgeschöpft, auch für theta=0 ohne
HC-Balance. Sättigung allein selektiert also nicht theta=pi/4.

## 5. Orts-/Impuls-Unschärfe und eine Domänengrenze

Für Q=t und P=-i d/dt gilt auf geeigneten gemeinsamen Domänen
[Q,P]=iI und Delta Q Delta P>=1/2. Die Einheiten sind hier dimensionslos;
es folgt kein physikalisches hbar aus dem Modell.

Das scharfe Vorzeichen hat eine Grenze: Für das konkrete Profil mit
f(0) ungleich null besitzt Sf einen Sprung bei null. Seine distributionelle
Ableitung enthält 2f(0)delta_0. Daher liegt Sf nicht in H¹(R), der
Domäne des üblichen selbstadjungierten P. Dasselbe gilt für psi_±.
Eine endliche Impulsvarianz dieser Zustände darf nicht angegeben werden.
Das beeinträchtigt die beschränkte R/S-Unschärferelation nicht.

Eine Glättung S_epsilon=tanh(t/epsilon) beseitigt den Sprung, verliert
aber S_epsilon²=I und damit die unveränderten T-/HC-Identitäten.
Alternativ kann ein anderes gerades Profil bei null verschwinden;
das ist eine zusätzliche Profilwahl, die separat zu prüfen wäre.

## Ergebnis und nächster nativer Prüfpunkt

- Vorhandene Paritätsinstanz plus gerades Zeta-Profil: keine Koide-Balance.
- Eine echte, exakt ausschöpfbare Unschärferelation existiert im Spielmodell.
- Ihr Ausschöpfen allein wählt die Balance nicht aus.
- Eine stärkere T-Eigenzustandsregel würde die Balance auswählen,
  benötigt aber einen nativ konstruierten zweiten Operator und die
  entsprechende Phasen-/Zustandsselektion.
- Zeta und Primzahlen sind in dieser Herleitung austauschbar; bisher
  entsteht kein arithmetisch spezifisches Massenverhältnis.
- Zusätzlich fehlen weiterhin die Koide-Abbildung B, zulässige positive
  Wurzelauslesung, Generationenbasis sowie Phase und Massenskala.

Sinnvoller nächster Schritt: Im nativen Träger einen zweiten zulässigen
selbstadjungierten Operator A mit AJ=-JA suchen und prüfen, ob eine
vorhandene Dynamik Eigenzustände von -iJA auswählt. Erst bei einem
solchen Anschluss wäre ein zetaspezifischer Profiltest gerechtfertigt.
Keine OP-Schließung; keine automatische Übertragung in das Paper/QAM-Beweisregister.
