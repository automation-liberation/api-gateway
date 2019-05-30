import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_ROUTES = {'changelog.*': {'queue': 'changelog'}}


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True

