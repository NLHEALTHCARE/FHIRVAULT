class EntityClass:
    entity = 'ENT'
    health_chart_entity = 'HCE'
    living_subject = 'LIV'
    non_person_living_subject = 'NLIV'
    animal = 'ANM'
    microorganism = 'MIC'
    plant = 'PLNT'
    person = 'PSN'
    material = 'MAT'
    chemical_substance = 'CHEM'
    food = 'FOOD'
    manufactured_material = 'MMAT'
    container = 'CONT'
    holder = 'HOLD'
    device = 'DEV'
    certificate_representation = 'CER'
    imaging_modality_imagingmodalityentity = 'MODDV'
    organization = 'ORG'
    public_institution = 'PUB'
    state = 'STATE'
    nation = 'NAT'
    place = 'PLC'
    city_or_town = 'CITY'
    country = 'COUNTRY'
    county_or_parish = 'COUNTY'
    state_or_province = 'PROVINCE'
    group = 'RGRP'

class EntityDeterminer:
    specific = 'INSTANCE'
    described = 'KIND'
    described_quantified = 'QUANTIFIED_KIND'

class RoleClass:
    child = 'CHILD'
    credentialed_entity = 'CRED'
    nurse_practitioner = 'NURPRAC'
    nurse = 'NURS'
    physician_assistant = 'PA'
    physician = 'PHYS'
    role = 'ROL'
    roleclassassociative = '_RoleClassAssociative'
    roleclassmutualrelationship = '_RoleClassMutualRelationship'
    roleclassrelationshipformal = '_RoleClassRelationshipFormal'
    affiliate = 'AFFL'
    agent = 'AGNT'
    assigned_entity = 'ASSIGNED'
    commissioning_party = 'COMPAR'
    signing_authority_or_officer = 'SGNOFF'
    contact = 'CON'
    emergency_contact = 'ECON'
    next_of_kin = 'NOK'
    guardian = 'GUARD'
    citizen = 'CIT'
    covered_party = 'COVPTY'
    claimant = 'CLAIM'
    named_insured = 'NAMED'
    dependent = 'DEPEN'
    individual = 'INDIV'
    subscriber = 'SUBSCR'
    program_eligible = 'PROG'
    clinical_research_investigator = 'CRINV'
    clinical_research_sponsor = 'CRSPNSR'
    employee = 'EMP'
    military_person = 'MIL'
    guarantor_guarantorrole = 'GUAR'
    investigation_subject = 'INVSBJ'
    case_subject = 'CASEBJ'
    research_subject = 'RESBJ'
    licensed_entity = 'LIC'
    notary_public = 'NOT'
    healthcare_provider = 'PROV'
    patient = 'PAT'
    payee = 'PAYEE'
    invoice_payor = 'PAYOR'
    policy_holder = 'POLHOLD'
    qualified_entity = 'QUAL'
    coverage_sponsor = 'SPNSR'
    student = 'STD'
    underwriter = 'UNDWRT'
    caregiver = 'CAREGIVER'
    personal_relationship = 'PRS'
    roleclasspassive = '_RoleClassPassive'
    access = 'ACCESS'
    adjacency = 'ADJY'
    connection = 'CONC'
    molecular_bond = 'BOND'
    continuity = 'CONY'
    administerable_material = 'ADMM'
    birthplace = 'BIRTHPL'
    place_of_death = 'DEATHPLC'
    distributed_material = 'DST'
    retailed_material = 'RET'
    exposed_entity = 'EXPR'
    held_entity = 'HLD'
    health_chart = 'HLTHCHRT'
    identified_entity = 'IDENT'
    manufactured_product = 'MANU'
    therapeutic_agent = 'THER'
    maintained_entity = 'MNT'
    owned_entity = 'OWN'
    regulated_product = 'RGPR'
    service_delivery_location = 'SDLOC'
    dedicated_service_delivery_location_health_care_facility = 'DSDLOC'
    incidental_service_delivery_location = 'ISDLOC'
    territory_of_authority = 'TERR'
    used_entity = 'USED'
    warranted_product = 'WRTE'
    roleclassontological = '_RoleClassOntological'
    equivalent_entity = 'EQUIV'
    same = 'SAME'
    subsumed_by = 'SUBY'
    has_generalization = 'GEN'
    has_generic = 'GRIC'
    instance = 'INST'
    subsumer = 'SUBS'
    roleclasspartitive = '_RoleClassPartitive'
    content = 'CONT'
    exposure_agent_carrier = 'EXPAGTCAR'
    exposure_vector = 'EXPVECTOR'
    fomite = 'FOMITE'
    ingredient = 'INGR'
    active_ingredient = 'ACTI'
    active_ingredient___basis_of_strength = 'ACTIB'
    active_ingredient___moiety_is_basis_of_strength = 'ACTIM'
    active_ingredient___reference_substance_is_basis_of_strength = 'ACTIR'
    adjuvant = 'ADJV'
    additive = 'ADTV'
    base = 'BASE'
    inactive_ingredient = 'IACT'
    color_additive_color = 'COLR'
    flavor_additive_flavor = 'FLVR'
    preservative = 'PRSV'
    stabilizer = 'STBL'
    mechanical_ingredient = 'MECH'
    located_entity = 'LOCE'
    stored_entity = 'STOR'
    member = 'MBR'
    part = 'PART'
    active_moiety = 'ACTM'
    specimen = 'SPEC'
    aliquot = 'ALQT'
    isolate = 'ISLT'

