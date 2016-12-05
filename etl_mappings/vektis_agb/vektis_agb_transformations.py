from pyelt.mappings.transformations import FieldTransformation, FieldTransformStep

__author__ = 'hvreenen'


class VektisTransformations():
    @staticmethod
    def text_to_date_transform(field_name):
        transform = FieldTransformation()
        transform.field_name = field_name
        transform.new_step("lpad({fld}, 8, '0')")
        transform.new_step("to_date({fld}, 'DDMMYYYY')")
        transform.new_step("CASE WHEN {fld} = '1901-01-01' OR {fld} = '0001-01-01 BC' THEN NULL ELSE {fld} END ")
        return transform

    @staticmethod
    def make_agb(specialisme_code_field, agb_field_name):
        transform = FieldTransformation()
        transform.field_name = agb_field_name
        transform.new_step("lpad({fld}, 6, '0')")
        transform.new_step("CONCAT(lpad(" + specialisme_code_field + ", 2, '0'), {fld})")
        return transform

    @staticmethod
    def agb_code_to_gender(agb_gender_field):
        transform = FieldTransformation()
        transform.field_name = agb_gender_field
        transform.new_step("CASE WHEN {fld} = '1' THEN 'm' WHEN {fld} = '2' THEN 'v' ELSE 'o' END")
        return transform

# transform = FieldTransformation('BK zorgverlener')
# transform.steps['1'] = FieldTransformStep(1, 'make 6 positions, add zero to the left', "lpad({fld}, 6, '0')")
# transform.steps['2'] = FieldTransformStep(2, 'concat zorgverlenersoort', "CONCAT(lpad(zorgverlenersoort, 2, '0'), {fld})")
# transformations[transform.name] = transform
# print (transform.get_sql())
#
# transform = FieldTransformation('BK praktijk')
# transform.steps['1'] = FieldTransformStep(1, 'make 6 positions, add zero to the left', "lpad({fld}, 6, '0')")
# transform.steps['2'] = FieldTransformStep(2, 'concat zorgverlenersoort', "CONCAT(lpad(zorgverlenersoort, 2, '0'), {fld})")
# transformations[transform.name] = transform
#
# transform = FieldTransformation('BK zorginstelling')
# transform.steps['1'] = FieldTransformStep(1, 'make 6 positions, add zero to the left', "lpad({fld}, 6, '0')")
# transform.steps['2'] = FieldTransformStep(2, 'concat zorgverlenersoort', "CONCAT(lpad(soort_instelling, 2, '0'), {fld})")
# transformations[transform.name] = transform
# print (transform.get_sql())
#
#
# transform = FieldTransformation('convert and clean date')
# transform.steps['1'] = FieldTransformStep(1, 'make 8 positions, add zero to the left', "lpad({fld}, 8, '0')")
# transform.steps['2'] = FieldTransformStep(2, 'convert str to date', "to_date({fld}, 'DDMMYYYY')")
# transform.steps['3'] = FieldTransformStep(3, 'invalid dates to null', "CASE WHEN {fld} = '1901-01-01' OR {fld} = '0001-01-01 BC' THEN NULL ELSE {fld} END ")
# transformations[transform.name] = transform
# print (transform.get_sql())
#
# transform = FieldTransformation('initcap')
# transform.steps['1'] = FieldTransformStep(1, 'initcap', "initcap({fld})")
# transformations[transform.name] = transform
#
# transform = FieldTransformation('lowercase')
# transform.steps['1'] = FieldTransformStep(1, 'lowercase', "lower({fld})")
# transformations[transform.name] = transform

# transform = FieldTransformation('code zorgverlenersoort')
# transform.steps['1'] = FieldTransformStep(1, 'make 2 positions, add zero to the left', "lpad({fld}, 2, '0')")
# transformations[transform.name] = transform
#
# transform = FieldTransformation('lookup zorgverlenersoort')
# transform.steps['1'] = FieldTransformStep(1, 'make 2 positions, add zero to the left', "lpad({fld}, 2, '0')")
# transform.steps['2'] = FieldTransformStep(1, 'lookup', "(SELECT description FROM rdv_ref.zorgverlenersoort_ref WHERE code = '{fld}')")
# transformations[transform.name] = transform
#
# transform = FieldTransformation('geslacht')
# transform.steps['1'] = FieldTransformStep(1, 'number to geslachtcode', "case when {fld} = 1 then 'M' else 'V' end")
# transformations[transform.name] = transform


# print(VektisTransformations.text_to_date_transform('datum').get_sql())
