# Methoden-Notiz: Lesart (b), ein Medium unter der Frame-Abbildung J_B (Erkundung, vor der Rechnung festgelegt)

23. November 2026. Auftrag des Autors: „Lesart (b) prüfen“ (zur Idee „das Medium funktioniert nur für den Photon-Frame und muss sich in den
anderen Frames verbiegen“). Keine H-Nummer.
**Nicht blind:** Eine Vorüberlegung legt fest, dass J_B lichtartige Richtungen entlang seiner Achse nur mit einer Phase ∓i versieht, sodass
Strahl-Anteile eines Mediums das Vorzeichen wechseln, und dass ein unter J_B invarianter Ausbreitungstensor im (t, e)-Block proportional zur
Metrik ist. Die Rechnung prüft das exakt und bestimmt die Folgen für die Kegelgrenze.

## Vorwissen geprüft
- Konvention F, OP1 Lesart B: T ist das J_B-Bild von M; J_B ist der komplexe Boost mit Rapidität η + iπ/2 (W1 + Holst, `wiki/Forschungsstand.md`:
  „lassen Boosts, Drehungen und der komplexe Boost η + iπ/2 die Wirkung unverändert“); das Vorzeichen von Re s trennt M und T.
- H79 (r84): Das Tachyonbild einer Wirkung ist der komplexe Boost mit Rapidität iπ auf Spinor und Argument; das Bild ist −L_M, isotrop und
  stabil. Das ist eine andere Abbildung als J_B (iπ/2) und wird nur als Kontrolle benutzt.
- H78 (r84): Die frühere, unvollständige Abbildung gab T quer zur M–T-Achse einen weiteren Kegel; durch H79 ersetzt.
- H120 (r50): Zwei lichtartige Gegenströme bilden nahe ihrem Gleichgewicht ein gesundes Medium (Kegelgrenze 0,803 bei κa = κb = 0,3);
  Mindestverlangsamung ε ≥ √(7g_m²/6); im Vakuum durch Laborgrenzen ausgeschlossen. Diese Schranke gilt in M weiter.
- r47/r49: Kegelgrenze; jede lichtschnelle Richtung verletzt sie, weil der massive Kanal in jeder Richtung koppelt.

## Werkzeug
Python mit sympy (exakte Algebra) und numpy (Eigenwerte); Wolfram war in dieser Sitzung mehrfach nicht erreichbar und ist hier nicht nötig.
Qiskit nicht geeignet. Skript `jb_medium.py`, Ausgabe `run/jb_medium.txt`.

## Rechnung
- **E1 Algebra:** J_B = komplexer Boost mit Rapidität iπ/2 entlang der M–T-Achse e = x. Erhält er η? Eigenrichtungen und Eigenwerte; Bild eines
  reellen zeitartigen Vektors.
- **E2 invariante Medien:** alle symmetrischen Tensoren S^{μν} mit J S Jᵀ = S (invariant) und J S Jᵀ = −S (Vorzeichenwechsel). Geschwindigkeit
  entlang e für die invarianten.
- **E3 Kegelgrenze:** (i) ein Medium aus zwei Gegenströmen entlang e in M (κa = κb = 0,3) und sein J_B-Bild in T; (ii) ein J_B-invariantes
  Medium mit Verlangsamung quer zu e; jeweils größtes Geschwindigkeitsquadrat wie r47 (Z = 1, g_0² = g_m² = 3/100, universell), über die
  Richtungen θ zu e (41 Werte) und α ∈ [0, 1] (21 Werte, konservativ). Ist das Bild in T reell?
- **E4 Kontrolle (H79, iπ):** dieselben Medien unter dem Boost mit Rapidität iπ.

## Raster (vorab)
- **trägt:** Es gibt ein Medium, das in M und in seinem J_B-Bild in T reell ist und dort jeweils die Kegelgrenze hält.
- **trägt teilweise:** Ein solches Paar hält die Grenze in einem der beiden Frames, oder nur für eine Teilmenge der Richtungen.
- **trägt nicht:** Für kein Medium halten M und T die Grenze zugleich.

Frames: M und T im Sinn von Konvention F; J_B (iπ/2) wird nicht mit dem Tachyonbild der Wirkung (iπ, H79) und nicht mit der Zeitumkehr
verwechselt. OP5 bleibt offen.
