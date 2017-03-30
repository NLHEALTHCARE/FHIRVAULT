from domainmodel.identity_domain import Patient
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *
from pyelt.datalayers.valset import DvValueset


################################################################################
# 	All resources within Definitional Artifacts module of FHIR Release 3 (STU)
#	https://www.hl7.org/fhir/resourcelist.html:
#
#	- Questionnaire:			Vragenlijst
#	- ActivityDefinition:		tbd
# 	- ServiceDefinition:		tbd
# 	- PlanDefinition:			tbd
#
################################################################################



class Vragenlijst(HubEntity):
	"""
	Based on FHIR Resource Questionnaire https://www.hl7.org/fhir/questionnaire.html
	Definition of Questionnaire in itself, including questions and value sets
	"""

	class Default(Sat):
		identificatie = Columns.TextColumn() 	# identifier
		versie = Columns.TextColumn()			# version
		status = Columns.TextColumn()			# status CNE ('draft', 'published', 'retired')
		datum = Columns.TextColumn()			# date
		uitgever = Columns.TextColumn()			# publisher
		telecom = Columns.TextColumn()			# contact 
		subject_type = Columns.TextColumn()		# subjectType
		url = Columns.TextColumn()				# not in FHIR: extension to include link to Dutch database of questionnaires


class Vraaggroep(HubEntity):
	"""
	Grouped questions. Groups may either contain questions or groups but not both.
	"""
	class Default(HybridSat):
		class Types:
			groep = 'groep'						# record defines a group 
			vraag = 'vraag'						# record defines a question
		groep_vraag_id = Columns.TextColumn()	# linkID
		titel = Columns.TextColumn()			# title
		concept = Columns.TextColumn()			# concept that represents this group/question in the questionnaire
												# preferably an internationally standardized code, e.g. LOINC
		tekst = Columns.TextColumn()			# text
		verplicht = Columns.BoolColumn()		# required
		herhaling = Columns.BoolColumn()		# repeats
		antwoordopties = Columns.JsonColumn()	# options of permitted answers. For now in JSON format, for flexibility


class VragenlijstVraaggroepLink(Link):
	"""
	Links Groups/Questions to the Questionnaire
	"""
	vragenlijst = LinkReference(Vragenlijst)
	groep_vraag = LinkReference(Vraaggroep)


class VraaggroepHierarchieLink(Link):
	"""
	Allow for nesting for groups
	"""
	parent = LinkReference(Vraaggroep)
	child = LinkReference(Vraaggroep)

