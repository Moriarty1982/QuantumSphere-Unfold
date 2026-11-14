# OP3: Slotphasen aus der Trialität – und die Grenze für Fourier

14. November 2026, Codex. Analytische und exakt symbolische Erkundung,
**nicht blind**: D und S waren als Ziele bekannt. Einordnung T5/T7/T8,
OP3. Keine Vorhersage, H-/k-Nummer, MMA-Rechnung oder Änderung eines Guards.

## Vorwissen geprüft und Suchrichtung

Ausgangspunkt ist `../op3_fourier_native_gate_2026_11_14.md` nach PR #122.
Gelesen: aktuelle Übergabe, Gesamtbild, r35.1(d) (Ladungsoperator),
r37.1(a)–(c) (Trialität und diagonale Farbe),
`../op3_triality_carrier_gate_2026_11_12.md`,
`../op3_tau_doublet_axis_2026_11_14.md`,
`../op3_slot_fourier_2t_2026_11_14.md`, die neutralen SU(2)- und
Sedenionen-Notizen sowie die bisherigen Vorbefunde in predictions,
v4_10_0-Runden und analysis. Die alte Schranke für monomiale Operationen
beantwortet nicht, welche Slotphasen die volle Trialität tatsächlich trägt.
CT-003 aus dem Sedenionenweg wird hier nicht vorausgesetzt.

Suchrichtung rückwärts: Zuerst eine gemeinsame Ladungszerlegung angeben,
dann die benötigten Phasen in der vorhandenen Trialität darstellen.
Erst danach fragen, ob Fourier als Symmetrie überhaupt möglich ist.
Keine weitere Trägersimulation oder Massenanpassung.

Der QAM-Leseserver ist weiterhin nicht verfügbar. Die lokale Ersatzabfrage
`python -X utf8 -m qam.tools.readout_db --read-only find --limit 3 -- triality`
endete mit Code 0 ohne Treffer. Aktualität/Vollständigkeit dieses lokalen
Index gegenüber den neu geholten Quellen ist nicht bestätigt. Es wird
kein Beleg-/Prämissenhash als Nachweis benutzt. Die folgenden Aussagen
werden unmittelbar hergeleitet und separat exakt geprüft.

## 1. Ein gemeinsamer farb- und ladungstypisierter Slotraum

Auf jeder reellen Kopie O setzen wir, in derselben Basis wie r35,

$$L=L_{e_7},\quad R=R_{e_7},\quad
J_0=(L+R)/2,\quad J_c=(L-R)/2.$$

J_0 dreht nur die farbfeste Ebene E=span_R(1,e_7), J_c nur ihr
sechsdimensionales orthogonales Komplement W. Beide sind schiefsymmetrisch,
kommutieren und erfüllen J_0 J_c=0. Farbautomorphismen fixieren e_7 und
kommutieren deshalb mit L und R. In jedem Slot ist somit

$$g_i=\exp(\alpha_i J_0+\beta_i J_c)$$

orthogonal, komplex-linear bezüglich L und farbneutral. Auf der externen
Komplexifizierung benutzen wir den ausdrücklich gemeinsamen r35-Operator

$$Q_8=\tfrac12 I-\tfrac{i}{6}L-\tfrac{i}{3}R.$$

Alle g_i kommutieren mit Q_8. Das liefert gleichartige ladungstypisierte
Mehrfachräume auf den drei Slots, ohne volle Spin(8)-Darstellungen für
äquivalent zu erklären:

| Q_8 | innere Eigenwirkung | Phase von g_i | Mehrfachraum auf drei Slots |
|---|---|---|---|
| 0 | J_0=-i | exp(-i alpha_i) | C³, farbfest |
| 1 | J_0=+i | exp(+i alpha_i) | C³, farbfest |
| 2/3 | J_c=-i | exp(-i beta_i) | drei Farbtripletkopien |
| 1/3 | J_c=+i | exp(+i beta_i) | drei konjugierte Farbtripletkopien |

Insbesondere hat w=1+i e_7 die Ladung Q_8=0, sein Konjugat die Ladung 1.
Die externe Einheit i ist von der inneren komplexen Struktur L zu trennen.
Auf E als innerer komplexer Geraden lautet die Phase exp(+i alpha_i);
auf der extern komplexifizierten Q_8=0-Geraden ist sie konjugiert.

Dies ist die vorhandene Q_8-Auslesung, keine vollständige Identifikation
von Lorentz-, Isospin-, Hyperladungs- und Chiralitätsdarstellungen.
Unter der r41-Wahl Y/2=Q_8-1/2 und einer getrennten, unberührten T_3-Wirkung
würde auch Q_em=T_3+Y/2 kommutieren. Diese zusätzliche Produktdarstellung
wird nicht allein aus O³ hergeleitet.

