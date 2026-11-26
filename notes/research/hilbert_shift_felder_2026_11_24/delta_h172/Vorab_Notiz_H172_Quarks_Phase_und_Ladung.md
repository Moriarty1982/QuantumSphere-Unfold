# Vorab-Notiz H172: Quarks als Prüfstein. Hängt die Phasenlage an der Ladung?

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Nicht blind bezüglich der Daten:** Die Quark-Phasen stehen seit H1 im Repo (δ_u ≈ 0,052 bis 0,075,
δ_d ≈ 0,100 bis 0,110) und wurden bei der Vorwissen-Prüfung gesehen, bevor diese Notiz geschrieben war. Die Regel unten ist die, die sich aus H168 bis H171
ergibt, und wurde nicht an die Zahlen angepasst. **Erwartung nach Überschlag: widerlegt.** Der Test wird trotzdem geführt, weil er die Lesart „Ladung ↔
Phasenlage“ gegen Daten stellt. Anlass: Autor, 26.11.2026, „mach das“ auf den Vorschlag eines Quark-Tests. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4.
Vergeben: H172, k367 (geprüft: frei).

## Vorwissen geprüft
- **H1** (`../../v4_8_0_r03_r12/llm/Ergebnis_H1_Koide_Phase.md`, k14): δ = 2/9 und δ = K/3 für Quarks widerlegt; K_u = 0,888 (M_Z) bzw. 0,849, K_d = 0,748 bzw.
  0,731; δ hängt bei Quarks deutlich von der Skala ab. Daten und Verfahren (Phase der Fourier-Komponente, Monte Carlo) werden von dort übernommen.
- **H168 bis H171** (`../delta_h168/` … `../delta_h171/`): neutral (Q = 0) → Phasenlage 0, geladen (|Q| = 1) → Phasenlage π/2 in 2δ (χ = π/4); gemeinsamer
  Versatz x = 0,0395773407; Baumwerte π/6 bzw. π/12.
- **H127, k277** (Quarks bei exakter A₄ entartet), **H125** (relative Orientierung Leptonen/Quarks), **H144** (Signatur folgt der Ladung).
- `Pruefung_Quarks_Oktonionen.md`, `Trennung_Farbe_Generation.md` (v4.8.0): keine Vorhersage für Quark-Phasen.
- Suche nach „δ_u“, „δ_d“, „Quark-Phase“ zusammen mit „π/12“, „Ladung“ in `notes/`, `wiki/`: kein Vorbefund zu einer ladungsabhängigen Phasenlage.

**Suchrichtung:** vorwärts als Test (Regel → Vorhersage → Daten), danach rückwärts als Bericht (welche Phasenlage verlangen die Daten). **Werkzeugwahl:** Python
(numpy, Monte Carlo wie k14); Wolfram unabhängig für die Zentralwerte von K, δ und die Vorhersagewerte. Qiskit nicht geeignet.

## Regel (festgelegt)
Die Phasenlage des Spin-1-Terms ist linear in der Ladung: χ(Q) = |Q|·π/4, dazu derselbe Versatz x mit beiden Vorzeichen. Minima bei χ + {0, π/2}, gefaltet.
Die Variante „ein Schritt −i je Drittel Ladung“ (χ = 3|Q|·π/4) gibt für |Q| = ⅓, ⅔ dieselben gefalteten Werte. Damit:
- **Down-Typ (|Q| = ⅓):** Baumwert π/12 = 0,261799; mit Versatz π/12 − x = 0,222222 oder π/12 + x = 0,301377.
- **Up-Typ (|Q| = ⅔):** Baumwerte 0 und π/6 = 0,523599; mit Versatz x = 0,039577, π/6 − x = 0,484021 oder π/6 + x = 0,563176.

## Daten und Verfahren (k367, `k367_test_h172.py`; Gegenprobe `k367b_gegenprobe.wl`)
Wie k14: Primärdaten laufende Massen bei M_Z, Sekundärdaten PDG-Standardskalen (Werte und Fehler aus k14 übernommen). δ = Phase von Σ√m_k ω^{−k}, gefaltet auf
[0, π/3]; K = Σm/(Σ√m)². Fehler aus 10⁶ Ziehungen, Seed 20261126. Zusatzvariante: leichteste Wurzel negativ (wie bei den Neutrinos in H99); sie wird
getrennt ausgewiesen und zählt als eigener Vergleich.

## Hypothesen und Kriterien
- **H172a (Test):** Für jeden Quarktyp liegt die gemessene Phase bei einem der vorhergesagten Werte. **Bestätigt**, wenn in den Primärdaten |z| < 3 für einen
  Kandidaten gilt und derselbe Kandidat in den Sekundärdaten |z| < 5 hat. **Widerlegt**, wenn in den Primärdaten kein Kandidat innerhalb 5σ liegt.
  Sonst unentschieden. Urteil je Typ getrennt; die Regel gilt als bestätigt nur, wenn beide Typen bestätigt sind.
- **H172b (Kontrolle, nicht blind):** Die Leptonen (Polmassen) geben mit demselben Verfahren δ = δ* innerhalb 10⁻⁶ und K = ⅔ innerhalb 10⁻⁵.
- **H172c (Bericht, rückwärts):** Welche Phasenlage χ_q = δ_q + x bzw. δ_q − x (und gefaltete Partner) verlangen die Daten, und wie stark hängt sie von der
  Skala ab (M_Z gegen Standardskalen)? Dazu K_q. Kein Kriterium, keine Zahlensuche.

## Folge, vorab festgelegt
- a bestätigt: Die Lesart „Ladung ↔ Phasenlage“ hätte eine erste Stütze außerhalb der Leptonen; eigener Folgetest nötig.
- a widerlegt: Die lineare Zuordnung Ladung ↔ Phasenlage gilt für Quarks nicht. Das trifft die Lesart aus H168 bis H171 nur in ihrer Ausdehnung auf
  Quarks; für Leptonen bleibt sie eine Lesart unter H99. Einschränkung, die dann mitzuteilen ist: Die Regel setzt K = ⅔ (Postulat J) voraus, und K = ⅔ gilt
  für Quarks nicht (H1). Der Test prüft die Phase allein.
- Kein Vorzeichen wird gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen.
