# Vorab-Notiz H179: Was die übliche Physik für den Unterschied der Quarksektoren erwartet

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026: „versuche erstmal das, was die normale physik erwarten würde dann das andere“
(Antwort auf die Frage aus k378, ob der Unterschied Up gegen Down über die Ladung oder über die HS-Stufe gesucht werden soll).
Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3. Vergeben: H179, k379 (geprüft: frei).

## Vorwissen geprüft
- H172, H177, k376, H178, k378 (`../delta_h172/`, `../konfigurationen_h177/`, `../quarks_k376/`, `../farbe_h178/`, `../farbanteil_k378/`): Quarkwerte
  (ρ, x) fast skalenstarr; Farbe trennt Up und Down nicht.
- Suche im Repo nach Georgi-Jarlskog und Froggatt-Nielsen: keine Fundstelle. Beides ist hier neu.

## Was die übliche Physik sagt
1. **Eichladungen wirken generationsblind.** Ladung, Hyperladung und schwacher Isospin sind für alle drei Generationen eines Sektors gleich. Jede
   Wirkung, die nur von ihnen abhängt, multipliziert alle drei Massen eines Sektors mit demselben Faktor und lässt K, ρ, δ unverändert (exakt). Die einzige
   generationsabhängige Wirkung im Standardmodell ist die Yukawa-Kopplung selbst (H177: über die Top-Kopplung, wenige Prozent).
2. **Vereinheitlichung (Georgi-Jarlskog):** An der Vereinheitlichungsskala gilt m_b = m_τ, m_s = m_μ/3, m_d = 3·m_e. Das verknüpft den Down-Sektor mit den
   geladenen Leptonen **ohne freien Parameter**.
3. **Hierarchie aus einer Familienladung (Froggatt-Nielsen):** Massen ∝ ε^(Ladungssumme); üblich ist, dass die Up-Hierarchie eine feste Potenz der
   Down-Hierarchie ist (im einfachsten Muster das Quadrat).

## Hypothesen und Kriterien
- **H179a (blind):** Die Down-Konfiguration folgt aus den Leptonmassen über die Georgi-Jarlskog-Faktoren (3, ⅓, 1). Vorhersage: K_d und δ_d (und ρ_d, x_d)
  aus (3m_e, m_μ/3, m_τ). Vergleich mit den gemessenen Down-Werten, hochgerechnet mit dem Ein-Schleifen-Laufen aus k375 auf I zwischen I(10¹³ GeV) = 0,108
  und I(M_Planck) = 0,134. **Bestätigt**, wenn K_d und δ_d bei einem gemeinsamen I in diesem Bereich beide innerhalb von 3σ (Massenfehler der Quarks)
  liegen. **Widerlegt**, wenn eine der beiden Größen im ganzen Bereich mehr als 5σ entfernt ist. Dazwischen: unentschieden. Zusätzlich wird die Abweichung in
  Prozent berichtet, weil die theoretische Unschärfe der Relation (Schwellen, anderes Laufen in supersymmetrischen Modellen) größer ist als die Messfehler.
- **H179b (blind):** Dasselbe für die drei einzelnen Massenverhältnisse m_b/m_τ, 3m_s/m_μ, m_d/(3m_e) an der Skala: Bericht der drei Zahlen; die Relation
  verlangt, dass die beiden Verhältnisse der Verhältnisse (unabhängig von der gemeinsamen Normierung) 1 sind. Kriterium wie a (3σ / 5σ).
- **Nicht blind (Bericht, Zahlen aus k376 bekannt):** (i) einfache SU(5)-Gleichheit (Down = Leptonen, also K_d = ⅔) ist durch K_d = 0,74 ausgeschlossen;
  (ii) Ein-Parameter-Gesetze in der Ladung (Verhältnis Up zu Down gleich 2 oder 4 für θ − 45°, ln ρ, K − ⅔) gegen die gemessenen 2,3 bis 3,3;
  (iii) Potenzgesetz m_u-Hierarchie = (m_d-Hierarchie)^p: p aus den beiden Verhältnissen einzeln (vorab überschlagen: 1,70 und 1,41).

## Werkzeugwahl
Python (numpy, Monte Carlo 10⁵, Seed 20261126; Laufen wie k375) und Wolfram Language als unabhängige Kontrolle der Zentralwerte. Qiskit nicht geeignet.

## Grenzen (vorab)
Laufen nur im Standardmodell, eine Schleife, Top-Dominanz; Leptonverhältnisse als skalenunabhängig genommen. Georgi-Jarlskog wird als Zahlenrelation
geprüft, nicht als Modell übernommen. Kein Vorzeichen gesetzt; OP3/OP4 bleiben offen.
