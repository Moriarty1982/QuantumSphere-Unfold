# Vorab-Notiz H169: Erzwingt der Chiralitätsprojektor aus r42 die Ladungsmischung c = 1?

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Nicht blind:** a bis d stehen analytisch fest und sind von Hand überschlagen; die Rechnung ist eine
exakte Nachprüfung (Nullreste). Nur e hat einen offenen Ausgang (Vorzeichenmuster), dort gibt es keine Vorhersage. Anlass: Autor, 26.11.2026, „ja bitte“ auf
die Frage, ob nach H168 geprüft werden soll, ob c = 1 im geladenen Sektor erzwungen ist. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4.
Vergeben: H169, k364 (geprüft: frei).

## Vorwissen geprüft
- **k278** (`../rueckwaerts/k278/README.md`): Z_a = X(v) + a·C·X(v), Einträge (−a + e₇)v; Tr Z² = 2(1 + a²)|v|², N(Z) = 2(3a − a³)xyz, Tr Z⁴ = (Tr Z²)²/2.
  Dort offen: „Prüfen, ob r42 die Ladungsmischung a festlegt“; Vermutung: der Projektor ½(1 + iL_e₇) gäbe a = 1.
- **k282** (`../rueckwaerts/k282/README.md`): σ (e₇ → −e₇) und C (Multiplikation mit e₇) als die zwei Strukturabbildungen; σ als Ladungskonjugation (Lesart).
- **v4.9.0-r42, r43, r51** (`../../v4_10_0_r34_r47/rounds/`, `../../v4_10_0_r48_r55/rounds/v490_r51_round.tex`): C_ch = ½(1 + iL_e₇) mit **äußerem** i in ℂ⊗𝕆;
  Kompensator- und Partnerport; T tauscht die Ports, R lässt sie fest; iL_e₇ = äußeres z ↦ iz mal inneres L_e₇.
- **H158e** (`../generationszahl_h138/`): c dreht nur die Phase. **H166:** δ ist der σ-ungerade Dipol. **H167, H168** (`../delta_h167/`, `../delta_h168/`):
  c = 1 und c = 0 als Setzungen; Spin-1-Term −cos 2(δ − χ), χ = arctan c; gemeinsamer Versatz x = 0,0395773407.
- Suche nach „c = i“, „σ-ungerade“ zusammen mit „Ladungsmischung“, „Cσ“ in `notes/`, `wiki/`: kein Vorbefund.

**Suchrichtung:** rückwärts. Ziel c ∈ {0, 1}. Notwendige Bedingung gesucht: Welche Eigenschaft haben genau diese beiden Werte, und ist der Projektor ein
Mitglied der Familie 1 + c·e₇? **Werkzeugwahl:** Python (sympy) exakt; Wolfram unabhängig als Gegenprobe. Qiskit nicht geeignet (keine Schaltung).

## Aufbau (k364, `k364_test_h169.py`; Gegenprobe `k364b_gegenprobe.wl`)
Ebene span(1, j) mit j = e₇ (inner), dazu das äußere i; i und j vertauschen, (ij)² = 1. P = ½(1 + ij), P̄ = ½(1 − ij). Nebendiagonale z = s + jv = r e^{jδ}
(s Spin 2, v Spin 1), Mischung z = (1 + cj)(s′ + jv′). σ: j → −j. C: Multiplikation mit j.

## Hypothesen und Kriterien
- **H169a (exakt): Der Projektor ist c = i, nicht c = 1.** 1 + cj = (1 − ic)P + (1 + ic)P̄, also 2P = 1 + cj genau für c = i (P̄ für c = −i). Kein reelles c
  gibt einen Projektor; ½(1 + j) ist kein Projektor (Quadrat j/2). Kriterium: symbolische Nullreste.
- **H169b (exakt): Bei c = ±i ist das Feld quadratisch null.** Spin-1-Term (1 + c²)v′² ≡ 0, Tr Z² = 0, Tr Z⁴ = 0, N(Z) = ±8i·xyz ≠ 0 (k278 fortgesetzt,
  hier direkt auf H₃ über ℂ⊗ℂ nachgerechnet). Der Projektor allein erzeugt also keinen δ-abhängigen quadratischen Term. Kriterium: Nullreste.
- **H169c (exakt): Reelles c ist die relative Phase der beiden Chiralitätsanteile.** Für z = r e^{jδ} ist der P-Anteil r e^{−iδ}, der P̄-Anteil r e^{+iδ};
  die Mischung verschiebt δ um χ. σ tauscht P und P̄. Cσ: z ↦ j z̄ tauscht s und v (Spin 2 gegen Spin 1). Kriterium: Nullreste.
- **H169d (exakt, rückwärts): c = 0 und c = ±1 sind genau die Fälle fester σ-Parität.** −cos 2(δ − χ) ist σ-gerade genau für c ∈ {0, ∞} und σ-ungerade genau
  für c = ±1. Für c = 1 ist der Spin-1-Term (s² + v²)/2 − s·v, also die unter Cσ (Tausch s ↔ v) invariante Form; für c = 0 ist er v², σ-invariant.
  Kriterium: Nullreste; Lösungsmenge der Paritätsbedingungen vollständig.
- **H169e (Bericht, kein Kriterium):** Beide Sektoren in Paritätssprache: reiner Paritätsterm plus Beimischung der anderen Parität. Für den geladenen Sektor
  ist das Verhältnis tan 2x (H167: 0,0793204). Für den neutralen Sektor (H99, δ_ν = π/6 − x) das Verhältnis und sein Vorzeichen ausrechnen und
  berichten. Betragsgleichheit ist eine Identität aus H168; offen ist nur das Vorzeichenmuster. Keine Vorhersage.

## Folge, vorab festgelegt
- a und b bestätigt: Die Vermutung aus k278 („Projektor gäbe a = 1“) ist **widerlegt**. Der Projektor erzwingt c = 1 nicht.
- c und d bestätigt: Die Setzung „c = 1“ ist gleichwertig zu „der Spin-1-Term des geladenen Sektors ist rein σ-ungerade“ (oder: invariant unter Cσ),
  „c = 0“ zu „rein σ-gerade“. Für den neutralen Sektor ist σ-gerade die natürliche Lesart (σ als Ladungskonjugation, k282). Für den geladenen Sektor
  ist „rein σ-ungerade“ damit **nicht hergeleitet**; die Setzung ist umformuliert, nicht entfernt.
- Kein Vorzeichen wird gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen. Keine neue Datenvorhersage.
