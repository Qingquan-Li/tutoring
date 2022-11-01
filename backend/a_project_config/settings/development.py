"""
Applying migrations to database:
$ python manage.py migrate --settings=a_project_config.settings.development

Creating an admin user:
$ python manage.py createsuperuser --settings=a_project_config.settings.development

Running tests:
$ python manage.py test --settings=a_project_config.settings.development

Runserver:
$ python manage.py runserver 0:8000 --settings=a_project_config.settings.development
"""


import os

from dotenv import load_dotenv

from .production import *  # noqa

# https://saurabh-kumar.com/python-dotenv/
load_dotenv()  # take environment variables from .env

# DEBUG = False  # Unable to load static files automatically
DEBUG = True

ALLOWED_HOSTS = [os.getenv('SERVER_IP'), 'localhost']
