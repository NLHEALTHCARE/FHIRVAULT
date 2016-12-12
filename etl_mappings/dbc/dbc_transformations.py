from pyelt.mappings.transformations import FieldTransformation


class DbcTransformations():
    @staticmethod
    def text_to_date_transform(field_name):
        transform = FieldTransformation()
        transform.field_name = field_name
        transform.new_step("CASE WHEN {fld} = '' THEN NULL ELSE to_date({fld}, 'YYYYMMDD') END ")
        return transform