# Mitmachen

Wie kann man bei [kohr.supply](/about/) __mitmachen__?
Generell braucht man ein [Nutzerkonto](/signup).

## Lieferant
![carrying](//img.klml.de/devel/ptap/ptap_carrying__80.png#right)
Wer Lieferungen ausliefern will:

* stellt rechts oben seinen carrierestatus auf 'carrying'
* sucht auf der [Übersicht offener Tranporte](/) in <a href="#" class="getlocal">seiner Nähe</a> oder [filtert passenden Transporte](#filter)
* holt sich eine oder mehrere Lieferungen ab 
* Übernimmt den Transport mit dem Button "I take this transport"
* sucht sich einen **Hub** der sinnvoll in Richtung des Ziels liegt
* und übergibt dort die Sendung und achtet darauf das der (Zwischen)-Empfänger die Lieferung auch übernimmt.

## Hubbing
![hubbing](//img.klml.de/devel/ptap/ptap_hubbing__80.png#right)

Wer Lieferungen bei sich umschlagen will:

* stellt seinen carrierestatus auf 'hubbing'
* checkt in seiner aktuellen [location](/locations) ein 
* wartet auf Lieferanten die Lieferungen bringen
* Übernimmt den Transport mit dem Button "I take this transport"
* wartet auf andere Lieferanten die Lieferungen abholen
* und übergibt diesem die Sendung und achtet darauf dass der neue Lieferant auch die Lieferung übernommen hat.


Wer als Hubber seine aktuellen Lieferungen los werden will, stellt seinen Status auf 'flodding'.

## Nur Senden oder Empfangen
![flooding](//img.klml.de/devel/ptap/ptap_flooding__80.png#right)
![grabbing](//img.klml.de/devel/ptap/ptap_grabbing__80.png#right)

Wer ganz klassische Lieferungen senden oder empfangen will, der:

* checkt in seiner aktuellen [location](/locations) ein
* ein __Sender__ stellt seinen carrierestatus auf 'flooding'
    * erstellt einen neue [Lieferung](/transport/edit/)
    * und wartet auf einen Lieferanten.
* ein __Empfänger__ stellt seinen carrierestatus auf 'grabbing' 
    * und wartet auf einen Lieferanten.
    * 'closed' dann die Lieferung

Wer gar nicht mehr teilnehemen will stellt sich auf __sleeping__ ![sleeping](//img.klml.de/devel/ptap/ptap_sleeping__15.png).

<h2 id="filter">Filtern</h2>

Bisher gibt es folgende Filtermöglichkeiten:

* [?class=nonfood](/?class=nonfood) schränkt auf Contentklassen (food, nonfood, people, etc) ein.
* [?lat=48.1&lon=11.6&wide=6](/?lat=48.1&lon=11.6&wide=6) begrenzt den geographischen Suchbereich.

Da gibt es noch viele gute Ideen, z.B. [Transport in eine bestimmte Richtung](//github.com/klml/kohrsupply/issues/8).
Weitere Vorschläge gern auf [github.com issues](//github.com/klml/kohrsupply/issues).