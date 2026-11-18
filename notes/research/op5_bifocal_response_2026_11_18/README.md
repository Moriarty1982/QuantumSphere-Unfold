# Kristall-Schnittstelle: explizite bifokale Formantwort

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](Vorab.md), Commit e09950dbdf5ab035c8a3afdaefbaca38b99dccef. Der eingesetzte Quellenparameter u verändert den halben Brennpunktabstand von c auf c+u. Er ist keine physikalische Identifikation des M–T-Überschusses.

Im unverformten Chart x(t)=(a cos t,b sin t) sei G=d_-+d_+−2a. Am Ausgang ist die partielle Ableitung nach c gleich 2ac sin²t/(a²−c²cos²t); diejenige nach b ist 2ab sin²t/(a²−c²cos²t). Die Quellvariation ist gerade unter dem Gegenpunkt t↦t+π und für c>0 nicht identisch null. Eine starre Translation des Rands erzeugt dagegen den ungeraden Term ∇_xG·v. Durch Addition einer ungeraden Antwort lässt sich der gerade Quellterm nicht punktweise beseitigen.

Die Antwort b'(0)=−c/b beseitigt ihn überall. Exakt liefert b(u)=√(a²−(c+u)²) wieder G=0, solange |c+u|<a. Kontrolle auf 256 Punkten für a=√2, c=b=1: Beim Halbieren von u halbiert sich der unkompensierte maximale Defekt näherungsweise; mit b−cu/b fällt er quadratisch; mit der exakten Form liegt er bei Rundungsgröße.

Damit enthält die bekannte Chartgeometrie einen konkreten reparierenden Freiheitsgrad: die kleine Halbachse bei fester großer Halbachse. Er ist weder eine globale Dualitätsdrehung noch eine starre Verschiebung. Für OP5 bleibt zu klären, welcher native Zellübergang den Fokusabstand tatsächlich ändert, ob die passende Formantwort in Phase, P-Einbindung und Gesamtenergie zulässig ist, und ob ihrer Auslenkung eine eigene Rückstellenergie entgegensteht. Der geometrische Nullwert allein sagt nichts über Druck und H96. OP5 bleibt offen.
