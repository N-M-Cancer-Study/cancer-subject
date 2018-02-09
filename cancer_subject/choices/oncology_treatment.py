CHEMO_INTENT = (
    ('Standard', 'Standard'),
    (' Adjuvant', ' Adjuvant'),
    (' Neo-Adjuvant', ' Neo-Adjuvant'),
    ('concurrent_with_radiation', 'Concurrent with radiation')
)
WHY_DELAYED = (
    ('HemeTox', 'Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)'),
    ('HepatoTox', 'Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.) '),
    ('RenalTox', 'Toxicity - renal failure (increased creatinine, swelling, etc)'),
    ('OtherTox', 'Toxicity - other, specify '),
    ('No Response', 'Cancer not responding to treatment'),
    ('Default', 'Defaulted visit or lost-to-follow-up'),
    ('Outage', 'Outage of medication, supplies, laboratory results'),
    ('Clinic busy', 'Clinic too busy to accommodate'),
    ('Other, specify ', 'Other, specify '),
)
WHY_REDUCED = (
    ('HemeTox', 'Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)'),
    ('HepatoTox', 'Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.)'),
    ('RenalTox', 'Toxicity - renal failure (increased creatinine, swelling, etc)'),
    ('OtherTox', 'Toxicity - other, specify '),
    ('No Response', 'Cancer not responding to treatment'),
    ('Default', 'Defaulted visit or lost-to-follow-up'),
    ('Outage', 'Outage of medication, supplies, laboratory results'),
    ('Clinic busy', 'Clinic too busy to accommodate'),
    ('Standard protocol', 'Dose reduced due to standard protocol (i.e. reduced intensity CHOP)'),
    ('Other, specify ', 'Other, specify '),
)

DRUG_CODE = (
    ('AMOX = amoxicillin', 'AMOX = amoxicillin'),
    ('ALLO = allopurinol', 'ALLO = allopurinol'),
    ('BLEO = bleomycin', 'BLEO = bleomycin'),
    ('CARB = carboplatin', 'CARB = carboplatin'),
    ('CARM = carmustine', 'CARM = carmustine'),
    ('CAPC = capecitabine', 'CAPC = capecitabine'),
    ('CDX = casodex', 'CDX = casodex'),
    ('CIPR = ciprofloxacin', 'CIPR = ciprofloxacin'),
    ('CISP = cisplatin', 'CISP = cisplatin'),
    ('CYCL = cyclophosphamide', 'CYCL = cyclophosphamide'),
    ('CYTB = cytarabine', 'CYTB = cytarabine'),
    ('CTXM = cotrimoxazole', 'CTXM = cotrimoxazole'),
    ('DAUN = daunorubicin,', 'DAUN = daunorubicin,'),
    ('DCAR = dacarbazine', 'DCAR = dacarbazine'),
    ('DEXA = dexamethasone', 'DEXA = dexamethasone'),
    ('DOXO = doxorubicin', 'DOXO = doxorubicin'),
    ('DTAX = docetaxel', 'DTAX = docetaxel'),
    ('ETOP = etoposide', 'ETOP = etoposide'),
    ('FLOR = fluorouracil', 'FLOR = fluorouracil'),
    ('GEMC = gemcitabine', 'GEMC = gemcitabine'),
    ('GLEE = gleevec', 'GLEE = gleevec'),
    ('HERC = herception', 'HERC = herception'),
    ('HYDX = hydroxyurea', 'HYDX = hydroxyurea'),
    ('IFOS = ifosfamide', 'IFOS = ifosfamide'),
    ('IRIN = irinotecan', 'IRIN = irinotecan'),
    ('LEUK = leukovorin', 'LEUK = leukovorin'),
    ('LEUP = leuprolide', 'LEUP = leuprolide'),
    ('LDOX = liposomal doxorubicin', 'LDOX = liposomal doxorubicin'),
    ('MECH = mechlorethamine', 'MECH = mechlorethamine'),
    ('METO = metocloperamide (maxolone)', 'METO = metocloperamide (maxolone)'),
    ('METX = methatrexate', 'METX = methatrexate'),
    ('MITO = mitoxantrone', 'MITO = mitoxantrone'),
    ('OXAL = oxaliplatin', 'OXAL = oxaliplatin'),
    ('PROC = procarbazine', 'PROC = procarbazine'),
    ('PROM = promethazine', 'PROM = promethazine'),
    ('PRED = prednisone', 'PRED = prednisone'),
    ('PTAX = paclitaxel', 'PTAX = paclitaxel'),
    ('RANT = ranitidine', 'RANT = ranitidine'),
    ('RITX', 'RITX = Rituximab'),
    ('TAMX = tamoxifen', 'TAMX = tamoxifen'),
    ('VINC = vincristine', 'VINC = vincristine'),
    ('VINB = vinblastine', 'VINB = vinblastine'),
    ('VINO = vinorelbine', 'VINO = vinorelbine'),
    ('ZDX = zoladex', 'ZDX = zoladex'),
    ('OTHR = other', 'OTHR = other'),
)
DOSE_CATEGORY = (
    ('1 = Standard', '1 = Standard'),
    ('2 = Reduced Dose', '2 = Reduced Dose'),
    ('3 = Other ', '3 = Other '),
)

NUMBER_OF_CHEMO_CYLCES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('OTHER', 'other'),
    ('UNK', 'unknown'),
)

NUMBER_OF_CHEMO_INTERVALS = (
    ('1 week', '1 week'),
    ('2 weeks', '2 weeks'),
    ('3 weeks', '3 weeks'),
    ('4 weeks', '4 weeks'),
    ('OTHER', 'other'),
    ('UNK', 'unknown'),
)

CANCER_TREATMENT_GOAL = (
    ('Curative', 'Curative'),
    ('Palliative', 'Palliative'),
    ('UNK', 'Unknown'),
)
