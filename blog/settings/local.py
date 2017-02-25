from base import *

DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'phill',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}