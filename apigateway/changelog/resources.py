from flask_restful import Resource, reqparse

from apigateway.celery import celery


class ChangelogEntry(Resource):
    """
    Interface for handling a changelog entry.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('service', required=True, type=str)
    parser.add_argument('version', required=True, type=str)
    parser.add_argument('header', required=True, type=str)
    parser.add_argument('body', required=True, type=str)

    def get(self):
        """
        Get information about a specific changelog entry based on id.

        :return: a json of the changelog entry requested
        """
        parser = reqparse.RequestParser()
        parser.add_argument('changelog_entry_id', required=True, type=str)

        return celery.send_task('changelog.entry.get', kwargs=parser.parse_args()).get()

    def post(self):
        """
        Creates a new changelog entry based on parsed parameters unless one already exists.

        :return: a json of the changelog entry requested.
        """
        args = self.parser.parse_args()
        return celery.send_task('changelog.entry.post', kwargs=args).get()


class ServiceChangelogEntries(Resource):
    """
    Interface for handling multiple changelog entries.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('service', type=str)
    parser.add_argument('version', type=str)

    def get(self):
        """
        Get information about specific changelog entries based on optional parameters.
        If service is added as a parameter it will narrow down the search per service.
        If version is added as a parameter it will narrow down the search per version.
        If no parameter is given all entries will be returned

        :return: list of changelog entries
        """
        args = self.parser.parse_args()
        return celery.send_task('changelog.entries.get', kwargs=args).get()
