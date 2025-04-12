from blockchain import Blockchain

def check_blockchain():
    blockchain = Blockchain()
    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    check_blockchain()
