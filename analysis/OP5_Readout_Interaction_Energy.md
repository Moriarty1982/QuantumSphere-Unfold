# OP5: Ausleseprotokoll, Kopplungsenergie und erneuertes Reservoir

Datum: 26. Oktober 2026. Basisrevision: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Begrenzte analytische und endliche Zwei-Qubit-Vergleiche, keine native QAM-
Hamiltonherleitung, keine physikalischen Sekunden-/Joulewerte und keine
kosmologische Vakuumvorhersage.

## Ergebnis

Welche Observable wann und durch welche Kopplung ausgelesen wird, kann sowohl
den Folgezustand als auch den Energieaustausch ändern. Dieser Einfluss ist real
in einem festgelegten dynamischen Vergleichsmodell. Ein bloßer passiver Wechsel
der Darstellung bei gleichzeitig transformierten Zuständen, Hamiltonoperatoren
und Ausleseoperatoren ändert dagegen weder Wahrscheinlichkeiten noch Energie.

Die vorliegenden nativen Kanäle spezifizieren noch keine vollständige gemeinsame
Energiebilanz ihrer Kicks, Messgeräte, ausgetauschten Partner und Reservoirquelle.
Die fehlende Bilanz ist aber berechenbar, sobald diese Operatoren geliefert
werden. Ein expliziter Zweiqubit-Test zeigt die genaue Unterscheidung zwischen
energieerhaltendem Austausch, extern getriebener Auslese und verworfenem Meter.

## 1. Native Anker und begrenzte Aussagekraft

- r27, `sources/research/parts/v490-post-release-layers.tex:3823–3940`, schlägt
  Rotation plus kompensatorische Messung vor. Der Doubletzustand ist
  `rho=(I+b.sigma)/2`, `C_HC=(I+sigma_x)/2`; der Kick rotiert um sigma_y.
  Die Kopplung, physikalische Energie und der Messagent werden nicht daraus
  bestimmt. Die Rotation ist zunächst eine Zustandsoperation, keine vollständige
  Energiebilanz.
- r28, dieselbe Datei `:3991–4055`, realisiert Messung durch kontrollierte
  Kopplung und Austausch durch einen Partial Swap. Ein erneuerter Partner kann
  einen nichttrivialen stationären Zustand erhalten. Das sind ausdrücklich
  verschiedene Protokolle: geschlossener Meter, jeweils neues Gegenbild und
  fest präpariertes frisches Reservoir.
- r29, `:4135–4178`, zeigt, dass der eingehende Reservoirzustand nach dem Einsatz
  verändert ist; seine Polarisation muss ersetzt werden. Vakuumpaare werden als
  Quelle vorgeschlagen, aber Rate und Kohärenz bleiben offen. Die zu ersetzende
  Polarisation darf nicht ohne Hamiltonoperator als kostenfreie Energiequelle
  oder als Vakuumstress interpretiert werden.
- r31, `:4394–4419`, stabilisiert Markov-Flussfraktionen mit einer zusätzlichen
  Rückkehrrate. Das ist noch keine Energiestrom- oder Metrikvariationsgleichung.
- Native Beispielskripte:
  `notes/research/v4_10_0_r26_r31/llm/k64_dynamik_kick_messung.py` und
  `k65_messgeraet_tachyon_feld.py`. Sie liefern Kanal-/Zustandsoperationen,
  aber keinen daraus abgeleiteten vollständigen gravitativen Energieoperator.

H25 unterscheidet zusätzlich bilineare und hermitesche Vergleichsregeln.
Ein Vorzeichenwechsel eines bilinearen Readouts ist nicht automatisch ein
negativer Erwartungswert eines festgelegten hermiteschen Hamiltonoperators.
Die folgende Energiedefinition ist deshalb offen als Vergleich deklariert.

## 2. Die vollständige Pulsbilanz

Definiere System und Meter mit

\[
H_0=H_S\otimes I+I\otimes H_M,\qquad H(t)=H_0+V(t).
\]

