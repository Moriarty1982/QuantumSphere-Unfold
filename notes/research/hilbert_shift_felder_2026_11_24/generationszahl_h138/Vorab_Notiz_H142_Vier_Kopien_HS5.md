# Vorab-Notiz H142: Noch eine Generation mehr – vier Oktonion-Kopien auf HS(5)

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Dimensionen folgen aus H138 (Richtungen der 9 oktonionischen
Kopien, Rang 4) durch Abzählen; Ladungsspektren, Lecks und die Frage nach den Leptonen sind nicht gerechnet. Anlass: Autor (25.11.2026, 20:00):
„ok, versuche noch eine Generation mehr“, Auftrag über den Koordinator: einen weiteren Träger nehmen und prüfen, was er trägt, ob sich die
fehlenden Leptonen (Ladung 0 und 1) schließen und ob eine gemeinsame erhaltene Ladung entsteht.

## Vorwissen geprüft
- H141 (589b1c3, k324): drei getrennte Kopien → ℂ⊗𝕊: Kern 9 = 1 ⊕ 1 ⊕ 1 ⊕ 3 ⊕ 3̄; Farbteil ladungsstabil (⅓, ⅔), Singuletts ½ und leckend.
- H140 (94694e6, k323): keine gemeinsame Ladung α + βL_x + γR_x für die drei Kopien; Farbe gemeinsam.
- H138 (k321b): auf HS(5) neun oktonionische Kopien v = a ⊗ b (a, b aus den drei Sedenion-Richtungen), Rang 4, nie orthogonal.
- In 𝕊 gibt es keine vierte Kopie (Im z³ = 0); eine vierte braucht HS(5).

## Aufbau
Träger ℂ⊗A₅ (32 komplex). Kopien C_v = ℂ⊗O_v, O_v = span{1} ⊕ Im 𝕆 ⊗ v (v aus den 9 oktonionischen Richtungen von k321b), Ladung je Kopie
Q_v = ½ − (i/6)L_{u_v} − (i/3)R_{u_v} mit u_v = e₇ ⊗ v, Farbe = Stabilisator von e₇ in der blockweisen g₂.
Für **alle 126 Viererauswahlen** der 9 Kopien (darunter die 6, die die drei Sedenion-Kopien enthalten): getrennte Träger V = ⊕ C_v (32 Zustände),
Summenabbildung Φ: V → ℂ⊗A₅, Kern K, Kokern, gestauchte Ladung auf K, Ladungs-Leck, gemeinsame Ladung in der Familie α + βL_x + γR_x
(x ∈ Im A₅, 200 Starts je Klasse). Skript k325 (Python), Gegenprobe k325b (Wolfram, exakt für eine Auswahl je Klasse).

## Hypothesen und Kriterien
- **H142a (Farbe und je Kopie eine Generation):** Für alle 9 Kopien bildet Q_v die Kopie in sich ab (Leck < 10⁻¹²) mit Spektrum 0, ⅓³, ⅔³, 1,
  und su(3) ist für alle dieselbe.
- **H142b (Leptonen schließen sich nicht):** In keiner Viererauswahl enthält das Spektrum der auf K gestauchten Ladung die Werte 0 oder 1
  (Abstand > 10⁻⁶). Widerlegt, wenn eine Auswahl 0 und 1 im Kern hat.
- **H142c (keine gemeinsame Ladung):** Für keine Viererauswahl gibt es α + βL_x + γR_x, das alle vier Kopien erhält (min Leck² > 10⁻³).
- **H142d (Rest wird kleiner):** Bei Auswahlen mit linear unabhängigen Richtungen (Rang 4) besteht der Kern nur aus 3 Singuletts (kein
  Farbteil, kein Quark-Satz); bei Rang 3 hat der Kern zusätzlich einen Farbteil 1 ⊕ 3 ⊕ 3̄. Kriterium: dim K = 3 bzw. 10 und Casimir-Zerlegung.
- **Kontrolle:** die drei Sedenion-Kopien in A₅ reproduzieren H141 (Kern 9, Spektrum ⅓³, ½³, ⅔³).

## Folge, vorab festgelegt
- b und c bestätigt: Eine Generation mehr bringt weder die Leptonen des Rests noch eine gemeinsame Ladung; der Turm liefert dann gleichwertige,
  aber getrennt geladene Kopien, und jede weitere Kopie verkleinert nur den Rest.
- b widerlegt: Mit vier Kopien schließen sich die Leptonen; das wäre ein Hinweis auf eine Vierer- statt Dreierstruktur und bekäme einen eigenen Folgetest.
- Was in keinem Fall folgt: Massen, Mischung, Vorzeichen. OP3, OP4 offen; kein Guard berührt. Vergeben: H142, k325.
