import requests

MINER_ADDRESS = "my_wallet_address"
NODE_URL = "http://127.0.0.1:5000"

while True:
    print("Mining new block...")
    response = requests.get(f"{NODE_URL}/mine?miner={MINER_ADDRESS}")
    print(response.json())