Die Kopplung sei am Anfang und am Ende aus. Für die geschlossene unitäre
Entwicklung der beiden Systeme gilt direkt aus der von-Neumann-Gleichung

\[
\frac d{dt}\operatorname{Tr}(\rho H)
=\operatorname{Tr}(\rho\,\partial_t H),
\qquad
\Delta E_S+\Delta E_M=W_{\rm switch},
\]

mit `W_switch=int Tr(rho dV/dt)dt`. Während eines Pulses gehört auch
`E_int=Tr(rho V)` zur Gesamtenergie. Bei dauerhaft eingeschalteter Kopplung
darf dieser Anteil an den Endpunkten nicht weggelassen werden. Kommen weitere
offene Bäder hinzu, muss deren Energie-/Wärmebilanz ebenfalls aufgenommen werden.

Diese Identität sagt nicht, dass jede Messung denselben positiven Arbeitswert
hat. Das Vorzeichen und die Aufteilung werden von Hamiltonoperatoren,
Eingangszuständen, Kontrollpuls und Kopplungsprotokoll bestimmt.

## 3. Energieerhaltender Partial Swap

Verwende zwei identische Vergleichs-Qubits mit Energielücke omega>0:

\[
H_S=H_M=\frac\omega2(I+\sigma_z),\qquad
U_\theta=\cos\theta I-i\sin\theta\,\mathrm{SWAP}.
\]

Weil SWAP mit H0 kommutiert, gilt exakt Delta E_S+Delta E_M=0. Bei einem
einfachen eingeschalteten und wieder ausgeschalteten SWAP-Puls ist die gesamte
Schaltarbeit null: der Erwartungswert des SWAP-Generators ist während dieses
Pulses konstant, sodass Ein- und Ausschaltbeiträge sich aufheben.

Für einen Produktinput `rho tensor sigma` ist der reduzierte Systemzustand

\[
\rho'_S=\cos^2\theta\,\rho+\sin^2\theta\,\sigma
             +i\cos\theta\sin\theta[\rho,\sigma].
\]

**Eigenes Gegenbild.** Sind die beiden Blochvektoren b und -b, kommutieren die
Zustände und der Ausgangsvektor ist `cos(2theta)b`, genau die radiale Form des
r28-Modells. Der Verlust von Systemenergie erscheint dabei als Zunahme der
Meterenergie. Im getesteten Beispiel b=(sqrt(3)/2,0,1/2), theta=pi/6 und omega=1:

\[
\Delta E_S=-0.125,\qquad \Delta E_M=+0.125.
\]

Das frische eigene Gegenbild für jeden neuen Systemzustand ist kein festes
thermisches Bad. Seine jeweils neue Präparation ist eine zusätzliche Ressource.

**Festes thermisches Vergleichsbad.** Für einen jeweils frischen diagonalen
Gibbsinput `sigma=diag(p,1-p)` ist der Energie-Kommutatorbeitrag null und

\[
E'_S=\cos^2\theta E_S+\sin^2\theta\,\omega p.
\]

Der stationäre Systemwert ist omega p, festgelegt durch das gewählte Bad.
Für p=0.2, theta=pi/6 und anfängliche E_S=0.75 ergibt der 160-Schritt-Test
E_S=0.200000000000003 und summierte Meteraufnahme 0.550000000000269.
Das ist eine offene Badpräparation mit bekanntem Energieabfluss, keine
aus der Frame-Notation bestimmte Vakuumenergie.

**Geschlossener endlicher Meter.** Derselbe Meter wird nicht nach jedem Einsatz
verworfen oder ersetzt. Anfang: System im Grundzustand, Meter angeregt,
theta=pi/4. Nach n gleichen Pulsen gilt

\[
E_S(n)=\omega\sin^2(n\theta),\qquad E_M(n)=\omega-E_S(n).
\]

