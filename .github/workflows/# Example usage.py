#!/usr/bin/env python3
# Example usage
blockchain = Blockchain()

# Add some transactions
blockchain.add_transaction("Alice", "Bob", 50)
blockchain.add_transaction("Bob", "Charlie", 30)

# Mine block
blockchain.mine_pending_transactions("miner_address")

# Verify chain
print(f"Chain valid: {blockchain.is_chain_valid()}")
print(f"Miner balance: {blockchain.get_balance('miner_address')}")