## 2. Die Trialitätsbedingung koppelt neutrale und farbige Phasen

Die gemeinsame G2-Wirkung genügt hier nicht. Wir erlauben verschiedene
g_i und verlangen die volle Trialitätsbedingung

$$t(g_0x,g_1y,g_2z)=t(x,y,z),\qquad t(x,y,z)=\operatorname{Re}((xy)z).$$

Im gewählten Phasentorus gelten genau, modulo 2 pi,

$$\alpha_0=\beta_2-\beta_1,\quad
\alpha_1=\beta_0-\beta_2,\quad
\alpha_2=\beta_1-\beta_0,\qquad
\beta_0+\beta_1+\beta_2=0.$$

**Notwendigkeit:** Auf einer Quaternionen-Unteralgebra E+E u mit u senkrecht
zu E werden die drei gemischten neutral/farbigen Terme der Form getrennt
erhalten; sie verlangen die drei Differenzbeziehungen. Der nichtverschwindende
rein farbige Dreiformanteil verlangt die letzte Summenbeziehung. Die rein
neutrale Form Re(z_0 z_1 z_2) verlangt dann alpha_0+alpha_1+alpha_2=0.

**Hinreichende Konstruktion:** Für a=exp(e_7 theta) erhält das Tripel

$$(L_a,\ R_a,\ L_{\bar a}R_{\bar a})$$

t exakt. Die Moufang-Identität gibt (ax)(ya)=a(xy)a. Mit dem reellen
Skalarprodukt $\operatorname{Re}(uv)=\langle u,\bar v\rangle$ wird die Invarianz zur Orthogonalität von
L_a R_a, denn die Konjugierte des dritten Bildes ist a bar(z) a.
Die drei Winkelpaare sind (alpha;beta)=(theta,theta,-2theta;theta,-theta,0).
Zyklische Varianten und ihre kommutierenden Produkte erzeugen den
zweidimensionalen Phasentorus. Dessen Projektion auf neutrale Phasen mit
Produkt eins ist surjektiv, mit drei Urbildern; diese unterscheiden sich
um das gemeinsame Farbzentrum beta_i -> beta_i+2 pi/3.

Infinitesimal, mit reellen Winkeln ohne modulo, gilt äquivalent

$$\sum_i\alpha_i=0,\qquad
\beta_i=(\alpha_{i+1}-\alpha_{i-1})/3$$

(Indizes modulo drei). Die exakte Rechnung über alle 512 Tensorstellen
liefert bei sechs Unbekannten Rang vier und genau diesen zweidimensionalen
Kern. Die Rechnung prüft diesen Sechsparameteransatz; sie ersetzt keine
vollständige unabhängige Reklassifikation von Spin(8).

## 3. D existiert, aber die volle Wirkung hat Ordnung neun

Auf der inneren neutralen Ebene sei omega=exp(2 pi i/3) und
D=diag(1,omega,omega²). Wähle

$$\alpha=(0,2\pi/3,-2\pi/3),\qquad
\beta=(4\pi/9,-2\pi/9,-2\pi/9).$$

Das ist eine konkrete Trialitätshebung von D. Auf dem Q_8=0-Mehrfachraum
wirkt sie als D^-1; die inversen g_i liefern dort genau D.
Ihre dritte Potenz ist auf E³ die Identität, auf W³ aber das gemeinsame
Farbzentrum omega² (bezüglich L). Erst die neunte Potenz ist überall eins.
Auch die beiden anderen Hebungen haben denselben Kubus: Multiplikation
mit einem Farbzentrum der Ordnung drei ändert ihn nicht. D hat daher in
diesem Phasentorus keine Hebung der Ordnung drei.

Dies widerspricht nicht der neutralen Ordnung drei. Es verbietet nur,
die neutrale Wirkung unverändert auf alle Teilchenarten zu übertragen.
Die aus dem Ziel D gewählten Winkel werden von der Trialitätsbedingung
zugelassen, aber nicht dynamisch ausgewählt.

## 4. S existiert nur projektiv auf dem neutralen Sektor

S=diag(1,omega,omega) verletzt schon die neutrale Produktbedingung.
Aus t(1,1,1)=1 würde t(1,omega,omega)=Re(omega²)=-1/2.
Eine genaue Hebung von S als t-erhaltendes Tripel ist damit ausgeschlossen.

Das projektiv gleiche S'=c S mit c=exp(-4 pi i/9) ist dagegen möglich:

$$\alpha=(-4\pi/9,2\pi/9,2\pi/9),\qquad
\beta=(0,2\pi/9,-2\pi/9).$$

