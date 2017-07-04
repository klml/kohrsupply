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


## Lizenz

Die Lizenzen der contentClass sind von 

* [U+267A](//commons.wikimedia.org/wiki/File:U%2B267A.svg) (gemeinfrei)
* [Rpb_clothing_icon](//commons.wikimedia.org/wiki/File:Rpb_clothing_icon.svg) (CC 0)
* [Ravintola_724_tunnusosa](//commons.wikimedia.org/wiki/File:Ravintola_724_tunnusosa.svg) (gemeinfrei)
* [Community_Noun_project_2280](//commons.wikimedia.org/wiki/File:Community_Noun_project_2280.svg) T. Weber, from The Noun Project
* [Symbol_solid_precipitation_70](https://commons.wikimedia.org/wiki/File:Symbol_solid_precipitation_70.svg) (gemeinfrei)
* [Symbol_solid_precipitation_73](https://commons.wikimedia.org/wiki/File:Symbol_solid_precipitation_73.svg) (gemeinfrei)
* [Octicons-package](//commons.wikimedia.org/wiki/File:Octicons-package.svg) ( MIT/SIL license v2.0.1)
* [Trash_Can_23](//commons.wikimedia.org/wiki/File:U%2B267A.svg) (gemeinfrei)

