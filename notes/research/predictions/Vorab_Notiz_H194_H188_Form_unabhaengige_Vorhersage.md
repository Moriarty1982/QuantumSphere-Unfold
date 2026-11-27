# Vorab-Notiz H194: Die H188-Form mit einer unabhängigen Vorhersage prüfen

**Datum:** 27.11.2026. **Nummern:** H194 (Test), k402 (Rechnung). **Strang:** Quarkmassen nach H190. **Anlass:** Der Autor wählte
auf der Karte (27.11., 09:17) „H188-Form testen". Die H188-Notiz (`.../ableitungsterme_h188/`) hat die Form **nachträglich**
gefunden und ausdrücklich festgehalten, sie sei „kein Befund, sondern ein Kandidat, der nur mit einer neuen Vorab-Notiz und einer
unabhängigen Vorhersage (etwa einer Beziehung zwischen b/a für Up und Down oder einer Herleitung der Form) geprüft werden kann."
Genau das ist H194.

## Die Form
m ∝ (a·l_k + b·l_k²) / (l_i + l_j)², Zuordnung B (leichteste Generation beim Paar (μ,τ)), Lesart X = m.

- l₁, l₂, l₃ = Eigenwerte des **Leptonvakuums** W₀ (Zirkulante in H₃(𝕆), K = ⅔, δ = 2/9 — die δ-Phase stammt aus den geladenen
  Leptonen, **nicht** aus den Quarks; sie ist ein stehender Eingabewert des Projekts, nicht für diese Frage justiert):
  l = [0,040350, 0,580212, 2,379438].
- (i, j, k) ist je Generation eine Permutation: k der „eigene" Index, i, j die beiden anderen; z = (l_i + l_j)².
- Je Sektor zwei angepasste Zahlen a, b für drei Massen (ein Freiheitsgrad je Sektor). Bekannter nachträglicher Fit (k391c):
  Up a = −5,71·10⁻⁴, b = 3,31·10⁻², b/a = −57,9 (χ² = 4,8); Down a = 1,65·10⁻³, b = −1,41·10⁻⁴, b/a = −0,085 (χ² = 3,1).

## Kernfrage
Ein linearer Zwei-Parameter-Fit (a, b) trifft drei Massen fast immer — das allein ist kein Befund. Die Form trägt nur, wenn sie
**über den Fit hinaus Inhalt hat**: entweder teilen sich die Sektoren die Gestalt (ein gemeinsames b/a), oder der Fit gelingt
**gerade** mit den leptonischen l_k und nicht mit beliebigen. H194 prüft beides mit vorab festgelegten Kriterien.

## Daten (wie H187/H188)
Up (M_Z, Yukawa): [7,04·10⁻⁶, 3,56·10⁻³, 0,967], σ [0,15·10⁻⁶, 0,06·10⁻³, 0,004].
Down (M_Z): [1,54·10⁻⁵, 3,06·10⁻⁴, 1,630·10⁻²], σ [0,02·10⁻⁵, 0,04·10⁻⁴, 0,009·10⁻²].

## Teile und Kriterien
- **H194a (nicht blind, Kontrolle).** Den bekannten Fit je Sektor (a, b frei) reproduzieren. Das ist der nachträgliche Fit aus
  k391c, kein Test; er belegt nur, dass die Form mit zwei Zahlen je Sektor passt (χ² ≈ 3–5, ein Freiheitsgrad). Analytisch
  vorhersehbar, daher nicht blind.
- **H194b (Test — unabhängige Vorhersage 1: gemeinsame Gestalt).** Ein **einziges** ρ = b/a für **beide** Sektoren, Gesamtskala je
  Sektor frei: m_gen = S_sektor·(l_k + ρ·l_k²)/z. Drei Parameter (ρ, S_up, S_down) für sechs Massen.
  - **bestätigt:** ein gemeinsames ρ bringt beide Sektoren alle drei Massen < 3σ, und ρ hat eine Projektbedeutung (ein
    Modellwert, kein beliebiger Fit).
  - **teilweise:** ein gemeinsames ρ bringt beide < 3σ, aber ρ ist nur eine Zahl ohne Bedeutung; oder nur ein Sektor < 3σ.
  - **widerlegt:** kein gemeinsames ρ bringt beide Sektoren unter 3σ.
