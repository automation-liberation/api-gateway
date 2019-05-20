from flask import Flask
from flask_restful import Api

from apigateway.celery import celery


def create_app():
    """
    Initialize and returns a Flask app.

    :return: Flask application.
    """
    return entrypoint(mode='app')


def create_celery():
    """
    Initializes and returns a Celery app.

    :return: Celery application.
    """
    return entrypoint(mode='celery')


def entrypoint(mode='app'):
    """
    Initializes a application based on mode.

    :param mode: Type of application to initialize.
    :return: An initialized app.
    """
    assert isinstance(mode, str), 'bad mode type "{}"'.format(type(mode))
    assert mode in ('app', 'celery'), 'bad mode "{}"'.format(mode)

    app = Flask(__name__)

    configure_app(app)
    configure_celery(app, celery)

    api = Api(app)
    init_api(api)

    if mode == 'app':
        return app
    elif mode == 'celery':
        return celery


def configure_app(app):
    """
    Fetch configuration.

    :param app: Flask application.
    """
    app.config.from_object('config.DevConfig')


def configure_celery(app, celery):
    """
    Configures Celery application based on configuration.

    :param app: Flask application.
    :param celery: Celery application .
    """
    celery.conf.update(app.config)
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']

    celery.finalize()


def init_api(api):
    """
    Fetches all the different parts of the api and initializes them.

    :param api: Flask_Restful api application.
    """
    from apigateway import webscraper

    webscraper.init_api(api=api)
