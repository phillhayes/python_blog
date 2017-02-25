from base import *
import dj_database_url
import psycopg2

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {'default': dj_database_url.config(default='postgres://grlioeawbrlzmg:89699375894665079a05a693cb9668c2f1fb4c6d966aa5b2f93f3903b6e66b65@ec2-23-21-76-49.compute-1.amazonaws.com:5432/d49m5uihliqf7e')}

