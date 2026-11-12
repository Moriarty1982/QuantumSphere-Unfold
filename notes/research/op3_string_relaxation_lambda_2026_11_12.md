# Expansion, Längenvorgabe und Relaxation der drei Strings

12. November 2026. Autorenidee; analytische, nicht blinde Erkundung.
Einordnung T8/T9/T13, OP3/OP5. Kein natives Companion-Gesetz, kein
Hypothesentest, kein neuer Beleg und keine Änderung offener Guards.

## Vorwissen geprüft

Gesamtbild, op3_string_length_exploration_2026_11_12.md, OP3-Torusgrenze,
op5_neuaufbau_2026_11_06.md und die zurückgestellten Ideen wurden geprüft.
Die Suche nach Kriechen, Ermüdung, Ausleiern und viskoelastischer Relaxation
in notes/research (einschließlich predictions und v4_10_0-Runden) und analysis
ergab kein entsprechendes natives Materialgesetz. Andere Relaxationsbegriffe
in OP5 begründen keines. I3 wird durch den Lambda-Bezug berührt; die alten
gescheiterten Lambda-Auslesungen werden dadurch nicht wieder bestätigt.

## Geometrische Lambda-Annahme

Dimensionsmäßig ist Lambda=C/L² möglich. Wird L zusätzlich als Umfang
eines Großkreises am Horizont einer reinen vierdimensionalen de-Sitter-
Raumzeit identifiziert, gilt L=2*pi*sqrt(3/Lambda), also C=12*pi².
Das ist eine zusätzliche Identifikation, keine Herleitung von Lambda.
Eine feste Horizontlänge ist von einer mit dem Skalenfaktor a wachsenden
materiellen Schleife zu unterscheiden. Für L proportional a hätte eine
separat erhaltene isotrope Komponente rho proportional L^-2 die
Zustandsgleichung w=-1/3, nicht die Vakuumgleichung w=-1 (c=1).

Die weiche Kopplung U=kappa*(L-sum ell_i)²/2 erzeugt dieselbe generalisierte
Kraft kappa*(L-sum ell_i) auf alle drei Längen. Unterschiedliche Reaktionen
benötigen unterschiedliche Materialdaten oder eine begründete Geometrie.
Diese Strafe erzwingt die Längengleichheit nicht exakt. Bei exakter
Nebenbedingung ist die Differenz null; die Zwangskraft ist separat zu lösen.

## Minimaler dissipativer Vergleich

Im gespannten Bereich, mit k_i>0 und eta_i>0 konstant:

    F_i = k_i (ell_i-r_i),   dot(r_i)=F_i/eta_i,
    dot(F_i) = k_i dot(ell_i)-F_i/tau_i,   tau_i=eta_i/k_i.

r_i ist eine innere unbelastete Länge. Dies ist ein Maxwell-artiger
Vergleich für Kriechen und Relaxation, kein bereits hergeleitetes Gesetz
für fundamentale Strings und kein allgemeines zyklisches Ermüdungsmodell.
Bei festgehaltener ell_i fällt F_i exponentiell. Bei weiterer Dehnung fällt
F_i genau dann, wenn k_i*dot(ell_i)<F_i/tau_i. Verschiedene tau_i erlauben
unterschiedliche Relaxation bei gleicher vorgegebener Dehnung.

Die Energiebilanz für U_i=k_i*(ell_i-r_i)²/2 lautet
dot(U_i)=F_i*dot(ell_i)-F_i²/eta_i. Die Dissipation ist nichtnegativ;
ihre Energie muss bei kosmologischer Interpretation mitgeführt werden.
Bei schlaffen Strings ist ein einseitiges Zuggesetz nötig; die obige
lineare Formel darf nicht als negative Seilzugkraft fortgesetzt werden.

Gilt sum ell_i=L konstant jederzeit, dann sum dot(ell_i)=0: alle drei
tatsächlichen Längen können nicht gleichzeitig wachsen. Ihre inneren
Ruhelängen können dennoch wachsen und Zugkräfte abfallen. Ist die Summe
nur eine Endbedingung, gilt diese Geschwindigkeitsrestriktion vorher nicht.
In einem frei umverteilbaren quasistatischen Längenmodell sind die
Gleichgewichtszugkräfte gleich; unterschiedliche Relaxation bedeutet
deshalb nicht automatisch dauerhaft unterschiedliche Gleichgewichtskräfte.

## Offene Frage am Übergang zu Version 5

Können drei gekoppelte Strings bei kosmischer Expansion unterschiedlich
relaxieren oder bleibend weicher werden, und kann eine begründete Kopplung
an eine feste äußere Längenskala eine stabile ungleiche Aufteilung wählen?

Zu bestimmen sind Netzgeometrie/Wicklungen, die Belastung durch Expansion,
Material- bzw. innere Zustandsvariablen, vollständige Energiebilanz und
ein Mechanismus, der die Relaxation begrenzt. Weder Lambda noch Koide 2/3
oder das Leptonspektrum folgen aus dem Vergleich. Die Frage bleibt offen
und soll im v5-Paket ausdrücklich als Forschungsfrage enthalten sein.

## Gelesene externe Quellen

- Guo, de-Sitter-Radius: https://arxiv.org/abs/hep-th/0607017
- Carroll, Vakuumzustandsgleichung, Abschnitt 6:
  https://www.preposterousuniverse.com/wp-content/uploads/2015/08/grtinypdf.pdf
- Penn State, Kriechen und Spannungsrelaxation:
  https://courses.ems.psu.edu/matse202/node/717
- Lin et al. (2022), endliche Belastungsraten und viskoelastische Modelle:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC9143375/

Die Materialquellen stützen die Analogie, nicht ihre kosmologische Anwendung.
