## locations

Orte zur Aufgabe, Übergabe und letztlich Annahme sind 'locations', die immer einen Namen und Besitzer haben und

*   eine Adresse
*   und oder eine Geo Koordoanten

Meistes sind locations feste Orte (Geschäfte, Warenlager) können aber auch fliegende locations sein. Es genügt nicht das Ort nur Koordinaten sind, da z.B. an einer Haustüre auch mehrere User wohnen können.

## userstate

Transporte können entweder gerade unterwegs sein (carry), auf Abholung warten (getit), wartend (passv) oder ausgeliefert (close) sein. Die Status der Transport hängen an den Userstatus, diese sind ähnlich dem Transportstatus, aber der user hat noch die Möglichkeit das er gerade nur Pakete an sich annehmen will (keine zur Weiterleitung) oder alle nur soch die vorhandenen abgeben will.

    User     : Transport
    -----------------
    sleeping : sleep
    carrying : carry
    hubbing  : hubbing
    flooding : flood
    grabbing : sleep
             : close


## Glossar

* __currentHolder__: Ist immer der jenige der eine Sendung gerade physisch besitzt. Das kann der Versender, der Empfänger, ein Transporteur oder ein Zwischenhalt (hub) sein. 
* __distance2destination__: sagt wie weit ein Transport von seinem ziel weg ist, das brauchen Transporteure um abschätzen zu können ob er ein Pakerl in der nachbarschaft austragen soll, oder eins das an eine überlandhub richtig hamburg soll. Nach distance2destination kann man in der trasnportliste filtern. (zeige mir alle Transport mit weniger als 1 km abstand zum Ziel)