Die getestete Folge E_S/omega ist `0, 1/2, 1, 1/2, 0`. Ein einzelner endlicher
Partner gibt daher ohne weitere Entkopplung/Erneuerung keine monotone
Thermalisierung. Die Rückkehr ist ein konkreter negativer Kontrollfall gegen
die Verwechslung von geschlossenem Partner und fortlaufend frischem Reservoir.

## 4. Eine zeitabhängige Auslese kann Energie zuführen oder entziehen

Behalte `H_S=omega(I+sigma_z)/2`, setze für den Vergleich `H_M=0` und wähle
eine nichtenergetische Messachse `N=(sigma_x+sigma_z)/sqrt(2)`.
Ihre Projektoren sind P_+=(I+N)/2 und P_-=(I-N)/2.

Die nichtselektive Auslese ist

\[
\mathcal D_N(\rho)=P_+\rho P_++P_-\rho P_-.
\]

Für einen Blochvektor b wird daraus `(b.n)n`. Beginne mit
`b0=(sqrt(3)/2,0,1/2)` und lasse den Zustand vor der Auslese unter H_S bis zur
Phase phi=omega t frei präzedieren. Seine Energie bleibt dabei zunächst 3omega/4.
Die anschließende Auslese ändert sie um

\[
\boxed{\Delta E_S=\frac\omega8(\sqrt3\cos\phi-1)}.
\]

| Auslesephase phi | Delta E_S / omega |
| --- | ---: |
| 0 | +0.0915063509461 |
| pi/2 | -0.1250000000000 |
| pi | -0.3415063509461 |

Hier ändert also bereits der Auslesezeitpunkt bei festem Hamiltonoperator,
fester Achse und gleicher Ausgangsenergie den Energieaustausch einschließlich
seines Vorzeichens. Das ist eine tatsächliche Protokolländerung, kein bloßer
Framewechsel des gleichen Experiments.

### Wo die Energie im Messmodell herkommt

Präpariere den Meter in |0> und implementiere die Auslese als Prä-Messung

\[
U=P_+\otimes I+P_-\otimes\sigma_x.
\]

Nach Weglassen des Meters ist der Systemkanal exakt D_N. Eine ausdrücklich
kontrollierte endliche Pulsrealisierung mit Dauer tau verwendet

\[
K=\frac\pi{2\tau}P_-\otimes(I-\sigma_x),\qquad
V=K-H_0
\]

während des Pulses; außerhalb ist V=0. Der externe Controller kompensiert in
diesem Beispiel H0 während des Pulses, damit der Gesamtgenerator K und somit
`exp(-i tau K)=U` ist. Dieser Controller ist reale Zusatzstruktur des Vergleichs,
keine aus QAM hergeleitete kostenfreie Operation.

Da K mit U kommutiert, ergibt sich aus den beiden Sprüngen

\[
W_{\rm on}=\operatorname{Tr}(V\rho_{\rm in}),\quad
W_{\rm off}=-\operatorname{Tr}(V\rho_{\rm out}),\quad
W_{\rm on}+W_{\rm off}=\Delta E_S+\Delta E_M=\Delta E_S.
\]

Der Meter hat hier absichtlich degenerierte Energie und Delta E_M=0; er kann
trotzdem Information/Korrelationen aufnehmen. Positive Systemenergie wird vom
Controller geliefert, negative wird von ihm aufgenommen. Die verglichene
Auslese erzeugt daher keine freie Energie.

Für eine Messachse, die mit H_S kommutiert, bleibt die Systemenergie unter
diesem nichtselektiven Kanal dagegen unverändert. Ein endlicher Kontrollapparat
kann dennoch eigene Kosten haben; aus Delta E_S=0 folgt keine universelle
Kostenfreiheit seines gesamten Betriebs.

## 5. Wiederholung, Aufzeichnung und Reset sind eigene Vorgaben

Im letzten Modell ist U²=I. Solange der Meter nicht weggeworfen und kein
unabhängiger irreversibler Datensatz erzeugt wird, macht ein zweiter identischer
Puls die gemeinsame Prä-Messung rückgängig. System, Meter und Korrelationen
kehren zum Ausgang zurück; die summierte Schaltarbeit ist null. Das ist eine
unitäre Rücknahme der Prä-Messung, keine kostenlose Löschung einer dauerhaft
extern gespeicherten klassischen Messgeschichte.

