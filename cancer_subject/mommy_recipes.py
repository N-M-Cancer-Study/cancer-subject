from datetime import date
from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_constants.constants import NO
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, seq

from cancer_subject.models import (
    Ae010, Af004, Af005, BaseRiskAssessmentAlcohol,
    BaseRiskAssessmentCancer, BaseRiskAssessmentChemical,
    BaseRiskAssessmentDemo, BaseRiskAssessmentEating,
    BaseRiskAssessmentFemale, BaseRiskAssessmentFuel,
    BaseRiskAssessmentMining, BaseRiskAssessmentSmoking,
    BaseRiskAssessmentSun, BaseRiskAssessment, BaselineHIVHistory,
    BHHCd4, BHHHivTest, BHHWhoIllness, CancerDiagnosis,
    BaseChemoMedication, LabResultCd4, LabResultChemistry,
    SubjectConsent, SymptomsAndTesting, SubjectLocator,
    RadiationTreatment, HaartRecord, BaseHaartMedication,
    CurrentSymptoms)
from edc_consent.tests import EdcConsentProvider
from edc_constants.choices import YES, POS
from cancer_subject.patterns import subject_identifier


class DateProvider(BaseProvider):

    def next_month(self):
        return (get_utcnow() + relativedelta(months=1)).date()

    def last_year(self):
        return (get_utcnow() - relativedelta(years=1)).date()

    def three_months_ago(self):
        return (get_utcnow() - relativedelta(months=3)).date()

    def thirty_four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=34)).date()

    def four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=4)).date()

    def yesterday(self):
        return (get_utcnow() - relativedelta(days=1)).date()


fake = Faker()
fake.add_provider(DateProvider)
fake.add_provider(EdcConsentProvider)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    study_site='40',
    consent_datetime=get_utcnow(),
    dob=fake.dob_for_consenting_adult,
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials=fake.initials,
    gender='M',
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    is_dob_estimated='-',
    is_incarcerated=NO,)

symptomsandtesting = Recipe(
    SymptomsAndTesting,
    subject_identifier=None,
    symptom_prompt='bleeding',
    symptom_date=fake.last_month,
    medical_doctor_date=fake.last_month,
    trad_doctor_date=fake.last_month,
    facility_first_seen='00-0-00',
    facility_first_seen_other='Church',
    hiv_tested=YES,
    hiv_test_result=POS,
    pos_date=fake.last_year,
    neg_date=fake.last_year,
    hiv_result='Pending',
    arv_art_therapy=YES,
    arv_art_start_date=fake.last_month,
    arv_art_now=NO,
    art_art_stop_date=fake.last_week,)

subjeclocator = Recipe(
    SubjectLocator,
    alt_contact_cell_number='72123721',
    has_alt_contact=NO,
    alt_contact_name='John Doe',
    alt_contact_rel='Sibling',
    alt_contact_cell='78298422',
    other_alt_contact_cell='71297390',
    alt_contact_tel='3178634',
    local_clinic='00-0-00',
    home_village='Oodi',)

radiationtreatment = Recipe(
    RadiationTreatment,
    treatment_start_date=fake.last_month(),
    treatment_end_date=date.today(),
    tumour_stages='X',
    lymph_stages='3',
    metastasis_stages='1',
    overall_stages='2',
    stage_modifier='D',
    treatment_itent='Palliative',
    treatment_relationship='no modaliites',
    side_effects_other='dizzyness',
    response='Almost Complete',
    response_other='Incomplete',
    any_missed_doses=NO,
    if_doses_missed='unresponsive',
    if_doses_missed_other='incompatible',
    any_doses_delayed=NO,
    if_doses_delayed='no transport',
    if_doses_delayed_other='too expensive',
    first_course_radiation=YES,
    comments='few descriptive words here, blah blah',
    treatment_name='Scar Boost',
    start_date=fake.three_months_ago(),
    end_date=fake.next_month(),
    dose_delivered='0.5',
    dose_described='2.0',
    fractions='3',
    dose_per_fraction='2',
    radiation_technique='Opposite laterals',
    radiation_technique_other='blah blah',
    modality='Photons',
    brachy_length='2',
    brachy_type='T&SR',)

