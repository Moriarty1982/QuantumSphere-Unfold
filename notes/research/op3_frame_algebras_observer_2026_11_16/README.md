# OP3: eine Algebra je Frame-Abbildung, die vierte als Betrachter (Herleitung, Erkundung, nicht blind)

16. November 2026. Idee des Autors: „eine Algebra pro Frame benutzen und die vierte als Betrachter definieren“; Nachtrag: „bei der Aufteilung
in 3 könnte es sein, dass man HS(8) in zwei HS(7) aufteilen muss und ein HS(7) in zwei HS(6)“. Auftrag: Zuordnung aus dem Bestand herleiten,
H110 nur, wenn ein Mechanismus ohne freie Wahl entsteht. Skript `frame_observer.py`, Ausgabe `run/frame_observer_stdout.txt`.
Nicht blind: Der Zielwert 0,666665 war bekannt. Keine Kandidatenwerte für den offenen Parameter ausgewertet.

Namenshinweis: $R$ heißt hier die Frame-Abbildung von r16 (Tachyon-Abbildung $z\mapsto iz$, auf $\chi$ $\sigma_z$), nicht der Bezugsframe R
von Konvention F.

## 1. Die vier Kopien sind die Kleinsche Vierergruppe (hergeleitet, ohne freie Wahl)
Die Frame-Abbildungen $\{1,R,T,J_B\}$ bilden auf den drei Vorzeichen eines Feldes die Kleinsche Vierergruppe (r16.4(a)) und wirken auf $\chi$ als
$\{1,\sigma_z,\sigma_x,\sigma_y\}$ bis auf Phase (r16.7). Die vier Kopien von HS(8) tragen zwei Bits. Die Zuordnung
Bits $(a,b)\mapsto X^aZ^b$ ist ein Gruppenisomorphismus $\mathbb Z_2\times\mathbb Z_2\to\{1,R,T,J_B\}$ (numerisch geprüft):

| Kopie | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| Abbildung | 1 (Betrachter) | $R$ | $T$ | $J_B$ |

Eindeutig bis auf die Automorphismen der Gruppe, die die drei Abbildungen vertauschen. Die Kopie der Eins ist der Betrachter: Sie liest ohne
Abbildung. Damit hat der Träger genau einen Platz je Frame-Abbildung. Das liefert eine Lesart für die offenen Bedingungen (1) und (3) von r16.7
(„eine Auslesung je Frame-Abbildung“, „alle kommen vor“), keinen Beweis.

## 2. Auslesungen in den Frame-Kopien: der Oktant
Auslesung in Kopie $F$ = Eigenzustand von $F$ (r16.7). Die drei Auslesungen bilden den Oktanten: Überlappung ½, $K=2/3$, Phase $\pi/4=0{,}785398$.
Das ist ein Spin-½-Dreieck auf $\chi$, nicht das Spin-1-Dreieck von r25 (0,679042), weil die Kopien jetzt Frames tragen statt Generationen.

## 3. Ein reiner Betrachter kann die Phase nicht biegen (Satz, nachgerechnet)
- Generationssymmetrisch heißt: Der Betrachter sitzt auf der Zyklusachse. Seine Bilder unter $R$, $T$, $J_B$ bilden mit ihm ein reguläres Tetraeder
  (Überlappungen 1/3, Phase $\pi/2$).
- Jede zyklussymmetrische reine Dreiergruppe auf $\chi$ liegt auf einem Kegel um die Zyklusachse; Überlappung ½ legt den Kegel fest und damit die
  Phase $\pi/4$. Kein reiner Filter des Betrachters (beliebige Stärke geprüft) ändert das. Es ist dieselbe Starrheit wie in H109 (L1).

## 4. Ein verschränkter Betrachter biegt die Phase, und $K$ bleibt 2/3
Ist der Betrachter mit den Frame-Kopien verschränkt, sind die Auslesungen nach dem Ausspuren des Betrachters gemischt:
$\rho_k=\tfrac12(1+\lambda\,e_k\cdot\sigma)$ mit Sichtbarkeit $\lambda$. Auf dem Oktanten gilt exakt (die drei Bloch-Vektoren sind orthogonal):

$$\operatorname{Tr}\rho_i\rho_j=\tfrac12\ \text{für jedes }\lambda,\qquad \arg\operatorname{Tr}(\rho_0\rho_1\rho_2)=\arctan\lambda^3 .$$

Die Phase läuft stetig von $\pi/4$ ($\lambda=1$) nach 0, die Überlappung ½ bleibt. Für 0,666665 braucht es $\lambda^3=\tan 0{,}666665=0{,}786840$,
also **$\lambda=0{,}923199$**. Erstmals trennt ein Mechanismus Phase und Überlappung; genau das hatte H109 als nötig gefolgert.

