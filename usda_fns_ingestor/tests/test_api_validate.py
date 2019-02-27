from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.conf import settings


class ApiValidateTests(APITestCase):
    def test_api_validate_json_empty(self):
        """
        Ensure we can post to the API for validation.
        """
        url = reverse('data_ingest:validate')
        data = []
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_validate_csv_empty(self):
        """
        Ensure we can post to the API for validation.
        """
        url = reverse('data_ingest:validate')
        data = ','.join([str(x) for x in settings.UPLOAD_COLUMNS])
        response = self.client.post(url, data, content_type='text/csv')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