Es wird konkret durch (L_bar(a) R_bar(a),L_a,R_a) mit a=exp(2 pi e_7/9)
realisiert. Wieder gilt auf Q_8=0 die konjugierte Wirkung, umkehrbar durch
Inversion aller Winkel. Auf dem isolierten neutralen Qubit ist die
Gesamtphase für reine Zustandsüberlappungen unsichtbar. Auf ganz O³ ist
sie das nicht: Die dritte Potenz wirkt neutral als omega I, farbig als
diag(1,omega,omega²). Die volle Wirkung hat Ordnung neun.

Also: Der Achsenwinkel der bedingten neutralen F/S-Konstruktion kann
projektiv erhalten bleiben. Eine gemeinsame 2T-Wirkung auf allen Arten
oder die Auswahl der Winkel/Bezüge folgt daraus nicht.

## 5. Eine stärkere Grenze: Fourier erhält die Trialitätsform nicht

Sei p(x_0,x_1,x_2)=t(x_0,x_1,x_2) die kubische Funktion auf O³.
Die ursprüngliche Fourier-Matrix hat

$$p(1,0,0)=0,\qquad
p\bigl(F(1,0,0)\bigr)=p(1,1,1)/(\sqrt3)^3=1/(3\sqrt3).$$

Damit kann keine p-erhaltende Operation, welche E³ invariant lässt, dort
genau als F wirken. Auch eine innere Gesamtphase lambda hilft nicht:
Für v=(lambda^-1,0,0) bleibt p(v)=0, aber lambda F v=(1,1,1)/sqrt3.

Die ladungstypisierte externe Komplexifizierung umgeht das nicht. Sei
p_C die komplex-lineare Fortsetzung des **Oktonionen-Realteils** in jeder
Tensorstelle (kein zusätzlicher Realteil der externen Zahlen). Für
w=1+i e_7 gilt w²=2w, w³=4w, also t_C(w,w,w)=4. Daher hat (w,0,0)
den Wert null, sein Bild unter lambda F für jedes lambda ungleich null
aber den Wert 4 lambda³/(3 sqrt3). Eine t_C-erhaltende Erweiterung von F
auf diesem Q_8=0-Mehrfachraum ist ebenfalls ausgeschlossen.

**Geltungsgrenze:** Ausgeschlossen ist F als aktive Symmetrie der
ursprünglichen Trialitätsform bei dieser Sektoreinbettung. Nicht
ausgeschlossen sind eine Dynamik, die t nicht erhalten muss, ein neuer
physikalischer Operator, eine andere Zustandsabbildung oder ein passiver
Basiswechsel mit gemeinsam transformiertem Tensor. Solche Änderungen
brauchen aber eine eigene Begründung. Summen von Trialitätssymmetrien
sind im Allgemeinen keine Trialitätssymmetrien.

## Ergebnis, Nachweis und nächster Schritt

Die native Phasenfrage ist teilweise beantwortet: D und projektives S
sind innerhalb der farbneutralen, Q_8-verträglichen Trialität realisierbar.
Die volle Wirkung trägt zusätzliche Farbphasen und Ordnung neun.
Die reine Symmetrieroute zur fehlenden Fourier-Operation scheitert
dagegen direkt an der Trialitätsform. Ihre Herkunft kann nicht allein
aus einer weiteren Trialitätssymmetrie folgen.

Nächste Pflicht ist daher eine benannte **Dynamik- oder Operatorbrücke**,
die auf den drei gleichartigen Zuständen aktiv mischt und t brechen darf,
mit begründetem Generator und physischer Rolle. Ohne eine solche Brücke
hier anhalten; keine weiteren Zielwinkel-, F4- oder Massenfits.
Koide und die Phase sind weiterhin nicht hergeleitet.

Reproduzierbare exakte Kontrolle: `check.py --result PATH`, Vertrag in
`contract.json`, geprüfter Lauf in `run/`. Aus dem Repo:

```
python notes/research/op3_triality_slot_phases_2026_11_14/check.py --result build/op3-triality-slot-phases-check.json
```

Der begrenzte Nachweislauf hat Status `completed`; Eingabe-/Ausgabehashes,
Versionen und Aufruf stehen in `run/manifest.json`. Manifest samt aktuellen
Eingabehashes erfolgreich validiert. Exakt geprüft: 512 Tensorstellen,
Rang/Kern, Q_8-Kommutatoren, Winkel und Ordnungen. Die Fourier-Sperre ist
der oben ausgeschriebene analytische Gegenbeweis, kein numerisches Urteil.
Eine unabhängige Prüfung bestätigte die Moufang-Konstruktion, Phasen-
und Ladungszeichen sowie diesen Gegenbeweis; ihr zusätzlicher numerischer
Stichprobenwert wird nicht als gespeicherter Beleg benutzt.

I1–I5 erneut geprüft: kein neuer Auslöser. OP1–OP5, C5, C6/T2 und alle
Guards unverändert. H100/H102 bleiben offen; CT-001/CT-002-Route ruht weiter.
