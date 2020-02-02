"""
Django settings for backin project.
"""
from __future__ import unicode_literals

name = "Backin"

import os, ast
from datetime import timedelta
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
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
ENABLE_SSL = os.environ.get('ENABLE_SSL', 'False')

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
    'projects',
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
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST', ''),
        'NAME': os.environ.get('DATABASE', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PORT': 5432,
        'OPTIONS': {
            'sslmode': 'disable',
        },
    },
    'mirror1': {
        'NAME': 'mirror1',
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('HOST_MIRROR', ''),
        'NAME': os.environ.get('DATABASE_MIRROR', ''),
        'USER': os.environ.get('USER_MIRROR', ''),
        'PASSWORD': os.environ.get('PASSWORD_MIRROR', ''),
        'PORT': os.environ.get('PORT_MIRROR', ''),
        'OPTIONS': {
            'sslmode': 'disable',
        },
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': os.environ.get('JWT_SECRET_KEY', ''),
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(seconds=30000),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}

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

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler']

# Authentication and User
REST_USE_JWT = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATICFILES_DIRS = [
    ('assets', os.path.join(PROJECT_ROOT, 'static', 'assets')),
    ('favicons', os.path.join(PROJECT_ROOT, 'static', 'favicons')),
    ('images', os.path.join(PROJECT_ROOT, 'static', 'images')),
    ('dashboard/images', os.path.join(
        PROJECT_ROOT, 'static', 'dashboard', 'images'))
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder']

#CORS configuration
ACCESS_CONTROL_ALLOW_HEADERS = '*'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost',
    'http://localhost',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://0.0.0.0:3000',
)

CORS_ORIGIN_REGEX_WHITELIST = (
    'localhost',
    'http://localhost',
    'http://localhost:3000',
    '127.0.0.1:3000',
    '0.0.0.0:3000',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
    'PATCH',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Activate Django-Heroku.
django_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']
