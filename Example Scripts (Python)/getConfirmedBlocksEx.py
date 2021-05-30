import requests

url = "http://127.0.0.1:8042/confirmedBlocks/"

start_slot = "80471566"

response = requests.get(url + start_slot)

print(response.json())
