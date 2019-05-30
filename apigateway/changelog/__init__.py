from flask_restful import Api

from apigateway.changelog import resources


def init_api(api: Api):
    """
    Initializes everything to do with the stockchecker package

    :param api: Main Flask api
    """
    api.add_resource(resources.ChangelogEntry, '/changelog')
    api.add_resource(resources.ServiceChangelogEntries, '/changelog/service-entries')
