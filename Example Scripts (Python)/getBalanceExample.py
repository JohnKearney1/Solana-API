import requests

url = "http://127.0.0.1:8042/balance/"

addr = "8HGyAAB1yoM1ttS7pXjHMa3dukTFGQggnFFH3hJZgzQh"

response = requests.get(url + addr)

print(response.json())