class ParticipationType:
    participation = 'PART'
    participationancillary = '_ParticipationAncillary'
    admitter = 'ADM'
    attender = 'ATND'
    callback_contact = 'CALLBCK'
    consultant = 'CON'
    discharger = 'DIS'
    escort = 'ESC'
    referrer = 'REF'
    participationinformationgenerator = '_ParticipationInformationGenerator'
    author_originator = 'AUT'
    informant = 'INF'
    transcriber = 'TRANS'
    data_entry_person = 'ENT'
    witness = 'WIT'
    custodian = 'CST'
    direct_target = 'DIR'
    analyte = 'ALY'
    baby = 'BBY'
    catalyst = 'CAT'
    consumable = 'CSM'
    device = 'DEV'
    non_reuseable_device = 'NRD'
    reusable_device = 'RDV'
    donor = 'DON'
    exposureagent = 'EXPAGNT'
    exposureparticipation = 'EXPART'
    exposuretarget = 'EXPTRGT'
    exposuresource = 'EXSRC'
    product = 'PRD'
    subject = 'SBJ'
    specimen = 'SPC'
    indirect_target = 'IND'
    beneficiary = 'BEN'
    causative_agent = 'CAGNT'
    coverage_target = 'COV'
    guarantor_party = 'GUAR'
    holder = 'HLD'
    record_target = 'RCT'
    receiver = 'RCV'
    information_recipient = 'IRCP'
    ugent_notification_contact = 'NOT'
    primary_information_recipient = 'PRCP'
    referred_by = 'REFB'
    referred_to = 'REFT'
    tracker = 'TRC'
    location = 'LOC'
    destination = 'DST'
    entry_location = 'ELOC'
    origin = 'ORG'
    remote = 'RML'
    via = 'VIA'
    performer = 'PRF'
    distributor = 'DIST'
    primary_performer = 'PPRF'
    secondary_performer = 'SPRF'
    responsible_party = 'RESP'
    verifier = 'VRF'
    authenticator = 'AUTHEN'
    legal_authenticator = 'LA'

