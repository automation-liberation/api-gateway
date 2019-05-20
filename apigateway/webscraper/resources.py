from flask_restful import Resource

from apigateway.celery import celery


class FondMarknadenScraper(Resource):
    """
    Interface for interacting with the Fond Marknaden web scraper.
    """

    def get(self, fond_id):
        """
        Gets data about a fond based on an internal id from Fond Marknaden from webscraper microservice.

        :param fond_id: Internal id from Fond Marknaden
        :return: dictionary of values pertaining to a fond.
        """
        return celery.send_task('webscraper.fondmarknaden.get_fondmarknaden_value', (fond_id,)).get()
