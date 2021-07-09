import json
from collections import defaultdict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from parameterized import parameterized


def load(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def load_test_cases(file_ext):
    import fnmatch
    import os
    # where is this module?
    thisDir = os.path.dirname(__file__)
    test_data_dir = os.path.join(thisDir, "test_data")

    return [(os.path.join(test_data_dir, file), (os.path.join(test_data_dir, "test_results", file + ".json")))
            for file in os.listdir(test_data_dir) if fnmatch.fnmatch(file, '*.' + file_ext)]


def get_errors_only(response):
    out = []
    results = response['tables'][0]
    for row in results['rows']:
        sfa_id = row['data']['sfa_id']
        state_id = row['data']['state_id']
        sfa_name = row['data']['sfa_name']
        errors = [err['code'] for err in row['errors']]
        out.append({'state_id': state_id, 'sfa_id': sfa_id,
                    'sfa_name': sfa_name, 'errors': errors})

    return out

def get_error_by_code(response):
    out = []
    results = response['tables'][0]
    for row in results['rows']:
        sfa_id = row['data']['sfa_id']
        state_id = row['data']['state_id']
        sfa_name = row['data']['sfa_name']
        errors = [err['code'] for err in row['errors']]
        out.append({'state_id': state_id, 'sfa_id': sfa_id,
                    'sfa_name': sfa_name, 'errors': errors})

    return out

def get_total_errors(results):
    out = defaultdict(lambda: 0)
    for item in results:
        for e in item['errors']:
            out[e] += 1
    return out


class ExtensiveTests(APITestCase):

    fixtures = ['fixtures/test_data.json']

    @parameterized.expand(load_test_cases('csv'))
    def test_validate_csv(self, name, expected):
        print(name + expected)
        url = reverse('data_ingest:validate')
        data = load(name)
        token = "this1s@t0k3n"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, content_type='text/csv')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        err_resp = get_errors_only(response.data)
        total_err = (dict(get_total_errors(err_resp)))
        exp_data = json.loads(load(expected))
        print("exp_data")
        print(exp_data)
        print("actual_data")
        print(total_err)
        self.assertDictEqual(exp_data, total_err)

    @parameterized.expand(load_test_cases('json'))
    def test_validate_json(self, name, expected):
        print(name + expected)
        url = reverse('data_ingest:validate')
        data = load(name)
        token = "this1s@t0k3n"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        err_resp = get_errors_only(response.data)
        print("START 109 Full Response")
        print(response.data)
        print("END 109  Full Response")
        total_err = (dict(get_total_errors(err_resp)))
        exp_data = json.loads(load(expected))
        print("exp_data")
        print(exp_data)
        print("actual_data")
        print(total_err)
        self.assertDictEqual(exp_data, total_err)
