# Voorstel concept map voor klinische domein DWH2.0

## Context
- Doel: Een domein model voor het klinische gedeelte, waarmee DWH2.0 op een effectieve en efficiënte manier predictive analytics kan ondersteunen op patiënt niveau
- Uitgangspunten: model is gebaseerd op relevant standaarden, met name zorginformatiebouwstenen, FHIR en Snomed CT
- Klinische model is zodanig generiek dat het alle informatie t.a.v. PROMs en klinische observabelen (oogmetingen, Kellgren score MRI) kan bevatten

## Concept map
Onderstaand tabel is een samenvatting van de mapping van de verschillende concepten

| voorstel DHW2.0 | ZIBS | FHIR | SnomedCT |
|:----------------|:-----|:-----|:---------|
|Meettraject      | n/a |[EpisodeOfCare](https://www.hl7.org/fhir/episodeofcare.html)| n/a |
|Meetmoment       |[GeplandeZorgActiviteit](https://zibs.nl/wiki/OverdrachtGeplandeZorgActiviteit(NL))|[Order](https://www.hl7.org/fhir/order.html)| n/a |
|Vragenlijst      | n/a  |[Questionnaire](https://www.hl7.org/fhir/orderresponse.html)|[Assessment scale (273249006)](http://browser.ihtsdotools.org/?perspective=full&conceptId1=273249006&edition=en-edition&release=v20170131&server=http://browser.ihtsdotools.org/api/snomed&langRefset=900000000000509007)|
|VragenlijstAntwoord | n/a |[QuestionnaireResponse](https://www.hl7.org/fhir/questionnaireresponse.html)|[Assessment using assessment scale (445536008)](http://browser.ihtsdotools.org/?perspective=full&conceptId1=445536008&edition=en-edition&release=v20170131&server=http://browser.ihtsdotools.org/api/snomed&langRefset=900000000000509007)|

* Een __episode__ bestaat uit een vooraf gedefinieerd behandelplan voor een patient. Kenmerken zijn o.a. diagnose, betreffende lichaamsdeel, operatietype. Binnen een zijn een of meerdere meetmomenten gedefinieerd, om op vooraf vastgestelde tijden dezelfde metingen uit te voeren.
* Tijdens een __meetmoment__ worden een of meerdere klinische observabelen bepaald. Dit kunnen objectieve observabelen zijn (b.v. visus meting) of een subjectieve, patient-reported afname van een vragenlijst
* In het geval van PROMs heeft een __vragenlijst__ vooraf gedefinieerde vragen en antwoord-categorieën. Een vragenlijst kan ook een specifieke scoringsmethodiek hebben, om het totaal resultaat te kwantifceren in een waarde.
* Een __vragenlijstAntwoord__ is een ingevulde vragenlijst.
* Naast bovengenoemde bestaat natuurlijk ook de entiteiten __klinieken__ en __patient__


## Implicaties voor doorontwikkeling van DWH2.0

Mapping van dit voorstel naar domeinmodel van TelePsy PromsManager en Interactive Studios OnlineProms

| voorstel DHW2.0     | PromsManager    | OnlineProms     |
| :----------------   | :------------:  | :-----------:   |
| Kliniek             | n/a             | instantie       |
| Patient             | Dossier         | Patient         |
| Meettraject         | n/a             | Traject         |
| Meetmoment          | TestDeployment  | Evaluatiemoment |
| Vragenlijst         | Test            | Vragenlijst     |
| VragenlijstAntwoord | Answers, Scores | Antwoord        |

Met dit voorstel worden de volgende namen aangepast c.q. dient de code gerefactored te worden:
- Episode vervangen met meettraject
- __instantie__ binnen OnlineProms gebruiken voor __patient-herkenbare merken, met eenduidige huisstijl en manier van communiceren__ Een instantie heeft dus een of meerdere __klinieken__ onder zich zoals gedefinieerd in DWH2.0. Binnen Clinics kennen we de volgende merken:
    + Orthopedium
    + Medinova
    + Nedspine
    + Oogziekenhuis Zonnestraal (incl. lasercentrum)
    + Dermicis
- OnlineProms kent naast bovenstaande entiteiten ook
    + Lichaamsdeel (DWH2.0: anatomie) om aan te duiden waar het meettraject betrekking op heeft
    + Voor elk lichaamsdeel kunnen trajecten worden gedefinieerd, met de verschillende meetmomenten.


