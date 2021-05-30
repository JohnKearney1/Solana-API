import requests

url = "http://127.0.0.1:8042/blockTime/"

slot = "80471566"

response = requests.get(url + slot)

print(response.json())
