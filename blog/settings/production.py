from base import *
import dj_database_url
import psycopg2

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}

