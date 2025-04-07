import json
import hashlib

class Wallet:
    # ...existing code...

    def compute_hash(self):
        block_data = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()
