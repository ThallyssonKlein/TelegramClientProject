from dotenv import load_dotenv

load_dotenv()

from os import environ, makedirs
from os.path import exists

if not environ.get('DATABASE_USERNAME'):
    raise Exception('DATABASE_USERNAME not set in .env')
else:
    DATABASE_USERNAME = environ.get('DATABASE_USERNAME')

if not environ.get('DATABASE_PASSWORD'):
    raise Exception('DATABASE_PASSWORD not set in .env')
else:
    DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')

if not environ.get('DATABASE_HOST'):
    raise Exception('DATABASE_HOST not set in .env')
else:
    DATABASE_HOST = environ.get('DATABASE_HOST')

if not environ.get('DATABASE_NAME'):
    raise Exception('DATABASE_NAME not set in .env')
else:
    DATABASE_NAME = environ.get('DATABASE_NAME')

if not environ.get('API_ID'):
    raise Exception('API_ID not set in .env')
else:
    API_ID = environ.get('API_ID')

if not environ.get('API_HASH'):
    raise Exception('API_HASH not set in .env')
else:
    API_HASH = environ.get('API_HASH')

MEDIA_DIR = environ.get('MEDIA_DIR')
APP_LOG = environ.get('APP_LOG')

if not exists(MEDIA_DIR):
    makedirs(MEDIA_DIR)
if not exists(APP_LOG):
    makedirs(APP_LOG)

env = environ