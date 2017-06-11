# kohr.supply

**kohr.supply** (Peer2PeerTrAnsport) ist eine Crowd Logistik Anwendung um Sendungen von Personen an Personen zu befördern.  
Das wichtigste dabei: auch die Beförderung von Teilstrecken sind möglich und sogar wichtig

User können entweder

*   Sendungen befördern (Status des Users und der Sendung 'carry'), jemand der transportiert muss nicht sagen wohin
*   Sendungen anbieten, dann sind die Status
    *   Sendung ist getit
    *   User ist 'hubing nehme alle' (fetal) oder 'hubing aber nur abgeben' (flood)

User du nur Ihre Pakete annehmen wollen sind 'ich nehme nur an mich an' (fetmy)

## Wer wie was

kohrsupply ist ein Tool. Was ihr damit macht ist eurer Kreativität überlassen. Ob ihr Essen auf Rädern in der Nachbarschaft organisiert oder einen alternativen [deliverooo](https://deliveroo.de) aufmacht. Ob ihr Getränke an der Isar oder auf einem Festival routet, oder Umzugs Kartons als Mitfaherzentrale nach Hamburg mit nehmt, uns egal. Ob ihr das als nebenberufliche Geldquelle macht oder [Schenker](https://schenker.com) seit, alles cool. Ob ihr aus gamification [Punkte](./reputation) sammelt wie pokemon go oder einfach die Schönheit von effizienter Logistik liebt. kohrsupply ist das Internet für reale Güter, so wie das Internet mal gebaut war. Als Ort für Gleiche, clients oder citicens. Das bedeutet auch das man scheiß bauen kann.

### warum

Warum sollte ptpa funktionieren, es gibt doch viele andere [alternative Logistikansätze](http://regionales-wirtschaften-wiki.de/Netzlogistik_Abgrenzung)?

Neben der Eigenschaft dass kohrsupply p2p ist und "Logistiklaien" ansprechen will ist vor allem wichtig das kohrsupply sich darauf konzentriert auch die einzelne Übergaben innehhalb der SupplyChainan fokusi


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



## Routing

Wir machen kein Routing. Gern kann jemadn ein Routing per API anhängen. Aber erst mal klassiches Routing Ortsname oder per Postleitzahl.

## Funktionen und Featurewunsche

* Recipienst haben eine Location, die sie udpaten, wenn sie das tun wird die Sendung an dei jewils aktuelel lactiongeroutet (wer das nicht will muss sich sleeping stellen) 
* feature wunsch: user können Sendungen an unterschiedlicehn Loactions mepfangen (und sind nur auf grabbing wenn sie an der ziel Destination sind )
