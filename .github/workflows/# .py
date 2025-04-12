use std::collections::HashMap;

#[derive(Debug, Clone)]le:
pub struct NFT {(self):
    pub id: u64,cle_data = {}
    pub owner: String,quests = {}
    pub metadata: String,
}   def request_data(self, request_id, source_url):
        if request_id in self.oracle_requests:
#[derive(Debug)]rn None
pub struct NFTMarketplace {s[request_id] = {"source_url": source_url, "data": None, "fulfilled": False}
    nfts: HashMap<u64, NFT>,equests[request_id]
    next_id: u64,
}   def fulfill_request(self, request_id, data):
        if request_id in self.oracle_requests and not self.oracle_requests[request_id]["fulfilled"]:
impl NFTMarketplace {le_requests[request_id]["data"] = data
    pub fn new() -> Self {quests[request_id]["fulfilled"] = True
        NFTMarketplace {data[request_id] = data
            nfts: HashMap::new(),
            next_id: 1,
        }
    }ef get_data(self, request_id):
        return self.oracle_data.get(request_id, None)
    pub fn mint_nft(&mut self, owner: String, metadata: String) -> u64 {
        let nft = NFT {ting:
            id: self.next_id,
            owner: owner.clone(),
            metadata,{}
        };lf.reputation_scores = {}
        self.nfts.insert(self.next_id, nft);
        let id = self.next_id;proposal_id, proposer, description):
        self.next_id += 1;self.proposals:
        println!("NFT minted with ID: {}, Owner: {}", id, owner);
        idlf.proposals[proposal_id] = {
    }       "proposer": proposer,
            "description": description,
    pub fn transfer_nft(&mut self, nft_id: u64, new_owner: String) {
        if let Some(nft) = self.nfts.get_mut(&nft_id) {
            println!("Transferring NFT ID: {} from {} to {}", nft_id, nft.owner, new_owner);
            nft.owner = new_owner;osal_id]
        } else {
            println!("NFT with ID: {} not found", nft_id);
        }f proposal_id not in self.proposals or self.proposals[proposal_id]["status"] != "open":
    }       return None
        if proposal_id not in self.votes:
    pub fn display_nfts(&self) {id] = {}
        println!("NFTs in the marketplace:");
        for (id, nft) in &self.nfts { already voted
            println!("ID: {}, Owner: {}, Metadata: {}", id, nft.owner, nft.metadata);
        }elf.votes[proposal_id][voter] = vote
    }   self.proposals[proposal_id]["votes"][vote] += weight
}       return True

    def finalize_proposal(self, proposal_id):
        if proposal_id in self.proposals and self.proposals[proposal_id]["status"] == "open":
            if self.proposals[proposal_id]["votes"]["yes"] > self.proposals[proposal_id]["votes"]["no"]:
                self.proposals[proposal_id]["status"] = "approved"
            else:
                self.proposals[proposal_id]["status"] = "rejected"
            return self.proposals[proposal_id]["status"]
        return None

    def get_proposal(self, proposal_id):
        return self.proposals.get(proposal_id, None)

    def get_reputation_score(self, voter):
        return self.reputation_scores.get(voter, 1)  # Default reputation is 1

    def update_reputation_score(self, voter, change):
        self.reputation_scores[voter] = max(1, self.reputation_scores.get(voter, 1) + change)
        return self.reputation_scores[voter]

class Blockchain:
    def __init__(self):
        # ...existing code...
        self.decentralized_oracle = DecentralizedOracle()
        self.reputation_based_voting = ReputationBasedVoting()
        # ...existing code...

# ...existing code...

@app.route('/request_oracle_data', methods=['POST'])
def request_oracle_data():
    data = request.json
    request_id = data['request_id']
    source_url = data['source_url']
    oracle_request = blockchain.decentralized_oracle.request_data(request_id, source_url)
    return json.dumps({"request_id": request_id, "oracle_request": oracle_request}), 201 if oracle_request else 400

@app.route('/fulfill_oracle_request', methods=['POST'])
def fulfill_oracle_request():
    data = request.json
    request_id = data['request_id']
    response_data = data['data']
    success = blockchain.decentralized_oracle.fulfill_request(request_id, response_data)
    return json.dumps({"request_id": request_id, "fulfilled": success}), 201 if success else 400

@app.route('/get_oracle_data', methods=['GET'])
def get_oracle_data():
    request_id = request.args.get('request_id')
    data = blockchain.decentralized_oracle.get_data(request_id)
    return json.dumps({"request_id": request_id, "oracle_data": data}), 200

@app.route('/create_proposal', methods=['POST'])
def create_proposal():
    data = request.json
    proposal_id = data['proposal_id']
    proposer = data['proposer']
    description = data['description']
    proposal = blockchain.reputation_based_voting.create_proposal(proposal_id, proposer, description)
    return json.dumps({"proposal_id": proposal_id, "proposal": proposal}), 201 if proposal else 400

@app.route('/vote_on_proposal', methods=['POST'])
def vote_on_proposal():
    data = request.json
    proposal_id = data['proposal_id']
    voter = data['voter']
    vote = data['vote']
    success = blockchain.reputation_based_voting.vote_on_proposal(proposal_id, voter, vote)
    return json.dumps({"proposal_id": proposal_id, "voted": success}), 201 if success else 400

@app.route('/finalize_proposal', methods=['POST'])
def finalize_proposal():
    data = request.json
    proposal_id = data['proposal_id']
    result = blockchain.reputation_based_voting.finalize_proposal(proposal_id)
    return json.dumps({"proposal_id": proposal_id, "final_status": result}), 200

@app.route('/get_proposal', methods=['GET'])
def get_proposal():
    proposal_id = request.args.get('proposal_id')
    proposal = blockchain.reputation_based_voting.get_proposal(proposal_id)
    return json.dumps({"proposal_id": proposal_id, "proposal": proposal}), 200

@app.route('/update_reputation_score', methods=['POST'])
def update_reputation_score():
    data = request.json
    voter = data['voter']
    change = data['change']
    new_score = blockchain.reputation_based_voting.update_reputation_score(voter, change)
    return json.dumps({"voter": voter, "new_reputation_score": new_score}), 201

# ...existing code...
