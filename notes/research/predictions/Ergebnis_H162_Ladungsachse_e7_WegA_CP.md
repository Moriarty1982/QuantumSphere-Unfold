# Ergebnis H162: Weg A und das relative CP-Vorzeichen hängen nicht an der Achse e₈; mit e₇ setzt die Ladung die oktonionische Ladung einer Kopie fort

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H162_Ladungsachse_e7_WegA_CP.md` (Commit 080d9a9, vor der Rechnung; weitgehend nicht blind: a, b, d waren
von Hand begründet, c und e offen). Skripte `notes/research/hilbert_shift_felder_2026_11_24/ladungsachse_h162/k360_test_h162.py` (Ausgabe `k360_out.txt`),
`k360b_exakt.wl` (`k360b_out.txt`). Status: H162a, b, c, d bestätigt; e Erkundung.**

Werkzeuge: Python (numpy) auf der Infrastruktur von r13/r14 und k252. Wolfram Language exakt und unabhängig aufgebaut (Cayley–Dickson-Rekursion,
g₂ und su(3)_c als exakte Nullräume) für a, b und d. Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich. Kein Guard berührt.

Offengelegt: Der erste Wolfram-Lauf war ungültig (Inverse einer singulären Matrix beim Projektor P₃, Namenskonflikt bei der symbolischen Achse)
und wurde mit PseudoInverse und eigenen Symbolnamen wiederholt. Teil c ist nur numerisch gerechnet.

## Aufbau
Q_u = P₀(½ − (i/2)L_u)P₀ + ⅔P₃ + ⅓P₃̄ für eine Einheit u ∈ span(e₇, e₈, e₁₅); Q_* = Q_{e8} (r13.1, Platzhalter CT-003).

## Kontrollen
| Kontrolle | Messwert | |
|---|---|---|
| Q_{e8} = Q_* aus `fs.setup()` | Abweichung 0 | erfüllt |
| Ränge P₀, P₃, P₃̄ | 4, 6, 6; P₃ vertauscht mit su(3)_c (Wolfram exakt) | erfüllt |
| k252 mit u = e₈ reproduziert | 24 + 24 Zuordnungen, det −1 / +1 | erfüllt |

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| **H162a** | Q_{e7}: Spektrum 0 (2), ⅓ (6), ⅔ (6), 1 (2); char. Polynom x²(x−1)²(3x−1)⁶(3x−2)⁶/3¹² exakt; [Q, su(3)_c] = 0 und Q̄ = 1 − Q exakt | Reste < 10⁻¹⁰ | **bestätigt** (nicht blind) |
| **H162b** | [R_x, Q_{e7}] = 0 exakt; [R_e7, R_e8] = −2R_e15 (Leptonen), +2R_e15 (Quarks); Bargmann ¼ − i/4 gegen ¼ + i/4 exakt; jede Teilchenart ein Dublett (Casimir ¾); 200/200 Zufallsachsen | Reste < 10⁻¹⁰ | **bestätigt** (nicht blind) |
| **H162c** | Mit Q_{e7}: Verflechter-Raum Dimension 20; 24 Zuordnungen vollen Rangs je Sektor, det −1 (Leptonen), +1 (Quarks); ebenso für die zwei gedrehten Achsen | 24/24 mit diesen Vorzeichen | **bestätigt** |
| **H162d** | Q_{e7} lässt ℂ⊗𝕆₀ invariant (Leck 0) und ist dort gleich Q₈ (Abweichung 0, exakt). Q_*: Leck² = ½. Q_{e7} auf 𝕆₁₂₀, 𝕆₂₄₀: Leck 0,612 (Leck² = 3/8). Jede der drei Kopienachsen leistet dasselbe für ihre Kopie | Rest < 10⁻¹⁰, Lecks > 10⁻³ | **bestätigt** (nicht blind) |
| H162e (Erkundung) | ‖[Q_{e7}, ψ]‖ = √3; ψ bildet den Kern N₇ nicht in sich ab (0 für e₈). Mit dem Ersatzzyklus exp(−(π/3)R_u) und einer Hurwitz-Einheit als Bezug: ρ² = ½, Phase π/4 für u = e₇ und u = e₈; für die gedrehten Kopienachsen ρ² = 0,283 oder 0,717 | – | – |

## Warum es so ausgeht
- H_n = span(1, e₇, e₈, e₁₅) ist assoziativ. Deshalb ist L_u² = −1 auf H_n für **jede** Einheit u (Wolfram symbolisch), und Q_u hat dort die
  Eigenwerte 0 und 1 je zweimal. Der farbige Teil von Q_u hängt nicht von u ab.
- Rechtsmultiplikationen vertauschen auf H_n mit L_u (Assoziativität) und auf dem farbigen Teil mit P₃ (sie vertauschen mit su(3)_c).
  Die Familien-su(2) und ihre entgegengesetzte Orientierung auf Leptonen und Quarks sind eine Eigenschaft der Sedenionen-Rechtsmultiplikation
  und der Farbe. Die Ladungsachse geht nicht ein.
- Was e₈ auszeichnet, ist allein [Q, ψ] = 0. Was e₇ (und jede Kopienachse) auszeichnet, ist die Fortsetzung der oktonionischen Ladung Q₈ ihrer Kopie.
  Beides zugleich leistet keine Achse.

## Lesart
- **Weg A (zwei Generationen, r13.3), die Familien-su(2) (r13.4) und H125 Stufe A (r59.6) gelten für jede Achse u in Im H_n.** Der Status
  „bedingt unter CT-003“ lässt sich abschwächen zu „bedingt unter der Form Q_u der Ladung“. H130 gefährdet diese drei Aussagen nicht.
- **Unter e₇ geht verloren:** ψ ist keine Symmetrie der Ladung mehr. Die Aussagen, die ψ auf dem neutralen Kern benutzen (r13.1: ψ = diag(1, ω) auf N;
  r13.2: Bahn unter ψ mit ρ² = ½; r13.3: ψ als Phase je Generation), gelten für e₇ nicht in dieser Form. Der Ersatzzyklus gibt für e₇ dieselben
  Zahlen, ist aber eine gesetzte Rechtsdrehung und kein Automorphismus. Wie in r13.2 ist das eine Konstruktion, keine Herleitung von Koide.
- **Unter e₇ kommt dazu:** Q_{e7} ist auf der Kopie 𝕆₀ genau die Ladung einer vollständigen Generation (k85) und gibt auf ganz ℂ⊗𝕊 zwei.
  Die anderen beiden Kopien passen nicht dazu (H140: keine gemeinsame Ladung).
- **Unverändert:** Es sind zwei Generationen, nicht drei. Die Wahl der Achse bleibt eine Setzung, jetzt zwischen zwei benannten Kriterien
  (ψ-fest oder kopientreu). H125 Stufe B (sin δ_PMNS < 0) bleibt offen bis 2035 und hängt weiter an der Setzung S1. Keine Vorhersage gegen Messdaten.
  OP3 und OP4 bleiben offen.

## Frames
Algebra auf dem Träger, frame-unabhängig; kein Vergleich mit Daten. Die Tachyon-Abbildung z ↦ iz und die Zeitumkehr z ↦ z̄ kommen nur über
Q̄ = 1 − Q vor (komplexe Konjugation der Ladung).

## Nicht gerechnet
- Nachgetragen in der Erkundung k361 (`ladungsachse_h162/README.md`): die Ladungen der Form ½ − (i/2)R_u. Das relative Vorzeichen hängt an der Setzung „dieselbe Seite der Multiplikation für beide Sektoren“.
- Ob r14.4 (Abbildung nach ℂ⊗ℍ⊗𝕆) über Teil c hinaus alle Aussagen behält.
- Eine Runde im Companion: nachgetragen als v4.10.0-r65 (`notes/research/v4_10_0_r65_ladungsachse/`).
