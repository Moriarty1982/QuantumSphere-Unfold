# Ergebnis H224 (k438): Keine Wigner-Drehung aus den Frame-Boosts trifft φ; ein lockerer Treffer ohne Gewicht

**Datum:** 2026-11-28. **Vorab:** `Vorab_H224_Wigner_Drehung.md` (Commit 3ff1909, vor der Rechnung). **Urteil nach dem Wortlaut der Vorab: trägt teilweise**
(kein strenger Treffer; ein lockerer Treffer bei Zufallserwartung 0,066, Poisson-Wahrscheinlichkeit 6 %). **In der Sache: kein Treffer, φ ist nicht als Wigner-Drehung
hergeleitet.** **Werkzeuge:** Python (`k438_test_h224.py` → `k438_out.txt`; Formel und Matrix-Komposition, Abweichung 1,8·10⁻¹⁵), Wolfram unabhängig aus der
Komposition von 4×4-Boostmatrizen (`k438b_gegenprobe.wl` → `k438b_out.txt`); alle 48 Werte gleich. Blind (Kandidatenliste vorab vollständig). Qiskit nicht einschlägig.

## Frage
Der gemeinsame Versatz beider Lepton-Sektoren ist eine dimensionslose Drehung φ (H221). Eine solche Drehung entsteht von selbst, wenn zwei nicht kollineare Boosts
hintereinander wirken (Wigner-Drehung). Liefert eine der vorab festgelegten Kombinationen aus den Frame-Rapiditäten ε = artanh β_sym, 2ε = arcosh γ_L und den
Rahmenwinkeln π/2, π/4, 2π/3, π/3 (geteilt durch 1, 2, 3, 6) den Wert φ = 0,0395773?

## Ergebnis
| Größe | Wert |
|---|---|
| Kandidaten | 48 (3 Rapiditätspaare × 4 Winkel × 4 Teiler), Bereich 0,0198 bis 0,5973 |
| strenge Treffer (3σ unter J, σ = 7,8·10⁻⁷) | **0** |
| nächster Kandidat | ω(ε, ε, π/4)/3 = 0,0396695, relativ +0,23 %, **+118σ** unter J; mit freiem a (σ 6,3·10⁻⁶) +15σ |
| lockere Treffer (< 1 %) | 1 (derselbe); Zufallserwartung 0,066, P(≥ 1) = 0,064 |
| innerhalb 2σ von x_ν (nur Bericht) | 2 |

## Lesart
- **φ ist keine Wigner-Drehung dieser Frame-Boosts.** Der nächste Kandidat liegt 0,23 % daneben; bei der Genauigkeit von x unter J sind das 118σ. Auch mit freiem a
  (Polmassen ohne J) bleibt es 15σ.
- **Der lockere Treffer hat kein Gewicht.** Ein Treffer innerhalb 1 % bei 48 Kandidaten kommt in 6 % der Fälle zufällig vor. Er fällt auf die „Achteldrehung“
  (π/4) mit dem symmetrischen Frame-Versatz ε auf beiden Seiten, geteilt durch 3; die Teilung durch 3 ist nicht begründet. Nach dem Wortlaut der Vorab
  („über der Zufallserwartung“) heißt das „trägt teilweise“; es wird hier nicht als Befund gewertet.
- **Bilanz der Wertsuchen für φ:** H151d, H158d, H167d1, CT-002 (γ_M/6, 2,2σ mit freiem a, rund 15σ unter J), op3-Scans und jetzt H224: kein Treffer, der die
  Genauigkeit von x unter J erreicht. Der Wert von φ bleibt die eine gemessene Zahl des Lepton-Bildes.

## Hergeleitet, gesetzt, nachträglich
- **Gerechnet:** 48 Wigner-Winkel, unabhängig über Formel und Matrix-Komposition.
- **Gesetzt:** Zuordnung der Boost-Richtungen zu Rahmenwinkeln; Rapiditäten ε, 2ε aus β_sym (Zählpostulat r67); Teiler 1, 2, 3, 6.
- **Nachträglich:** keine weitere Kombination geprüft (keine Nachsuche, um den Blick nicht zu verbreitern).

## Grenzen
Welcher Vorgang zwei Frame-Boosts hintereinanderschaltet, ist nicht hergeleitet; andere Rapiditäten (etwa aus dem Lichtpunkt P) und andere Winkel sind nicht geprüft.
β_sym selbst ist ein Postulat (OP1). Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H224_Wigner_Drehung.md`, `k438_test_h224.py`/`k438_out.txt`, `k438b_gegenprobe.wl`/`k438b_out.txt`.

Vergeben: H224, k438. Nächste frei: H225, k439 (vor Vergabe gegen `main` prüfen).