Zwei Setzungen sind offen:
- **$\lambda$ ist nicht festgelegt.** Der Bestand sagt nicht, wie stark der Betrachter mit den Frame-Kopien verschränkt ist.
- **Lesart von $K$:** Mit $\operatorname{Tr}\rho_i\rho_j$ bleibt $K=2/3$. Normiert man auf die Reinheit $\operatorname{Tr}\rho_i^2=(1+\lambda^2)/2$, ändert sich $K$.

## 5. Die Aufteilung 7+6+6 des Autors in dieser Lesart
Die Hälften von HS(8) nach einem Bit sind die Nebenklassen einer Untergruppe der Ordnung 2: Eine HS(7)-Hälfte ist $\{1,F\}$, also Betrachter plus
eine Frame-Kopie, die andere Hälfte zerfällt in die beiden übrigen Frame-Kopien (je ein HS(6)). Das ist die Aufteilung 7+6+6 (dieselbe Grammatik
wie H107, aber mit Frames statt Generationen). Folgen:
- Die HS(7)-Hälfte ist genau der Ort, an dem Betrachter und eine Frame-Kopie einen Zwei-Kopien-Zustand bilden, also verschränkt sein können. Sie
  ist ein natürlicher Kandidat für die Herkunft von $\lambda$.
- Sie bricht die Gleichheit der drei Frames: Nur $F$ sitzt beim Betrachter. Es gibt drei solche Aufteilungen (eine je Untergruppe, also je
  Bitreihenfolge). Generationsgleich wird es erst, wenn alle drei gleichberechtigt eingehen (z. B. als Summe oder Mittel über die drei
  Aufteilungen), oder wenn eine Aufteilung aus dem Bestand bevorzugt ist (Kandidat: $R$, weil $M$ und $T$ nach r16.6 eine Bahn sind).

## Folgerung
Kein H110 bisher: Der Mechanismus (§ 4) ist da, aber $\lambda$ ist ein freier Parameter. Ein Test entsteht erst, wenn eine Konstruktion $\lambda$
festlegt, zum Beispiel ein aus dem Bestand hergeleiteter Zustand der HS(7)-Hälfte $\{1,F\}$ (§ 5). Weil der Zielwert $\lambda=0{,}923199$ jetzt
bekannt ist, wäre jeder solche Test nur in der Konstruktion blind, nicht im Zahlenwert; die Konstruktion muss vor dem Auswerten feststehen.
OP3 offen.

## Nachtrag (16.11.2026): K für gemischte Auslesungen, Berichtigung zu § 4
Skript `k_reading.py`, Ausgabe `run/k_reading_stdout.txt`. § 4 hat $K$ über $\operatorname{Tr}\rho_i\rho_j$ allein gelesen und so behauptet, $K$ bleibe
bei jedem $\lambda$ gleich 2/3. Die natürliche Fortsetzung der Gram-Lesart nimmt aber den Frame-Operator $S=\sum_k\rho_k$, also auch die Reinheiten
auf der Diagonale: $K=\operatorname{Tr}S^2/(\operatorname{Tr}S)^2=(9+|R|^2)/18$ mit $R=\sum_k r_k$ (Summe der Bloch-Vektoren). Für reine Zustände ist
das dasselbe wie $\operatorname{Tr}G^2/(\operatorname{Tr}G)^2$.
- **Berichtigung:** Gleichmäßig geschrumpfte Auslesungen geben $K=(3+\lambda^2)/6$, also $K=2/3$ nur bei $\lambda=1$. Mit $\lambda=0{,}9232$ wäre
  $K\approx0{,}642$. Der Mechanismus aus § 4 hält $K$ in dieser Lesart **nicht**.
- **Was $K$ hält:** eine Dephasierung in der Basis des Betrachters auf der Zyklusachse $n$. Sie lässt den Längsanteil $r_k\cdot n=1/\sqrt3$ fest und
  multipliziert den Queranteil mit einem Kohärenzfaktor $\kappa$. Dann bleibt $R$ und damit $K=2/3$ exakt, und die Phase ist
  $\arctan\bigl(\kappa^2/(2-\kappa^2)\bigr)$. Für 0,666665 braucht es **$\kappa=0{,}938459$**.
- Physikalisch: Der Betrachter hält in zwei Zuständen fest, ob die Auslesung entlang $+n$ oder $-n$ steht; $\kappa$ ist die Überlappung dieser
  beiden Betrachterzustände.
- **Vor der Vorab-Notiz H110 gesehen (nicht gezählt):** Nimmt man als Betrachterzustände $o$ und $Fo$ (Betrachter ohne und mit Frame-Abbildung),
  ist $\kappa=|n\cdot f|=1/\sqrt3$ und die Phase $\arctan(1/5)=0{,}197$. Weit weg.
