from domainmodel_fhir import test_domain
from domainmodel_fhir.test_config import test_configs
from pyelt.pipeline import Pipeline

pipeline = Pipeline(config=test_configs)
pipe = pipeline.get_or_create_pipe('test')
pipe.register_domain(test_domain)
pipeline.run()