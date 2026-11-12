# OP3: Rückwärtsdiagnose aus gemessenen Leptonmassen

12. November 2026. Explizit beauftragte bekannte-Daten-Erkundung, nicht blind,
kein neuer H-Test, keine Vorhersage oder native Operatorrekonstruktion.
Einordnung Gesamtbild T8/T13. Ausgangsrevision 8da1e87.

## Eingaben und Vorwissen

Positive Ruhe-Massenenergien, c=1, in MeV:

| Teilchen | Zentralwert | Zitierte Unsicherheit |
|---|---:|---:|
| Elektron | 0.51099895069 | 0.00000000016 |
| Myon | 105.6583755 | 0.0000023 |
| Tau | 1776.93 | 0.09 |

Elektron/Myon: [CODATA 2022, NIST-Gesamtliste](https://physics.nist.gov/cuu/pdf/all.pdf),
Seiten 2/3. Tau: [PDG 2025 update, Tau-Liste](https://pdg.lbl.gov/2025/listings/rpp2025-list-tau.pdf),
Seite 1. Am 12.11.2026 abgerufen. Der ältere Tau-Wert in der NIST-Liste
wird ausdrücklich nicht verwendet. Dies sind keine laufenden Yukawa-
Parameter an einer gewählten Renormierungsskala; deren Matching fehlt.

Vorwissen: bisherige OP3-Gram-/Frame-Notizen, r33/H18 und r53/H37,
`analysis/Coupling_Scale_Determination.md` und
`notes/research/koide_original_op3_cycle_phase.md`. Die zuletzt genannte
Notiz enthält bereits Rückrechnungen aus PDG-Massen in Wurzelphasen.
Hier wird keine solche Anpassung als neuer Mechanismus ausgegeben:
Gegenstand sind notwendige Schranken der im Chat untersuchten Routen.

## Wo die Rückrechnung scheitert

1. **H18 auf farbfestem r15-Torus.** Dort sind Massen proportional zu
   Sehnenlängen. Die notwendige Bedingung m_tau≤m_mu+m_e scheitert an
   1776.93 gegenüber 106.16937445069 MeV. Der Fehlbetrag ist
   1670.76062554931 MeV, also 94.0251 Prozent von m_tau. Der bereits
   analytisch bewiesene Ausschluss ist damit an den Messdaten lokalisiert;
   keine neue Entdeckung gegenüber der historischen Hierarchieproblematik.
2. **Koide als nachgeschaltete Diagnose.** Aus den Eingaben folgt
   K=0.6666644634. Die Nähe zu 2/3 ist empirisch, nicht exakt gesetzt.
   Die Torusroute verlangt K≤1/2. Sie scheitert schon an der deutlich
   stärkeren Massendreiecksprüfung oben, nicht erst an einer kleinen
   Koide-Abweichung.
3. **Eigenmassen der vollen H-Matrix.** H hat auf diesem Torus Rang≤1;
   ein Ziel mit drei positiven Massen benötigt Rang drei. Ein gemeinsamer
   invertierbarer Frame-/Basiswechsel erzeugt keinen zusätzlichen Rang.
   Für einen direkten Massenoperator mit Singulärwerten (m_e,m_mu,m_tau)
   ist der kleinste relative Frobeniusfehler einer Rang-eins-Näherung
   sqrt((m_e²+m_mu²)/sum m_i²)=0.0593570. Das dominante Tau kann daher
   einen optisch kleinen Gesamtfehler vortäuschen, obwohl zwei Massen fehlen.
4. **H82-Frame-Normierung.** Alle Massen skalieren mit p/k gemeinsam.
   Die Quotienten tau/e=3477.3653 und tau/mu=16.81769 bleiben bestehen.
   Das gilt auch für die positiven Singulärwerte einer global imaginär
   gedrehten Dirac-Matrix. Eine gemeinsame Phase repariert keine dieser
   notwendigen Bedingungen.

Die r53-Spurlosroute fordert ebenfalls m_max=sum der beiden anderen
positiven Eigenwertbeträge in ihrer reell-hermiteschen Lesart. Ihr
historischer geladener-Lepton-Ausschluss wird durch denselben Fehlbetrag
illustriert, nicht durch diese Rechnung auf allgemeine komplexe Kopplungen erweitert.

## Was eine zusätzliche generationsabhängige Wirkung mindestens leisten müsste

Angenommen, l_i sind zulässige H18-Dreiecks-Massen und die physikalischen
Massen wären m_i=f_i l_i mit f_i>0. Dann folgt notwendig

$$\frac{m_\tau}{f_\tau}\leq\frac{m_e}{f_e}+\frac{m_\mu}{f_\mu}
\quad\Longrightarrow\quad
\frac{f_{\max}}{f_{\min}}\geq\frac{m_\tau}{m_e+m_\mu}=16.73674738.$$

Dies ist nur eine notwendige Schranke, kein ausreichender Fit oder neues
Naturgesetz. Sie betrifft positive skalare Faktoren in derselben Zuordnung,
keine beliebigen nichtkommutierenden Matrixkorrekturen. Eine gemeinsame
Skala hat Verhältnis eins und kann diese Schranke nicht erfüllen.

Anderer, ausdrücklich hypothetischer Rückwärtsansatz: D=d I und identische
diagonale Z_L=Z_R=diag(z_i). Dann D_c=diag(d/z_i). Die Daten erzwingen

$$z_e:z_\mu:z_\tau=3477.3653:16.81769:1.$$

Würde nur eine Chiralität kinetisch gewichtet, wären die nötigen Verhältnisse
die Quadrate, etwa 12.092 Millionen:282.835:1. Diese Zahlen sind rückwärts
eingesetzte Anforderungen, keine Herleitung kinetischer Gewichte. Sie
zeigen, wo eine Hierarchie versteckt würde, wenn der Ausgangsoperator
selbst noch keine enthält. Bei einem bereits hierarchischen D gilt diese
spezielle Z-Forderung nicht.

## Grenze der inversen Information

Die drei gemessenen Massen bestimmen drei Singulärwerte, nicht den nativen
Operator, seine Basis oder seinen kinetischen Ursprung. Matrizen
U diag(m_i) V* für beliebige unitäre U,V reproduzieren dieselben Massen.
Kinetische Gewichte und Kopplung können die Hierarchie ebenfalls zwischen
sich umverteilen. Ohne weitere native Daten ist die Umkehrung deshalb
nicht eindeutig. Die Rückrechnung lokalisiert Unverträglichkeiten, sie
rekonstruiert keine eindeutige Theorie.

## Ausführung und Kontrolle

`backsolve.py` liest `inputs.json`; 50-stellige Decimal-Rechnung, ein
Zentralwerttripel und acht Ecken der individuellen Unsicherheitsbox.
Keine Zufallszahlen, Optimierung oder großen Rechnungen; deshalb lokal
ohne parallele Agenten ausgeführt. Der massenlineare Fehlbetrag ist
zusätzlich als exakter Decimal-Wert geprüft; Gleichmassen und das
entartete Dreieck dienen als handrechenbare Koide-Kontrollen.

`run02/manifest.json`: Status completed, Eingabehashes und Befehl erfasst;
Manifestprüfung mit --root erfolgreich. `run02/results.json` enthält die
Zahlen. Erster Lauf `run/`: durch einen Nullmassen-Kontrollfall in einer
Diagnosefunktion mit Division durch tau gescheitert. Kontrollfall danach
direkt ohne Quotientendiagnostik geprüft; Fehlprotokoll bleibt erhalten.
Das alte Fehlmanifest bezieht sich auf den damaligen Skripthash.

An den acht Unsicherheitsecken bleibt der Fehlbetrag zwischen
1670.670623 und 1670.850628 MeV und die nötige Faktorstreuung zwischen
16.735899 und 16.737595. Das ist keine gemeinsame statistische
Konfidenzregion; Korrelationen wurden nicht modelliert. Die Größenordnung
des Ausschlusses hängt erkennbar nicht von der Messunsicherheit ab.
Die universellen Strukturfolgen stammen aus den vorhandenen analytischen
Beweisen; dieser Lauf prüft ihre Anwendung auf die angegebenen Eingaben.

Nächste Pflicht: Eine native Kopplung muss entweder schon vor der
Frame-Normierung eine Hierarchie tragen oder eine unabhängig definierte
relative Wirkung liefern. Ein kleiner gemeinsamer Phasenschritt oder
Skalenfaktor reicht für die geprüften Routen nicht.
Keine neuen MMA-Belege, kein unabhängiges Audit, keine OP-/Guard-Änderung.
Die zurückgestellten Ideen ergeben hier keinen neuen einschlägigen Auslöser.
