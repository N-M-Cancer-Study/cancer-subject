from datetime import datetime

import arrow
from dateutil.tz import gettz
from django.apps import apps as django_apps
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

app_config = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v1 = Consent(
    'cancer_subject.subjectconsent',
    version='1',
    start=arrow.get(
        datetime(2010, 5, 3, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2023, 2, 15, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=120,
    gender=[MALE, FEMALE])

v3 = Consent(
    'cancer_subject.subjectconsent',
    version='3',
    start=arrow.get(
        datetime(2023, 2, 16, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2025, 12, 31, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=120,
    gender=[MALE, FEMALE])

site_consents.register(v1)
site_consents.register(v3)
