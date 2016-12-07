from domainmodel import identity_domain, workflow_domain, clinical_domain, financial_domain
from domainmodel.test_configs import general_config
from pyelt.pipeline import Pipeline


pipeline = Pipeline(general_config)
pipe = pipeline.get_or_create_pipe('fhir')
pipe.register_domain(identity_domain)
pipe.register_domain(workflow_domain)
pipe.register_domain(clinical_domain)
pipe.register_domain(financial_domain)
pipeline.run()
