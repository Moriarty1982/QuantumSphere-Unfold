# Erkundung k459 (nicht blind): Ist der Versatz φ eine kleine ℤ₃-Brechung?

**Datum:** 2026-11-28. **Art:** Erkundung ohne Vorab-Notiz. Das Ergebnis stand vor der Rechnung analytisch fest; die Rechnung bestätigt es nur
(`k459_z3_bruch_phi.py` → `k459_out.txt`, Wolfram `k459b_gegenprobe.wl` → `k459b_out.txt`). Anlass: Marc „weiter“ (20:32) nach H242; Vorschlag, φ als
kleine ℤ₃-Brechung zu lesen. Das ist eine neue Idee, die Ruheregel für φ (Marc 15:41) gilt nur ohne neue Idee.

## Ergebnis: Nein, φ ist keine kleine ℤ₃-Brechung. Die φ-Ruheregel bleibt.
1. **Die Brechung ist nicht klein.** Die ℤ₃-geschlossenen Lagen (H242: 3δ ≡ 0 mod π) liegen 12,73° (δ_Im) bzw. 27,73° (δ_Re) von den gemessenen Phasen
   entfernt, φ sind aber nur 2,27°. Schon die Basislagen ohne Versatz, π/12 und π/6, brechen ℤ₃ stark (|sin 3δ| = 0,707 und 1). Der Schlussbruch |sin 3δ| misst
   die Basislage und nicht φ.
2. **Die Leck-Energie legt φ nicht auf x.** Mit q → 0⁻ (H236) ist das Baum-Potential in φ flach (reine Drehung), und die Leck-Energie
   E(φ) = w_I sin²3δ_Im(φ) + w_R sin²3δ_Re(φ) allein bestimmt φ. Es gilt exakt dE/dφ = −3(w_I cos 6φ + w_R sin 6φ).
   - Gleiche Gewichte: Minimum bei **π/8** (E″ = 18√2), Maximum bei −π/24. Das ist wieder der Symmetriepunkt aus H225.
   - Zählgewichte 2:1 (H235): Minimum bei 0,339. Umgekehrt 1:2: 0,446. Nur Im: π/12. Nur Re: π/6. Keiner liegt in der Nähe von x = 0,0396.
   - Damit φ = x stationär ist, braucht es w_I/w_R = −tan 6x = −0,24203, also entgegengesetzte Vorzeichen in den beiden Sektoren und ein Verhältnis
     ohne erkennbaren Grund. Der nächste einfache Bruch −1/4 läge 3,2 % daneben; φ ist auf etwa 10⁻⁷ bekannt.
3. **Zufallskontrolle:** Zufällige Gewichte in [−1, 1]² legen das Minimum in 0,06 % der Fälle innerhalb 1 % von x. Das entspricht der reinen
   Fensterbreite (0,15 % der Periode, davon etwa die Hälfte Minima). Ein Treffer wäre also Zufall, und es gibt keinen ausgezeichneten Kandidaten.

## Einordnung
- Wie H235 (Satz vor der Rechnung): Ein Term, der nur von φ abhängt, kann x_ν nicht ändern. Hier legt er auch φ nicht fest, ohne ein angepasstes
  Gewichtsverhältnis.
- Die ℤ₃-Struktur der Kopien (H241/H242) erklärt die Dreizahl und die Form 2πk/3 der Brannen-Phasen. Die Lage δ (Basis π/12 bzw. π/6, Versatz φ) bleibt
  davon unberührt.
- Bekannt aus H166: δ_Im = 2/9 − 1,75·10⁻⁷, und „3δ = K“ ist ein Selbstbezug, der von den Daten nicht getrennt wird. k459 ändert daran nichts.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** dE/dφ in geschlossener Form; Extrema π/8 und −π/24 bei gleichen Gewichten; das nötige Verhältnis −tan 6x.
- **Gesetzt:** die Leck-Energie als φ-Potential, die Sektorgewichte und die Baumlagen π/12 und π/6 (H225/H236).
- **Offen:** φ bleibt die einzige Messzahl des Leptonbilds. Die Ruheregel gilt weiter, bis eine Idee kommt, die nicht nur von φ abhängt.

## Werkzeuge
Python (Extrema, Zufallskontrolle) und Wolfram (symbolische Ableitung, exakte Extrema). Qiskit nicht einschlägig.
