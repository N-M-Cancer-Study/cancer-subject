"""
Django settings for cancer_subject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = 'cancer_subject'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jwggbn11gw22h6&0n@q0t97e)&)pg^n_*$18xj350f0%w+ywba'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ETC_DIR = os.path.join(BASE_DIR, 'etc')

ALLOWED_HOSTS = []

SITE_ID = 10
REVIEWER_SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    #'edc_reference.apps.AppConfig',
    #'edc_metadata_rules.apps.AppConfig',
    #'edc_sync.apps.AppConfig',
    #'edc_sync_files.apps.AppConfig',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    #'edc_offstudy.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    #     'edc_visit_schedule.apps.AppConfig',
    'cancer_subject.apps.EdcVisitTrackingAppConfig',
    'cancer_subject.apps.AppConfig',
    'edc_base_test.apps.AppConfig',
    'cancer_subject.apps.EdcDeviceAppConfig',
    'cancer_subject.apps.EdcProtocolAppConfig',
    #'cancer_subject.apps.EdcAppointmentAppConfig',
    #'cancer_subject.apps.EdcTimepointAppConfig',
    #'cancer_subject.apps.EdcMetadataAppConfig',
    'cancer_visit_schedule.apps.AppConfig',
    'cancer_metadata_rules.apps.AppConfig',
    'cancer_reference.apps.AppConfig',
    'cancer_subject.apps.EdcFacilityAppConfig',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'cancer_subject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cancer_subject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'cancer_subject', 'static')
STATIC_URL = '/static/'
DEVICE_ID = '99'
EDC_LAB_REQUISITION_MODEL = 'cancer_subject.subjectrequisition'
DEVICE_ROLE = 'CentralServer'
# KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')
GIT_DIR = BASE_DIR
COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, APP_NAME, 'holidays.csv')

DEFAULT_APPOINTMENT_MODEL = 'cancer_subject.appointment'

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

DASHBOARD_URL_NAMES = {
    'consent_listboard_url': 'cancer_dashboard:consent_listboard_url',
    'checklist_listboard_url': 'cancer_dashboard:checklist_listboard_url',
    'subject_dashboard_url': 'cancer_dashboard:subject_dashboard_url',
}

if 'test' in sys.argv and 'mysql' not in DATABASES.get('default').get('ENGINE'):
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        "edc_call_manager": None,
        "edc_appointment": None,
        "edc_call_manager": None,
        "edc_consent": None,
        "edc_death_report": None,
        "edc_export": None,
        "edc_identifier": None,
        "edc_lab": None,
        "edc_metadata": None,
        "edc_rule_groups": None,
        "edc_registration": None,
        "edc_sync_files": None,
        "edc_sync": None,
        "cancer_subject": None, }
