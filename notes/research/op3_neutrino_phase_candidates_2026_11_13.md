# Erkundung: Varianten zu H99 nach den Ideen 1–3 (Verschiebung, Auslesung, Skala)

13. November 2026, abends. Autorenauftrag: „behalte Idee 3 im Kopf, mach mit
Idee 1 und 2 weiter“. Erkundung, **nicht blind**: Der Zielwert war vorher
bekannt (NuFIT 6.1, H99b). Kein Test, keine H-Nummer, kein MMA-Beleg, keine
Änderung offener Guards. Einordnung T8 (Massen), OP3/OP4.
Skript `op3_neutrino_phase_candidates_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft

- H99 (Vorab 5b23c5a, k221) mit H99b (+1,80σ gegen NuFIT 6.1); H2 (v4.8.0-r12).
- v4.8.0-r11 (H1, `k14_test_h1.py`): laufende MS-bar-Yukawas bei M_Z (Antusch, Hinze,
  Saad, arXiv:2510.01312), dort K = 0,6678 und Phase 0,2211; δ ≈ 2/9 gilt nur bei Polmassen.
- `op3_gram_eigen_readout_2026_11_13.md`: s_k = 1 + 2ρ cos(θ + 2πk/3),
  K = (1 + 2ρ²)/3, det S = 1 − 3ρ² + 2ρ³ cos 3θ; Bogen |θ| ≤ π/12 bei ρ² = 1/2.
- `op3_indefinite_form_2026_11_13.md`: bilineare Form im neutralen Sektor,
  Signatur (2,1) außerhalb des Bogens.
- r44.1(d): einziger eichinvarianter Verbinder ohne Higgs wirkt auf ν^c
  (Grund, eine Seesaw-Auslesung mitzuprüfen).
- Zurückgestellte Ideen I1–I5: kein Auslöser getroffen.

## Ziel und notwendige Bedingung (Rückwärtssuche)

Mit ρ² = 1/2 und der Lesart √m ∝ s verlangt NuFIT 6.1
θ_ν = 0,48024 ± 0,00213. Bei Polmassen ist θ_e = 0,22222; die nötige
Verschiebung ist also 0,2580 statt π/12 = 0,2618 (1,4 % kleiner). Ein
gleichverteiltes θ_ν in [π/12, π/3] trifft das 2σ-Fenster mit 1,1 %.

## Raster (24 Versuche, alle ausgegeben)

Vier Beziehungen × drei Auslesungen × zwei Skalen, jeweils ρ² = 1/2:

- Beziehungen: (a) θ_e + π/12 (H99); (b) π/6 − θ_e, Spiegelung am Rand;
  (c) π/3 − θ_e, Vorzeichenwechsel aller Überlappungen wie unter z ↦ iz;
  (d) det S_ν = −det S_e.
- Auslesungen: √m ∝ s (H99); m ∝ |s|; Seesaw m ∝ s⁴.
- Skalen für θ_e: Polmassen, M_Z.

Ergebnis: Nur (a) mit √m ∝ s liegt innerhalb 2σ (Pol +1,80σ, M_Z +1,27σ).
Alle anderen 22 Kombinationen liegen 49σ bis über 1000σ daneben. Bei 24
Versuchen hätte mindestens ein zufälliger Treffer eine Wahrscheinlichkeit
von etwa 23 %; die Versuche sind aber nicht unabhängig (Pol und M_Z liegen
dicht beieinander).

- **Idee 1** (andere Beziehung): Die naheliegenden Alternativen scheiden
  deutlich aus. Die Verschiebung um den Rand des Bogens ist unter ihnen
  die einzige, die passt.
- **Idee 2** (andere Auslesung): Masse statt Massenwurzel und die einfache
  Seesaw-Auslesung scheiden deutlich aus. Lässt man K_ν frei, passt
  K_ν = 0,6739 (Pol) bzw. 0,6718 (M_Z); das ist ein Fit ohne Vorhersage.

## Verbindung von Idee 1 und 2: Verschiebung = Rand des eigenen Bogens

H99 benutzt π/12, weil das der Rand des Bogens bei ρ² = 1/2 ist. Bei
allgemeiner Überlappung liegt der Rand bei cos 3θ_b = (3ρ² − 1)/(2ρ³).
Setzt man θ_ν = θ_e + θ_b(ρ_ν²) und lässt ρ_ν² frei, passt
K_ν = 0,66854 (Pol) bzw. 0,66799 (M_Z), also nur knapp über 2/3.

**Nachträglich, aus diesem Fit gefunden:** 0,66799 liegt sehr nahe am
Koide-Wert der geladenen Leptonen bei M_Z (0,66783). Das legt eine
Fassung von H99 ohne freie Zahl nahe, die alle Größen bei derselben Skala
nimmt:

    ρ_ν² = ρ_e²(μ),   θ_ν = θ_e(μ) + θ_b(ρ_e²(μ)).

Bei μ = Polmassen ist das H99 (ρ_e² = 0,499997). Bei μ = M_Z:

| Größe | H99 (Pol) | eine Skala, M_Z |
|---|---|---|
| ρ_e², K | 0,499997; 0,666664 | 0,501743; 0,667829 |
| Rand θ_b | 0,26180 | 0,26006 |
| θ_ν | 0,48403 | 0,48119 |
| R = Δm²₂₁/Δm²₃₁ | 0,030840 | 0,030087 |
| gegen NuFIT 6.1 | +1,80σ | **+0,16σ** |
| gegen NuFIT 6.0 | +1,31σ | +0,36σ |
| Δm²₂₁ mit Δm²₃₁ = 2,511 | 7,744·10⁻⁵ eV² | 7,555·10⁻⁵ eV² |
| gegen JUNO allein (7,50 ± 0,12) | +2,03σ | +0,46σ |
| Massen | 0,38; 8,81; 50,11 meV | 0,38; 8,70; 50,11 meV |

Die Skala löst also zusammen mit dem eigenen Bogenrand die ganze
Abweichung; die Skala allein (Idee 3) löst 29 %.

**Die drei Ideen in Kombination** (Autor: „der Mechanismus könnte an der
Stelle komplizierter sein“). Der Kandidat ist genau die Kombination:

| Idee | Rolle im Kandidaten | allein |
|---|---|---|
| 3 Skala | θ_e und ρ_e² werden bei M_Z genommen | 29 % der Lücke, +1,27σ |
| 2 Annahme K_ν = 2/3 | ersetzt durch K_ν = K_e(μ) = 0,6678 | nur als freier Fit |
| 1 Verschiebung π/12 | ersetzt durch den Rand des eigenen Bogens, θ_b(ρ²) = 0,26006 | Alternativen (b)–(d) scheiden aus |

Keine Idee allein reicht. Zusammen ändern sie nichts an der Struktur von
H99, sondern nehmen deren drei Bestandteile (Überlappung, Rand, Phase)
konsequent bei einer Skala. Dadurch kommt keine freie Zahl hinzu; das
Problem verschiebt sich auf die Frage, welche Skala die richtige ist.

## Bewertung

- Das ist **kein Befund**, sondern ein Kandidat. Er wurde nach Kenntnis der
  Daten aus einem Fit abgelesen; Skala und Formulierung sind nachträglich
  gewählt. Bei rund 26 betrachteten Varianten ist ein Treffer innerhalb
  0,2σ nicht beweiskräftig.
- Für den Kandidaten spricht: Er hat keine freie Zahl, er ist die
  wörtliche Lesart von H99 („gleiche Überlappung, Verschiebung um den
  Rand“) bei einer einzigen Skala, und M_Z ist keine für diesen Zweck
  gesuchte Skala, sondern die Skala aus H1.
- Dagegen spricht: Warum M_Z und nicht eine andere Skala, ist nicht
  begründet; zwischen Pol und M_Z wandert R stetig, und jede Skala
  dazwischen wäre ebenfalls verträglich. Die Annahmen „Massenwurzel =
  Eigenwert“, negative Wurzel und gleiche Überlappung bleiben ungezeigt.
- Prüfbar wird der Kandidat durch künftige JUNO-Werte: H99 verlangt
  R = 0,030840, die Fassung bei M_Z 0,030087. Der Abstand von 0,00075 ist
  etwa dreimal der Fehler, den R nach JUNO haben wird (dann begrenzt durch
  Δm²₃₁, rund 0,9 %). Eine blinde Prüfung braucht eine Vorab-Notiz, bevor
  neue Werte bekannt sind.
- OP3/OP4 bleiben offen; OP1–OP5, C5, C6/T2 unverändert.

## Nachtrag: Grund für die Skala M_Z (13.11., Autor: „Grund für M_Z suchen“)

Rückwärtssuche: Welche Eigenschaft muss die Skala haben, und gibt der
Companion sie her? Rechnung im selben Skript (Abschnitt „Nachtrag“).

**1. M_Z ist nicht ausgezeichnet.** Die Fassung „eine Skala“ hängt kaum von
der Skala ab, solange sie über den Leptonmassen liegt:

| Skala der laufenden Massen | R | gegen NuFIT 6.1 |
|---|---|---|
| Polmassen | 0,030840 | +1,80σ |
| 5 GeV (QED, 1 Schleife) | 0,030056–0,030107 | +0,09σ bis +0,20σ |
| M_Z (QED, 1 Schleife) | 0,030064–0,030114 | +0,11σ bis +0,21σ |
| M_Z (r11-Daten, 2 Schleifen) | 0,030087 | +0,16σ |
| 1 TeV (QED, 1 Schleife) | 0,030071–0,030120 | +0,12σ bis +0,23σ |
| 1 TeV bis 2·10¹⁶ GeV (SM-Laufen ab M_Z) | Änderung ≤ 2·10⁻⁶ | – |

Die Spannweite bei 1 Schleife kommt von der Wahl α(0) oder α(M_Z).

**2. Woher der Unterschied kommt.** In der QED gilt bei einer Schleife
m(μ) = m_pol/[1 + (α/π)(1 + (3/2) ln(μ/m_pol))]. Im Verhältnis zweier
Leptonen fällt μ heraus; es bleibt der Faktor 1 + (3α/2π) ln(m_i/m_j),
für τ/e etwa 2,8 %. Oberhalb von M_Z laufen die Verhältnisse der
Lepton-Yukawas praktisch nicht (Anteil (3/2) y², y_τ ≈ 0,01). Die Frage ist
also nicht „welche Skala“, sondern **„Polmassen oder Kopplungen“**: Pol-
massen enthalten die langreichweitige Photonwolke (QED-Selbstenergie), die
laufenden Massen bei jeder kurzreichweitigen Skala sind die Kopplungen.

**3. Was der Companion dazu sagt.** Die Brannen-Form entsteht in den
bisherigen Erkundungen in **Kopplungskonstanten**, nicht in Massen: in der
Platzkopplung über den Verbinder aus r44.1(b) mit h als Dublett-Richtung
(`op3_dixon_slot_coupling_2026_11_13.md`) und in W2 (r82.1: Higgs-Dublett,
Yukawa-Kopplungen über diese Verbinder). Eine solche Struktur gehört auf
die Seite der Kopplungen. Neutrinos sind elektrisch neutral; für sie
fehlt die Photonwolke, ihre Verhältnisse sind auf beiden Seiten gleich.
Ein Vergleich beider Sektoren ist deshalb nur auf der Kopplungsseite
gleichartig.

**4. Was dagegen spricht.** Koide 2/3 ist mit Polmassen exakt
(K = 0,666661), auf der Kopplungsseite nicht (0,6678). H1 (r11) hat
dasselbe für die Phase 2/9 gefunden. Die Kopplungs-Lesart erklärt also
die Neutrino-Beziehung und macht zugleich die Genauigkeit von Koide bei
Polmassen zum Zufall; die Pol-Lesart umgekehrt. Beides zugleich gelingt
keiner Lesart.

**Bewertung.** Für M_Z selbst gibt es keinen und braucht es keinen Grund;
jede kurzreichweitige Skala liefert dasselbe. Für die Wahl der
Kopplungsseite gibt es einen strukturellen Grund (Brannen-Form in
Kopplungen, Neutrinos ohne Photonwolke). Er ist nicht hergeleitet, weil
die Platzkopplung als Yukawa-Kopplung im Companion eine Lesart ist und
weil er der exakten Pol-Koide-Beziehung widerspricht. Die Fassung hat
damit keine freie Skala mehr, nur eine binäre Wahl. Das macht sie als
Vorhersage schärfer: R = 0,0301 ± 0,00003 (Spannweite der Skalen) gegen
H99 mit 0,030840.

## Nachtrag: die Koide-Spannung (13.11., Autor: „Erst Koide-Spannung“)

Vorwissen geprüft: Suche nach Sumino, Familien-Eichsymmetrie, QED-Korrektur
zu Koide in notes/, sources/, wiki/: kein Treffer. Einschlägig sind
thm:koide-triolic (Koide empirisch, Herleitung offen), H1 (r11), v4.8.0-r14
und r33 (Generationen brauchen eine zweite Dreierstruktur außerhalb von O).
Literatur: Y. Sumino, „Family Gauge Symmetry as an Origin of Koide's Mass
Formula and Charged Lepton Spectrum“, arXiv:0812.2103, JHEP 0905 (2009) 075.

**1. Wie scharf die Spannung ist.** K_pol − 2/3 = −2,2·10⁻⁶ ± 5,1·10⁻⁶ (aus
m_τ). Die QED-Verschiebung zwischen Pol und Kopplung ist +1,16·10⁻³. Die
Pol-Koide-Beziehung trifft also auf 0,2 % dieser Verschiebung. Liegt die
Struktur auf der Kopplungsseite, wäre das ein Zufall dieser Größe. Das
spricht deutlich für die Polseite.

**2. Ausweg nach Sumino.** Bei Sumino ist die Struktur exakt, und eine
Korrektur aus einer Familien-Eichwechselwirkung hebt die QED-Korrektur
für geladene Leptonen genau auf; deshalb gilt Koide für Polmassen (dort
mit Vereinigung von U(3) und SU(2)_L bei etwa 10²–10³ TeV). Neutrinos sind
neutral: Die QED-Korrektur fehlt, die Familienkorrektur nicht. Sie wirkt
bei ihnen allein und mit umgekehrtem Vorzeichen der QED-Korrektur.

Rechnung (nachträglich, nicht blind): Struktur nach H99 mit θ_e aus
Polmassen (Koide exakt); die physikalischen Neutrinomassen erhalten den
Faktor Q_k^(−c) mit Q_k = 1 + (α/π)(1 + (3/2) ln(μ/m_k)) der geladenen
Generation k. Zuordnung über den Index der Brannen-Form: ν₃ ↔ τ, ν₁ ↔ e
(negative Wurzel), ν₂ ↔ μ. Der Exponent c hängt davon ab, wie die
Familienkorrektur in den Neutrino-Massenterm eingeht.

| c | R (α(0)) | gegen NuFIT 6.1 | R (α(M_Z)) | gegen NuFIT 6.1 |
|---|---|---|---|---|
| 0 (H99) | 0,030840 | +1,80σ | 0,030840 | +1,80σ |
| 1/2 | 0,030545 | +1,16σ | 0,030524 | +1,11σ |
| 1 (wie der geladene Massenterm) | 0,030253 | +0,52σ | 0,030213 | +0,43σ |
| 2 | 0,029677 | −0,74σ | 0,029598 | −0,91σ |

**Bewertung.**
- Der Sumino-Weg löst die Spannung im Prinzip: Koide bleibt für Polmassen
  exakt, und die Neutrinos rücken an die Daten heran. Für c = 1 bleibt
  +0,5σ; jedes c zwischen 1/2 und 2 ist verträglich.
- Die Richtung folgt aus dem Mechanismus, nicht aus den Daten: Die
  Familienkorrektur muss bei den geladenen Leptonen die QED-Korrektur
  aufheben und wirkt deshalb bei den Neutrinos mit entgegengesetztem
  Vorzeichen. Der Betrag hängt an c und ist nicht festgelegt.
- Nicht nativ: Der Companion hat keine Familien-Eichsymmetrie; die zweite
  Dreierstruktur für Generationen fehlt (r14, r33). Der Weg ist Literatur.
  Ob die Platzkopplung eine Familien-Eichwechselwirkung tragen kann, ist
  eine neue offene Frage.
- Die Fassung „Kopplungsseite“ (R = 0,0301) und der Sumino-Weg mit c = 1
  (R = 0,0302) liegen nahe beieinander; künftige Daten trennen beide kaum,
  wohl aber beide von H99 (0,030840).
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.

## Nachtrag: Exponent c und Familiensymmetrie (13.11., Autor: „wie muss man c wählen … und dann die Familiensymmetrie“)

**1. c für null Abweichung** (nachträglich; Skript, Abschnitt „Familiensymmetrie“):

| Zuordnung | α | R bei c = 1 | c für z = 0 |
|---|---|---|---|
| ν_k ↔ e, μ, τ nach Brannen-Index | α(0) | 0,030253 (+0,52σ) | 1,41 (1σ: 0,62–2,21) |
| ν_k ↔ e, μ, τ nach Brannen-Index | α(M_Z) | 0,030213 (+0,43σ) | 1,32 (1σ: 0,58–2,06) |
| mit PMNS-Mittelung (NuFIT 6.1) | α(0) | 0,030387 (+0,81σ) | 1,83 |
| mit PMNS-Mittelung (NuFIT 6.1) | α(M_Z) | 0,030356 (+0,74σ) | 1,71 |

Die Familienkorrektur ist in der Basis der geladenen Leptonen diagonal.
Wegen der großen Mischung erhält jeder Neutrino-Zustand ein mit |U_ik|²
gewichtetes Mittel der Korrekturen von e, μ, τ (erste Ordnung). Die
Zuordnung nach dem Brannen-Index war eine Vereinfachung; die gemittelte
Fassung ist die richtige erste Näherung.

**2. Was Sumino für c sagt** (arXiv:0812.2103, nachgelesen). Das
linkshändige Dublett ℓ_L liegt in **3** von U(3), e_R in **3̄**. Weil
beide dieselbe elektrische Ladung, aber konjugierte Familienladungen
tragen, hat die Familienkorrektur dieselbe Form wie die QED-Korrektur mit
umgekehrtem Vorzeichen. Bei α_F = 4α heben sich beide auf; Sumino
erreicht das durch Vereinigung von U(3) und SU(2)_L bei 10²–10³ TeV.
Neutrinos: Der Majorana-Term ℓ_L ℓ_L (Weinberg-Operator) hat zwei Beine in
**3**, also wie ψ̄_L e_R zwei gleichgerichtete Familienladungen. Das
Vorzeichen der Korrektur ist dann dasselbe wie bei den geladenen
Leptonen, die Richtung der Rechnung stimmt. Erhält jeder familien-
geladene Massenterm dieselbe Log-Korrektur je Diagonalelement, ist
**c = 1** (auch für Typ-I-Seesaw, wenn Dirac- und Majorana-Term beide
korrigiert werden: −2 + 1). Gebraucht würde c ≈ 1,7–1,8; c = 1 liegt
innerhalb 1σ. Der genaue Faktor hängt am Modell der Neutrinomassen und
ist hier nicht hergeleitet.

**3. Familiensymmetrie im Companion.**

| Struktur | Quelle | Art | trägt Sumino? |
|---|---|---|---|
| S_3 aus den Sedenionen, Aut(S) = G_2 × S_3 | r13 (k28) | diskret | nein: keine Eichbosonen |
| Trialitätsplätze von Re((xy)z), S_3 | r14, Träger r15 (Hopf) | diskret | nein |
| Δ(96) ⊂ SU(3), Stabilisator von e_7 | r12.2 | diskret, liegt in der Farbe | nein (r14) |
| Farb-SU(3) | Kern | stetig, geeicht | nein: Farbe, nicht Generation |
| Quaternionen-Richtungen i, j, k | r33 | Labels | ausgeschieden (nicht Q_em-invariant) |
| U(3) auf dem Platzindex der Gram-Matrix | Gram-Notiz | stetig, global | **Kandidat**, nicht geeicht |

Native stetige Familien-Eichsymmetrie: **keine**. Der Companion kennt
nur diskrete Dreiersymmetrien (S_3) und die Farbe.

Formale Nähe, nicht mehr: Die Massen hängen in der Gram-Lesart nur von
den Eigenwerten der hermiteschen 3×3-Matrix S ab, also invariant unter
S → U S U† mit U ∈ U(3) auf dem Platzindex. Sumino bringt sein
9-komponentiges Feld Φ durch eine U(3)×SU(2)-Transformation auf hermitesche
Form Φ = V d V†, mit √m_i ∝ Eigenwerten. Die Gram-Matrix spielt also
formal die Rolle von Φ. Auch die konjugierte Ladung von e_R hat ein
mögliches Gegenstück: Die Dixon-Platzkopplung F_b(x, y, h) = ⟨(x^ y) h⟩
konjugiert den ersten Eintrag.

Was fehlt, damit daraus Suminos Mechanismus wird:
1. Die Platzindex-U(3) müsste geeicht sein (ein Zusammenhang auf dem
   Platzindex mit eigenen Eichbosonen); der Companion hat dafür kein Feld.
2. Die Massen der Familienbosonen müssten aus S kommen und die Struktur
   M_ij² ∝ v_i² + v_j² haben (bei Sumino aus Φ in drei (3,1)).
3. α_F = 4α bei der passenden Skala, etwa über Vereinigung mit SU(2)_L.
   Im Companion sitzt SU(2)_L im Quaternionenfaktor; eine Vereinigung mit
   einer Platzindex-U(3) ist nicht angelegt.

**Bewertung.** c ≈ 1,7–1,8 gleicht exakt aus; das natürliche c = 1 bleibt
innerhalb 1σ (+0,7σ bis +0,8σ). Eine Familien-Eichsymmetrie gibt es im
Companion nicht; die global wirkende Platzindex-U(3) der Gram-Lesart ist
der einzige stetige Kandidat und müsste erst geeicht werden. Das wäre ein
neues Strukturelement, keine Folgerung. OP3/OP4 offen; OP1–OP5, C5,
C6/T2 unverändert.

## Nachtrag: c als Maß einer Abweichung, als Integral gelesen (13.11., Autor)

**1. Wie gut c bestimmt ist** (mit PMNS-Mittelung): c = 1,83 ± 1,0 (α(0)),
1,79 ± 1,0 (α(m_τ)), 1,71 ± 0,97 (α(M_Z)). R hängt fast linear von c ab
(dR/dc ≈ −4,6·10⁻⁴). Damit ist c − 1 = 0,7–0,8 nur 0,8σ von null entfernt;
c = 0 (H99) liegt 1,8σ entfernt. Die Daten verlangen also eine Korrektur
dieser Art (c > 0), aber keine Abweichung von c = 1.

**2. c als Verhältnis zweier Integrale.** Die generationsabhängigen Teile
beider Korrekturen sind Integrale über die Skala zwischen den Schwellen:

    QED (geladen):  δ ln(m_i/m_j) = (3/2π) ∫ from m_j to m_i of α(μ) d ln μ,
    Familie:        dieselbe Form mit α_F zwischen den Schwellen der
                    Familienbosonen (M_i² ∝ m_i, also halbe Log-Länge).

So gelesen ist c = (Familien-Integral, das der Neutrino-Massenterm sieht)
/ (QED-Integral der geladenen Leptonen). Suminos Bedingung α_F = 4α ist
genau die Aussage, dass beide Integrale für die geladenen Leptonen gleich
sind. Sieht der Neutrino-Term dieselben Familienschwellen, ist c = 1; das
gilt in Suminos Rahmen unabhängig davon, ob die Neutrinomassen über den
Weinberg-Operator oder einen Seesaw oberhalb oder unterhalb der
Familienskala entstehen, weil die Generationsabhängigkeit nur aus den
IR-Schwellen der Bosonen kommt.

**3. Lesart.** c − 1 wäre ein Maß dafür, wie weit das Integral auf der
Neutrinoseite vom geladenen abweicht: andere Schwellen, ein anderes
Laufen von α_F, eine unvollständige Aufhebung bei den geladenen Leptonen
oder ein zweiter Effekt wie die Skalenwahl aus Idee 3. Ein bestimmtes c ≠ 1
folgt aus keinem dieser Punkte ohne weiteres Modell. Mit heutigen Daten
ist c = 1 verträglich; ein eigenes Integral wird erst gebraucht, wenn
genauere Daten c ≠ 1 verlangen. Künftige JUNO-Werte bringen σ_c auf etwa
0,5; c = 0 und c = 1 trennen sie dann mit etwa 2σ, c = 1 und c = 1,8 kaum.