class ActClass:
    act = 'ACT'
    record_organizer = '_ActClassRecordOrganizer'
    composition_attestable_unit = 'COMPOSITION'
    document = 'DOC'
    clinical_document = 'DOCCLIN'
    cda_level_one_clinical_document = 'CDALVLONE'
    record_container = 'CONTAINER'
    category = 'CATEGORY'
    document_body = 'DOCBODY'
    document_section_section = 'DOCSECT'
    topic = 'TOPIC'
    extract = 'EXTRACT'
    electronic_health_record = 'EHR'
    folder = 'FOLDER'
    grouper = 'GROUPER'
    cluster = 'CLUSTER'
    accommodation = 'ACCM'
    account = 'ACCT'
    accession = 'ACSN'
    financial_adjudication_financial_adjudication_results = 'ADJUD'
    control_act = 'CACT'
    action = 'ACTN'
    information = 'INFO'
    state_transition_control = 'STC'
    contract = 'CNTRCT'
    financial_contract = 'FCNTRCT'
    coverage = 'COV'
    consent = 'CONS'
    container_registration = 'CONTREG'
    clinical_trial_timepoint_event = 'CTTEVENT'
    disciplinary_action = 'DISPACT'
    exposure = 'EXPOS'
    acquisition_exposure = 'AEXPOS'
    transmission_exposure = 'TEXPOS'
    incident = 'INC'
    inform = 'INFRM'
    invoice_element = 'INVE'
    working_list = 'LIST'
    monitoring_program = 'MPROT'
    observation = 'OBS'
    actclassroi = '_ActClassROI'
    bounded_roi = 'ROIBND'
    overlay_roi = 'ROIOVL'
    subject_physical_position = '_SubjectPhysicalPosition'
    subject_body_position = '_SubjectBodyPosition'
    left_lateral_decubitus = 'LLD'
    prone = 'PRN'
    right_lateral_decubitus = 'RLD'
    semi_fowlers = 'SFWL'
    sitting = 'SIT'
    standing = 'STN'
    supine = 'SUP'
    reverse_trendelenburg = 'RTRD'
    trendelenburg = 'TRD'
    detected_issue = 'ALRT'
    battery = 'BATTERY'
    clinical_trial = 'CLNTRL'
    condition_node = 'CNOD'
    concern = 'CONC'
    condition = 'COND'
    public_health_case = 'CASE'
    outbreak = 'OUTB'
    diagnostic_image = 'DGIMG'
    genomic_observation = 'GEN'
    determinant_peptide = 'DETPOL'
    expression_level = 'EXP'
    locus = 'LOC'
    phenotype = 'PHN'
    polypeptide = 'POL'
    bio_sequence = 'SEQ'
    bio_sequence_variation = 'SEQVAR'
    investigation = 'INVSTG'
    observation_series = 'OBSSER'
    correlated_observation_sequences = 'OBSCOR'
    position = 'POS'
    position_accuracy = 'POSACC'
    position_coordinate = 'POSCOORD'
    specimen_observation_actclassspecobs = 'SPCOBS'
    verification = 'VERIF'
    care_provision = 'PCPR'
    encounter = 'ENC'
    policy = 'POLICY'
    jurisdictional_policy = 'JURISPOL'
    organizational_policy = 'ORGPOL'
    scope_of_practice_policy = 'SCOPOL'
    standard_of_practice_policy = 'STDPOL'
    procedure = 'PROC'
    substance_administration = 'SBADM'
    substance_extraction = 'SBEXT'
    specimen_collection = 'SPECCOLLECT'
    registration = 'REG'
    review = 'REV'
    specimen_treatment = 'SPCTRT'
    supply = 'SPLY'
    diet = 'DIET'
    storage = 'STORE'
    substitution = 'SUBST'
    transfer = 'TRFR'
    transportation = 'TRNS'
    financial_transaction = 'XACT'

class ActStatus:
    normal = 'normal'
    aborted = 'aborted'
    active = 'active'
    cancelled = 'cancelled'
    completed = 'completed'
    held = 'held'
    new = 'new'
    suspended = 'suspended'
    nullified = 'nullified'
    obsolete = 'obsolete'

