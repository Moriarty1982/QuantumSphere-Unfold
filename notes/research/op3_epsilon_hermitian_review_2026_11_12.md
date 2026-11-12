# OP3: Komplexes Kreuzprodukt und volle Gram-Auslesung

12. November 2026. Autorenauftrag: eigene Levi-Civita-Variante bzw.
phasenempfindliche Kopplung untersuchen, mit Netzquellen. Analytische
Erkundung und Selbstprüfung, nicht blind; keine Simulation, H-/k-Nummer,
Manuskriptänderung oder OP-Schließung. Lokale Ausgangsrevision f4daadb.
Einordnung Gesamtbild T7/T8/T13: Farbe, Generationen und Operatorbindung.

## Vorwissen und Quellenabgleich

Geprüft: die vier OP3-Träger-/Gram-/Torusnotizen vom 12.11.; r33.2,
`formal/QSFormal/Lesarten.lean` (`gram_pure`, `gram_right`), sowie r53
(`notes/research/v4_10_0_r48_r55/rounds/v490_r53_round.tex`). Suchen in
predictions/, v4_10_0_*-Notizen und analysis/ nach Levi-Civita, epsilon,
Kofaktoren und Kreuz-/Gram-Auslesungen. Die r53-Kopplung ist eine eigene
reelle symmetrische, spurlose Slotmatrix, kein Nachweis der hier
vorgeschlagenen hermiteschen Auslesung. Historische numerische H37-Befunde
werden nicht neu geprüft oder auf komplexe Erweiterungen übertragen.

Webrecherche am 12.11.2026, englische Suchbegriffe: Baez octonions G2
cross product invariant 3 form complex cross product SU(3). Primärtexte:

1. John C. Baez, *The Octonions*, Autoren-HTML, Abschnitt 2.1:
   https://math.ucr.edu/home/baez/octonions/node4.html
   Gelesen: zyklische Quaternion-/Fano-Multiplikation und Vorzeichenwechsel.
2. Dasselbe Werk, Abschnitt 4.1:
   https://math.ucr.edu/home/baez/octonions/node14.html
   Gelesen: x×y=[x,y]/2 auf Im O, Normidentität, G2-Erhaltung und
   alternierende Dreiform phi(x,y,z)=<x,yz> für imaginäre Argumente.
3. John C. Baez, *Diary — July 2020*, Einträge 20./26. Juli:
   https://math.ucr.edu/home/baez/diary/july_2020.html
   Gelesen: komplexe Konjugation in der SU(3)-angepassten
   Oktonionenmultiplikation und Zerlegung O=C⊕C³ nach Wahl einer Einheit.

Autoren-HTML ist hier die geprüfte Fassung; kein PDF-/arXiv-Versionsabgleich,
keine globale Neuheitsprüfung und kein gespeicherter Quellenhash.
Die ausführlichen verlinkten Blogseiten waren per Firecrawl/Browser
nicht abrufbar (Proxy-/403-/Timeoutfehler). Ihre Suchauszüge dienen nur
der Entdeckung. Die genaue komplexe Formel unten wird deshalb zusätzlich
direkt hergeleitet. Quellen stützen Algebra, keine physikalische Massenbrücke.

## 1. Eine geeignete komplexe Version existiert bereits

Für V=C³ mit standardmäßigem hermiteschem Skalarprodukt und gewählter
komplexer Volumenform definiere

$$C(u,v)_a=\sum_{b,c}\varepsilon_{abc}\bar u_b\bar v_c
=\overline{(u\times v)_a}.$$

Dies ist antilinear in beiden Argumenten, nicht komplex-bilinear.
Das gewöhnliche bilineare Produkt erfüllt für U∈SU(3)
(Uu)×(Uv)=U^{-T}(u×v)=bar(U)(u×v). Konjugieren ergibt
C(Uu,Uv)=U C(u,v). Die Determinantenidentität liefert den ersten Schritt,
Unitarität den zweiten. So bleibt epsilon unverändert; ergänzt werden
die passende Konjugation und die korrekte Darstellung des Zielraums.

Verdikt: bekannte SU(3)-angepasste Operation, durch direkte Rechnung
verifiziert; ihre Identifikation als Generationenkopplung ist offen.
Die C³-Komponenten hier sind die Farbkomponenten von O=C⊕C³. Sie sind
nicht automatisch die drei Slot-/Generationenindizes unserer A_i.
Farbfeste Konfigurationen haben in dieser Zerlegung z=0; diese
Farb-Kreuzoperation liefert dort folglich null.

## 2. Das siebendimensionale Gegenstück

