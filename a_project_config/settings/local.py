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


import os

from .production import *  # noqa

# DEBUG = False  # Unable to load static files automatically
DEBUG = True

# ALLOWED_HOSTS = ['192.168.0.118', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']
