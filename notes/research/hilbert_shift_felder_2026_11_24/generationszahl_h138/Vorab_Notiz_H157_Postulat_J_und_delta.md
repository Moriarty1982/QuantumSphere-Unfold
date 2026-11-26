# Vorab-Notiz H157: Was folgt aus dem Postulat (Tausch J als Symmetrie) für δ?

**26.11.2026, vor jeder Rechnung committet.** Anlass: nach H156 nimmt der Autor vorerst das Postulat an: Materie-Frame und Tachyon-Frame sind gleichberechtigt, der
Tausch J (ψ ↦ Uψ̄) ist eine Symmetrie der Wirkung. Auftrag: damit weiterrechnen. Mit J ist K = ⅔ gesichert (H155a, H156). Offen ist der Phasenwinkel δ (Fit 2/9).
Vorzeichen werden nicht gesetzt. Vergeben: H157, Skripte k340 (Python) und k340b (Wolfram). Qiskit nicht vorgesehen (keine Schaltung). Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H155 (k338): mit J-symmetrischen Massen und Quartiken liegt das Minimum bei θ = π/4; ζN(W) verschiebt K; δ = 2/9 braucht einen Fit R* = −0,00758.
- H156: J ist eine Isometrie, kein Automorphismus; μ_A² = μ_B² nur aus J als Postulat. Z₄ ließe φy(y² − φ²) zu, ⟨J⟩ und D₄ passen.
- H152: voller Ansatz liefert δ nur in {0, π/3}; H149: θ = π/4 Fixpunkt des Tauschs, δ = 2/9 bleibt Fit.
- N(W) = φ³/(3√3) − φB/(2√3) + C₃/(3√6) mit C₃ = y₁³ − 3y₁y₂² (k336–k338).

## Vorüberlegung (vor der Rechnung)
Im Drei-Felder-Modell (φ, y₁, y₂) kann J nicht als lineare Isometrie einen Freiheitsgrad (φ) mit zwei (y₁, y₂) tauschen. Lesart des Postulats: J wirkt in jeder Ebene
span{1, n(δ)} durch das Vakuum, mit y = r·n(δ), als φ ↔ r bei festem δ. Ein Z₃⋊Z₂-invariantes Polynom P(φ, R = r², C₃ = r³c), c = cos 3δ, ist J-erlaubt, wenn
P(φ, r², r³c) = P(r, φ², φ³c) identisch in φ, r, c gilt. Monom φ^a R^b C₃^k gibt φ^a r^(2b+3k) c^k; der Partner braucht a ≥ 3k und a ≡ k (mod 2).
Daraus vorab: alle erlaubten Terme haben gerade Ordnung; der niedrigste cos3δ-Term ist φ³C₃ (Ordnung 6), der niedrigste cos²3δ-Term φ⁶C₃² (Ordnung 12).

## Hypothesen und Kriterien
- **H157a (nicht blind, Lesart):** Die H155-Form (gleiche Massen, gleiche λ, κ frei) erfüllt die Ebenen-Lesart; N(W) verletzt sie in jeder Ebene (enthält φ³ ohne
  Partner). Folgerung: ζN(W) ist unter dem Postulat verboten, also auch der H155-Fit über N(W). *Kriterium:* symbolischer Rest.
- **H157b (gewertet):** Aufzählung aller Z₃⋊Z₂-invarianten Polynome bis Ordnung 12, eingeschränkt auf die Ebene, und Bestimmung des J-erlaubten Unterraums je Ordnung
  und je Potenz k von cos 3δ. Vorhersage: (i) keine ungerade Ordnung erlaubt; (ii) k = 1 zuerst bei Ordnung 6 (nur φ³C₃); (iii) k = 2 zuerst bei Ordnung 12 (nur φ⁶C₃²).
  *Kriterium:* Dimensionen aus zwei unabhängigen Wegen (Python über Erzeuger φ, R, C₃; Wolfram über allgemeine Polynome in φ, y₁, y₂ mit direkter Invarianzforderung)
  stimmen überein, und (i)–(iii) gelten. Abweichung in einem Punkt heißt widerlegt.
- **H157c (gewertet):** Folge für δ. Mit erlaubten Termen bis Ordnung 10 hängt V bei festem (φ, r) linear von cos 3δ ab, also δ ∈ {0, π/3} (mod 2π/3) in jedem Minimum.
  Erst mit Ordnung 12 sind innere Werte möglich; δ = 2/9 braucht dann ein Verhältnis ζ₁₂/ζ₆ und eine Skala, also einen Fitparameter. Schätzung vorab bei Einheits-
  koeffizienten: Λ/v ≈ 0,76. *Kriterium:* Zufallsstichprobe (Koeffizienten aus [−1, 1], beschränkender Term positiv), volle Minimierung in (φ, y₁, y₂):
  bis Ordnung 10 alle Minima mit |sin 3δ| < 1e-5; mit Ordnung 12 Anteil innerer δ > 0. Angabe des Anteils mit θ = π/4 (spontane J-Brechung möglich, nicht gesetzt).
- **H157d (Lesart, nicht blind):** Massenspektren an den Endpunkten bei K = ⅔: δ = 0 gibt [1; 0,0147; 0,0147], δ = π/3 gibt [1; 0,0589; 1] (vor der Notiz ausgerechnet,
  daher nicht blind). Vergleich mit den Leptonen (m_μ/m_τ = 0,0595, m_e/m_τ = 2,9e-4): kein Endpunkt hat drei verschiedene Massen; die Nähe 0,0589 ↔ 0,0595 wird nur
  benannt, nicht gewertet.

## Grenzen
- Ebenen-Lesart des Postulats im Drei-Felder-Modell; die Wirkung von J auf 𝕆 bzw. 𝕊 jenseits der Ebene wird nur benannt.
- Baumniveau für δ; das Laufen der Ordnung-6- und -12-Kopplungen wird nicht gerechnet.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard wird berührt.
