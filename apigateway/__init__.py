from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from apigateway.celery import celery
from apigateway.database import db, roles
from config import DevConfig, TestConfig


def create_app():
    """
    Initialize and returns a Flask app.

    :return: Flask application.
    """
    return entrypoint(mode='app')


def create_test_app():
    """
    Initialize and returns a Flask app for testing purposes.

    :return: Flask application.
    """
    return entrypoint(mode='app', config=TestConfig)


def create_celery():
    """
    Initializes and returns a Celery app.

    :return: Celery application.
    """
    return entrypoint(mode='celery')


def initialize_database(app):
    db.init_app(app)
    migrate = Migrate(app, db)

    from apigateway.auth import models


def populate_database():
    roles.generate_permissions()
    roles.generate_roles()


def entrypoint(mode='app', config=DevConfig):
    """
    Initializes a application based on mode.

    :param mode: Type of application to initialize.
    :param config: Config object.
    :return: An initialized app.
    """
    assert isinstance(mode, str), 'bad mode type "{}"'.format(type(mode))
    assert mode in ('app', 'celery'), 'bad mode "{}"'.format(mode)

    app = Flask(__name__)

    configure_app(app, config)
    configure_celery(app, celery)

    with app.app_context():
        initialize_database(app)

        jwt = JWTManager(app)

    api = Api(app)
    init_api(api)

    if mode == 'app':
        return app
    elif mode == 'celery':
        return celery


def configure_app(app, config):
    """
    Fetch configuration.

    :param app: Flask application.
    :param config: Config object.
    """
    app.config.from_object(config)
    CORS(app)


def configure_celery(app, celery):
    """
    Configures Celery application based on configuration.

    :param app: Flask application.
    :param celery: Celery application .
    """
    celery.conf.update(app.config)
    celery.conf.BROKER_URL = app.config['CELERY_BROKER_URL']
    celery.conf.RESULT_BACKEND = app.config['CELERY_RESULT_BACKEND']

    celery.finalize()


def init_api(api):
    """ 
    Fetches all the different parts of the api and initializes them.

    :param api: Flask_Restful api application.
    """
    from apigateway import stockchecker, changelog, auth, drone, mission

    stockchecker.init_api(api=api)
    changelog.init_api(api=api)
    auth.init_api(api=api)
    drone.init_api(api=api)
    mission.init_api(api=api)
