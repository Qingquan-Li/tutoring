"""
Runserver:
$ python manage.py runserver 0:8000 --settings=a_project_config.settings.development

Applying migrations to database:
$ python manage.py migrate --settings=a_project_config.settings.development

Running tests:
$ python manage.py test --settings=a_project_config.settings.development

Using the shell:
$ python manage.py shell --settings=a_project_config.settings.development
"""


from .production import *  # noqa

DEBUG = False  # Unable to load static files automatically
# DEBUG = True

# Config the firewall rule on Ubuntu server:
# `$ sudo ufw allow from your_local_ip to any port 8000`
# then you can visit http://SERVER_IP:8000 locally.
ALLOWED_HOSTS = [
    os.getenv('SERVER_IP'),
    'localhost',
    'tutoring-development.helpyourmath.com',
]

# https://docs.djangoproject.com/en/4.1/ref/settings/#wsgi-application
WSGI_APPLICATION = 'a_project_config.wsgi_development.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tutoring_dev',
        'USER': 'tutoring_dev',
        'PASSWORD': os.getenv('DEVELOPMENT_POSTGRESQL_PASSWORD'),
        # https://docs.djangoproject.com/en/4.1/ref/settings/#host
        # default (empty HOST), the connection to the database is done through UNIX domain sockets.
        # If you want to connect through TCP sockets, set HOST to ‘localhost’ or ‘127.0.0.1’.
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
