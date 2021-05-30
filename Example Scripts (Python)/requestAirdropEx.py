import requests

url = "http://127.0.0.1:8042/airdrop/"

pubkey = "8xhjCzfzVcP79jE7jXR2xtNaSL6aJYoDRLVT9FMjpRTC"

lamports = "5000"

chain = "devnet"

normal = requests.get(url + f"{pubkey}&{lamports}&{chain}")

print(normal.json())

# https://explorer.solana.com/tx/2j2T33X7bUUwzD8Gh4BSuN9Z4m5t6AyqgAHCtpiyyN2ef4EC3Tge6eFuKirCDufFV22qxjMr9LfowqwaHbYd355d?cluster=devnet