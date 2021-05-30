import requests

url = "http://127.0.0.1:5000/recentBlockhash/"

chain = "mainnet"

normal = requests.get(url + f"{chain}")

print(normal.json())
