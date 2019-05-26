# noinspection PyPackageRequirements
from dotenv import load_dotenv

from .dev import *

# Getting env variables
email_env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=email_env_path)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

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

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE'),
        'NAME': os.getenv('SQL_DATABASE'),
        'USER': os.getenv('SQL_USER'),
        'PASSWORD': os.getenv('SQL_PASSWORD'),
        'HOST': os.getenv('SQL_HOST'),
        'PORT': os.getenv('SQL_PORT'),
    }
}

STATIC_URL = '/staticfiles/'

# Removing email DEV settings.
del EMAIL_BACKEND

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
