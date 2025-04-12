if __name__ == "__main__":
    print("Hello, Blockchain!")

def jls_extract_def(ecdsa, curve, all_in_blockchain):
    if __name__ == '__main__':
        # Example usage
        private_key1 = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key1 = private_key1.verifying_key
        sender_address = public_key1.to_string().hex()
    
        private_key2 = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key2 = private_key2.verifying_key
        recipient_address = public_key2.to_string().hex()
    
        # Add a transaction
        all_in_blockchain.add_transaction(sender_address, recipient_address, 10, private_key1.to_string().hex())
    
        # Mine the pending transactions
        miner_address = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1).verifying_key.to_string().hex()
        all_in_blockchain.mine_pending_transactions(miner_address)
    
        # Print the blockchain
        for block in all_in_blockchain.chain:
            print(f"Block #{block.index}:")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Transactions: {len(block.transactions)}")
            for tx in block.transactions:
                print(f"    Sender: {tx.sender}")
                print(f"    Recipient: {tx.recipient}")
                print(f"    Amount: {tx.amount}")
    return tx


def jls_extract_def(ecdsa, curve, all_in_blockchain):
    tx = jls_extract_def(ecdsa, curve, all_in_blockchain)
    
    return tx


def jls_extract_def(ecdsa):
    return ecdsa


tx = jls_extract_def(jls_extract_def(ecdsa), curve, all_in_blockchain)

python all_in_blockchain.py
