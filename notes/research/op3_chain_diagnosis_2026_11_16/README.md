# OP3: Woran die Biegung scheitert. Logikkette rückwärts, Abgleich mit OP5 (Erkundung, nicht blind)

16. November 2026. Auftrag des Autors: „versuche zu bestimmen, woran es liegt, gehe zur Not die ganze Logikkette zurück und/oder schaue mal bei
OP5 nach“. Anlass: sechs Wege ohne Erfolg (H106–H110, Renormierung), kein natives κ. Skript `chain.py`, Ausgaben `run/chain_stdout.txt` und
`run/spin_series.txt`. Rückwärtssuche gemäß AGENTS.md („Suchrichtung prüfen“); keine H-Nummer.

## Die Kette, vom Ziel aus rückwärts

| Glied | Aussage | Status |
|---|---|---|
| Z | Brannen-Form $\sqrt{m_k}\propto1+2|c|\cos(\delta+2\pi k/3)$ | gilt für **jede** positive Dreiergruppe (Mittelwert plus eine Fourier-Komponente); kein Inhalt |
| Z1 | $K=2/3\iff|c|=1/\sqrt2$ | nachgerechnet: Polmassen geben $2|F_1|/F_0=1{,}414201$ |
| Z2 | $\delta$ ist eine **zweite, unabhängige** Zahl; Polmassen: $3\delta=0{,}666689$ | Messung |
| G | Gram-Lesart: $\sqrt m$ = Eigenwerte der Gram-Matrix dreier Auslesungen; dann $|G_{01}|^2=K$-Bedingung und Bargmann-Phase $=3\delta$ | Setzung (r16.4); Identität nachgerechnet ($|G_{01}|^2=0{,}499991$, Phase 0,666689) |
| A | Auslesungen = Eigenzustände der Frame-Abbildungen → Überlappung ½ | hergeleitet unter Bedingungen (r16.7) |
| B | Phase aus derselben Geometrie: Oktant $\pi/4$; Kopien (r25) Spin-1-Dreieck 0,679042 | erzwungen, s. u. |
| H106–H110, κ | Verformungen von B im Träger: Singulett, Normierung, Verschränkung, Frames, Betrachter | alle ohne Erfolg |

Das Ziel ist richtig gelesen: Glieder Z, Z1, Z2 und G sind konsistent (Abweichungen im Bereich der Messfehler). Pol- gegen Laufmassen ist
geprüft (Renormierungs-Erkundung). Der Fehler sitzt nicht im Ziel.

## Woran es liegt

**1. Zwei unabhängige Zahlen, eine Geometrie.** Die Daten haben zwei unabhängige Zahlen, $|c|$ (also $K$) und $\delta$. Jede bisher geprüfte
Konstruktion liefert beide aus **einem** geometrischen Datum. Für eine reine, generationssymmetrische Bahn legt die Überlappung den Kegel fest
und der Kegel die Phase. Nachgerechnet für kohärente Zustände mit Überlappung² ½:

| Spin $j$ (Kopien $2j$) | Kegel | Phase |
|---|---|---|
| ½ (Oktant) | 54,74° | 0,785398 |
| 1 (zwei Kopien, r25) | 38,68° | 0,679042 |
| 3/2 | 31,63° | 0,650463 |
| 2 | 27,42° | 0,637118 |
| 3 | 22,42° | 0,624334 |
| 10 | 12,30° | 0,607299 |

Die Werte sind starr und fallen monoton. 2/3 liegt zwischen Spin 1 und Spin 3/2, und kein kohärenter Spin trifft es. Alle sechs Wege haben
versucht, die zweite Zahl aus derselben Geometrie zu holen, die schon die erste festlegt. Das kann nur mit zusätzlicher Struktur gehen, und
diese Struktur war jedes Mal eine Setzung (Gewicht, Verschränkung, Aufteilung, κ).

**2. Der Zielzustand ist nicht kohärent, und das steht schon im Bestand.** Schreibt man die Bahn wie r16.9 als Spin-1-Zustand unter dem
Drittelzyklus $U=\operatorname{diag}(\omega,1,\bar\omega)$, dann verlangen $K=2/3$ und $\varphi=2/3$ die Gewichte 0,793146 / 0,193404 / 0,013450
(wie r16.9(a)). Ein kohärenter Zustand hat das Kohärenzmaß $r=2\sqrt{p_{\rm groß}\,p_{\rm klein}}/p_{\rm mitte}=1$; das Ziel braucht
$r=1{,}068084$. Nach r16.8 heißt das: Die Invariantenmatrix $S$ des Feldes muss **Rang zwei** haben (Takagi-Verhältnis zwischen 0,0066 und 0,2087,
je nach freier relativer Phase). r16.8 sagt dazu: Dieser Anteil existiert, aber „its size, the Takagi ratio, is free for every field“.

