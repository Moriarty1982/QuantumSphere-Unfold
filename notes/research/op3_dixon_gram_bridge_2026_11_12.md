# OP3: Rechte Gram-Labels sind eine konkrete Auslesung, keine linearen Generationenzustände

12. November 2026. Quellenprüfung und analytische Selbstprüfung, nicht blind.
Geprüfte Revision: 8e168b0. Keine neue Simulation oder H-/k-Nummer.
Einordnung im Gesamtbild: T5/T7 Träger und Darstellung, T8 Massen, T13 Operator.

## Prüfbehauptung und Urteil

Prüffrage: Liefert r33 eine konkrete Brücke vom Trialitätstripel zu drei
Auslesungen oder bereits zu drei physikalischen linearen Zuständen?

**Urteil: konkrete nichtlineare Auslesung vorhanden; physikalische
Massenzuordnung und lineare Generationeneinbettung nicht etabliert.**
Die vorherige Schnittstellenprüfung ist entsprechend zu präzisieren:
R_m selbst liefert keine Regel, aber r33 liefert separat Gram-Funktionen
auf dem linearen Slotraum, die auch an r15-Konfigurationen auswertbar sind.
Ihre Definition darf nicht mit einem erfolgreichen Massengesetz gleichgesetzt werden.

## Vorwissen geprüft und Quellen

- `v4_10_0_r32_r33/rounds/v490_r33_round.tex`, r33.1, r33.2 und H18.
- Dort `llm/Pruefung_Dixon_Ablage.md`, Abschnitte 3, 9, 10;
  `Ergebnis_H18_Links_invariante_Massen.md` und Quelltext
  `k72_links_invariant.py`. Numerische Programme hier nicht neu ausgeführt.
- `formal/QSFormal/Lesarten.lean`: `left_leaves_im`, `gram_left`,
  `gram_right`, `right_cyc`, `gram_pure`, `lagrange8`.
  Quelltext geprüft; kein neuer Lean-Build behauptet.
- Vorangehende OP3-Trialitäts-/Massenbrückennotizen;
  Suchen in predictions/, v4_10_0_*-Notizen und analysis/.
  H18 ist der einschlägige bereits beantwortete Massentest.

## Die tatsächlich vorhandene Abbildungskette

Für reelle Oktonionenslots x_1,x_2,x_3 schreibt r33

$$E(x)=i\otimes x_1+j\otimes x_2+k\otimes x_3\in\mathbb H\otimes\mathbb O.$$

Dies kodiert O³ linear und injektiv in den rein imaginären Quaternionanteil.
Mit den acht Quaternionenspalten h_c des kodierten Elements definiert die
Quelle G_cd=conj(h_c)h_d. Dessen drei imaginäre Komponenten A_i liefern

$$\mu_i=\sum_{c,d}(A_i)_{cd}^2
 =2\bigl(\|x_j\|^2\|x_k\|^2-\langle x_j,x_k\rangle^2\bigr),$$

wobei (i,j,k) zyklisch ist. Gemeint ist zweimal das **Quadrat** der
aufgespannten Parallelogrammfläche, nicht zweimal deren Fläche.
G ist quadratisch, mu quartisch in den reellen Slotkoordinaten. Daher
ist x↦(mu_1,mu_2,mu_3) keine lineare Seed-Isometrie.

Die Restriktion auf den r15-Träger ist mathematisch definiert: Dessen
Einheitsoktonionentripel sind Elemente von O³. Die Auslesung benötigt die
Produktbedingung (ab)c=1 nicht für ihre Definition. Diese Einschränkung
macht die Auslesung aber noch nicht zu einer physikalischen Massenmessung.

## Abhängigkeiten und Pflichten

Die Kette ist: Slotkodierung E → Quaternionprodukt G → Komponenten A_i
→ reelle Quadratsummen mu_i → zusätzlich postuliertes Massengesetz.
Die ersten Pfeile sind explizite algebraische Definitionen; der letzte ist
eine physikalische Identifikationsannahme. Folgende Grenzen sind wesentlich:

| Pflicht | Befund der Selbstprüfung |
|---|---|
| Reelle positive Auslesung | Erfüllt für reelle Slots: Quadratsummen; parallele Slots können null liefern |
| Erhaltung des reinen Slotraums unter linker Spinorwirkung | Nicht erfüllt: schon i·i=−1 verlässt Im H (`left_leaves_im`) |
| Gram-Invarianz unter Einheitsquaternionen links | Erfüllt durch conj(qh_c)(qh_d)=G_cd; allgemein reell skaliert G mit \|q\|² und mu mit \|q\|⁴ |
| Lorentz-Boost-Fassung | Nur mit der ausdrücklich komplex-bilinearen Fortsetzung; keine Identifikation mit einer positiven hermiteschen Norm |
| Drei lineare Zustände desselben physikalischen Typs | Durch drei skalare Gram-Labels nicht konstruiert |
| Native Massenskala, Closure, HC-Gradierung und Operatorbindung | Durch diese Auslesefunktionen nicht bestimmt |
| Auswahl einer Massenhierarchie | H18 für die geprüften Potentialfamilien als widerlegt dokumentiert; kein allgemeiner Ausschluss anderer Mechanismen |

Entscheidendes kleines Beispiel für die Trägerpflicht ist das bereits
formalisierte i·i=−1. Es widerlegt die Interpretation von Im H⊗O als
unter der angegebenen Linkswirkung abgeschlossener Spinorraum. Es widerlegt
nicht die Gram-Auslesung auf dem größeren Träger H⊗O: Dort darf ein Bild
eine skalare Quaternionenkomponente besitzen. Die Quelle löst den Konflikt
auf Ebene der Labels, nicht durch Erhaltung der ursprünglichen drei Slots.

Die komplex-bilinearen Identitäten und positive reelle Quadratsummen haben
verschiedene Definitionsbereiche. Aus einer bilinearen Boost-Invarianz
allein folgt kein positiver Hilbertraum von drei Masseneigenzuständen.
Die Lean-Quelldatei formalisiert die genannten Polynomkerne über Int;
sie ist hier kein neu geprüftes Zertifikat der gesamten physikalischen Route.

## Massentest und verbleibende Aufgabe

H18 setzt m_k proportional sqrt(mu_k) an Minima zweier Potentialfamilien.
Die Ergebnisnotiz dokumentiert keine bestimmten drei verschiedenen
nichtnullartigen Werte; H18a/H18b sind dort widerlegt. Das ist ein Bericht
des historischen Tests, kein neuer Replay oder Ausschluss jedes Potentials.
Die Auswahl der Winkel und die Massenzuordnung bleiben zusätzliche Pflichten.

Stärkste sichere Aussage: Es existiert eine konkrete algebraische
Dreifachauslesung von Trialitätstripeln in der Dixon-Ablage. Ihr Bild besteht
aus skalaren Labels und ersetzt keine lineare Generationeneinbettung.
Nächster enger Schritt: diese bereits definierte Auslesung auf den
farbfesten r15-Torus einschränken und ihre Abhängigkeiten analytisch prüfen,
bevor neue Auswahlpotentiale oder Simulationen erwogen werden.

QAM-Leseserver weiterhin nicht verfügbar; lokale read-only Suche `r33`
ohne Ausgabe. Keine MMA-Belege oder Hashverifikation behauptet.
GitHub-Abgleich erneut durch Verbindungsfehler verhindert.
Keine neuen Auslöser zurückgestellter Ideen. OP1–OP5/C5/C6/T2 und Guards
unverändert. Prüfung durch denselben Assistenten, kein unabhängiges Audit.