Auf Im O ist x×y=(xy−yx)/2 eine bereits vorhandene antisymmetrische
Operation. Ihre Strukturkonstanten f_abc werden durch die gewählte
Oktonionenmultiplikation festgelegt. Die zugehörige alternierende
Dreiform wird von G2 erhalten (Baez, Abschnitt 4.1). Das ist keine
beliebige siebendimensionale Levi-Civita-Volumenform: Diese hätte sieben
Indizes; f hat drei und kodiert zusätzliche algebraische Struktur.

Die gesamten Torus-Slots liegen in span_R(1,e7); ihre imaginären Teile
sind alle Vielfache von e7. Daher verschwindet ihr Im-O-Kreuzprodukt.
Das ist eine andere Operation als der äußere Flächentensor x_j∧x_k
im reellen achtdimensionalen Slotraum, der durchaus ungleich null ist.
Beide Konstruktionen dürfen nicht ausgetauscht werden.

## 3. Selbstprüfung des im Chat vorgeschlagenen H

Vorgeschlagen war für die Komponenten A_i des quaternionischen Gram-Tensors

$$H_{ij}=\sum_{c,d}(A_i)_{cd}\overline{(A_j)_{cd}}.$$

H ist hermitesch positiv semidefinit, da H=BB* für die Matrix B der
abgeflachten A_i-Zeilen. Seine Diagonale enthält die Betragsquadratsummen;
die Nebendiagonale zusätzlich relative Korrelationen. Eine gemeinsame
Phase oder das gemeinsame Vorzeichen aller A_i bleibt unsichtbar.
Es ist daher keine vollständige Wiederherstellung aller Orientierungsdaten.

**Entscheidende Rangprüfung auf dem bisherigen Torus:** Setze
u=1, v=e7 und W_cd=u_c v_d−v_c u_d. Dann ist ||W||_F²=2 und

$$A_i=-\sin(\alpha_k-\alpha_j)W=s_i W,\qquad
H=2ss^{\mathsf T}.$$

Damit hat H für s≠0 exakt ein positives Eigenmaß 2||s||² und zweimal
null; für s=0 verschwindet H. Unter einer zusätzlich postulierten
Masseninterpretation seiner Eigenwerte oder ihrer positiven Wurzeln
entstünde somit nur eine nichtnullartige Masse (K=1), nicht die
H18-Dreifachauslesung der Diagonale und nicht drei positive Leptonmassen.
Die Formel gilt für jede Torusphase; ein Phasenscan ist überflüssig.
Auch eine gemeinsame zusätzliche komplexe Phase ändert den Rang nicht.

Abhängigkeiten: zweidimensionaler gemeinsamer Slotraum → eindimensionaler
Raum seiner äußeren Zweiformen → proportionale A_i → H mit Rang≤1.
Positivität, Nullfall, Indexreihenfolge und Faktor zwei sind direkt geprüft.
Dies ist ein analytischer Beweis; kein numerisches Programm oder externer
Satz trägt die Rangfolgerung. Der Chatvorschlag wird damit eingeschränkt,
nicht als neu hergeleitetes natives Massengesetz übernommen.

## Urteil und nächste Pflicht

| Vorschlag | Ergebnis |
|---|---|
| Komplexes epsilon-Kreuzprodukt | Existiert mit Konjugation und SU(3)-Äquivarianz; Farb-/Slotbindung offen |
| Oktonionisches f_abc | Bereits nativ algebraisch vorhanden; auf den imaginären Torusanteilen null |
| Volle hermitesche Gram-Matrix H | Behält mehr Korrelationen, bleibt auf diesem Torus aber Rang≤1 |
| Neue positive Massenspektren | Durch keine dieser Beobachtungen physikalisch hergeleitet |

Kein freies neues epsilon oder Gewicht wird eingeführt. Nächster sinnvoller
Quellenauftrag: prüfen, ob eine bereits definierte Kopplung auf dem
dreifachen farbneutralen linearen Umgebungsraum L³ statt auf dieser
Torus-Konfigurationsauslesung wirkt. Dafür müssen physikalische Darstellung,
Closure/HC und Operatorbindung angegeben sein. Ohne solche native Daten
würde eine allgemeine 3×3-Matrix lediglich zusätzliche Freiheit einsetzen.

QAM-Lese-MCP nicht verfügbar; lokale read-only Suche epsilon ohne Ausgabe.
Keine gespeicherten MMA-Belege oder Hashprüfungen behauptet. Keine neuen
Auslöser der zurückgestellten Ideen; OP1–OP5/C5/C6/T2 und Guards unverändert.
