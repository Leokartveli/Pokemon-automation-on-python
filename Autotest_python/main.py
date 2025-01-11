# Оптимизированный
import requests 
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '56cd77b7f94c8e6dcd214a47d9344a03'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': f'{TOKEN}'
}

body_create_pokemon = {
    "name": "Чурчхела",
    "photo_id": 23
}
change_name = {
    "pokemon_id": "189532",
    "name": "Хванчкара",
    "photo_id": 15
}
catch_pokemon = {
    "pokemon_id": "189534"
}
responses = {
    "POST Create Pokemon": requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon),
    "PUT Change Pokemon": requests.put(url=f'{URL}/pokemons', headers=HEADER, json=change_name),
    "POST Catch Pokemon": requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=catch_pokemon),
}
for action, response in responses.items():
    print(f"Action: {action}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

# Неоптимизированный код 
'''
import requests 
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '56cd77b7f94c8e6dcd214a47d9344a03'
HEADER = {'Content-Type': 'application/json',
          #'Authorization': f'Bearer {TOKEN}',
          'trainer_token': f'{TOKEN}'
}
body_create_pokemon = {
    "name": "Чурчхела",
    "photo_id": 23
}
change_name = {
    "pokemon_id": "189532",
    "name": "Хванчкара",
    "photo_id": 15
}

catch_pokemon = {
    "pokemon_id": "189534"
}
response_post = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_name)
response_catch_post = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_pokemon)
print(response_post)
print(response_post.json())
print(response_put)
print(response_put.json())
print(catch_pokemon)
print(response_catch_post.json())
'''