haartrecord = Recipe(
    HaartRecord,
    haart_status='Never started HAART',
    comments='blah blah',)

basehaartmedication = Recipe(
    BaseHaartMedication,
    drug_name='ATR',
    mod_reason='13 = Vomiting',
    arv_reason='1 = Treatment',
    start_date=fake.three_months_ago(),
    stop_date=date.today(),)

currentsymptoms = Recipe(
    CurrentSymptoms,
    any_worry=YES,
    symptom_desc='blah blah blah',
    patient_own_remedy='details here',
    severity='mild',
    ra_advice='details here',
    outcome_update='details here',)

ae010 = Recipe(
    Ae010,
    report_type='Resolution',
    onset_date=fake.last_month(),
    event_grade='details here',
    relationship_description='Probably related to study activites',)

aef004 = Recipe(
    Af004,
    date_off_study=fake.three_months_ago(),
    date_last_contact=fake.three_months_ago(),
    off_study_reason='details here',
    off_study_code='Death',
    comments='Details here',)

aef005 = Recipe(
    Af005,
    death_date=fake.last_week(),
    primary_death_cause='Clinical record',
    death_cause_description='details here',
    death_cause_category='Cancer',
    diagnosis_code='details here',
    comments='details here',)

baseriskassessmentalcohol = Recipe(
    BaseRiskAssessmentAlcohol,
    alcohol_weekly='3',
    amount_drinking='8',)

baseriskassessmentcancer = Recipe(
    BaseRiskAssessmentCancer,
    family_cancer=YES,
    family_cancer_type='Breast Cancer',
    family_cancer_other='other details here',
    had_previous_cancer=YES,
    previous_cancer='Esophageal cancer',
    previous_cancer_other='other details here',)

baseriskassessmentchemical = Recipe(
    BaseRiskAssessmentChemical,
    asbestos=YES,
    asbestos_no_protection='less than 5 years',
    chemicals=YES,
    chemicals_time='less than 5 years',
    arsenic_smelting=YES,
    total_time_no_protection='between 5 and 20 years',)

baseriskassessmentdemo = Recipe(
    BaseRiskAssessmentDemo,
    marital_status='Single',
    marital_status_other='other details here',
    race='Asian',
    race_other='other details here',
    ethnic_grp='Basarwa',
    ethnic_grp_other='other details here',
    community='040',
    community_other='other details here',
    district20='Central',
    setting20='Village',
    district='Kweneng',
    setting='Farm/lands',
    education='Primary',
    occupation='Domestic work',
    occupation_other='other details here',
    money_provide='Unsure',
    money_provide_other='other details here',
    money_earned='None',
    electricity=YES,
    toilet='Indoor toilet',
    toilet_other='other details here',
    household_people='details here',
    food_security='Rarely',)

baseriskassessmenteating = Recipe(
    BaseRiskAssessmentEating,
    five_fruit=YES,
    meals_weekly='4',
    meal_sorghum='5',
    meal_millet='2',
    meal_rice='1',
    meal_peanuts='4',)

baseriskassessmentfemale = Recipe(
    BaseRiskAssessmentFemale,
    age_period='14',
    children='2',
    years_breastfed=YES,)

baseriskassessmentfuel = Recipe(
    BaseRiskAssessmentFuel,
    fuel_20y='solid fuels',
    fuel_20y_other='other details here',
    cooking=YES,
    fuel_mm='electricity',
    fuel_mm_other='other details here',
    cooking_mm=YES,)

