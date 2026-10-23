# Ergebnis H17: Massen aus Potentialen mit Realteil-Invarianten auf dem Tripel-Raum

Vorab-Notiz: `Vorab_Notiz_H17_Realteile_Tripelraum.md`, Commit 2a7271a (2026-10-22 21:11 MESZ), vor der Prüfung.
Der Rechner war nicht erreichbar, deshalb wurde die Notiz im Container committet und dem Autor vor der Rechnung
geschickt (SHA-256 0bcb6145…).
Skripte: `k69_test_h17.py` (Test), `k70_achse_e3.py` (Nachkontrolle nach dem Urteil). Kriterium unverändert.
Gerechnet wurde im Container unter den Namen k66/k67; diese Namen waren auf dem Rechner inzwischen vergeben, deshalb
wurden die Skripte ohne Änderung am Code umbenannt. Die Runde heißt aus demselben Grund v4.9.0-r32.

## Ergebnisse (M)

V_R = −S + βS² + γQ − κt − μL − νR₂ − λL², minimiert über alle 24 Koordinaten von 𝕆³.

**H17a, feste Verteilung, N = 2000:**

| Muster des globalen Minimums | Anzahl |
|---|---|
| drei gleiche Normen | 1483 |
| zwei verschiedene Normen, alle ≠ 0 (entartetes Paar) | 517 |
| drei verschiedene, alle ≠ 0 | **0** |

1629 der 2000 Minima liegen auf der reellen Achse. Dort ist G₂ ungebrochen, die Farbgruppe SU(3) also nicht
ausgezeichnet.

**H17b (Leptonen):** Gitter 21 × 4 × 7 × 3 über die Vieta-Familie:

| Ergebnis am Gitterpunkt | Anzahl |
|---|---|
| nicht nach unten beschränkt | 696 |
| Hessematrix mit negativem Eigenwert | 1061 |
| lokal, aber nicht global | 7 |
| **globales Minimum** | **0** |

**H17c:** Ohne Minima mit drei verschiedenen Normen gibt es keine K-Verteilung.

## Urteil nach dem festgelegten Kriterium

H17a, H17b und H17c sind **widerlegt**. Die Realteile heben das Hindernis nicht auf.

## Strukturbefund: der Grund (M, nach dem Urteil, exakt geprüft; Theoremlet v4.9.0-r32.1)

Auf der reellen Achse (a_k = n_k) gilt t = e₃ = n₁n₂n₃, R₂ = S und L = e₁. V_R ist dort ein symmetrisches Polynom
in n vom Grad 4 und darin **linear in e₃**:

  V_R = A(e₁, e₂) + e₃·(4γe₁ − κ),

weil Q = e₁⁴ − 4e₁²e₂ + 2e₂² + 4e₁e₃. Bei drei verschiedenen n_k ist die Hessematrix in (e₁, e₂, e₃) an der Stelle
(3,3) null und hat an (1,3) den Eintrag 4γ. Der 2×2-Hauptminor ist −16γ² < 0, also liegt ein **Sattelpunkt** vor.
Ein Sattel der Einschränkung auf die Achse ist auch ein Sattel auf ganz 𝕆³.

Damit haben die Realteile das Hindernis nur verschoben: Ohne Realteile war V linear in e₂ (v4.9.0-r26.1), mit Realteilen ist
es auf der Achse linear in e₃. Allgemein ist ein symmetrisches Polynom in n vom Grad ≤ 5 linear in e₃,
V = A + e₃·B. Bis auf den entarteten Fall ∇B = 0 am kritischen Punkt ist dann jeder solche Punkt ein Sattel. Auf der
Achse braucht ein Minimum mit drei verschiedenen Normen deshalb im Allgemeinen mindestens Grad 6 (e₃² = P²);
hinreichend ist das nicht gezeigt.

**Die sieben „lokalen Minima“ aus H17b:** Mit 50 Stellen gerechnet hat jedes einen negativen Eigenwert auf der Achse
(−1,4·10⁻⁷ bis −9,1·10⁻⁷, relativ etwa 10⁻⁹). Die vorab festgelegte Toleranz von 10⁻⁸ hat sie als lokale Minima
durchgelassen, die globale Suche fand jeweils tiefere Punkte. Am Urteil ändert das nichts.

Abseits der Achse ist kein entsprechender Satz gezeigt; numerisch trat dort kein Minimum mit drei verschiedenen Normen
auf.

## Einordnung

- Drei Tests (H11, H16, H17) zeigen dasselbe Muster: Natürliche Potentiale, die unter der Generationen-S₃
  symmetrisch sind, liefern höchstens zwei verschiedene Massen. Der Grund ist jedes Mal derselbe: Die höchste
  elementarsymmetrische Größe tritt nur linear auf.
- Eine Hierarchie würde Terme ab Grad 6 (mit Realteilen) bzw. ab Grad 8 (ohne) verlangen, mit entsprechend vielen
  freien Koeffizienten. Das wäre eine Anpassung, keine Herleitung.
- Die meisten Minima liegen auf der reellen Achse und lassen G₂ ungebrochen. Die Farbgruppe entsteht dort also nicht
  von selbst.
- Damit bleibt als nächster prüfbarer Weg die explizite Brechung der S₃. Dabei müsste vorab festgelegt werden, was als
  Vorhersage zählt.
