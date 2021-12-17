"""
Django settings for HFC project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_KEY_ID'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.5,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%q9#g6m-+#uj78gxwghng(l&2#xhf04y@jmh^7#t#77dox5*xm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
"""SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True"""

ALLOWED_HOSTS = [
    'staging.hackforchange.co.in',
    'hackforchange.co.in',
    'www.hackforchange.co.in',
    'hackforchange-staging.herokuapp.com',
    'hackforchange-production.herokuapp.com',
    '127.0.0.1',
    'www.staging.hackforchange.co.in'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HFCCore',
    'TFC',
    'ScreeningApp',
    'django.contrib.sites',
    'storages',
    'django_celery_beat',
    'django_celery_results',
    'blog',
    'django_summernote',
    'EventsEngine',
    'django.contrib.sitemaps'
]

SITE_ID = 2

MIDDLEWARE = [
    'HFC.virtualhostmiddleware.VirtualHostMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HFC.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'HFC.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#AWS_STORAGE_BUCKET_NAME = 'hackforchange-development-files'
AWS_STORAGE_BUCKET_NAME =  os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'
#AWS_LOCATION = 'static'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')
MAILCHIMP_SUBSCRIBE_LIST_ID = os.environ.get('MAILCHIMP_SUBSCRIBE_LIST_ID')
BASE_URL=os.environ.get('BASE_URL')
CELERY_BROKER_URL = os.environ.get('REDIS_URL')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_IMPORTS = (
    'HFCCore.tasks',
    
)
ADMIN_LINK = os.environ.get('ADMIN_LINK')

#Google credential
#client_id 
CLIENT_ID = os.environ.get('CLIENT_ID')
#redirect_uri
REDIRECT_URI = os.environ.get('REDIRECT_URI')
#client_secret
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
#MAILING LIST
EVENT_MAILING_LIST = os.environ.get('EVENT_MAILING_LIST')
PROGRAM_MAILING_LIST = os.environ.get('PROGRAM_MAILING_LIST')
MEMBER_SIGNUP_MAILING_LIST = os.environ.get('MEMBER_SIGNUP_MAILING_LIST')

# Activate Django-Heroku.
django_heroku.settings(locals())

X_FRAME_OPTIONS = 'SAMEORIGIN'
# Overwrite settings
try:
    from .local_settings import *
except:
    pass

