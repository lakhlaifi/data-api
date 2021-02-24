
import requests

Api= "http://api.zippopotam.us/fr/75015"


def test_check_status_code_equals_200():
     response = requests.get(Api)
     assert response.status_code == 200


def test_check_content_type_equals_json():
     response = requests.get(Api)
     assert response.headers["Content-Type"] == "application/json"



def test_check_country_equals_france():
     response = requests.get(Api)
     response_body = response.json()
     assert response_body["country"] == "France"