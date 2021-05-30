import requests

url = "http://127.0.0.1:8042/feeGovernor/"

chain = "mainnet"

response = requests.get(url + f'{chain}')

print(response.json())