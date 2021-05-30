import requests

url = "http://127.0.0.1:8042/version/"

chain = "devnet"

normal = requests.get(url + f"{chain}")

print(normal.json())
