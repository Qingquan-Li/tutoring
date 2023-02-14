"""
Applying migrations to database:
$ python manage.py migrate --settings=a_project_config.settings.production

Creating an admin user:
$ python manage.py createsuperuser --settings=a_project_config.settings.production

Running tests:
$ python manage.py test --settings=a_project_config.settings.production

Using the shell:
$ python manage.py shell --settings=a_project_config.settings.production
"""


import os
from pathlib import Path

from dotenv import load_dotenv

# https://saurabh-kumar.com/python-dotenv/
load_dotenv()  # take environment variables from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'xxx'  # Hide the original auto-generated SECRET_KEY
# https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = [
    'tutoring.helpyourmath.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'corsheaders',

    # Local
    'accounts.apps.AccountsConfig',
    'tutoring_info.apps.TutoringInfoConfig',
    'contact_us.apps.ContactUsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'a_project_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # new
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

WSGI_APPLICATION = 'a_project_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tutoring',
        'USER': 'tutoring',
        'PASSWORD': os.getenv('PRODUCTION_POSTGRESQL_PASSWORD'),
        # https://docs.djangoproject.com/en/4.1/ref/settings/#host
        # default (empty HOST), the connection to the database is done through UNIX domain sockets.
        # If you want to connect through TCP sockets, set HOST to ‘localhost’ or ‘127.0.0.1’.
        'HOST': 'localhost',
        'PORT': '5432',
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True  # new

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = 'django_static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# #################### Newly expanded content ####################


# docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'accounts.CustomUser'

# https://docs.djangoproject.com/en/4.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "django_static")

# DRF default settings are in:
# .venv/lib/python3.8/site-packages/rest_framework/settings.py
# Setting the global throttling policy:
# https://www.django-rest-framework.org/api-guide/throttling/
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        # anonymous users. The IP address of the request will be used as the unique cache key.
        'anon': '600/minute',
        # given user. The user id will be used as a unique cache key if the user is authenticated.
        'user': '600/minute',
    },
}

# Cross-Origin Resource Sharing (CORS)
# https://github.com/adamchainz/django-cors-headers
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://192.168.0.118:3000',
    #'https://tutoring.helpyourmath.com', # same origin
    #'http://tutoring.helpyourmath.com', # same origin
    'https://tutoring.pages.dev',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://[\w-]+\.tutoring\.pages\.dev$",
]

# https://docs.djangoproject.com/en/4.1/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# https://docs.djangoproject.com/en/4.1/ref/csrf/
# docs.djangoproject.com/en/4.1/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS
# CSRF_TRUSTED_ORIGINS = [
#    'https://tutoring.helpyourmath.com',
#    'http://tutoring.helpyourmath.com',
# ]
