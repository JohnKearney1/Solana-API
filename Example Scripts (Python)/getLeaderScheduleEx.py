import requests

url = "http://127.0.0.1:8042/leaderSchedule/"

slot = "80471566"

chain = "mainnet"

response = requests.get(url + f'{slot}&{chain}')

print(response.json())

