import requests

url = "http://127.0.0.1:8042/accountInfo/"

addr = "8HGyAAB1yoM1ttS7pXjHMa3dukTFGQggnFFH3hJZgzQh"

chain = "mainnet"

response = requests.get(url + f'{addr}&{chain}')

print(response.json())

