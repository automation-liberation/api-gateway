import json
import unittest
from unittest.mock import patch, MagicMock

from apigateway import create_test_app


class ChangelogEntryTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Test Setup
        """
        self.app = create_test_app()
        self.client = self.app.test_client()
        self.mock_response = {
            "service": "Apigateway",
            "version": "0.1.0",
            "header": "Feature",
            "body": "Added stuff"
        }

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_get_entry(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response)
        res = self.client.get('/changelog?changelog_entry_id=5cf0007923e1c05902dd3c18')

        self.assertTrue(json.loads(res.data) == self.mock_response)

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_get_entry_no_id(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response)
        res = self.client.get('/changelog/5cf0007923e1c05902dd3c18')
        self.assertTrue(res.status_code == 404)

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_post_entry(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response)
        res = self.client.post('/changelog', data=self.mock_response)

        self.assertTrue(json.loads(res.data) == self.mock_response)

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_post_entry_missing_fields(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response)
        res = self.client.post('/changelog', data={"service": "Apigateway"})

        self.assertTrue(json.loads(res.data)['message']['version'] == 'Missing required parameter in the JSON body or the post body or the query string')
        self.assertTrue(res.status_code == 400)


class ServiceChangelogEntriesTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Test Setup
        """
        self.app = create_test_app()
        self.client = self.app.test_client()
        self.mock_response = {
            "_id": {
                "$oid": "5cf0007923e1c05902dd3c18"
            },
            "service": "Apigateway",
            "version": "0.1.0",
            "header": "Feature",
            "body": "Added stuff"
        }
        self.mock_response_list = [self.mock_response, ]

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_get_entries(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response_list)
        res = self.client.get('/changelog/service-entries')
        self.assertTrue(json.loads(res.data) == self.mock_response_list)

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_get_entries_service(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response_list)
        res = self.client.get('/changelog/service-entries?service=apigateway')
        self.assertTrue(json.loads(res.data) == self.mock_response_list)

    @patch('apigateway.stockchecker.resources.celery.send_task')
    def test_get_entries_version(self, mock_task):

        mock_task().get = MagicMock(return_value=self.mock_response_list)
        res = self.client.get('/changelog/service-entries?version=0.1.0')
        self.assertTrue(json.loads(res.data) == self.mock_response_list)
