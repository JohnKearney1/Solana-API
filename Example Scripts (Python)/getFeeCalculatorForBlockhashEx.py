import requests

url = "http://127.0.0.1:8042/feeCalculator/"

blockhash = "3g5pycTMrgjDdwBAYputnx2deuuFsPxGNcNM4EnU41F4"

chain = "mainnet"

response = requests.get(url + f'{blockhash}&{chain}')

print(response.json())