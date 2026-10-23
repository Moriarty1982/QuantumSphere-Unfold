# Ergebnis H25: Die zweiseitige Kontraktion ist über Frames kovariant, nicht invariant; die schwache SU(2) kommt nicht aus der Triality

Vorab-Notiz: `Vorab_Notiz_H25_Zweiseitige_Kontraktion_Frames.md`, Commit d1aba48 (2026-10-23 19:51 MESZ), vor der Rechnung.
Skript `k81_test_h25.py`, Ausgabe `k81_out.txt`. Kriterium unverändert; eine Nachkontrolle nach der Auswertung ist im Skript als solche
gekennzeichnet.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H25a Seiten getrennt | **bestätigt** (Kontrolle) | Vordere (D₄, L_q) und hintere Abbildungen (R_q, SU(3)_c) vertauschen auf ℂ⊗ℍ⊗𝕆 |
| H25b Regel 1 | **bestätigt** | ω_α X^α: invariant unter R, komplex konjugiert unter T und J_B |
| H25c Regel 2 | **bestätigt** | bilinear q: R ↦ −q, T ↦ q̄, J_B ↦ −q̄; hermitesch h: unter allen 8 Elementen von D₄ invariant |
| H25d Farbe und SU(2) | **bestätigt** | Zentralisator von 𝔰𝔲(3)_c in der Triality-Algebra: Dimension 2, abelsch. Auf W bilden L_q und R_q zwei 𝔰𝔲(2), die mit der Farbe und D₄ vertauschen |
| H25e Spinor-Plätze | **bestätigt** (Kontrolle) | Kein Element der Triality-Algebra wirkt nur auf einem Spinor-Platz |
| *Nachkontrolle* | — | Der Zentralisator der Farbe ist auf jedem Platz genau span(L_{e₇}, R_{e₇}), also die beiden Erzeuger, aus denen Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇} gebaut ist (H20d) |

## Einordnung

1. **Erste Benutzung über mehrere Frames: Die Regeln funktionieren, aber nicht so, wie sie im Text stehen.**
   - Regel 1 sagt „bleibt unverändert“. Über Frames gilt das nur für die Drehung R. Unter den antilinearen Frame-Abbildungen T und
     J_B wird das Ergebnis komplex konjugiert. Frame-invariant sind nur reelle Readouts.
   - Regel 2 (aktiv–aktiv über G) hängt davon ab, ob der Vergleich bilinear oder hermitesch ist. Der Text legt das nicht fest.
   - Die Notation ist damit **frame-kovariant, nicht frame-invariant**. Das ist ein Befund über die Notation, kein Rechenfehler. Sie
     wurde bisher nur in einem Frame benutzt.
2. **Das tachyonische Vorzeichen steckt in der Notation.** Der bilineare Vergleich q(X) = G X X wechselt beim M → T-Übergang
   z ↦ iz das Vorzeichen, q ↦ −q. Liest man q als Massenquadrat, ist das m² ↦ −m², also genau der Tachyon. Der hermitesche Vergleich
   sieht keinen Unterschied zwischen M und T. Die Wahl zwischen bilinear und hermitesch ist damit inhaltlich:
   - Bilinear unterscheidet die Frames.
   - Hermitesch macht sie ununterscheidbar.
3. **Die schwache SU(2) kommt nicht aus der Triality.** In Spin(8) vertauscht kein 𝔰𝔲(2) mit der Farbe; was vertauscht, ist nur ein
   zweidimensionaler abelscher Rest. Und dieser Rest ist genau span(L_{e₇}, R_{e₇}), die Bausteine der elektrischen Ladung (Nachkontrolle).
   - Die Triality-Ebene enthält also Farbe und Ladung, aber keine schwache Wechselwirkung.
   - Eine mit der Farbe vertauschende SU(2) gibt es erst im ℍ-Faktor, und zwar zwei: von links (Vorderseite) und von rechts
     (Rückseite).
4. **Chiralität und Zweiseitigkeit.** Die beiden SU(2) von ℍ sitzen auf den beiden Seiten der zweiseitigen Notation. „Die schwache
   SU(2) wirkt nur links“ wäre in dieser Lesart „die schwache SU(2) ist eine Seite“. Das ist eine Lesart, nicht gezeigt.
   - **Konflikt bleibt:** Links liegt auch die Lorentz-Drehung (K79.2), rechts die Generationen-ℤ₃ (r33). Der ℍ-Faktor bleibt
     überbelegt.
5. **Vorschlag zur Notation** (Autorentscheidung): Regel 1 und 2 um eine Frame-Klausel ergänzen.
   - Readouts sind reell, oder sie werden beim antilinearen Frame-Wechsel mitkonjugiert.
   - Für jeden Vergleich G wird angegeben, ob er bilinear (frame-unterscheidend) oder hermitesch (frame-blind) ist.