class ActRelationshipType:
    act_relationship_type = 'ART'
    actrelationshipconditional = '_ActRelationshipConditional'
    has_contra_indication = 'CIND'
    has_pre_condition = 'PRCN'
    has_reason = 'RSON'
    blocks = 'BLOCK'
    curative_indication = 'CURE'
    adjunct_curative_indication = 'CURE.ADJ'
    diagnosis = 'DIAG'
    mitigates = 'MITGT'
    recovery = 'RCVY'
    adjunct_mitigation = 'MTGT.ADJ'
    symptomatic_relief = 'SYMP'
    has_trigger = 'TRIG'
    has_component = 'COMP'
    has_member = 'MBR'
    arrival = 'ARR'
    has_control_variable = 'CTRLV'
    departure = 'DEP'
    has_part = 'PART'
    has_outcome = 'OUTC'
    act_relationsip_objective = '_ActRelationsipObjective'
    has_continuing_objective = 'OBJC'
    has_final_objective = 'OBJF'
    has_goal = 'GOAL'
    has_risk = 'RISK'
    has_pertinent_information = 'PERT'
    actclasstemporallypertains = '_ActClassTemporallyPertains'
    actrelationshiptemporallypertainsend = '_ActRelationshipTemporallyPertainsEnd'
    ends_after_end_of = 'EAE'
    ends_after_start_of = 'EAS'
    ends_during = 'EDU'
    ends_before_start_of = 'EBS'
    ends_concurrent_with = 'ECW'
    concurrent_with = 'CONCURRENT'
    actrelationshiptemporallypertainsstart = '_ActRelationshipTemporallyPertainsStart'
    starts_after_end_of = 'SAE'
    starts_after_start_of = 'SAS'
    starts_during = 'SDU'
    starts_before_start_of = 'SBS'
    starts_concurrent_with = 'SCW'
    concurrent_with = 'CONCURRENT'
    occurs_during = 'DURING'
    overlaps_with = 'OVERLAP'
    actrelationshipaccounting = '_ActRelationshipAccounting'
    actrelationshipcosttracking = '_ActRelationshipCostTracking'
    has_charge = 'CHRG'
    has_cost = 'COST'
    actrelationshipposting = '_ActRelationshipPosting'
    has_credit = 'CREDIT'
    has_debit = 'DEBIT'
    authorized_by = 'AUTH'
    is_etiology_for = 'CAUS'
    covered_by = 'COVBY'
    is_derived_from = 'DRIV'
    episodelink = 'ELNK'
    provides_evidence_for = 'EVID'
    exacerbated_by = 'EXACBY'
    has_explanation = 'EXPL'
    items_located = 'ITEMSLOC'
    limited_by = 'LIMIT'
    has_metadata = 'META'
    is_manifestation_of = 'MFST'
    assigns_name = 'NAME'
    has_previous_instance_previous_instance = 'PREV'
    refers_to = 'REFR'
    uses = 'USE'
    has_reference_values = 'REFV'
    relieved_by = 'RELVBY'
    has_support = 'SPRT'
    has_bounded_support = 'SPRTBND'
    has_subject = 'SUBJ'
    summarized_by = 'SUMM'
    is_sequel = 'SEQL'
    is_appendage = 'APND'
    has_baseline = 'BSLN'
    complies_with = 'COMPLY'
    documents = 'DOC'
    fulfills = 'FLFS'
    occurrence_is_occurrence_of = 'OCCR'
    references_order = 'OREF'
    schedules_request_schedules = 'SCH'
    has_generalization = 'GEN'
    evaluates_goal = 'GEVL'
    instantiates_master = 'INST'
    modifies = 'MOD'
    matches_trigger = 'MTCH'
    has_option = 'OPTN'
    re_challenge = 'RCHAL'
    reverses = 'REV'
    replaces = 'RPLC'
    succeeds = 'SUCC'
    updates_condition = 'UPDT'
    excerpts = 'XCRPT'
    excerpt_verbatim = 'VRXCRPT'
    transformation = 'XFRM'

class ActMood:
    actmoodcompletiontrack = '_ActMoodCompletionTrack'
    potential = '_ActMoodPotential'
    definition = 'DEF'
    permission = 'PERM'
    resource_slot = 'SLOT'
    event_occurrence = 'EVN'
    intent = 'INT'
    desire = '_ActMoodDesire'
    act_request = '_ActMoodActRequest'
    appointment_request = 'ARQ'
    permission_request = 'PERMRQ'
    request = 'RQO'
    proposal = 'PRP'
    recommendation = 'RMD'
    promise = 'PRMS'
    appointment = 'APT'
    actmoodpredicate = '_ActMoodPredicate'
    criterion = 'CRT'
    event_criterion = 'EVN.CRT'
    expectation = 'EXPEC'
    goal = 'GOL'
    risk = 'RSK'
    option = 'OPT'

