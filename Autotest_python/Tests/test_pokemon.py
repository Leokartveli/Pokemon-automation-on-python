import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '56cd77b7f94c8e6dcd214a47d9344a03'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': f'{TOKEN}'
}
TRAINER_ID = '12439'
TRAINER_NAME = 'Leo'
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Leo'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Leo'), ('id', TRAINER_ID)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value 