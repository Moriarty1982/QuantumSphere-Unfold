# Guard-Prüfung im Datenstrom

Der [HDL-Baustein](guard_stream.sv) bekommt je Kandidat eine 32-Bit-ID und zwei 2-Bit-Masken für die H117-Zulässigkeit. Bit 0 steht für die positive Orientierung, Bit 1 für die negative. Auf den Ausgang gehen ID und Richtung genau dann, wenn nach dem bitweisen Schnitt genau eine Orientierung bleibt. Gesperrte und mehrdeutige Fälle werden separat gezählt. Ein registrierter Ausgabeslot puffert einen Treffer und hält ihn bei Rückstau stabil. Bei freiem Ausgang nimmt der Baustein gleichzeitig mit einer Ausgabe den nächsten Kandidaten entgegen.

## Lauf in WSL mit Icarus 10.3

~~~sh
python3 -m qam.examples.zuse_machine.hdl.guard_stream_check --rows 65536
~~~

Die Testbench erzeugt die Kandidaten fortlaufend im Simulator und spielt jedes der 16 Maskenpaare gleich häufig aus. Sie akzeptiert auch eine Vektordatei für Randfälle. MMA liefert die Referenz für die vier möglichen Eingabepaare einer einzelnen Orientierung. Daraus wird jede erwartete Entscheidung für die zwei Orientierungen aufgebaut. Der Vergleich prüft IDs, Reihenfolge, Vorzeichen und getrennte Zähler. Zwei Läufe prüfen einen immer bereiten und einen periodisch blockierten Empfänger. Im Rückstauversuch sind zwei Takte frei und drei gesperrt. Die Zusatzfälle umfassen den leeren Strom, beide Ausgaberichtungen, die größte 32-Bit-ID und wiederholte IDs.

| Empfänger | Eingang | Eindeutige Ausgaben | Gesperrt | Mehrdeutig | Takte | Kandidaten/Takt |
|---|---:|---:|---:|---:|---:|---:|
| Bereit | 65.536 | 24.576 | 36.864 | 4.096 | 65.536 | 1 |
| Mit Rückstau | 65.536 | 24.576 | 36.864 | 4.096 | 102.397 | 0,640019 |

Der synthetische Strom ergibt **62,5 % weniger Ausgabedatensätze**. Gezählt als logische Nutzlast aus 36 Eingangsbits und 33 Bits je ausgegebenem Treffer sinkt die Menge von 2.359.296 auf 811.008 Bit, also um **65,625 %**. Zähler, Paketierung und Bussignale sind eigene Kosten. Der Benchmark nutzt einen in der Testbench erzeugten Strom. Der Vergleich der Nutzlast ist eine Rechnung aus den erfassten Übergaben, keine Messung eines physischen Busses.

Icarus verarbeitete den bereiten Lauf mit rund 118.500 Kandidaten pro Sekunde einschließlich Ausgabe, im Rückstauversuch rund 105.300. Das sind Simulatorwerte. Für ein physisches FPGA ergeben sich Kandidaten pro Sekunde aus der erreichten Taktfrequenz und den Kandidaten pro Takt. Ein Boardlauf mit Takt- und Transfermessung steht aus.

Die 209 bisherigen MMA-/HDL-Referenzfälle bestanden separat. Yosys 0.9 meldete null Strukturprobleme und 2.113 generische Zellen für den neuen Baustein einschließlich der vier 64-Bit-Zähler. Der Lauf zählt generische Logik vor dem Mapping auf ein konkretes FPGA.

## Tatsächliche Ausgaben

Icarus/MMA-Testtreiber:

~~~json
{
  "mma_guard_cases": 4,
  "mask_pairs": 16,
  "edge_cases": 4,
  "reference_ms": 27.57,
  "streams": {
    "ready": {
      "cycles": 65536,
      "accepted": 65536,
      "selected": 24576,
      "blocked": 36864,
      "ambiguous": 4096,
      "candidates_per_cycle": 1,
      "input_payload_bits": 2359296,
      "output_payload_bits": 811008,
      "output_record_reduction_pct": 62.5,
      "payload_reduction_pct": 65.625,
      "icarus_ms": 553.118,
      "icarus_candidates_per_second": 118485
    },
    "backpressure": {
      "cycles": 102397,
      "accepted": 65536,
      "selected": 24576,
      "blocked": 36864,
      "ambiguous": 4096,
      "candidates_per_cycle": 0.640019,
      "input_payload_bits": 2359296,
      "output_payload_bits": 811008,
      "output_record_reduction_pct": 62.5,
      "payload_reduction_pct": 65.625,
      "icarus_ms": 622.4,
      "icarus_candidates_per_second": 105296
    }
  },
  "compile_ms": 35.62
}
~~~

Wolfram prüfte die unabhängige Auszählung mit `Counts[Flatten[Table[BitAnd[a,b],{a,0,3},{b,0,3}]]]` und multiplizierte jede Klasse mit 4096. Die Nutzlastschranke folgt aus `1-(24576*33)/(65536*36)`.

~~~text
During evaluation of In[1]:= Wolfram: 15.0.1 for Linux x86 (64-bit) (July 2, 2026)
During evaluation of In[1]:= Counts by persistent mask 0..3: {9, 3, 3, 1}
During evaluation of In[1]:= 65536 uniform cases, counts by mask: {36864, 12288, 12288, 4096}
During evaluation of In[1]:= Raw ingress and selected egress bits: {2359296, 811008}
During evaluation of In[1]:= Relative egress payload reduction: 21/32

Out[1]= Null
~~~

Yosys `synth -noabc -top guard_stream; check -assert; stat`, relevanter Ausschnitt:

~~~text
4. Executing CHECK pass (checking for obvious problems).
checking module guard_stream..
found and reported 0 problems.

5. Printing statistics.

=== guard_stream ===

   Number of wires:                269
   Number of wire bits:           2161
   Number of public wires:          17
   Number of public wire bits:     334
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:               2113
     $_AND_                        460
     $_DFF_P_                      290
     $_MUX_                       1094
     $_NOT_                          4
     $_OR_                           6
     $_XOR_                        259
~~~
