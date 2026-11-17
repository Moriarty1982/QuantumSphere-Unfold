# OP1: Rückwärtssuche nach den Arbeiten vom 16./17.11. und eine offene Voraussetzung (Erkundung, keine Rechnung)

17. November 2026. Auftrag des Autors: „weiter“ nach PR #172. Nach AGENTS.md („nach zwei Varianten mit derselben offenen Voraussetzung prüfen, ob eine
Rückwärtssuche günstiger ist“) wird der Stand von OP1 hier als Rückwärtssuche festgehalten. Keine neue Rechnung, keine H-Nummer.

## Ziel
Eine Begründung, warum der Frame M jeden Spin mit Gewicht 2 zählt; gleichwertig (PR #172) eine Begründung für eine der Gestalten von
γ_L = 1,8647: Moran-Dimension, Frequenzverhältnis ω_M/ω_T, Registerbreite b_M = 1/γ_L, Lorentz-Faktor von (M, M̄).

## Notwendige Bedingungen (gesammelt)

| Nr. | Bedingung | Quelle |
|---|---|---|
| N1 | Die Auslesung von M ist eine Flächenauslesung (reichste ganze Kopienzahl in ℝ²) | PR #170, #171 |
| N2 | Sie zählt reine Stränge mit unbekanntem Port (ein Bit je Punktierung), nicht das M-Register | `op1_entropy_count_2026_11_17/`, PR #171 |
| N3 | Ihre Registerbreite b_M ≠ 0; liest man b als Helizitätsbreite (s. u.), braucht das relative Phasen, also eine Frequenz | `op1_flux_lines_2026_11_17/` |
| N4 | Die Frequenz ist γ_L · ln 2 · T_H; keine Ruhefrequenz eines Schwarzschild-Horizonts (16 Kandidaten) | PR #168 |
| N5 | Sie entsteht nicht durch einen reellen Boost aus T (Boost erhält s; T liegt um iπ/2 verschoben) | PR #172 |
| N6 | Ein Gleichgewichtshorizont liest wie P (Raumstufe), nicht wie M | PR #171 |

## Ausgeschlossen
Trägervarianten (H106–H111), topologische Festlegung (r28.6), (S1′) als masselose Querung am isolierten Horizont (PR #167), Quasinormal-Frequenz bei
Spektrum √(j(j+1)) (PR #168), Schwarzschild-Ruhefrequenzen (PR #168), Boost aus T (PR #172), das Helizitätsverhältnis des Koide-Zustands als Breite von M
(r16.9(d): |s₋|/|s₊| gegen β² und 23 weitere Kandidaten, kein Treffer).

## Eine offene Voraussetzung, die alles Weitere entscheidet
Die Registerbreite b von Konvention F lässt zwei Lesarten zu, die numerisch beide 1/γ_L geben:
- **(H) Helizitätsbreite:** b ist die Komponente des M/T-Dubletts entlang der Port-Achse; die Ports sind die Pole der Helizitätsachse von χ
  (r16.2(b), `op1_u1_check_2026_11_16/`). Dann ist b eine **Eigenschaft des Feldzustands**, Lorentz-invariant, für reelle Felder 0, und die Breite von
  M verlangt eine Frequenz (N3). Diese Lesart trägt die Kette von PR #171.
- **(B) Beobachterlesart:** b = r = |s|/(2u), das Verhältnis von Invariante zu Energiedichte, das ein Beobachter misst; ein Beobachter mit Rapidität η
  relativ zum flussfreien Profil sieht r = 1/cosh 2η = 1/γ_L (r11.5(b), PR #172). Dann ist M eine **Eigenschaft des Beobachters**, auch statische Felder
  erreichen b_M, und N3 entfällt; die Frequenzfrage stellt sich nicht, dafür die Frage, warum der Beobachter M sich gerade mit β_sym bewegt.

Der Bestand definiert M über den Kompensator-Port und spricht damit für (H); er nennt M, T, P aber durchgehend „Frames“, also Beobachter, was für (B)
spricht. Die beiden Lesarten führen OP1 in verschiedene Richtungen: (H) sucht eine zeitharmonische Struktur der Auslesung, (B) eine ausgezeichnete
Geschwindigkeit. Welche gemeint ist, ist eine Festlegung des Autors, keine Rechenfrage.

## Was übrig bleibt
- Unter (H): ein Mechanismus, der der Flächenauslesung relative Phasen mit |s₋|/|s₊| = β² gibt. Kein Kandidat im Bestand.
- Unter (B): ein Grund für die Geschwindigkeit β_sym des Beobachters M relativ zum flussfreien Profil. Das ist die alte Frage nach β_sym (T6, H48).
- In beiden: das Moran-Prinzip (größte ganze Kopienzahl auf der Fläche) legt die Zahl fest, ohne den Mechanismus zu geben.
- Ein blinder Test ist auf keinem der Wege in Sicht. OP1 offen.