- **H194c (Test — unabhängige Vorhersage 2: Spezifität der l_k).** Gelingt der Zwei-Parameter-Fit je Sektor **gerade** mit den
  leptonischen l_k (δ = 2/9) und der Zuordnung B, oder ebenso mit beliebigen l-Tripeln? 2000 zufällige l-Tripel (gleiche
  Normierung, gleiche Zuordnung) durch denselben Fit; Anteil, in dem **beide** Sektoren den beobachteten χ² erreichen oder
  unterbieten. Zusätzlich alle sechs Permutationen der l-Index-Zuordnung mit den echten l_k.
  - **spezifisch (stützt die Form):** die leptonischen l_k liegen im besten wenigen Prozent; Zufalls-l treffen selten.
  - **generisch (entwertet die Form):** beliebige l treffen ähnlich oft → der Fit kommt von den zwei Parametern, nicht von den l_k.
- **Nachträglich (kein Test).** Ob b/a je Sektor oder ihr Verhältnis/Produkt an einen Modellwert (β_sym, γ_L, δ, die l_k selbst)
  heranreicht — offen notiert, ohne Beweiskraft (viele Ziele).

## Gesamturteil (vorab)
Die H188-Form zählt als **echter Kandidat** nur, wenn H194b (gemeinsame Gestalt) **oder** H194c (Spezifität der leptonischen l_k)
ihr Inhalt über den reinen Zwei-Parameter-Fit hinaus gibt. Trifft keines zu, ist die Form **widerlegt** als eigenständiger Befund
und bleibt, was H188 schon sagte: ein per-Sektor-Fit mit zwei Zahlen.

## Erwartung (offen gelegt)
Ich erwarte **widerlegt**: Die bekannten b/a (−57,9 und −0,085) unterscheiden sich um das 680-fache, ein gemeinsames ρ kann beide
Sektoren kaum zugleich tragen (H194b); und ein Zwei-Parameter-Fit an drei Punkte trifft über l-Tripel hinweg leicht, sodass die
leptonischen l_k vermutlich nicht spezifisch herausragen (H194c). Ein echter Befund wäre ein gemeinsames ρ mit Modellbedeutung
oder eine klare Spezifität der leptonischen l_k. Der Wert liegt im sauberen Urteil über den Kandidaten.

## Werkzeuge
Python (numpy) für die Fits, die ρ-Suche und die Zufallskontrolle; Wolfram Language für die exakten leptonischen Eigenwerte
(δ = 2/9) und die exakten Basisvektoren der Form als Gegenprobe. Qiskit nicht nötig (kein Messprozess). Coprozessor-Maschine
nicht einschlägig (Zahlen-Fit).

## Vorwissen geprüft
- `.../ableitungsterme_h188/` (H188, k391, k391c): Herkunft der Form, bekannter Fit, Warnung „nur mit neuer Vorab prüfbar".
- `.../schwingungen_h184/` (H184): Leptonvakuum W₀, Eigenwerte l_k, δ = 2/9 als Eingabe (geladene Leptonen), K = ⅔.
- `.../adjunkte_h187/` (H187): Funktionsmenge R, Zufallsquote 2,45 % ohne kinetische Funktion.
- `.../generationsdrehung_h190/`, `.../baender_hs_stufen_h192/`, `.../getrennte_felder_h193/`: alle anderen Wege (ein Hebel,
  Geometrie, getrennte Felder) geprüft; Massenquelle bleibt offen.
- Memory: H188 nachträglicher Kandidat m ∝ (a l_k + b l_k²)/(l_i+l_j)² „nur mit neuer Vorab".

## Grenzen (vorab)
Fester Funktionsansatz und feste Zuordnung B (H194b/c prüfen genau deren Spezifität). Keine Herleitung der Form aus der
Feldgleichung — die bliebe der eigentliche Befund und ist nicht Gegenstand dieses Tests. OP3/OP4 bleiben offen.
