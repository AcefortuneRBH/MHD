import json
import hashlib
import time
import os

TX_DB = "transactions.json"

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.tx_hash = self.compute_hash()

    def compute_hash(self):
        return hashlib.sha256(json.dumps(self.__dict__, sort_keys=True).encode()).hexdigest()

    def save_transaction(self):
        if not os.path.exists(TX_DB):
            with open(TX_DB, "w") as f:
                json.dump([], f)

        with open(TX_DB, "r") as f:
            transactions = json.load(f)

        transactions.append(self.__dict__)

        with open(TX_DB, "w") as f:
            json.dump(transactions, f)

def get_all_transactions():
    if not os.path.exists(TX_DB):
        return []
    
    with open(TX_DB, "r") as f:
        return json.load(f)
