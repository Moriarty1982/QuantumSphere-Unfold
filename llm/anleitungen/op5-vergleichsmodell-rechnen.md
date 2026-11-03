# Anleitung: Rechnungen am OP5-Vergleichsmodell

Werkzeugunabhängig. Das Modell ist das feste Vergleichsmodell der Sondenfelder mit dem 70-stelligen Keim bei (1, 3/5, 0, 0).

## Regeln zuerst
- Jeder Test mit Entscheidungskriterium wird vorher als `llm/Vorab_Notiz_HNN_*.md` festgeschrieben und committet; der
  Zeitstempel zählt. Zuletzt vergeben ist H53.
- Erkundungen ohne Vorab-Notiz werden offen als „Erkundung“ geführt.
- Alles betrifft nur das Vergleichsmodell, nicht das QSC-Modell selbst. OP5 bleibt offen.
- Schwere Rechnungen (Jacobi-Matrizen, SVDs großer Symbole) im Hintergrund oder als eigenständigen Auftrag laufen lassen
  und nur Zahlen zurückmelden.

## Modell
- **Feldgleichung:** F = i Σ V^μ_a K_a D_μΨ − h(Y⊗β)Ψ mit D_μ = ∂_μ + iA_μ.
- **Verbindung:** A_0 = 0, A_k = G(x)·spin_k(x)⊗I4.
- **Coframe:** V = E⁻¹ mit E^a_μ = Re(Ψ†Q_a D_μΨ); dabei K_a = I3⊗(I, α_i) und Q_a = S⊗(I, α_i).
- **Skalare Bedingung:** g = 4 − hΨ†(Z⊗β)Ψ/2.
- **Vervollständigt:** R = (F, G, dg) mit 24 + 4 + 4 Zeilen. Die Formeln stehen in
  `analysis/op5-field-slices/state-sufficiency-2026-10-30/precision_completed_rebuild.py`.
- **Hintergrund:** h = h(t, r) und A = M(t) dφ.

## Daten
Im Ordner `analysis/op5-field-slices/state-sufficiency-2026-10-30` (GitHub und lokal):

| Grad | Datei |
|---|---|
| 0 | `precision-first-jet-70.json` (psi, point) |
| 1 | `precision-completed-root-result.json` (`first_derivatives_real_packed`) |
| 2 | `precision-second-jet-result.json` |
| 3 | `precision-omega-repair-result.json` |
| 4 und 5 | `precision-fifth-gate-repair-result.json` |

- **Packung:** `combinations_with_replacement(range(4), deg)`; je Eintrag 24 reelle Zahlen (12 Real-, dann 12
  Imaginärteile); es sind Monom-Taylorkoeffizienten.
- **Gefrorenes Symbol:** `completion-omega-witness.npz` (J 32×96, θ 480, float64). Es stammt vom älteren Keim.

## Werkzeuge
Auf GitHub unter `notes/research/v4_10_0_r71/llm/`, lokal unter `llm/`.
- `k135_tps.py`: abgeschnittene Potenzreihen. `Background(p)` baut den Hintergrund, `Rseries(psi4, bg)` liefert alle
  Taylor-Koeffizienten von R bis Grad 3, `load_germ(D)` lädt den Keim.
- `k127_symbol_frei.py`: punktweises R und Symbol J für beliebige Punkte und Jets.
- `k130_andere_punkte2.py`: setzt Lösungen zu anderen Punkten fort.
- `k109_unabhaengig_F.py`: exakte Reihen von F und g entlang von Geraden, mit 80 Stellen.
- `k111_hilbert.py`: direkter Symbolaufbau mit Dimensionszählung.

## Bekannte Ergebnisse (r71)
- Der Keim erfüllt R bis Grad 3 (≤ 2,4e-12 in float64).
- Das Grad-4-Symbol hat Rang 528 und einen Linkskern der Dimension 112. Ω ist eindeutig.
- Mit dem gespeicherten θ gilt dim g_p = 127, 208, 308, 427, 565, 726, 910, 1118, 1351 für p = 2…10. Daraus folgt
  dim H^{5,2} = dim g₇ − 722 = 4.
- Die freie Richtung ist eine exakte ϑ-Eichsymmetrie: δΨ = f·(ρ∂_z − z∂_ρ)·DΨ. Ω ist eichinvariant.
- Das Symbol hat einen Lichtkegel q und zwei windschiefe Ebenen.
- H49 und H50 sind widerlegt.
- Nächster Schritt war: ϑ-Eichung, dann ein Involutions- bzw. Cartan-Test (erledigt, siehe unten).

## Eichung und Cartan-Test (nach r71, 3. November 2026)
- **Eichung (k136):** algebraisch, s(Ψ) = Ψ†K₂Ψ = S(x); Eichvektor v = ∂_ϑΨ ist gemeinsamer Kern aller J-Blöcke,
  Ω steht senkrecht auf v. Auf Symbolebene ist jede transversale algebraische Eichung gleichwertig:
  g'_p = g_p − C(p+3, 3) = 117, 188, 273, 371, 481, 606, 745 für p = 2…8.
- **H51 bestätigt (k137):** Das geeichte Symbol ist erstmals bei p = 6 involutiv; dim g'^{(k)}_6 = 481, 111, 14, 0.
  Keine freie Funktion von vier Variablen mehr; formal 14 Funktionen von drei Variablen.
- **Formale Integrabilität (H52, H53, beide ungültig):** Werkzeuge `k138_tps_d.py` (Reihen beliebigen Grades),
  `k140_fortsetzung_exakt.py` (Fortsetzungssystem mit exakter Linearisierung über symmetrische Sonden),
  `k140_f8_schritte.py` (große Systeme speichersparend in Einzelschritten).
  - Der gespeicherte 5-Jet ist nicht fortsetzbar (erfüllt die abgeleitete Ω-Bedingung der Ordnung 5 nicht); Grad 5
    frei lassen, nur den reparierten 4-Jet festhalten.
  - Über dem 4-Jet bis Grad 7 (F₇) stimmen die Fasern sauber mit g' überein (371, 481).
  - Mit Grad 8 (F₈) fällt P₅₆ von 852 auf 848: möglicherweise 4 versteckte Bedingungen an 6-Jets (passt zu
    H^{5,2} = 4). Das liegt aber auf der Fehlerhöhe der Grad-3-Linearisierung (1e-9).
- Nächster Schritt: Grad-3-Linearisierung genauer machen, dann H54 (4 Bedingungen an 6-Jets ja/nein) mit Vorab-Notiz.
- Fallstrick: Der Cloud-Container wird bei Untätigkeit zurückgesetzt; lange Läufe in Schritte unter 10 Minuten teilen
  und Zwischenergebnisse speichern. Volle SVD von 10⁴ × 10⁴ sprengt 8 GB, nur Singulärwerte rechnen.

## Fallstricke
- Für Rangentscheidungen aus Differenzenquotienten den Fünfpunkt-Stencil mit Schritt 1e-3 nehmen. Den Rang an der
  größten Singulärwertlücke ablesen, nicht an einer festen relativen Schwelle.
- Rekursive Spencer-Basen sind schlecht konditioniert; Symbole besser direkt aufbauen.
- Lie-Ableitungen von 1-Formen vollständig rechnen, nicht nur die kartesischen Koeffizienten ableiten.
- Ältere Skripte enthalten den festen Pfad `C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold`. Diesen nur in
  einer Arbeitskopie anpassen; neue Skripte bekommen den Datenordner als Argument.
