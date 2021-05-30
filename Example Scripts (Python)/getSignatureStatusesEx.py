import requests

url = "http://127.0.0.1:8042/slotLeader/"

signature = "5tFBL4fSq1qpvNr2RDUc2opf3yt3SkFAuRcBnnB21CkiCE1j2SAHy6Fqp8WiQNPzErx4k36gDfQdhtfxjWkvT5zN"

chain = "testnet"

normal = requests.get(url + f"{chain}")

print(normal.json())
