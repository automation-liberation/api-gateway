from flask_restful import Api

from apigateway.webscraper import resources


def init_api(api: Api):
    """
    Initializes everything to do with the webscraper package

    :param api: Main Flask api
    """
    api.add_resource(resources.FondMarknadenScraper, '/webscraper/fond-marknaden/<fond_id>')
