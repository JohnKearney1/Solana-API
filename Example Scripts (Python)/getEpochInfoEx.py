import requests

url = "http://127.0.0.1:8042/epochInfo/"

chain = "mainnet"

response = requests.get(url + chain)

print(response.json())

