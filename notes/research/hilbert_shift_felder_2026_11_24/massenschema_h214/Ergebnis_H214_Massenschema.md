# Ergebnis H214 (k427): Polmassen sind das Schema des Rahmens — die M_Z-Lesart aus H213c ist unzulässig, der Abstand bleibt 1,78σ

**Datum:** 2026-11-27. **Vorab:** `Vorab_H214_Massenschema.md` (Commit e209c08, vor der Rechnung). **Urteil: trägt.**
**Werkzeuge:** Python (`k427_test_h214.py` → `k427_out.txt`), Wolfram unabhängig (`k427b_gegenprobe.wl` → `k427b_out.txt`) für a–c; alle gemeinsamen
Zahlen stimmen überein. Qiskit nicht einschlägig. Teil a nicht blind (H154), Teile b–d blind.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| a (nicht blind) | K: Pol 0,6666645 (−0,4σ); gemeinsam M_Z 0,6679287 (+110σ); gemeinsam m_τ bzw. 2 GeV 0,6678322 (+229σ) | \|K−⅔\| ≤ 2σ_K | **nur Pol** (von diesen drei) |
| b (blind) | je eigene Skala m̄(M) = M/(1+α(M)/π): K = 0,6666601 (−1,3σ), x = 0,0395696; Δx gegen Pol −5·10⁻⁶ = **0,002σ(x_ν)** (Hadron-Anteil 0 bis 2: 0,001–0,003σ) | zulässig? Δx < 0,3σ? | zulässig, praktisch gleich Pol |
| c (blind) | x = x_ν bei K = ⅔ verlangt m_e/m_μ **+22,6 %**, m_μ/m_τ −1,85 %; zulässige Schemata verschieben höchstens 0,004 % | Faktor > 10 | **Faktor 441: kein zulässiges Schema schließt den Abstand** |
| d (blind) | einschleifiges SM-Laufen des Weinberg-Operators (τ-Yukawa, C = −3/2): ΔR/R ≤ 6·10⁻⁶, Δx_ν ≤ 0,0004σ | < 0,1σ | **R schemafest** |

**Gesamturteil: trägt.** Polmassen (oder gleichwertig m̄ je an eigener Skala) sind das Schema, in dem die Form des Rahmens (K = ⅔, Amplitude √2) gilt.
Laufende Massen an einer gemeinsamen Skala erfüllen die Form nicht; x ist dort im Sinn des Rahmens gar nicht definiert. Die H213c-Lesart
(x_lepton(M_Z) = 0,0408, 1,22σ) ist damit unzulässig; der maßgebliche Abstand bleibt **1,78σ** und lässt sich durch keine Schemawahl verkleinern.

## Begründung aus dem Rahmen
1. **Die Form legt das Schema fest.** Der Rahmen setzt K = ⅔ exakt (Postulat J / Zählregel; K_ν = K_e = ⅔ geschützt, H178–H182). Der Versatz x ist als
   Abstand der Brannen-Phase δ vom Minimum π/12 nur in einem Schema definiert, in dem √m_k = μ(1 + √2 cos(δ + 2πk/3)) gilt. Das sind die Polmassen
   (und m̄ je an eigener Skala, weil der gemeinsame Faktor 1 + α/π dort herausfällt). Gemeinsames Laufen multipliziert die Massen mit M^(3α/2π)-artigen
   Faktoren, unter denen K nicht invariant ist (H154).
2. **Gleichartiger Vergleich.** Auf der Neutrino-Seite kommt R aus Oszillationen, also aus physikalischen Massendifferenzen; R ist praktisch schemafest (d).
   Der Vergleich x_ν gegen x_lepton ist nur mit physikalischen (Pol-)Massen der geladenen Leptonen gleichartig.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** Auswahl des Schemas durch die Form (a, mit H154), Gleichwertigkeit von Pol und eigener Skala (b), Rückwärtssuche (c), Schemafestigkeit von R (d).
- **Gesetzt:** K = ⅔ (Postulat J, H99); einschleifige QED mit pauschalem Hadron-Anteil an 1/α (Spielraum 0–2 geprüft); M_Z-Werte aus Xing–Zhang–Zhou 2008;
  |U_τi|² gerundet (0,24/0,33/0,43).
- **Nachträglich bemerkt:** Die Verbesserung in H213c (1,22σ) kam allein aus dem Bruch von K = ⅔ (freie Amplitude a = 1,4169 statt √2). Im Verhältnis
  m_e/m_μ gehen die M_Z-Massen sogar in die **falsche** Richtung (−2,1 % statt der verlangten +22,6 %).
- **Folge für die Vorhersage:** Gilt ein gemeinsamer Versatz, muss R auf R(π/6 − x_lepton) = 0,0308 rücken (H168c, heute +1,8σ). Das ist jetzt die einzige
  Stelle, an der der gemeinsame Versatz scheitern kann, und sie liegt ganz bei den Neutrino-Daten (JUNO, Δm²₂₁).

## Grenzen
Einschleifig; zweischleifige QED- und elektroschwache Beiträge zur Umrechnung Pol ↔ m̄(m̄) nicht gerechnet (Größenordnung (α/π)² ≈ 5·10⁻⁶ als gemeinsamer
Faktor, für K vernachlässigbar). Alles unter H99/Postulat J. Kein Guard berührt; OP3/OP4 bleiben offen.

## Dateien
- `Vorab_H214_Massenschema.md` — Vorab-Notiz (vor der Rechnung committet).
- `k427_test_h214.py`, `k427_out.txt` — Python-Rechnung und Ausgabe.
- `k427b_gegenprobe.wl`, `k427b_out.txt` — Wolfram-Gegenprobe und Ausgabe.

Vergeben: H214, k427. Nächste frei: H215, k428 (vor Vergabe gegen `main` prüfen).
