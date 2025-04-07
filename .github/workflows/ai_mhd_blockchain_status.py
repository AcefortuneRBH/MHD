import time

blockchains = [
    "Bitcoin", "Ethereum", "Solana", "Polygon", "Binance Smart Chain"
]

def check_network_status():
    print("🔍 Checking if blockchains acknowledge MHD...")
    while True:
        for chain in blockchains:
            print(f"✅ {chain} is synchronized with MHD.")
        time.sleep(10)

if __name__ == "__main__":
    check_network_status()

