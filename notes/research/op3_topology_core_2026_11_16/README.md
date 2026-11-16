# OP3: Das Kern-Bild topologisch (Erkundung, analytisch, nicht blind)

16. November 2026. Auftrag des Autors: „analysiere das mal topologisch“, nach der Linie Korrekturterm → Verbindung → undurchlässiger Rand
(`../op3_correction_term_2026_11_16/README.md`), die bei zwei Fragen endete: warum genau ein Kern, und warum ΔΦ = γ_M/2. Skript `topology.py`,
Ausgabe `run/topology_stdout.txt`. Kein Zielwert ausgewertet, keine H-Nummer.

## Vorwissen geprüft
- `../op3_guarded_core_flux_2026_11_15/README.md`: Chern-Zahl 1, Schritt 2 (Kugel ohne n Kappen hat n − 1 freie Holonomien; genau ein Kern
  ausgezeichnet), Umkehrwalze als Antipodenabbildung mit Θ² = −1 (Kramers), Faden 3 (Kugel B_ε(K) im S³ bricht Fasern über einer Kappe).
- r16.7 (Oktant, Phase ±π/4, zwei Bahnen nach dem Vorzeichen), v4.9.0-r02.2/r02.3 (Umkehrwalze antilinear, fixpunktfrei).

## 1. Was Topologie festlegen kann und was nicht
- **Ganze Zahlen und Symmetrieanteile, keine stetigen Werte.** Die Generationskugel trägt das Hopf-Bündel (Spin ½, Chern-Zahl 1, Gesamtfluss 2π).
  Der Oktant ist durch die Oktaedersymmetrie genau ein Achtel davon: π/4 = 2π/8. Die Zielphase 2/3 ist dagegen kein rationaler Teil von 2π
  (2/3 : 2π = 1/(3π)). **ΔΦ = π/4 − 2/3 kann deshalb nicht aus Topologie allein kommen**; es braucht eine stetige Eingabe. Im Bestand ist das γ_M aus
  der Zählregel (OP1). Das ist eine harte Grenze, keine Lesart.
- **Die Zahl der Kerne schon.** Die Kugel ohne n Scheiben hat eine Fundamentalgruppe vom Rang n − 1, also n − 1 freie Aharonov-Bohm-Holonomien.
  n = 0 biegt nicht, n = 1 biegt ohne freien Parameter, n ≥ 2 macht die Phase frei (Schritt 2 der Kern-Notiz). Genau ein Kern ist topologisch die einzige
  starre Biegung.

## 2. Neu: die Umkehrwalze als Symmetrie widerspricht Fall A
Θ = iσ_y K bildet den kohärenten Zustand bei n auf den bei −n ab, Θ² = −1 (300 Punkte geprüft). Für die natürliche Verbindung ist Θ eine Symmetrie:
Die Bargmann-Phase des Antipodendreiecks ist das Negative der Phase des Dreiecks (300 Zufallsdreiecke). Weil die Antipodenabbildung die Orientierung
umkehrt, heißt das für die Flussdichte: **F(−n) = F(n).**

Folge: Ist die Umkehrwalze eine **Symmetrie** der Verbindung, dann zieht ein flussfreier Kern bei der Zyklusachse z_c einen ebenso flussfreien Kern bei
−z_c nach sich. Fall A der Kern-Notiz (verdrängter Fluss *sammelt* sich am Gegenpol) verletzt diese Symmetrie. Die Lesart vom 15.11. („was in den Kern
hineinläuft, kommt am Gegenpol heraus“) benutzt die Umkehrwalze als **Abbildung** (Transport), nicht als Symmetrie. Beides zugleich geht nicht. Das ist
eine Präzisierung der Umkehrwalzen-Lesart, keine Widerlegung von H102 (H102 setzt nur φ = π/4 − γ_M/2, nicht den Mechanismus).

**Die Θ-symmetrische Alternative:** zwei flussfreie Kerne bei ±z_c, der verdrängte Fluss symmetrisch verteilt. Im Quotienten S²/Θ = ℝP² ist das
**eine** Punktierung, also wieder „genau ein Kern“, nur eine Ebene höher. ℝP² ohne Scheibe ist ein Möbiusband; ob die Θ-Bedingung die eine Holonomie
dort festlegt, ist nicht geprüft. Die Phase dieser Konfiguration hängt an Ω und an der Verteilung; ein Vergleich von Ω mit γ_M wäre nachträglich und
müsste vorab registriert werden. **Hier nicht ausgewertet.**

## 3. Neu: Die fermionische Umkehrwalze erzwingt Fluss (Borsuk–Ulam)
Auf dem trivialen Bündel gäbe es eine Struktur Θ mit Θ² = −1 über der Antipodenabbildung nur mit einer stetigen Funktion f: S² → S¹ mit f(−n) = −f(n).
Eine solche ungerade Abbildung gibt es nach dem Satz von Borsuk–Ulam nicht. **Also verlangt eine fermionische Umkehrwalze ein nichttriviales Bündel:**
Die Generationskugel muss eine von null verschiedene Chern-Zahl tragen, also Fluss, also eine von null verschiedene Bargmann-Phase. Das Hopf-Bündel
(Chern-Zahl 1) erfüllt es. Dass allgemein eine ungerade Chern-Zahl nötig ist, halte ich für richtig, habe es aber nicht nachgelesen.

Lesart: Dass die Leptonen überhaupt eine Koide-Phase haben, ist topologisch an ihre Fermion-Natur gebunden (Θ² = −1); welchen Wert sie hat, nicht.

## Ergebnis
1. „Genau ein Kern“ ist topologisch begründbar: auf S² als einzige starre Biegung, mit Umkehrwalze als Symmetrie als ein Kernpaar ±z_c, das in ℝP² eine
   Punktierung ist.
2. ΔΦ = γ_M/2 ist topologisch **nicht** erreichbar (kein rationaler Teil von 2π); die Zahl muss von außen kommen, und das bleibt OP1.
3. Die Umkehrwalze als Symmetrie und Fall A (Fluss sammelt sich am Gegenpol) schließen sich aus; die symmetrische Alternative ist das Kernpaar.
4. Eine fermionische Umkehrwalze erzwingt einen nichttrivialen Fluss (Borsuk–Ulam).

Offen: die Holonomie auf dem Möbiusband unter Θ; die Phase des Kernpaars (nur mit Vorab-Notiz). OP1 und OP3 offen; H102 unverändert.
