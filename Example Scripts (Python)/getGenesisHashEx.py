import requests

url = "http://127.0.0.1:8042/genesisHash/"

chain = "mainnet"

response = requests.get(url + chain)

print(response.json())

