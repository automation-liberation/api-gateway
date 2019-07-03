from flask_restful import Resource

from apigateway.celery import celery


class AvanzaFond(Resource):
    """
    Interface for interacting with the Fond Marknaden web scraper.
    """

    def get(self, fond_id):
        """
        Gets data about a fond based on an internal id from Avanza from stockchecker microservice.

        :param fond_id: Internal id from Avanza
        :return: dictionary of values pertaining to a fond.
        """
        return celery.send_task('stockchecker.avanza.get_avanza_fond_value', (fond_id,)).get()


class AvanzaStock(Resource):
    """
    Interface for interacting with the Avanza API .
    """

    def get(self, stock_id):
        """
        Gets data about a stock based on an internal id from Avanza from stockchecker microservice.

        :param stock_id: Internal id from Avanza
        :return: dictionary of values pertaining to a stock.
        """
        return celery.send_task('stockchecker.avanza.get_avanza_stock_value', (stock_id,)).get()