baseriskassessmentmining = Recipe(
    BaseRiskAssessmentMining,
    mine_time='less than 5 years',
    mine_type='gold',
    mine_prompt_other='other details here',
    mine_underground=YES,
    mine_underground_time='less than 5 years',
    last_mine=fake.three_months_ago(),)

baseriskassessmentsmoking = Recipe(
    BaseRiskAssessmentSmoking,
    smoke_now='yes',
    cigarette_smoking='14 or fewer cigarettes a day',
    years_smoked='11',
    cigarette_smoked='14 or fewer cigarettes a day',
    when_quit='less than 2 years ago',
    years_smoked_before='3',)

baseriskassessmentsun = Recipe(
    BaseRiskAssessmentSun,
    hours_outdoor='1 hour or less',
    sleeved_shirt='never',
    hat='rarely',
    shade_umbrella='sometimes',
    sunglasses='often',)

baseriskassessment = Recipe(
    BaseRiskAssessment,
    hepatitis=NO,
    tuberculosis=YES,
    year_tb='1988',
    has_worked_mine=YES,
    has_smoked=NO,
    age_firstsex='younger than 15 years old',
    has_alcohol=NO,
    tradmedicine='Never',
    is_albino=YES,)

baselinehivhistory = Recipe(
    BaselineHIVHistory,
    has_hiv_result=YES,
    had_who_illnesses=YES,
    has_cd4=YES,
    cd4_result='2860',
    cd4_drawn_date=fake.yesterday(),
    has_prior_cd4=YES,
    nadir_cd4='1245',
    nadir_cd4_drawn_date=fake.yesterday(),
    has_vl=NO,
    vl_result='4365',
    vl_drawn_date=fake.yesterday(),)

bhhcd4 = Recipe(
    BHHCd4,
    nadir_cd4='230',
    nadir_cd4_drawn_date=fake.last_week(),)

bhhivtest = Recipe(
    BHHHivTest,
    hiv_drawn_date=fake.yesterday(),
    hiv_testdate_est=NO,
    hiv_result='POS',)

bhhwhoillness = Recipe(
    BHHWhoIllness,
    who_illness='details here',
    who_illness_other='other details here',
    who_illness_date=fake.last_month,)

cancerdiagnosis = Recipe(
    CancerDiagnosis,
    onco_number='143098087',
    pathology_number='8636',
    pm_number='0123556889',
    diagnosis=YES,
    cancer_category='new',
    symptom_prompt='Lump/Mass',
    symptom_prompt_other='other details here',
    symptom_first_noticed=fake.last_month(),
    first_evaluation=fake.last_month(),
    date_diagnosed=fake.last_month(),
    diagnosis_basis='CLinical Only',
    diagnosis_basis_other='other details here',
    diagnosis_word='metatstatic breast cancer',
    cancer_site='C33.1',
    clinical_diagnosis='M4355/31',
    tumour='X',
    tumour_basis='Clinical',
    lymph_nodes='2',
    lymph_basis='Pathology',
    metastasis='O',
    metastasis_basis='Clinical',
    cancer_stage='X',
    cancer_stage_modifier='No stage modifier',
    any_other_results='other details here',
    paper_documents='details here',
    results_to_record='details here',
    results_to_record_other='other details here',)

basechemomedication = Recipe(
    BaseChemoMedication,
    drug_code='AMOX = amoxicillin',
    dose_category='2 = Reduced Dose',
    start_date=fake.last_month(),
    stop_date=fake.last_week,
    cycle_num='5',
    interval='1 week',
    specify_other_med='details here',
    oncology_treatment_plan='details',
    otr_chemo='details',)

labresultcd4 = Recipe(
    LabResultCd4,
    cd4_drawn_date=fake.last_month,
    cd4_result='2546',)

labresultchemistry = Recipe(
    LabResultChemistry,
    chem_drawn_date=fake.last_week(),
    alanine='3546',
    aspartate='4356',
    bilirubin='45',
    creatinine='347646',
    lactate='34657',
    comments='details here',)
