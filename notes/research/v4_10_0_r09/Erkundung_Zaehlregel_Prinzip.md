# Erkundung: Ein Prinzip für die Zählregel je Frame (OP1)

**7. November 2026. Status: Erkundung, nicht blind (das Ziel, DL/M für M und ABCK für T, ist bekannt), ohne Kriterium.** Begleitet H98.

## Ausgangspunkt
r63 hat zwei Bausteine geliefert, beide nach Autorhinweisen und nach H47:
- r63.2 (exakt): In |j, m⟩ sättigen genau die Zustände m = ±j die Robertson-Schranke ΔJ_x ΔJ_y ≥ ½|m|; bei j = ½ alle.
- r63.3 (exakt): Ein Tachyon, das Energie verliert, läuft gegen einen einzigen Boden E → 0 (bei festem Invariant); der Tachyon-Frame von
  Konvention F ist der Boden des Spiegel-Frames (r63.4).

## Prinzip P (Lesart)
Ein Frame zählt an einem Horizont genau die Zustände, die
1. **die Unschärfe sättigen** (P1), und
2. **mit seiner Energiebedingung verträglich sind** (P2): M hat Energien über der Ruhe, alle Anregungsstufen sind zugänglich; T relaxiert zum Boden
   und erreicht nur die kleinste von null verschiedene Anregung.

Brücke zwischen Energie und Spin: das lokale erste Gesetz isolierter Horizonte (Frodden–Ghosh–Perez 2011, Literatur): Für einen Beobachter in festem
Abstand ℓ ist die Energie E = A/(8πGℓ), also monoton in der Fläche. Die kleinste von null verschiedene Fläche eines Durchstoßpunkts ist a(½) = √3/2.

## Was P im Regelraum S von H98 auswählt (analytisch)
- P1 schließt das Gewicht 2j + 1 aus, außer bei j = ½, wo alle Zustände sättigen. Übrig: Gewicht 2 auf jedem Spinbereich.
- P2 für M: alle Stufen zugänglich, also alle j: **A, g = 2 (DL/M)**. Die Bereiche H und I bräuchten eine zusätzliche Auswahlregel, die P nicht hat.
- P2 für T: nur die kleinste Fläche, also nur j = ½: **S½ (ABCK)**. S1 hat größere Fläche.
- P wählt also im Raum S genau das Paar, das H98 als einziges mit allen drei Daten bestätigt.

## Bilanz in QAM-Begriffen
Die Eingabe „countrule“ (Z1, Kategorie R) wird zerlegt in:
| Baustein | Status | Kat. |
|---|---|---|
| Robertson-Sättigung von m = ±j (r63.2) | bewiesen | – |
| Tachyon-Boden (r63.3) | bewiesen (Kinematik) | – |
| lokales erstes Gesetz E ∝ A | Literatur | L |
| P1: ein Frame zählt nur sättigende Zustände | Lesart | A |
| P2: M alle Stufen, T nur die kleinste | Lesart | A |

Damit ist Z1 nicht hergeleitet, aber auf zwei Lesarten zurückgeführt, die je einen eigenen Grund haben (Unschärfe, Energie) und nicht auf die Daten
zugeschnitten sind; beide stammen aber aus Autorhinweisen nach H47 und sind deshalb nicht blind.

## Grenzen
- P1 ist eine Umdeutung: Meissner zählt die Projektionen m, nicht „sättigende Zustände“ (r68 Punkt 4). Die SU(2)-Behandlung der Literatur verletzt P1.
- P2 vermischt zwei Energiebegriffe: die Energie des Tachyon-Frames (r63.3, Kinematik eines Teilchens) und die Horizontenergie eines Beobachters
  (erstes Gesetz). Dass der T-Beobachter am Horizont nur die kleinste Anregung „sieht“, weil er selbst am Boden sitzt, ist die eigentliche
  ungeprüfte Brücke.
- Warum der Boden im Spiegel-Frame liegt (r63.4), bleibt offen.

## Mögliche nächste Schritte
1. Die Brücke in P2 präzisieren: Welche Horizontanregungen kann ein Beobachter mit Rapidität −η + iπ/2 (Boden) auflösen? Das ist eine Frage an
   die Boost-Energie am Rindler-Horizont (Dorau–Much, r06): Der Modularfluss ist der Boost, die Energie ist die Boost-Energie.
2. Eine echte, blinde Folgerung von P suchen, die nicht γ_L ist (etwa für einen dritten Frame oder eine andere Horizontgröße), und vorab festlegen.
