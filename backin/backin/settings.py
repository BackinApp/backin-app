"""
Django settings for backin project.
"""
from __future__ import unicode_literals

name = "Backin"

import os, ast
from datetime import timedelta
# import dj_database_url
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DNS', ''),
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
AUTH_USER_MODEL = 'accounts.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '@gi!0^&qap%-rkd-bj86*dsxbn9f#sz+%4ro59f$ppd%=v=3lb')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)
SITE_ID = 1
ALLOWED_HOSTS = ['*']

APPEND_SLASH = False
ENABLE_SSL = ast.literal_eval(os.environ.get('ENABLE_SSL', 'False'))

# Application definition

INSTALLED_APPS = [
    # External apps
    'rest_framework',
    'rest_framework.authtoken',
    'django_countries',
    'corsheaders',

    # Django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Platform modules
    'accounts',
    'techs',
    'dbengine',
    'database',
    'entity',
    # 'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backin.urls'
ENABLE_SSL = ast.literal_eval(os.environ.get('ENABLE_SSL', 'False'))
FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.TemporaryFileUploadHandler']

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

WSGI_APPLICATION = 'backin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DB_HOST', ''),
        'NAME': os.environ.get('DATABASE', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PORT': 5432
    },
    'mirror1': {
        'NAME': 'mirror1',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('HOST_MIRROR', ''),
        'NAME': os.environ.get('DATABASE_MIRROR', ''),
        'USER': os.environ.get('USER_MIRROR', ''),
        'PASSWORD': os.environ.get('PASSWORD_MIRROR', ''),
        'PORT': os.environ.get('PORT_MIRROR', '')
    },
    'django': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('NAME_MONGO', ''),
        'HOST': os.environ.get('HOST_MONGO', ''),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.'
        'password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
