"""
`HL7 RIM <http://www.hl7.org/implement/standards/rim.cfm>`_ als basis voor het NL Healthcare domein model
"""

# --------------------------------------------------------------------------------------------------------------
#
# HL& RIM Abstract base classes met mandatory attributen
#
# --------------------------------------------------------------------------------------------------------------
from domainmodel_hl7_rim.hl7rim_enums import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import Sat


class Entity(object):
    """HL7v3 RIM abstract base class"""
    # class Hl7(Sat):
    #     entity_class = Columns.TextColumn(default_value=EntityClass.entity)
    #     entity_determiner = Columns.TextColumn(default_value=EntityDeterminer.specific)
    # hl7_instance = Hl7()

class Role(object):
    """HL7v3 RIM abstract base class"""
    # class Hl7(Sat):
    #     role_class = Columns.TextColumn(default_value=RoleClass.role)
    # hl7_instance = Hl7()

class RoleLink(object):
    """HL7v3 RIM abstract base class"""
    class Hl7(Sat):
        role_link_type = Columns.TextColumn(default_value=RoleLinkType.relation)
    hl7_instance = Hl7()

class Act(object):
    """HL7v3 RIM abstract base class"""
    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.act)
        act_mood = Columns.TextColumn(default_value=ActMood.actmoodcompletiontrack)
    hl7_instance = Hl7()

class ActRelationship(object):
    class Hl7(Sat):
        act_relationship_type = Columns.TextColumn(default_value=ActRelationshipType.act_relationship_type)
    hl7_instance = Hl7()

class Participation(object):
    """HL7v3 RIM abstract base class"""
    class Hl7(Sat):
        participation_type = Columns.TextColumn(default_value=ParticipationType.participation)
    hl7_instance = Hl7()

