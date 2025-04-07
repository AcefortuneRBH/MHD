from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import Blockchain
from transaction import Transaction, get_all_transactions

app = Flask(__name__)
CORS(app)  # Allow frontend access

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    miner_address = request.args.get('miner')
    block = blockchain.mine_pending_transactions(miner_address)
    return jsonify({"message": "Block Mined!", "block": block.__dict__}), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    blockchain.add_transaction(tx_data['sender'], tx_data['recipient'], tx_data['amount'])
    return jsonify({"message": "Transaction added!"}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.__dict__ for block in blockchain.chain]), 200

@app.route('/block/<index>', methods=['GET'])
def get_block(index):
    block = blockchain.chain[int(index)]
    return jsonify(block.__dict__), 200

@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify({"blocks": [block.__dict__ for block in blockchain.chain]})

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify({"pending_transactions": blockchain.pending_transactions})

@app.route('/transaction/send', methods=['POST'])
def send_transaction():
    data = request.get_json()
    sender = data.get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")

    if not sender or not recipient or amount is None:
        return jsonify({"error": "Missing transaction details"}), 400

    tx = Transaction(sender, recipient, amount)
    tx.save_transaction()
    
    return jsonify({"message": "Transaction sent!", "transaction": tx.__dict__}), 200

@app.route('/transactions/history', methods=['GET'])
def transactions_history():
    transactions = get_all_transactions()
    return jsonify({"transactions": transactions}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
