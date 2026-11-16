# Methoden-Notiz 2: Zeitabhängige Verbindung statt Hamiltonterm (OP3)

Festgelegt am 2026-11-16, **vor** jeder Rechnung. Fortsetzung der Idee des Autors („Korrekturterm, der von der zeitlichen Entwicklung abhängt …
daraus etwas über die Dynamik lernen“) nach dem Ergebnis von `README.md`: Auf S hängt alles an den Populationen, und kein natives Element verschiebt
sie; der Korrekturterm dort zeigt nur Geometrie. Hier wird stattdessen die **Verbindung** auf der Generationskugel zeitabhängig gemacht, dort, wo der
bewachte Kern (H102) wirkt. Status: **Erkundung, nicht blind**. Keine H-Nummer. Skript (nach dem Commit dieser Notiz): `connection_flow.py`.

## 1. Vorwissen geprüft
- `../op3_guarded_core_flux_2026_11_15/README.md`: Spin-½-Berry-Phase als Fluss (Dichte ½ je sr, gesamt 2π, Chern-Zahl 1). Flussfreier Kern Ω im
  Dreieck biegt; Fall A (verdrängter Fluss außerhalb, am Gegenpol, Umkehrwalze) gibt φ = π/4 − Ω/2, Fall B (gleichmäßig verteilt, „Minimum der
  Feldenergie“) gibt φ = 0,6795 bei Ω = γ_M; genau ein Kern ist topologisch ausgezeichnet; Faden 3: Kugel im S³ bricht Fasern über einer Kappe.
  Ursprüngliche Idee des Autors dort: Der Kern wird „von außen nach innen“ verschoben. Gerechnet wurde nur statisch je Lage (Rampe), **ohne Zeit**.
- `README.md` und `Methoden_Notiz.md` (dieser Ordner): Rekonstruktion auf S, kein Befund, Grenze der Darstellung.
- r14.5–r14.7, H102 (eingefroren), CT-001/CT-002.

## 2. Vorab festgehaltene Eigenschaften (analytisch)
- In dieser Darstellung bleiben die drei Auslesezustände (Oktant) fest; **K = 2/3 bleibt exakt**, nur φ = Fluss durch das geodätische Dreieck T
  ändert sich. Ziel: Fluss durch T = 0,666674 statt π/4, also ΔΦ = 0,118724 aus T heraus.
- Der Gesamtfluss bleibt 2π (Chern-Zahl). Ein Korrekturterm ist deshalb eine **Umverteilung** von Fluss mit Kontinuitätsgleichung
  ∂F/∂t + div J = 0. Gesucht ist der Strom J(n, t).
- **Erwartung, offen gesagt:** Bei rein lokalem Transport ist es am billigsten, Fluss in einem schmalen Saum über die Ränder von T zu schieben
  (Randlösung), nicht einen Kern in der Mitte zu leeren und den Fluss zum Gegenpol zu bringen (H102, Fall A). Die Rechnung prüft, ob das stimmt und
  was es kostet, und vergleicht mit den Kern-Konfigurationen.

## 3. System
- Kugel S², diskretisiert als Ikosaeder-Gitter (Unterteilung 5, 10 242 Knoten; Kontrolle Unterteilung 4). Flussdichte F_i ≥ 0 je Knotenfläche,
  Start gleichmäßig ½ je sr. T = Oktant mit Ecken (1,0,0), (0,1,0), (0,0,1); Zyklusachse (1,1,1)/√3.
- Zeitfenster [0, 1] in 50 Schritten (bei quadratischem Transport skaliert τ nur die Kosten).

## 4. Korrekturterm und Auswahlprinzip
- **V0 (Haupt): lokaler Transport mit kinetischer Energie** (Benamou–Brenier): minimiere $\sum_t\sum_{\rm Kanten}J^2/\bar F$ unter Kontinuität,
  Gesamtfluss fest, F ≥ 0, Endbedingung Fluss(T) = 0,666674 (Spielraum 2·10⁻⁴).
- **V1:** quadratische Stromnorm $\sum J^2$ (ohne Gewichtung mit F).
- **V2:** Zyklussymmetrie erzwungen (Strom invariant unter Drehung um die Zyklusachse um 2π/3) gegen frei.
- **V3:** Gitterauflösung 4 gegen 5.
- **V4 (Umkehrwalze erlaubt):** zusätzliche Kanten jedes Knotens zu seinem Gegenpunkt mit Länge π (geodätischer Abstand), sonst wie V0. Prüft, ob ein
  Antipoden-Kanal bei gleichen Kosten je Länge benutzt wird.
- **Vergleichskonfigurationen (nicht optimiert, nur bewertet mit dem V0-Funktional bei optimalem Weg zum festen Endzustand):** K-A = flussfreie
  Kappe Ω um die Zyklusachse, Fluss am Gegenpol (H102); K-B = flussfreie Kappe, Fluss gleichmäßig auf den Rest. Ω jeweils so, dass Fluss(T) =
  0,666674.

