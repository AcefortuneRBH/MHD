from backend.node import Node

def mine_block():
    node = Node()
    block = node.mine_block()
    print(f"New block mined: {block}")

    latest_blocks = node.get_latest_blocks()
    print(f"Latest blocks: {latest_blocks}")

    transaction_history = node.get_transaction_history()
    print(f"Transaction history: {transaction_history}")

    mining_status = node.get_mining_status()
    print(f"Mining status: {mining_status}")

    wallet_balance = node.get_wallet_balance()
    print(f"Wallet balance: {wallet_balance}")

if __name__ == "__main__":
    mine_block()
