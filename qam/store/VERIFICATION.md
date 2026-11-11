# Automatische Matrixprüfung

Der erste Prüfer rational-projector-commutator-v1 prüft konkrete registrierte Seeds. Er verwendet rationale Arithmetik mit Fraction. Unterstützt werden quadratische Matrizen mit 1 bis 32 Zeilen. Einträge sind JSON-Ganzzahlen oder Zeichenketten wie "-2/3" mit höchstens 256 Zeichen. Fließkommazahlen, Nullnenner und uneinheitliche Zeilenlängen werden zurückgewiesen.

## Eingaben und Aufruf

Zuerst werden eine Definition und Seeds über STORE registriert. Die Seeds benötigen value_type rational-matrix und als value eine verschachtelte Zeilenliste. Ihre Interpretationsdefinition muss registriert und im gleichen deklarierten Frame sein. Die Definition beschreibt den Kontext als Text. Ihre semantische Übereinstimmung mit den Matrixeinträgen wird separat geprüft.

Eine Anfrage enthält projector als Versionshash und optional transport als zweiten Versionshash.

```json
{
  "projector": "HASH_DER_PROJEKTORVERSION",
  "transport": "HASH_DER_TRANSPORTVERSION"
}
```

```powershell
python -m qam.tools.store_db verify --request check.json
python -m qam.tools.store_db receipt --hash BELEGHASH
```

Optional legt --db eine andere Datenbank fest. verify liefert einen JSON-Beleg. passed bedeutet P²=P und bei angegebenem Transport zusätzlich MP=PM. failed bedeutet eine nichtverschwindende exakte Residualmatrix. blocked bedeutet, dass die konkreten Eingaben nicht geprüft werden konnten, etwa wegen falscher Dimension, fehlendem Frame oder ungültiger Matrixdarstellung. failed und blocked liefern Prozesscode 1, erhalten aber ihren Beleg. Ein syntaktisch ungültiger Anfragevertrag wird vor der Rechnung abgewiesen.

## Beleg und Geltungsbereich

Schema v3 ergänzt qstore_checks und qstore_check_inputs. Der Beleg enthält die genaue Anfrage, die überprüften Seed- und Definitionsversionen, Quellenmetadaten, Python-Version, Prüferkennung und SHA256 des Prüfer- und Registrierungscodes. Er protokolliert Residuen, Fehler und offene Voraussetzungen. Eingabeversionen sind zusätzlich für spätere Auswirkungsabfragen indexiert. Die Belegabfrage prüft den SHA256 des gespeicherten Inhalts. Identische Eingaben und derselbe Prüfkontext erzeugen denselben Beleg.

Versionshashes werden vor Verwendung erneut aus Identität, Typ, Frame, Status und Payload gebildet. Bereits registrierte Quellenstände bleiben im Beleg erhalten; der Prüflauf rechnet mit den unveränderlichen registrierten Werten und setzt keine Übereinstimmung mit inzwischen geänderten Quelldateien voraus. Annahmen der Seeds und Definitionen sowie registrierte offene oder fehlgeschlagene Guards an den Eingabeversionen werden mitgeführt. Ein erneuter Lauf nach geänderten Guards kann deshalb einen neuen Beleg ergeben.

passed zertifiziert ausschließlich die genannten endlichen Matrixgleichungen. Orthogonalität des Projektors, physikalische Zulässigkeit, T_N, LaTeX-Übersetzung und native OP-Closure sind zusätzliche Verpflichtungen. Der Prüfer verändert weder Aussage- noch Reviewstatus und schließt Guards nicht automatisch. Die Store-Belege haben ein eigenes Format; sie werden nicht als bereits vorhandene MMA-Belege ausgegeben.

## Regressionen

```powershell
python -m unittest qam.store.test_orm qam.store.test_registry qam.store.test_matrix_check
```

Die Beispiele werden in temporären Datenbanken angelegt. Geprüft werden ein rationaler Projektor, ein kommutierender und ein nichtkommutierender Transport mit handprüfbarem Residuum, ungültige Fließkomma- und Matrixeingaben, fehlende Versionen, Dimensionsfehler, offene Guards, Unveränderlichkeit und Wiederholung der Belege sowie alte Belege nach neuer Seedversion. Der CLI-Pfad wird für passed und failed einschließlich Prozesscodes ausgeführt.

## Dauerhaftes Vergleichsbeispiel

python -m qam.tools.store_example registriert die Definition und drei rationale Seeds aus qam/store/matrix_example.json im eigenen Frame store-matrix-comparison. Anschließend prüft es P²=P mit einem kommutierenden und einem nichtkommutierenden Transport und liest die gespeicherten Belege zur Hashkontrolle zurück. --db ermöglicht eine getrennte Vergleichsdatenbank.

Der deklarierte Projektor ist [[1/2,1/2],[1/2,1/2]]. Der Transport [[5/4,3/4],[3/4,5/4]] kommutiert damit. Beim Kontrolltransport diag(1,2) ist MP−PM gleich [[0,−1/2],[1/2,0]]. Der Lauf erwartet daher einen bestandenen und einen fehlgeschlagenen Beleg. Beide behalten die offene physikalische Interpretation als Voraussetzung. Das Beispiel ist ein explizit deklarierter Vergleichsbestand.

Die lokale Ausführung am 11. November registrierte vier Objekte und zwei Prüfbelege. Ein identischer zweiter Lauf ließ das Ledger unverändert. Eine Kopie des Repositorys kann den Bestand mit diesem Befehl aus den versionierten Quellen wiederaufbauen.
