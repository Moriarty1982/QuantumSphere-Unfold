# Ergebnis H107: Verschachtelte Normierung in HS(8) legt das Singulettgewicht nicht passend fest (widerlegt)

**16.11.2026.** Vorab-Notiz `Vorab_Notiz_H107_Verschachtelte_Normierung.md` (Commit 30a4a50, vor der Rechnung erweitert auf die volle
Grammatik von HS(8) mit Commit 44cda89), Skript `k229_test_h107.py` (Commit 4699cac), Ausgabe `k229_out.txt`, Kreuzprüfung mit
`tools/hs_partition.py` in `k229_kreuzpruefung.txt`. Idee des Autors. Blind nur darin, dass die Mechanismen vor der Rechnung festgelegt
waren; der Zielwert 0,666665 war bekannt.

## Ergebnis: widerlegt
Zehn Mechanismen, je zwei Lösungen, also 20 Versuche; **kein Treffer** innerhalb 0,0002 rad. Die nächstgelegenen Lösungen:

| Mechanismus | ψ | w | Phase φ | φ − 0,666665 |
|---|---|---|---|---|
| N1 (ein mittleres HS(6), p₀₁) | 41,17° | 0,1083 | 0,665173 | −0,001492 |
| N5 = N7 = N9 (s²) | 41,63° | 0,1263 | 0,662517 | −0,004148 |
| N2 (leichtes HS(6), p₁₁) | 38,94° | 0,0123 | 0,677627 | +0,010962 |
| Spin-1-Dreieck (w = 0, Kontrolle) | 38,68° | 0 | 0,679042 | +0,012377 |

Alle übrigen Lösungen liegen um mehr als 0,02 rad daneben. Beide Implementierungen (k229 und `hs_partition.py`) geben dieselben Werte.

## Was die Rechnung strukturell zeigt
- **Die Normierung in einer HS(7)-Hälfte bringt nichts Neues.** Für den Triplettanteil |n⟩|n⟩ gilt exakt (geprüft):
  p₀₁/(p₀₀ + p₀₁) = p₁₁/(p₁₀ + p₁₁) = p₁₀ + p₁₁ = sin²(ψ/2) und p₁₀/(p₁₀ + p₁₁) = p₀₀/(p₀₀ + p₀₁) = p₀₀ + p₀₁ = cos²(ψ/2).
  Ein Produktzustand zerfällt über die Halbierung: Ein HS(6) in seinem HS(7) normiert ist einfach das Gewicht eines einzelnen Kopien-Qubits.
  Die zehn Beziehungen schrumpfen so auf sechs verschiedene Funktionen (c⁴, c²s², s⁴, 2c²s², s², c²).
- **Folge für die Idee des Autors:** Damit eine Verschachtelung HS(8) = HS(7) ⊕ HS(6) ⊕ HS(6) Information trägt, die über ein einzelnes HS(7)
  hinausgeht, müssen die Generationszustände über die beiden Kopien-Bits verschränkt sein. Kohärente Produktzustände sind es nicht; die
  Normierung „HS(7) als Normierung der beiden HS(6)“ fällt bei ihnen auf das HS(7) selbst zurück. Das ist eine Aussage über diese Zustände,
  nicht über die Verschachtelung an sich.
- **Knapp daneben, nicht gezählt:** N1 schließt den Rest zu 88 % (−0,0015 statt −0,0124), liegt aber außerhalb der festgelegten Toleranz.
  N1 war zudem vom nachträglichen Befund aus H106 angeregt. Das wird nicht gedeutet.

## Einordnung
- Zusammen mit H106: Weder ein festes Singulettgewicht (¼), noch Normalen-Paare, noch das Gewicht eines Knotens der verschachtelten
  Aufteilung schließt den Rest 0,012376.
- Offen bleiben die zwei vom Autor genannten Wege: (i) verschränkte Generationszustände, bei denen die Verschachtelung echte Information trägt;
  (ii) Renormierung, also der Abgleich zwischen Polmassen und laufenden Massen.
- OP3 bleibt offen. H102 und H105 sind unberührt.
