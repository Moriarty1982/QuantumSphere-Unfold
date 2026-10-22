# Vorab-Notiz H14: Tachyon-Kegelwinkel und Weinberg-Winkel

Festgelegt am 2026-10-21, **vor** der Berechnung des Vergleichs mit Messwerten. Bezug: v4.9.0-r04 (Zustandsscheibe,
doppelter Winkel), v4.9.0-r05.1 (Portgewichtung), v4.9.0-r06.2 (Kegel), v4.9.0-r06.4 (elektroschwache Massenmatrix).

## Rahmen

r06.2: Eine Tachyon-Trefferkette mit v = 1/β_sym erzeugt einen Lichtkegel mit cos ϑ_c = β_sym, ϑ_c = 56,68°. Für
diesen Kegel gibt es **keine Messung**. Er wird hier nicht mit Beobachtungen verglichen. Eine Suche nach einem solchen
Kegel bräuchte eine eigene Notiz.

r06.4: Die elektroschwache Massenmatrix auf (W³, B) ist eine Portgewichtung mit masselosem Photonport. Bei θ_W = 45°
wäre dieser Port genau der Kompensator. Beim tatsächlichen θ_W ist er ein um θ_W − 45° gedrehter Kompensator. Nach
r04.2(b) dreht eine Dublettdrehung um α den Zustand um 2α.

H14 prüft eine einzige, fest gewählte Beziehung zwischen ϑ_c und θ_W.

## Hypothese (V)

**H14:** ϑ_c = 2 θ_W. Gleichwertig:

    cos 2θ_W = β_sym      ⇔      sin²θ_W = (1 − β_sym)/2.

**Begründung, schwach:** Der Kegel ist die Aberration der Senkrechten um β_sym (r06.2c). Die Lage des Photonports in der
Zustandsscheibe ist um 2θ_W − 90° gegen den Kompensator gedreht (r04.2b, r06.4). Die Hypothese setzt beide Winkel
gleich. Hergeleitet ist das nicht. Die Dubletts sind verschieden: (E, B) in r04, (W³, B) in r06.4.

## Eingaben (verbindlich)

- **β_sym** = tanh(½ arcosh γ_L), mit γ_L = γ_BI/γ_string, γ_BI = 0,2375 und γ_string = ln 2/(π√3), wie in
  `llm/k37_gl_umrechnungen.py`. Zum Vergleich wird auch der Dokumentwert 1/1,820 berichtet; entschieden wird mit dem
  ersten Wert.
- **θ_W, primär (entscheidend):** On-shell-Definition sin²θ_W = 1 − m_W²/m_Z². Begründung: In r06.4 sind die Portgewichte
  die Massen, und auf Baumgraphen-Niveau gilt cos θ_W = m_W/m_Z.
- **θ_W, sekundär (nur berichtet):** MS-bar-Wert ŝ²_Z(M_Z) und effektiver leptonischer Wert sin²θ_eff.
- **Daten:** Review of Particle Physics der PDG (aktuelle Ausgabe, Summary Tables / Electroweak Review). Verwendet werden
  der Weltmittelwert von m_W, m_Z und ŝ²_Z mit ihren angegebenen Unsicherheiten. Die Werte werden erst nach dem Commit
  dieser Notiz abgerufen und mit Quelle und Abrufdatum im Ergebnis vermerkt.

## Offenlegung (vor dem Festschreiben bekannt)

1. **Kegelwinkel bekannt.** ϑ_c = 56,68° und β_sym = 0,5493 stehen seit r06 fest.
2. **Ungefähre Messwerte bekannt, Vergleich nicht blind.** Aus dem Gedächtnis waren vor dieser Notiz bekannt:
   sin²θ_W ≈ 0,231 (MS-bar) und ≈ 0,223 (on-shell). Beim Entwurf der Notiz ist aufgefallen, dass 2θ_W ≈ 57,5° nahe bei
   56,7° liegt. Überschlagen ergab sich cos 2θ_W ≈ 0,554 (on-shell) und ≈ 0,538 (MS-bar), gegen β_sym = 0,549. **Die
   Hypothese wurde erst nach dieser Beobachtung formuliert.** Die Wahl der On-shell-Definition als primär ist durch r06.4
   begründet, fiel aber nach diesem Überschlag.
3. **Erwarteter Ausgang.** Der Überschlag lässt für die On-shell-Form eine Abweichung in sin²θ_W von etwa 0,002
   erwarten. Das wäre ein Vielfaches der experimentellen Unsicherheit. Erwartet wird also: als exakte Beziehung
   widerlegt, als Baumgraphen-Beziehung innerhalb der Schemabreite.
4. **Eine Beziehung, keine Suche.** Andere Beziehungen (etwa ϑ_c = θ_W + 45°, Halbwinkel, Komplementwinkel, andere
   Potenzen von β_sym) werden **nicht** gerechnet und nicht berichtet.
5. **Look-elsewhere.** Selbst ein Treffer wäre kein Beleg. Die Hypothese ist nachträglich, und es gibt mehrere ähnlich
   einfache Beziehungen, die man hätte wählen können. Ein Treffer begründet höchstens einen echten Test mit einer vorher
   unbekannten Größe.

## Verfahren (verbindlich)

Skript `llm/k43_test_h14.py`, erst nach dem Commit dieser Notiz:
1. β_sym aus den Eingaben; Vorhersage s²_pred = (1 − β_sym)/2.
2. On-shell-Wert s²_OS = 1 − m_W²/m_Z² mit Fehlerfortpflanzung σ_exp aus σ(m_W) und σ(m_Z).
3. Δ = s²_pred − s²_OS; z = Δ/σ_exp.
4. Schemabreite: Band B = [min(s²_OS, ŝ²_Z), max(s²_OS, ŝ²_Z)], an beiden Enden um 3σ der jeweiligen Größe erweitert.
5. Berichten: β_sym (beide Werte), s²_pred, s²_OS, ŝ²_Z, sin²θ_eff, z, Lage von s²_pred relativ zu B, Winkel ϑ_c und 2θ_W
   für beide Definitionen.
6. Look-elsewhere-Abschätzung: Anteil der Breite von B an einem plausiblen Wertebereich von sin²θ_W, nämlich [0, 0,5].
   Das ist die Trefferwahrscheinlichkeit einer beliebigen einfachen Beziehung. Für fünf gleich einfache Kandidaten wird
   sie hochgerechnet.

## Entscheidungskriterium (verbindlich)

- **(A) Exakte Beziehung, On-shell:** |z| < 2 verträglich, 2 ≤ |z| < 3 Spannung, |z| ≥ 3 **widerlegt**.
- **(B) Baumgraphen-Beziehung:** s²_pred liegt in B: **nicht entscheidbar auf Baumgraphen-Niveau**. Außerhalb von B:
  **widerlegt**, auch als Baumgraphen-Beziehung.
- Kein Ausgang zählt als Beleg (Offenlegung 2 und 5). Ist (A) verträglich, ist die Konsequenz nur ein neuer Test mit einer
  Größe, die vor der Festlegung unbekannt ist.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
