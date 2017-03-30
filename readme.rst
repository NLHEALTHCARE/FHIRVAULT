Clinical Datavault (project name tbd)
=====================================

This project aims to develop a generic Clinical Datavault based on `FHIR <http://hl7.org/fhir/ />`. It is intended to be used as a generic dataplatform to support machine learning, analytics etc. in a clinical setting (hospitals, specialty clinics, mental care facilities). 

It addresses the challenge many data scientists face in their day-to-day work, namelijk data acquisition, cleansing and prepartion. By virtue of the datavault modeling technique, all clinical data is semantically linked and integrated using the `pyelt <http://pythonhosted.org/pyelt/ />` framework.

The structure of the domain model follows `FHIR Release 3 (DTU) <https://www.hl7.org/fhir/resourcelist.html/>` and its `modules <https://www.hl7.org/fhir/modules.html/>`. As an example, domainmodel.clinical.diagnostics contains all resources related to diagnostics.

Where available, the Dutch `Zorginformatiebouwstenen <http://zibs.nl/>` is used as a guideline for translating the terminology into Dutch.

