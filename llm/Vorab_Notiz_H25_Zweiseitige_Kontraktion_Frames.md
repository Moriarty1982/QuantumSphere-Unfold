# Vorab-Notiz H25: Die zweiseitige Kontraktion über mehrere Frames, und woher eine schwache SU(2) kommen kann

Festgelegt am 2026-10-23, **vor** der Rechnung. Autorhinweis (2026-10-23): Die neue Kontraktion
(`def:two-sided-admissible-contractions`) ist noch nie benutzt oder getestet worden; es wird nicht erwartet, dass sie sofort
funktioniert. Bezug: `def:two-sided-structural-tensor-interface` (vordere Indizes = Frame/Readout, hintere = Struktur), die vier
Kontraktionsregeln (1 klassisch oben–unten unverändert; 2 aktiv–aktiv nur über G_{αβ}; 3 passiv–passiv nur über G^{αβ}; 4 Selektor
χ_mn), Konvention F (T-Frame = Bild unter z ↦ iz), K77.8/K80 (T, R, J_B = R ∘ T auf dem ℂ-Faktor), H22/H23 (Triality-Algebra 𝔤),
Bestandsaufnahme Test 3 (Chiralität, schwache SU(2)).

## Rahmen (Modellwahl, offen gelegt)

- **Vorderseite:** der ℂ-Faktor der Dixon-Ablage. Ein aktiver Vektor X^α hat komplexe Komponenten, ein passiver ω_α ebenso.
  Frame-Abbildungen: R (linear, X ↦ iX, kontragredient ω ↦ −iω), T (antilinear, X ↦ X̄, ω ↦ ω̄), J_B = R ∘ T.
- **Rückseite:** reelle Struktur (𝕆, ℍ von rechts); Strukturabbildungen wirken nur auf α.
- Klassische Kontraktion (Regel 1): ω_α X^α, ℂ-bilinear. Aktiv–aktiv (Regel 2): q(X) = G_{αβ} X^α X^β mit reellem symmetrischem G,
  ℂ-bilinear; zum Vergleich die hermitesche Form h(X) = G_{αβ} X̄^α X^β.
- W = ℂ ⊗ ℍ ⊗ 𝕆 (reell 64-dim.); vorne: D₄ auf ℂ und Linksmultiplikation L_q mit Einheitsquaternionen; hinten: Rechtsmultiplikation R_q
  auf ℍ und Stab(e₇) = SU(3)_c auf 𝕆.

## Hypothesen

- **H25a (Seiten getrennt, Kontrolle):** Auf W vertauschen alle vorderen Abbildungen (D₄, L_q) mit allen hinteren (R_q, 𝔰𝔲(3)_c).
- **H25b (Regel 1 über Frames):** ω_α X^α ist invariant unter R und wird unter T und J_B komplex konjugiert. Frame-invariant ist die
  klassische Kontraktion also nur für reelle Readouts (bzw. ihren Realteil).
- **H25c (Regel 2 über Frames):** Die ℂ-bilineare Form q geht unter R in −q, unter T in q̄, unter J_B in −q̄ über; die hermitesche Form h
  ist unter allen acht Elementen von D₄ invariant. Lesart: Die bilineare aktiv–aktiv-Kontraktion trägt beim Übergang M → T das
  tachyonische Vorzeichen (m² ↦ −m²), die hermitesche nicht.
- **H25d (Farbe und SU(2) in der Triality):** Der Zentralisator von 𝔰𝔲(3)_c in der Triality-Algebra 𝔤 ≅ 𝔰𝔬(8) hat Dimension 2 und ist
  abelsch. Es gibt also in 𝔤 kein 𝔰𝔲(2), das mit der Farbe vertauscht. Auf W dagegen bilden L_q und R_q zwei 𝔰𝔲(2), die mit 𝔰𝔲(3)_c und
  mit D₄ vertauschen.
- **H25e (Spinor-Plätze, Kontrolle):** Kein Element ≠ 0 von 𝔤 wirkt auf einem Spinor-Platz trivial und auf dem anderen nicht (folgt aus
  H22a). In der Lesart von r38 (Materie, Tachyon = Spinor-Plätze) kann keine Symmetrie von t nur auf der Materie wirken.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H25b, c bestätigt ⇒ Regel 1 („bleibt unverändert“) gilt über Frames nur bis auf Konjugation, Regel 2 nur bis auf Vorzeichen und
  Konjugation. Die Notation ist dann nicht frame-invariant, sondern frame-kovariant, und muss festlegen, ob Readouts reell sind und
  ob Vergleiche bilinear oder hermitesch sind. Das wäre ein **Befund über die Notation**, kein Fehler der Rechnung: Bisher wurde sie nur
  in einem Frame benutzt.
- H25d bestätigt ⇒ Eine mit der Farbe vertauschende schwache SU(2) kommt nicht aus der Triality auf 𝕆³, sondern muss aus dem ℍ-Faktor
  kommen, also aus einer der beiden Seiten von ℍ. Das verbindet die Chiralitätsfrage mit der Zweiseitigkeit. Dann bleibt aber der
  Konflikt aus K79.2: Links ist auch die Lorentz-Drehung, rechts die Generationen-ℤ₃ (r33).

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
