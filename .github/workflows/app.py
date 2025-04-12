from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    miner_address = request.args.get('miner')
    block = blockchain.mine_pending_transactions(miner_address)
    return jsonify({"message": "Block Mined!", "block": block.__dict__}), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    blockchain.add_transaction(tx_data)
    return jsonify({"message": "Transaction added!"}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.__dict__ for block in blockchain.chain]), 200

@app.route('/explorer', methods=['GET'])
def explorer():
    return jsonify({"blocks": [block.__dict__ for block in blockchain.chain]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
