from flask_restful import Api

from apigateway.auth import resources


def init_api(api: Api):
    """
    Initializes everything to do with the stockchecker package

    :param api: Main Flask api
    """
    api.add_resource(resources.Authentication, '/authentication')
    api.add_resource(resources.Authorization, '/authorization')
