import requests

url = "http://127.0.0.1:8042/voteAccounts/"

chain = "testnet"

normal = requests.get(url + f"{chain}")

print(normal.json())
