"""
Runserver:
$ python manage.py runserver 0:8000 --settings=a_project_config.settings.local

Creating an app:
python manage.py startapp [app_name] --settings=a_project_config.settings.local

Creating an admin user:
$ python manage.py createsuperuser --settings=a_project_config.settings.local

Creating new migrations based on models:
$ python manage.py makemigrations [app_name] --settings=a_project_config.settings.local

Applying migrations to database:
$ python manage.py migrate --settings=a_project_config.settings.local

Running the collectstatic management command:
$ python manage.py collectstatic --settings=a_project_config.settings.local

Running tests:
$ python manage.py test --settings=a_project_config.settings.local

Using the shell:
$ python manage.py shell --settings=a_project_config.settings.local
"""


from .production import *  # noqa

# DEBUG = False  # Unable to load static files automatically
DEBUG = True

# ALLOWED_HOSTS = ['192.168.0.118', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']


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
        'PASSWORD': os.getenv('LOCAL_POSTGRESQL_PASSWORD'),
        # https://docs.djangoproject.com/en/4.1/ref/settings/#host
        # default (empty HOST), the connection to the database is done through UNIX domain sockets.
        # If you want to connect through TCP sockets, set HOST to ‘localhost’ or ‘127.0.0.1’.
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
