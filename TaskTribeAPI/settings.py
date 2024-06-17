"""
Django settings for TaskTribeAPI project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd7ca2f72-340e-45b1-8c28-04ceb904e40f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'drf_spectacular',
    'django_filters',
    'Team',
    'notifications.apps.NotificationsConfig',
    'Task',
    'Project',
    'Core.User',
    'Core.Auth',
    'Core',
    'channels',
    'ChatRoom',
]


# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # 'apitoolkit_django.APIToolkit',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'TaskTribeAPI.urls'
AUTH_USER_MODEL = 'User.User'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'TaskTribeAPI.wsgi.application'
ASGI_APPLICATION = 'TaskTribeAPI.asgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "dbTaskTribe",
        # "USER": "salem",
        "USER":"",
        # "PASSWORD": "TonePave66$",
        "PASSWORD":"",
        # "HOST": "africoda-server-2.database.windows.net",
        "HOST":"KIRKPC\SALEMSERVER",
        "PORT": "",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server"},
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS':'drf_spectacular.openapi.AutoSchema',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 100,  # Set your desired page size
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'], #Opt to use django filters,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Task Tribe API',
    'DESCRIPTION': 'API to support task tribe backend',
    'VERSION': '1.0.0',
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
     "http://localhost:8088",
     ]

APITOOLKIT_KEY = "x6IdeZZNPSkzztNOgaZsHj8c9GGWRoOev7650bpbom0B/Y/D"

APITOOLKIT_REDACT_HEADERS = ["Authorization", "Cookie","Content-Length", "Content-Type"] # optional
APITOOLKIT_REDACT_REQ_BODY = ["$.password", "$.credit_card"] # optional
APITOOLKIT_REDACT_RES_BODY = ["$.credentials", "$.social_security_number"] # optional
