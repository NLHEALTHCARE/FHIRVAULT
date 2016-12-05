from domainmodel_fhir import identity_domain, workflow_domain, clinical_domain, financial_domain
from domainmodel_fhir.test_configs import test_configs
from pyelt.pipeline import Pipeline


pipeline = Pipeline(test_configs)
pipe = pipeline.get_or_create_pipe('fhir')
pipe.register_domain(identity_domain)
pipe.register_domain(workflow_domain)
pipe.register_domain(clinical_domain)
pipe.register_domain(financial_domain)
pipeline.run()
