class MultiSignatureWallet:
    def __init__(self):
        self.wallets = {}

    def create_wallet(self, wallet_id, owners, threshold):
        if wallet_id in self.wallets:
            return None
        self.wallets[wallet_id] = {
            "owners": owners,
            "threshold": threshold,
            "pending_transactions": []
        }
        return self.wallets[wallet_id]

    def propose_transaction(self, wallet_id, transaction):
        if wallet_id not in self.wallets:
            return None
        self.wallets[wallet_id]["pending_transactions"].append({
            "transaction": transaction,
            "approvals": []
        })
        return True

    def approve_transaction(self, wallet_id, transaction_index, owner):
        if wallet_id not in self.wallets:
            return None
        if owner not in self.wallets[wallet_id]["owners"]:
            return False
        transaction = self.wallets[wallet_id]["pending_transactions"][transaction_index]
        if owner in transaction["approvals"]:
            return False
        transaction["approvals"].append(owner)
        if len(transaction["approvals"]) >= self.wallets[wallet_id]["threshold"]:
            return self.execute_transaction(wallet_id, transaction_index)
        return True

    def execute_transaction(self, wallet_id, transaction_index):
        if wallet_id not in self.wallets:
            return None
        transaction = self.wallets[wallet_id]["pending_transactions"][transaction_index]
        if len(transaction["approvals"]) >= self.wallets[wallet_id]["threshold"]:
            self.wallets[wallet_id]["pending_transactions"].pop(transaction_index)
            return transaction["transaction"]
        return None

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.multisig_wallets = MultiSignatureWallet()

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )
    block = blockchain.new_block(proof)
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200

@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    data = request.json
    wallet_id = data['wallet_id']
    owners = data['owners']
    threshold = data['threshold']
    wallet = blockchain.multisig_wallets.create_wallet(wallet_id, owners, threshold)
    return json.dumps({"wallet_id": wallet_id, "wallet": wallet}), 201 if wallet else 400

@app.route('/propose_transaction', methods=['POST'])
def propose_transaction():
    data = request.json
    wallet_id = data['wallet_id']
    transaction = data['transaction']
    success = blockchain.multisig_wallets.propose_transaction(wallet_id, transaction)
    return json.dumps({"wallet_id": wallet_id, "success": success}), 201 if success else 400

@app.route('/approve_transaction', methods=['POST'])
def approve_transaction():
    data = request.json
    wallet_id = data['wallet_id']
    transaction_index = data['transaction_index']
    owner = data['owner']
    success = blockchain.multisig_wallets.approve_transaction(wallet_id, transaction_index, owner)
    return json.dumps({"wallet_id": wallet_id, "success": success}), 201 if success else 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
