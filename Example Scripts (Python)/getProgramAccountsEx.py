import requests

url = "http://127.0.0.1:8042/programAccounts/"

pubkey = "CuieVDEDtLo7FypA9SbLM9saXFdb1dsshEkyErMqkRQq"

chain = "mainnet"

response = requests.get(url + f'{pubkey}&{chain}')

print(response.json())

