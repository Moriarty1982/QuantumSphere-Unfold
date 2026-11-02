# Gegenprüfung des OP5-Stands bei cf48496 (Ende der Arbeit des anderen Sprachmodells)

Stand 2026-11-02. Ziel: auf denselben Stand kommen und ihn intern gegenprüfen, bevor weitergearbeitet wird.

## Wo das andere Modell aufgehört hat

Letzter Commit `cf48496` (30.10., 20:12), Notizen unter `analysis/op5-field-slices/state-sufficiency-2026-10-30/`
(`ALL_ORDER_PROGRAM.md`, `ALL_ORDER_RESULT.md`, `PRECISION_FIFTH_GATE_REPAIR.md`).

- Vergleichsmodell (fest): F = i Σ V^μ_a K_a D_μΨ − h (Y⊗β) Ψ, Coframe E^a_μ = Re(Ψ† Q_a D_μ Ψ), skalare Bedingung g = 4 − h Ψ†(Z⊗β)Ψ/2;
  vervollständigtes System R = (F, G, dg). Kein natives QSC-Modell.
- Am Punkt (t,x,y,z) = (1, 3/5, 0, 0) gibt es einen 70-stelligen numerischen Feldkeim bis Grad 5, der R bis Ordnung 4 erfüllt
  (alle 1120 Gleichungen ≤ 2,8·10⁻⁶²). Dafür mussten die Koeffizienten vom Grad 4 über ein vierdimensionales „Quell-Gate“ deutlich
  verändert werden (bis 192 in normierten Einheiten); Grad 0–3 blieben fest.
- Gefunden und erzwungen: eine zusätzliche Bedingung Ω an die dritten Ableitungen (nicht automatisch erfüllt).
- Bewiesen (bedingt): Vollständigkeit des ursprünglichen Symbols, zwei vervollständigte Projektionsschritte; skalare Bedingung exakt
  lokal lösbar.
- Offen: höherer Rang/Spencer-Kohomologie des um Ω erweiterten Systems (bei Grad 5 numerisch nicht entscheidbar), voller Ω-Kovektor
  am reparierten Keim, exakte/Intervall-Zertifizierung, Wachstum/Konvergenz, regionale und physikalische Existenz.
- Vorgeschlagene nächste Schritte: Erweiterung auf Ordnung 6 an diesem gemeinsamen Keim mit hoher Genauigkeit, oder das Gesetz des
  Quell-Gates rekonstruieren statt weiter zu fitten.

## Gegenprüfung

1. **Wiederholung:** `precision_fifth_gate_check.py` neu ausgeführt; Ergebnis Zeichen für Zeichen gleich der eingecheckten Datei.
   Dazu musste ein fest eingebauter Pfad auf die Arbeitskopie des anderen Modells
   (`C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold`) auf das Repository umgebogen werden; 8 Skripte enthalten
   diesen Pfad.
2. **Eigene Implementierung (`k109_unabhaengig_F.py`):** Modell neu aus den Formeln aufgeschrieben, Feld als Polynom bis Grad 5 aus
   den gespeicherten Koeffizienten, Auswertung entlang von Geraden mit exakter Potenzreihen-Arithmetik (80 Stellen, keine numerische
   Ableitung, kein fremder Code). Sieben Richtungen, davon zwei neue:
   - F bis Ordnung 4: höchstens 1,2·10⁻⁶⁰,
   - g bis Ordnung 5: höchstens 1,6·10⁻⁶³,
   - det E₀ = 13,63 (nicht entartet).
   Gegenprobe: ein Grad-5-Koeffizient um 10⁻³ verschoben ergibt F-Ordnung 4 = 0,036; ein Grad-3-Koeffizient um 10⁻⁶ verschoben ergibt
   F-Ordnung 2 = 1,2·10⁻⁵. Die Auswertung erkennt Fehler also an der richtigen Stelle.
   Nicht unabhängig geprüft: der Anteil G von R (Kompatibilitätsfunktionen) und die Rang-/Ω-Aussagen.

Urteil: Der Stand ist reproduzierbar, und der Keim erfüllt die Feldgleichung und die skalare Bedingung in einer unabhängigen
Implementierung. Das ist ein endlicher numerischer Befund an einem Punkt, keine Lösung auf einem Gebiet und kein Abschluss von OP5.