## 5. Formmerkmale
- **N1 Wo verlässt der Fluss T?** Anteil des Abflusses über die Ränder von T gegen aus dem Inneren (Abstand vom Schwerpunkt); bildet sich ein
  flussfreies Gebiet (F < 0,05 · ½) in T, und wo?
- **N2 Wohin geht er?** Mittlerer Abstand der Ablage von T; Anteil in der Gegenpol-Kappe (Winkelabstand > 150° zur Zyklusachse).
- **N3 Zeitverlauf:** Verlauf des Gesamtstroms über die Zeit (gleichmäßig, früh, spät).
- **N4 Kosten:** minimaler Wert des Funktionals; Verhältnis zu den Kosten von K-A und K-B.

## 6. Was als Befund zählt
- **Befund** ist ein Merkmal, das über V0–V3 qualitativ gleich bleibt und nicht der vorab genannten Erwartung (Randlösung) entspricht. Bestätigt
  sich die Randlösung, ist das ein **Ausschluss**: Ein lokaler, sparsamster Fluss erzeugt keinen Kern; H102 bräuchte dann einen nicht-lokalen Grund
  (Umkehrwalze) oder eine andere Bedingung.
- Zeigt V4, dass der Antipoden-Kanal bei gleichen Kosten je Länge benutzt wird und ein Kern entsteht, ist das ein Befund nur, wenn er über V2, V3 stabil
  ist; danach Übertragungstest mit eigener H-Nummer (Neutrinosektor, zwei Oktanten, Faden 2 der Kern-Notiz).
- Ein Kern mit Ω innerhalb 10⁻³ relativ an γ_M zählt nicht als Befund, weil die Zielbedingung Ω für K-A schon festlegt (zirkulär).

## 7. Offenlegung
Ziel bekannt; Transportprinzip und Gitter sind Setzungen; die Erwartung (Randlösung) ist vorab genannt. Änderungen nach dem Commit nur als Nachtrag.

## Nachtrag N2 (16.11.2026, vor der Rechnung): Umsetzung statt dynamischem Gitterproblem
Das in Abschnitt 3/4 beschriebene dynamische Problem (10 242 Knoten × 50 Zeitschritte, konvexes Programm) ist mit den verfügbaren Lösern (scipy,
kein cvxpy) nicht lösbar. Es ist auch nicht nötig. Festgelegt wird deshalb, ohne dass ein Ergebnis bekannt ist:
- **V0:** Benamou–Brenier ist exakt gleichwertig mit dem statischen Transport (Wasserstein-2) und Verschiebungsinterpolation mit konstanter
  Geschwindigkeit. N3 (Zeitverlauf) ist damit analytisch: gleichförmig. Bei freiem Endzustand mit nur der Bedingung Fluss(T) = Ziel lohnt sich nur
  Transport aus T hinaus, jede Masseneinheit zum nächsten Punkt außerhalb; die Lösung ist gierig exakt (Masse mit kleinstem Randabstand zuerst).
  Gerechnet auf den Gittern 3, 4, 5 (642, 2562, 10 242 Knoten).
- **V1 (Stromnorm ohne Gewichtung):** analytisch: Der Strom kleinster Norm ist J ∝ Bᵀχ_T, also nur auf den Kanten, die den Rand von T kreuzen, mit
  Kosten ΔΦ²/(Zahl der Randkanten); wird mitgerechnet.
- **V2 (Zyklussymmetrie):** ändert die minimalen Kosten nicht (konvexes Problem, Mittel über die Drehungen ist wieder optimal); entfällt als Rechnung.
- **V4 (Antipoden-Kanal mit Länge π):** im statischen Transport ist jede geodätische Verschiebung schon erlaubt; ein Kanal mit Kosten gleich der
  geodätischen Länge ist keine neue Möglichkeit. V4 = V0; entfällt als Rechnung.
- **K-A, K-B:** exakter statischer Transport (lineares Programm, HiGHS) zwischen Start und festem Endzustand, dicht auf Gitter 3; auf Gitter 4 mit
  Abstandsschranke 0,6 rad (Kaskaden aus kurzen Schritten bleiben erlaubt; auf Gitter 3 gegen die dichte Lösung geprüft). K-A: flussfreie Kappe um die
  Zyklusachse, ihre Masse gleichmäßig in die gleich große Kappe um den Gegenpol; K-B: flussfreie Kappe, Masse gleichmäßig auf den ganzen Rest.
  Ω so, dass Fluss(T) das Ziel trifft (auf dem Gitter: so viele Knoten wie nötig, Rest anteilig).
- Kriterien (Abschnitt 6) unverändert.
