# Lesart (b): Ein Medium unter der Frame-Abbildung J_B kippt von Verengung in Weitung; trägt nicht (Erkundung, nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** J_B, der komplexe Boost mit Rapidität iπ/2 entlang der M–T-Achse, hält genau die lichtartigen Richtungen entlang
der Achse (bis auf Phasen ∓i) und die Querebene fest; ein Medium aus diesen Richtungen bekommt dadurch den Faktor −1, und was in M den
Lichtkegel verengt, weitet ihn in T über die Lichtgeschwindigkeit hinaus. Unter J_B unverändert sind nur Ausbreitungstensoren, die entlang der
Achse lichtschnell bleiben. **Nach dem vorab festgelegten Raster: trägt nicht.** Die Kontrolle mit dem Tachyonbild der Wirkung (iπ, H79) trägt
das Medium dagegen unverändert nach T.

Auftrag des Autors: „Lesart (b) prüfen“. Verfahren vorab: `Methoden_Notiz.md` (Commit 20c34729). Nicht blind. Skript `jb_medium.py` (Python,
sympy, numpy), Ausgabe `run/jb_medium.txt`. Wolfram war mehrfach nicht erreichbar und ist hier nicht nötig; Qiskit nicht geeignet. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| E1 | J_B = (t, x) ↦ (−ix, −it), y, z fest; erhält η. Eigenrichtungen: (1, 1, 0, 0) mit −i, (−1, 1, 0, 0) mit +i, Querebene mit 1. Ein reeller zeitartiger Vektor wird i-mal ein raumartiger (Norm bleibt 1). |
| E2 | Invariant unter J_B: im (t, x)-Block proportional zur Metrik, Querblock beliebig; Geschwindigkeit entlang e daher genau 1. Vorzeichenwechsel unter J_B: (t, x)-Block [[s, q], [q, s]], sonst null; dazu gehören die Strahl-Anteile l_±l_±. |
| E3 (i) | Gegenströme entlang e (κa = κb = 0,3): in M G = diag(1,6; −0,4; −1; −1), r zwischen 0,25 und 0,625, Kegelgrenze 0,803; J_B-Bild G_T = diag(0,4; −1,6; −1; −1), reell, r zwischen 2,5 und 4, Grenze 4,66. |
| E3 (ii) | J_B-invariantes Medium, quer verlangsamt (κ_t = 0,5): in M und T gleich, r zwischen 0,5 und 1, Grenze 1,1995 (entlang e lichtschnell). |
| E4 Kontrolle | Rapidität iπ (Tachyonbild der Wirkung, H79): (t, x) ↦ (−t, −x); das Gegenstrom-Medium bleibt gleich und hält die Grenze in beiden Frames (0,803). |

## Lesart
- Die Idee ist wörtlich erfüllt, aber mit dem falschen Vorzeichen: Die Strukturen des Photon-Frames sind die festen Richtungen von J_B, und das
  Medium „verbiegt“ sich beim Übergang M → T, und zwar von Verengung in Weitung. Ein Medium, das in M kausal ist, ist in T überlichtschnell.
- Nachträglich, als Lesart: T ist der Tachyon-Frame; dass dort Kegel weiter sind, passt zu seiner Rolle. Das Raster verlangte aber die
  Kegelgrenze in beiden Frames, und das Urteil bleibt. Zudem regelt nach H79 das Tachyonbild der Wirkung (iπ) die Dynamik in T, und unter iπ
  bleibt das Medium gesund. J_B gehört zur Auslese des Registers (Konvention F), nicht zur Dynamik; die „Verbiegung“ durch J_B betrifft damit die
  Beschreibung in T, nicht die Ausbreitung.
- Die Vakuumschranke aus H120 (ε ≥ √(7g_m²/6), mit Laborgrenzen g_m² ≲ 8,6·10⁻²⁷) gilt in M unabhängig von dieser Lesart.
- OP5 bleibt offen; damit sind beide Lesarten der Idee geprüft.
