create schema fhir;

CREATE TYPE fhir.period AS (start timestamp, "end" timestamp);
CREATE TYPE fhir.coding AS (system text, version text, code text, display text, user_selected boolean);
CREATE TYPE fhir.codeable_concept AS (codings fhir.coding[], text text);