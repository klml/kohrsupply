# kohr.supply

**kohr.supply** ist eine Crowd Logistik Anwendung um Sendungen von Personen an Personen zu befördern.  
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

Warum sollte kohr.supply funktionieren, es gibt doch viele andere [alternative Logistikansätze](http://regionales-wirtschaften-wiki.de/Netzlogistik_Abgrenzung)?

Neben der Eigenschaft dass kohrsupply p2p ist und "Logistiklaien" ansprechen will ist vor allem wichtig das kohrsupply sich darauf konzentriert auch die einzelne Übergaben innerhalb der SupplyChainan fokusiert.

Einen sehh  ähnlichen und schon wesentlich weiter implementierten Ansatz hat [PassLfix](http://pacifics.org/). PassLfix setzt vor allem auf die Blockchain. Ehrlich gesagt kommt es mir so vor als ob die [gehypte](http://blog.fefe.de/?q=Blockchain) bei der dezentralen Verfolgung von Paketen zum ersten mal richtig Sinn macht.
Aber PassLfix setzt hier imho auf die technisch-mathematische Lösung des sozialen Vertrauensdefizits innerhalb einer dezentralen SupplyChain. kohrsupply will das lieber mit menschlichen [Vertrauensmechanismen](https://github.com/klml/kohrsupply/issues/1) lösen.


## Routing

kohrsupply macht kein Routing. Das kann gern jemand  per API anhängen. Aber erst mal gibt es nur klassiches Routing mit Ortsnamen auf der Karte oder per Postleitzahl.
