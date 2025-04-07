import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 4  # Adjustable difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [], time.time())
        self.chain.append(genesis_block)

    def add_block(self, block):
        if block.previous_hash == self.chain[-1].hash and block.hash.startswith("0" * self.difficulty):
            self.chain.append(block)
            return True
        return False

    def mine_pending_transactions(self, miner_address):
        if len(self.pending_transactions) == 0:
            return False

        new_block = Block(len(self.chain), self.chain[-1].hash, self.pending_transactions, time.time())
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)

        self.pending_transactions = [{"from": "network", "to": miner_address, "amount": 50}]
        return new_block

    def proof_of_work(self, block):
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
