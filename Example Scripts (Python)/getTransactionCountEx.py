import requests

url = "http://127.0.0.1:8042/transactionCount/"

chain = "mainnet"

normal = requests.get(url + f"{chain}")

print(normal.json())
