import json
import unittest
from unittest.mock import patch, MagicMock

from apigateway import create_test_app


class FondMarknadenScraperTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Test Setup
        """
        self.app = create_test_app()
        self.client = self.app.test_client()

    @patch('apigateway.webscraper.resources.celery.send_task')
    def test_get_fond(self, mock_task):
        mock_response = {
            "id": "254",
            "name": "Swedbank Robur Technology",
            "value": "370.60"
        }
        mock_task().get = MagicMock(return_value=mock_response)
        res = self.client.get('/webscraper/fond-marknaden/254')

        self.assertTrue(json.loads(res.data) == mock_response)
