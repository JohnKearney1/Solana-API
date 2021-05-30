import requests

url = "http://127.0.0.1:8042/confirmedTransaction/"

signature = "51EVE1AnTWZKwWs2bwg1UzHWNrFBEH8GKDDkY4FNcKfG4bZHD5oFNDhsnMm9FLv2kVZRUasQ1RB3pVxyHVTKMCXk"

chain = "mainnet"

response = requests.get(url + f'{signature}&{chain}')

print(response.json())
