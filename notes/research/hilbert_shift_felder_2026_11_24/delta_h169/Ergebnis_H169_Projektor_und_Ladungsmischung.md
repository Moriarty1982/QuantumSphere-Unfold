# Ergebnis H169: Der Chiralitätsprojektor erzwingt c = 1 nicht; c = 0 und c = 1 sind die beiden Fälle fester σ-Parität

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H169_Projektor_und_Ladungsmischung.md` (Commit e462469, vor der Rechnung). **Nicht blind** (a bis d standen
analytisch fest; die Rechnung ist eine exakte Nachprüfung). Skripte k364 (Python, sympy) und k364b (Wolfram, unabhängig aufgebaut: j als Symbol modulo
j² + 1 statt als Matrix). Beide stimmen in allen Punkten überein. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Der Projektor ½(1 + iL_e₇) ist in der Familie 1 + c·e₇ der Punkt c = i, nicht c = 1, und erzeugt dort keinen quadratischen
Term; die Vermutung aus k278 ist widerlegt. Die Werte c = 0 und c = ±1 sind aber genau die, bei denen der Spin-1-Term eine feste Parität unter der
Konjugation σ hat (gerade bzw. ungerade), und c = 1 heißt gleichwertig: invariant unter dem Tausch von Spin 1 und Spin 2.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H169a | 1 + cj = (1 − ic)P + (1 + ic)P̄; ½(1 + cj) ist idempotent genau für c = ±i; 2P = 1 + ij. ½(1 + j) hat das Quadrat j/2 und ist kein Projektor, sondern (bis auf 1/√2) die Drehung um π/4 | Nullreste | **bestätigt** |
| H169b | Bei a = ±i: Tr Z² = 0, Tr Z⁴ = 0, N(Z) = ±8i·x₁x₂x₃; Spin-1-Term (1 + c²)v′² ≡ 0. Allgemein Tr Z² = 2(1 + a²)\|x\|², Tr Z⁴ = 2(1 + a²)²\|x\|⁴, N = 2(3a − a³)x₁x₂x₃ (k278 nachgerechnet) | Nullreste | **bestätigt** |
| H169c | P-Anteil von r e^{jδ} ist r e^{−iδ}, P̄-Anteil r e^{+iδ}; 1 + cj = √(1 + c²)·e^{jχ}; σ(P) = P̄; Cσ tauscht s und v. Relativer Faktor der Anteile: 1 bei c = 0, i bei c = 1 | Nullreste | **bestätigt** |
| H169d | −cos 2(δ − χ) = [(c² − 1) cos 2δ − 2c sin 2δ]/(1 + c²): rein σ-ungerade genau für c = ±1, rein σ-gerade genau für c = 0 (und c → ∞). (1 + c²)v′² = (cs − v)²/(1 + c²); für c = 1 gleich (s² + v²)/2 − sv; invariant unter s ↔ v genau für c = ±1 | Nullreste, vollständige Lösungsmenge | **bestätigt** |
| H169e | Beimischung der anderen Parität: in beiden Sektoren dieselben Beträge, 0,0793204 (= tan 2x), 1,4530942, 2,0998654, je nach Zweig. Beide Vorzeichen kommen in beiden Sektoren vor (Spiegelzweige δ → −δ) | Bericht | Vorzeichen **nicht festgelegt** |

## Lesart
- **Antwort auf die Frage.** Nein: Der Projektor aus r42 erzwingt c = 1 nicht. Er enthält das äußere i; in der Familie 1 + c·e₇ ist er der komplexe Punkt
  c = i. Dort verschwinden Tr Z² und der Spin-1-Term identisch, nur die kubische Norm bleibt. „c = 1“ entsteht aus dem Projektor nur, wenn man das äußere i
  weglässt, und ½(1 + e₇) ist kein Projektor. Die Lesart „Projektor gibt a = 1“ aus k278 und H167 ist damit zurückgenommen.
- **Was c dann ist.** Ein reelles Feld hat beide Chiralitätsanteile, zueinander konjugiert. Die Phase δ ist die halbe relative Phase der beiden Anteile,
  und c verschiebt sie. Bei c = 0 stehen die Anteile in Phase, bei c = 1 um eine Vierteldrehung (Faktor i) versetzt.
- **Was c = 0 und c = 1 auszeichnet (rückwärts gefunden).** Genau bei diesen Werten hat der Spin-1-Term eine feste Parität unter σ: gerade bei c = 0, ungerade
  bei c = ±1. Dazwischen ist er gemischt. Gleichwertig: Bei c = 0 ist der Term invariant unter σ, bei c = 1 invariant unter Cσ, dem Tausch von Spin-2- und
  Spin-1-Anteil. σ und C sind die beiden Strukturabbildungen des Verdopplungsschritts (k282). Das passt zu H166: δ ist der σ-ungerade Dipol.
- **Sektoren.** Neutral heißt dann: Der Term ist σ-gerade. Das ist die natürliche Lesart, wenn σ die Ladungskonjugation ist (k282) und das neutrale Feld
  sein eigenes Konjugiertes. Geladen heißt: rein σ-ungerade, oder invariant unter Cσ. **Dafür gibt es keine Herleitung.** Die Setzung „c = 1“ ist
  umformuliert in „der Spin-1-Term des geladenen Sektors ist Cσ-symmetrisch“, nicht entfernt.

## Nachträglich (nicht in der Vorab-Notiz)
- Die sechs Zweige geben in beiden Sektoren dieselben drei Beträge der Beimischung. Der Grund: 2δ_ν − 2δ_e = π/6, und zusammen mit der Faltung (4π/3 in 2δ)
  ist das eine Vierteldrehung 3π/2 in 2δ. Die Verschiebung π/12 aus H99 ist also dasselbe wie der Tausch „σ-gerade gegen σ-ungerade“. Der neutrale und der
  geladene Sektor gehen unter diesem Tausch exakt ineinander über, mit derselben kleinen Beimischung tan 2x = 0,0793204. Das ist H168 in anderer Sprache,
  keine neue Bestätigung.
- Das Vorzeichen der Beimischung ist eine Konvention (Spiegelzweig δ → −δ, gleiches Spektrum).
- Der kubische Term überlebt am Projektorpunkt (N = ±8i·xyz) und ist dort rein imaginär. Ob das eine Bedeutung hat, ist nicht untersucht.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H167 | Skala, J, c = 1 | Oktant; Phase aus dimensionslosen Termen | warum c = 1; ein kleines Verhältnis |
| H168 | dazu: Brannen-Form für Neutrinos, c = 0 neutral | π/12 zwischen den Sektoren; Versatz nicht aus fester gemeinsamer Skala | gemeinsamer Versatz x; warum c = 0 und 1 |
| H169 | nichts Neues | Projektor gibt c = i, nicht 1; c ∈ {0, ±1} = feste σ-Parität; π/12 = Paritätstausch | warum der geladene Term rein σ-ungerade (Cσ-symmetrisch) ist; die Beimischung tan 2x |

Geprüft nach der Regel: Das Ziel c = 1 war eine gesetzte Eingabe. Die Frage „welches c“ entsteht nur in der Zerlegung nach s und v; zerlegungsfrei lautet
sie: Welche der beiden Strukturabbildungen (σ oder Cσ) lässt den Term des jeweiligen Sektors invariant?

## Grenzen
- Nur die Ebene span(1, e₇) und H₃ über ℂ⊗ℂ; die volle Albert-Algebra wurde nicht neu gerechnet (k278 gilt dort für reelles a, hier polynomial fortgesetzt).
- Die Zuordnung von σ zur Ladungskonjugation und von T zum Tausch der Ports (r51) ist Lesart, nicht geprüft. Frames: alles im M-Bild formuliert.
- Sektorzuordnung weiter unter H99. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Keine neue Datenvorhersage.
- Vergeben: H169, k364. Nächste frei: H170, k365.