Die fehlende Zahl ist also **eine Eigenschaft des Feldzustands** (wie stark er von einem kohärenten, rang-eins Zustand abweicht), keine
Eigenschaft des Trägers oder der Auslesung. Die sechs Wege haben im Träger gesucht (Kopien, Frames, Betrachter); dort ist sie nicht.

**3. Der Zahlentyp passt nicht zu einer reinen Geometrie.** Eine geometrische Phase ist ein halber Raumwinkel. 2/3 rad entspräche 4/3 sr, also
keinem ausgezeichneten Raumwinkel (der Oktant hat $\pi/2$ sr). Dass die Phase in Bogenmaß zugleich mit $K=2/3$ übereinstimmt, sieht eher nach einer
dynamischen Phase oder einem Verhältnis aus als nach einem Winkel. Das ist eine Beobachtung, nicht blind und nicht belegt; die Literatur dazu ist
nicht geprüft.

## Abgleich mit OP5
OP5 scheitert an derselben Stelle, und das Wiki nennt sie als gemeinsamen Kern aller offenen Probleme („Es fehlt eine Dynamik“):
- **Zustandsauswahl.** Die OP5-Erkundung zur Zustandsauswahl (`../op5_state_selection_exploration_2026_11_06.md`) zeigt: Im Feld-/Gram-Modell gibt
  es bei fester Normierung eine ganze Familie mit beliebigem Eigenwertverhältnis $q$; dieselbe Projektoralgebra wählt den H96-Wert nicht aus.
  Für OP3 gilt nach Punkt 2 dasselbe: Die Algebra lässt das Takagi-Verhältnis frei; sie wählt den Zielzustand nicht aus.
- **Quelle–Rückweg.** Nach `../op5_route_inventory_2026_11_06.md` starten die zwei gerichteten Auslesungen am selben Quellzustand, nicht an den
  Enden eines berechneten Hin- und Rückwegs. Die Bargmann-Phase der Frame-Auslesungen ist genau so eine Größe ohne Transport. Bei einem
  wirklichen Umlauf käme zur geometrischen eine dynamische Phase hinzu. Sie wurde nie gerechnet, weil kein Transport definiert ist.
- **Uhr.** Punkt 7 der gemeinsamen Anforderungen: „Eine Uhr aus der Phasendifferenz zwischen Materie und Tachyon.“ r16.9 liest den
  Generationszyklus bereits als Zeitverschiebung um ein Drittel der Periode. In dieser Lesart sind $K$ und $\varphi$ zwei Bedingungen an zwei freie
  Gewichte, also entkoppelt. Was fehlt, ist das Gesetz, das die Gewichte (gleichwertig: $w$ gegen $s_\pm$) festlegt.

## Ergebnis
1. Ziel und Gram-Lesart sind in Ordnung. Der Fehler liegt in der Art der gesuchten Erklärung: Alle Wege haben die zweite Zahl ($\delta$) aus der
   Geometrie des Trägers holen wollen. Dort ist sie starr an $K$ gebunden.
2. Die zweite Zahl ist eine Eigenschaft des Feldzustands: das Rang-zwei-Gewicht der Invariantenmatrix $S$, gleichwertig das Kohärenzmaß
   $r=1{,}068084$ oder die Gewichte von r16.9(a). Sie verlangt ein Auswahlgesetz für den Zustand.
3. Das ist dieselbe Lücke wie bei OP5 (Zustandsauswahl, fehlender Umlauf) und der gemeinsame Kern aus dem Wiki (fehlende Dynamik). Weitere
   Varianten im Träger (Kopien, Frames, Betrachter, Sedenionen) werden nach diesem Befund nichts liefern. Fortschritt bei OP3 ist an die Dynamik
   gekoppelt (W1/W2, eingefroren), nicht an weitere Kinematik.

## Grenzen
- Nicht blind: Ziel und Gewichte waren bekannt; die Diagnose ordnet ein, sie beweist keine Unmöglichkeit für jede denkbare Struktur.
- Die Gram-Lesart (Glied G) bleibt eine Setzung. Fiele sie, wären alle Glieder darunter hinfällig, auch die Diagnose.
- OP3 offen; OP1–OP5, C5, C6/T2 unverändert.

