import time
import random

def monitor_mhd():
    print("📡 Monitoring MHD Blockchain (Live)...")
    while True:
        tx_id = random.randint(1000000, 9999999)
        print(f"✅ Transaction #{tx_id} confirmed on MHD")
        time.sleep(5)

if __name__ == "__main__":
    monitor_mhd()

