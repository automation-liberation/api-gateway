from flask_restful import Api

from apigateway.stockchecker import resources


def init_api(api: Api):
    """
    Initializes everything to do with the stockchecker package

    :param api: Main Flask api
    """
    api.add_resource(resources.AvanzaFond, '/stockerchecker/avanza/fond/<fond_id>')
    api.add_resource(resources.AvanzaStock, '/stockerchecker/avanza/stock/<stock_id>')
