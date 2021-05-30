import requests

url = "http://127.0.0.1:8042/rentExemption/"

size = "6"

chain = "mainnet"

response = requests.get(url + f'{size}&{chain}')

print(response.json())

