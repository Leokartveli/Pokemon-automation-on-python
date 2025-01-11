import requests 
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '56cd77b7f94c8e6dcd214a47d9344a03'
HEADER = {'Content-Type: application/json'
          'Authorization': f'Bearer {TOKEN}'
}
body_create_pokemon = {
    "name": "LeonardoDiKhinkali",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response)