## Nachtrag (16.11.2026): Auswahlgesetz angehen, mit Berichtigung
Auftrag des Autors: „Auswahlgesetz für den Feldzustand angehen“. Die Vorwissen-Suche dafür hat einen Bestand gefunden, den diese Diagnose
übersehen hatte: den **bewachten Kern** (`../op3_guarded_core_flux_2026_11_15/README.md`, r14.5–r14.7) und die offene Vorhersage **H102**
(`../predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`). Das ist mein Fehler: Ich hatte die Suche auf die Kopien-, Frame- und
Renormierungsnotizen beschränkt.

**Berichtigungen.**
1. *Zu „Der Zahlentyp passt nicht zu einer reinen Geometrie“:* falsch. Der Raumwinkel $2\varphi=1{,}33333$ sr ist $\pi/2-0{,}237466$, also der
   Oktant minus eine Kappe vom Raumwinkel $\gamma_M=0{,}237533$ (Abweichung $6{,}7\cdot10^{-5}$ sr, in der Phase $3{,}3\cdot10^{-5}$). Die
   Phase hat damit eine geometrische Lesart: $\varphi=\pi/4-\gamma_M/2$ (H102).
2. *Zu „Weitere Varianten im Träger werden nichts liefern“:* zu pauschal. Die Starrheit gilt für Zustände bei der natürlichen
   Berry-Verbindung. Der bewachte Kern ändert nicht die Zustände, sondern **die Verbindung** auf der Generationskugel: eine flussfreie Kappe,
   deren verdrängter Fluss am Gegenpol sitzt (Umkehrwalze, r02.2/r02.3). So entgeht er der Starrheit, ohne freie Gewichte.
3. *Zu „Kein natives κ“ und zu H109/H110:* bleibt richtig für Dephasierung und Verschränkung. Der Kern ist ein anderer Mechanismus mit genau
   einer Zahl.

**Was das Auswahlgesetz damit ist.** Die Kette steht im Bestand schon so:

| Glied | Inhalt | Quelle | Status |
|---|---|---|---|
| φ ← Kern | $\varphi=\pi/4-\Omega/2$ bei flussfreier Kappe Ω, verdrängter Fluss am Gegenpol | guarded core, Schritt 2, Umkehrwalze | Lesart |
| genau ein Kern | einzige Zahl, die biegt und keinen freien Parameter einführt | ebenda, Schritt 2 | topologisch begründet |
| Ω ← Frame | Kern = Flächenquant des Beobachter-Frames; geladene Leptonen im Frame M | ebenda, Punkt 1 | Regel, gesetzt |
| γ_M ← Zählregel | $\sum_j 2e^{-2\pi\gamma\sqrt{j(j+1)}}=1$ über alle Spins | r08–r10 | gewählt, nicht hergeleitet |
| Zählregel ← OP1 | warum M alle Spins mit Gewicht 2 zählt; T zählt Querungen (r24.4) | r17, r24 | offen ((S2) nicht begründbar, r24.1) |

Das Auswahlgesetz für den Feldzustand ist also kein offenes Feld, sondern läuft auf **eine** Frage hinaus: die Zählregel des Frames M (OP1). Die
Daten prüfen es schon: H102 sagt $m_\tau=1777{,}134$ MeV voraus und liegt heute $+2{,}3\sigma$ über PDG 2024; entschieden wird mit der ersten
PDG-Ausgabe nach dem 13.11.2026.

**Bezug zu Punkt 2 dieser Diagnose.** Die Aussage „die fehlende Zahl ist eine Eigenschaft des Feldzustands“ bleibt in der r16.9-Lesart richtig,
ist aber nicht die einzige Lesart. Im Kern-Bild ist sie eine Eigenschaft der Verbindung auf der Generationskugel, und deren Größe ist ein
Flächenquant. Beide Lesarten verlangen eine Zahl von außerhalb der Zustandsgeometrie; das Kern-Bild sagt, woher sie kommen soll.

**Folgerung für den nächsten Schritt.** Nicht eine neue Dynamik suchen, sondern die Lücke OP1 angehen, an der Kern und Zählregel hängen: warum
der Materie-Frame alle Spins mit Gewicht 2 zählt ((S2), (S3)), nachdem r24 die T-Seite als Querungszählung gelesen hat. H102 bleibt unverändert
und eingefroren. OP1 und OP3 offen.