class RoleLinkType:
    relation = 'REL' #todo: niet letterlijk teruggevonden in tabel
    backup = 'BACKUP' #todo: niet letterlijk teruggevonden in tabel
    content = 'CONT'
    dirauth = 'DIRAUTH'
    identified_entity = 'IDENT'
    indaut = 'INDAUT' #todo: niet letterlijk teruggevonden in tabel
    part = 'PART'
    repl = 'REPL' #todo: niet letterlijk teruggevonden in tabel



### voorbeeld stuk voor Rob voor opzet boomstructuur uitgevoerd in classes (gebruik dit voor de nictiz-data)
# class RoleTypes:
#     personen = 'PRS'
#     class PersoonTypes:
#         default = 'PRS'
#         patient = 'PAT'
#         klanten = 'KLT'
#         class MedewerkerType:
#             default = 'MDW'
#             hulpverlener = 'HLP'
#             artsen = 'ART'
#             class Artsen:
#                 default = 'ART'
#         class PatientTypes:
#             pass
#
# #
#
#
# RoleTypes.PersoonTypes.MedewerkerType.Artsen.default


### einde voorbeeld

"""
Enum gebaseerd op Nictiz bestanden:
"""



class RolecodenlZorgverlenertypePersonen:
    class AssignedRoleType:  # Oorspronkelijk: EenRoltypeWordtGebruiktOmEenEntiteitVerderAanTeDuidenDieEenRolSpeeltMetAssignedentityAlsModelattribuutRoleclassAbstractTypes
        default = 'AssignedRoleType'

        class ArtsTypes:
            default = '01.000'
            internist_allergoloog = '01.002'
            anesthesioloog = '01.003'
            apotheekhoudende_huisarts = '01.004'
            bedrijfsarts = '01.008'
            cardioloog = '01.010'
            cardiothoracaal_chirurg = '01.011'
            dermatoloog = '01.012'
            arts_v_maag_darm_leverziekten = '01.013'
            chirurg = '01.014'
            huisarts = '01.015'
            internist = '01.016'
            keel__neus__en_oorarts = '01.018'
            kinderarts = '01.019'
            arts_klinische_chemie = '01.020'
            klinisch_geneticus = '01.021'
            klinisch_geriater = '01.022'
            longarts = '01.023'
            arts_microbioloog = '01.024'
            neurochirurg = '01.025'
            neuroloog = '01.026'
            nucleair_geneeskundige = '01.030'
            oogarts = '01.031'
            orthopedisch_chirurg = '01.032'
            patholoog = '01.033'
            plastisch_chirurg = '01.034'
            psychiater = '01.035'
            radioloog = '01.039'
            radiotherapeut = '01.040'
            reumatoloog = '01.041'
            revalidatiearts = '01.042'
            uroloog = '01.045'
            gynaecoloog = '01.046'
            specialist_ouderengeneeskunde = '01.047'
            verzekeringsarts = '01.048'
            zenuwarts = '01.050'
            arts_maatschappij_en_gezondheid = '01.055'
            arts_voor_verstandelijk_gehandicapten = '01.056'
            jeugdarts = '01.070'
            spoedeisende_hulp_arts = '01.071'
            sportarts = '01.074'

        class TandartsTypes:
            default = '02.000'
            orthodontist = '02.053'
            kaakchirurg = '02.054'

        class VerloskundigeTypes:
            default = '03.000'

        class FysiotherapeutTypes:
            default = '04.000'

        class PsychotherapeutTypes:
            default = '16.000'

        class ApothekerTypes:
            default = '17.000'
            ziekenhuisapotheker = '17.060'
            openbaar_apotheker = '17.075'

        class GezondheidszorgpsycholoogTypes:
            default = '25.000'
            klinisch_psycholoog = '25.061'
            klinisch_neuropsycholoog = '25.063'

        class VerpleegkundigeTypes:
            default = '30.000'
            verpl_spec_prev_zorg_bij_som_aandoeningen = '30.065'
            verpl_spec_acute_zorg_bij_som_aandoeningen = '30.066'
            verpl_spec_intensieve_zorg_bij_som_aandoeningen = '30.067'
            verpl_spec_chronische_zorg_bij_som_aandoeningen = '30.068'
            verpl_spec_geestelijke_gezondheidszorg = '30.069'

        class ApothekersassistentTypes:
            default = '83.000'

        class KlinischFysicusTypes:
            default = '84.000'

        class TandprotheticusTypes:
            default = '85.000'

        class VigErTypes:
            default = '86.000'

        class OptometristTypes:
            default = '87.000'

        class HuidtherapeutTypes:
            default = '88.000'

        class DietistTypes:
            default = '89.000'

        class ErgotherapeutTypes:
            default = '90.000'

        class LogopedistTypes:
            default = '91.000'

        class MondhygienistTypes:
            default = '92.000'

        class OefentherapeutMensendieckTypes:
            default = '93.000'

        class OefentherapeutCesarTypes:
            default = '94.000'

        class OrthoptistTypes:
            default = '95.000'

        class PodotherapeutTypes:
            default = '96.000'

        class RadiodiagnistischLaborantTypes:
            default = '97.000'

        class RadiotherapeutischLaborantTypes:
            default = '98.000'


