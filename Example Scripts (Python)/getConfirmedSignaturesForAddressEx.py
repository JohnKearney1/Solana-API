import requests

url = "http://127.0.0.1:8042/confirmedSignatures/"

address = "CAavUPdd5R9K5GBqD1cnJtnLTzRym7npviMvGxoBFh5J"

start_slot = "80471566"

end_slot = "80471600"

response = requests.get(url + f'{address}&{start_slot}&{end_slot}')

print(response.json())
