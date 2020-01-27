import django_heroku
import dj_database_url

from .dev import *

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['myfamilycart.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'cart.apps.CartConfig',
    'crispy_forms',
]

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATIC_URL = '/staticfiles/'

# TODO: Add email config...

# Removing email DEV settings.
# del EMAIL_BACKEND

# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')


# Configure Django App for Heroku.
django_heroku.settings(locals())