class ObservationInterpretation:

    class GeneticObservationInterpretationAbstractTypes:
        default = '_GeneticObservationInterpretation'
        carrier = 'CAR'
        carrier = 'Carrier'

    class ObservationInterpretationChangeAbstractTypes:
        default = '_ObservationInterpretationChange'
        better = 'B'
        significant_change_down = 'D'
        significant_change_up = 'U'
        worse = 'W'

    class ObservationInterpretationExceptionsAbstractTypes:
        default = '_ObservationInterpretationExceptions'
        off_scale_low = '<'
        off_scale_high = '>'
        anti_complementary_substances_present = 'AC'
        insufficient_evidence = 'IE'
        quality_control_failure = 'QCF'
        cytotoxic_substance_present = 'TOX'

    class ObservationInterpretationNormalityAbstractTypes:
        default = '_ObservationInterpretationNormality'

        class AbnormalTypes:
            default = 'A'
            normal = 'N'

            class CriticalAbnormalTypes:
                default = 'AA'
                critical_high = 'HH'
                critical_low = 'LL'

            class HighTypes:
                default = 'H'

                class SignificantlyHighTypes:
                    default = 'H>'
                    critical_high = 'HH'

                class SignificantlyHighTypes:
                    default = 'HU'

            class LowTypes:
                default = 'L'

                class SignificantlyLowTypes:
                    default = 'L<'
                    critical_low = 'LL'

                class SignificantlyLowTypes:
                    default = 'LU'

    class ObservationInterpretationSusceptibilityAbstractTypes:
        default = '_ObservationInterpretationSusceptibility'
        intermediate = 'I'
        moderately_susceptible = 'MS'
        non_susceptible = 'NS'
        very_susceptible = 'VS'

        class ResistantTypes:
            default = 'R'
            synergy___resistant = 'SYN-R'

        class SusceptibleTypes:
            default = 'S'
            susceptible_dose_dependent = 'SDD'
            synergy___susceptible = 'SYN-S'

    class OutsideThresholdTypes:
        default = 'EX'
        above_high_threshold = 'HX'
        below_low_threshold = 'LX'

    class ObservationInterpretationDetectionAbstractTypes:
        default = 'ObservationInterpretationDetection'

        class IndeterminateTypes:
            default = 'IND'
            equivocal = 'E'

        class NegativeTypes:
            default = 'NEG'
            not_detected = 'ND'

        class PositiveTypes:
            default = 'POS'
            detected = 'DET'

    class ObservationInterpretationExpectationAbstractTypes:
        default = 'ObservationInterpretationExpectation'
        expected = 'EXP'
        unexpected = 'UNE'

    class ReactivityObservationInterpretationAbstractTypes:
        default = 'ReactivityObservationInterpretation'
        non_reactive = 'NR'

        class ReactiveTypes:
            default = 'RR'
            weakly_reactive = 'WR'

