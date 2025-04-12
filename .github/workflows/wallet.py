from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os, json

WALLET_DB = "wallets.json"

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = self.generate_key_pair()

    def generate_key_pair(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem.decode(), public_pem.decode()

    def save_wallet(self, address):
        if not os.path.exists(WALLET_DB):
            with open(WALLET_DB, "w") as f:
                json.dump({}, f)

        with open(WALLET_DB, "r") as f:
            wallets = json.load(f)

        wallets[address] = {"public_key": self.public_key, "balance": 0}
        
        with open(WALLET_DB, "w") as f:
            json.dump(wallets, f)

def get_wallet_balance(address):
    if not os.path.exists(WALLET_DB):
        return 0

    with open(WALLET_DB, "r") as f:
        wallets = json.load(f)

    return wallets.get(address, {}).get("balance", 0)
