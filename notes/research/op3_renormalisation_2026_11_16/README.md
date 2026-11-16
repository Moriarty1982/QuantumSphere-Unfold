# OP3: Schließt die Renormierung den Rest der Biegung? (Polmassen gegen laufende Massen)

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind**, ohne Vorab-Notiz und ohne H-Nummer: Die Richtung des Effekts stand schon vor der
Rechnung fest, weil H1 (v4.8.0-r12) die Phase der Leptonen mit laufenden Massen bei M_Z bestimmt hat. Nach AGENTS wird ein vorher feststehendes
Ergebnis nicht als blinder Test geführt. Auftrag des Autors: „Ja, Renormierung“, der zweite Weg nach H106–H108. Skript `phase_running.py`, Ausgabe
`run/phase_running_stdout.txt`.

## Vorwissen geprüft
- `../v4_8_0_r03_r12/llm/Ergebnis_H1_Koide_Phase.md`, `k14_test_h1.py`: Mit laufenden Lepton-Yukawas bei M_Z ist K = 0,667829 und δ = 0,221123;
  mit Polmassen K = 0,666664, δ = 0,222225. Koide und δ ≈ 2/9 gelten nur für Polmassen.
- `../op3_mass_backsolve_2026_11_12/README.md`: Die Polmassen sind keine laufenden Parameter; das Matching fehlt.
- `../op3_flux_two_thirds_2026_11_13.md`: δ = 2/9 nur bei Polmassen.
- H106–H108: Der Rest 0,012376 zwischen Spin-1-Dreieck (0,679042) und Lepton-Phase ist aus der Kopienstruktur von HS(8) nicht erklärt.

## Ergebnisse
1. **Phasen-Konvention:** Die Bargmann-Phase der Runden ist φ = 3δ mit dem δ von H1. Geprüft: Polmassen 3δ = 0,666674 (2/3), Spin-1-Dreieck aus
   seinen Wurzelgewichten 3δ = 0,679042.
2. **Laufende Massen bei M_Z (Daten aus H1):** 3δ = 0,663370, also **0,0033 unter** der Polmassen-Phase; K = 0,667829.
3. **Ein-Schleifen-QED ab den Polmassen** (m(μ) = M [1 − (α/π)(1 + (3/2) ln(μ/M))], α fest): Die Änderung ist ein fast fester Sprung von −0,0033
   (−0,003268 bei μ = m_τ, −0,003314 bei M_Z, −0,003427 bei 10⁹ MeV). Sie entsteht beim Übergang von Pol- zu laufenden Massen, weil die Logarithmen
   ln(μ/M_i) sich zwischen den Leptonen um den festen Betrag ln(M_j/M_i) unterscheiden; das weitere Laufen ist fast gleich für alle Leptonen. Die
   Rechnung reproduziert den M_Z-Wert aus H1 (0,663360 gegen 0,663370).
4. **Richtung und Größe:** Das Spin-1-Dreieck liegt **+0,0124 über** der Polmassen-Phase. Die Renormierung verschiebt die Phase **nach unten**, um etwa
   ein Viertel des Rests. Sie vergrößert den Abstand also, statt ihn zu schließen. Eine Skala unterhalb der Polmassen, an der die Phase steigen
   könnte, gibt es für laufende Leptonmassen nicht (Entkopplung).

## Folgerung
- **Die Renormierung im üblichen Sinn erklärt den Rest nicht.** Wenn das Spin-1-Dreieck ein „Strukturwert“ ist, der bei einer hohen Skala gilt, müsste
  die Phase beim Herunterlaufen steigen; sie fällt aber beim Hinauflaufen nur um 0,0033 und ist danach fast konstant.
- Selbst mit umgekehrtem Vorzeichen (etwa wenn die Polmassen selbst ein Schema-Effekt wären) wäre der Betrag mit 0,0033 nur ein Viertel des Rests. Diese
  Zahl wird nicht gedeutet.
- Mit H106, H107, H108 und dieser Erkundung sind vier Wege geprüft: Singulettbeimischung, verschachtelte Normierung, Verschränkung, Renormierung.
  Keiner schließt den Rest. Der Rest 0,012376 bleibt offen; ohne neue Struktur schlage ich vor, OP3 an dieser Stelle ruhen zu lassen.
- Grenzen: nur Ein-Schleifen-QED mit festem α, ohne elektroschwache Beiträge oberhalb M_Z; für die Richtung reicht das, und der M_Z-Wert stimmt mit H1.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