Für fortlaufend frische Meter oder Reservoirzustände muss ihre Präparation/
Rücksetzung mitgerechnet werden. Welche Arbeit und Wärme dabei auftreten,
hängt von Meter-Hamiltonoperator, Bad, Temperatur, Korrelationen, erlaubtem
Zugriff und Zielzustand ab. Der reine Kanal legt keinen universellen Resetpreis
fest. Hier wird daher insbesondere kein pauschaler Landauer-Wert eingesetzt.

## 6. Was dies für OP5 und einen gravitativen Vakuumterm bedeutet

Die Auslesereihenfolge und das Zeitprotokoll müssen Teil des erweiterten
Zustands-/Operationsvertrags sein. Ein stationärer offener Kanal kann nur dann
als energetisch stationär gelten, wenn System, frische Partner, Quelle und
Kontrollarbeit zusammen bilanziert werden. Gleiche lokale Messwahrscheinlich-
keiten oder stationäre Populationen garantieren keine verschwindenden Ströme.

Die Zuordnung zu Lambda bleibt eine weitere Frage: Eine konstante stationäre
Erwartungsenergie eines ausgewählten Vergleichs-Hamiltonoperators liefert
allein weder die räumlichen Spannungen noch eine Metrikvariation. Der Stress
der Quelle, Geräte und Kontrollen gehört in eine gemeinsame Wirkung; er darf
nicht durch Weglassen zum skalaren Vakuumterm erklärt werden.

Schließlich bleiben die Protokolldaten gegen einen gemeinsamen Energieshift
blind: `H_S->H_S+C I` ändert normierte Wahrscheinlichkeiten und Energiedifferenzen
nicht. Der Skripttest prüft dies für C=2.3. Ein gravitativer Volumenterm mit
derselben absoluten Dichte verändert dagegen die Metrikgleichung. Die Bilanz
der Kopplungsarbeit behebt daher nicht automatisch die C-Unbestimmtheit aus
`OP5_Native_Pair_Potential_Audit.md`.

## Rechnung und Grenzen

Kommando:

```powershell
python -B analysis/OP5_Readout_Interaction_Energy_Check.py
```

Ausgeführt mit Python 3.12.10 und NumPy 2.5.2 in der vorhandenen Umgebung. Geprüft wurden die
vollständigen 4x4-Unitaries und Teilspuren, die reduzierten Kanäle,
Energieerhaltung jedes Thermalbad-/Gegenbild-Kollisionsschritts, endliche
Meterrevivals, der Badfixpunkt, die drei Zeitphasen, Ein-/Ausschaltarbeit und
Shift-Invarianz. Numerische Toleranz 3e-13, für die Annäherung an den Fixpunkt
1e-9; alle Assertions bestanden. Die angegebenen universellen Identitäten
folgen aus den dargestellten Matrizen, nicht aus der endlichen Fallzahl.

Es wurden keine nativen Energieoperatoren, Thermostattemperaturen,
Reservoir-Erzeugungsraten, physikalischen Sekunden oder gravitativen
Gegenterme aus Daten bestimmt. Die Beispiele liefern konkrete Kontrollen für
die zukünftige native Energiebilanz, nicht deren vorweggenommenes Ergebnis.

SHA256 bei diesem Lauf:

```text
OP5_Readout_Interaction_Energy_Check.py 7FD5DD8BF98E312BCEF61B55CE00F766DC71D69304B4AD57E9E692074075BD3A
k64_dynamik_kick_messung.py 365DC659F87780F319D9D1A12722A50C3A6D5D11BD9C57D5CD2E1B627C5E4C6B
k65_messgeraet_tachyon_feld.py 6A9ADE6046842FD4B33B5FEF86BED2D9E96F693DCCE939A6ED434841DB26F86D
```
