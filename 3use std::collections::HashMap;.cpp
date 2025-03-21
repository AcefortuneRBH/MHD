use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

// ------------------------- MODULE DECLARATION -------------------------
mod networking;

// ------------------------- BLOCK STRUCTURE -------------------------
#[derive(Serialize, Deserialize, Debug, Clone)]
struct Block {
    index: u64,
    timestamp: u128,
    previous_hash: String,
    hash: String,
    data: String,
}

impl Block {
    fn new(index: u64, previous_hash: String, data: String) -> Self {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("Time went backwards")
            .as_millis();
        let hash = Self::calculate_hash(index, timestamp, &previous_hash, &data);
        Block {
            index,
            timestamp,
            previous_hash,
            hash,
            data,
        }
    }

    fn calculate_hash(index: u64, timestamp: u128, previous_hash: &str, data: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(index.to_string());
        hasher.update(timestamp.to_string());
        hasher.update(previous_hash);
        hasher.update(data);
        format!("{:x}", hasher.finalize())
    }
}

// ------------------------- BLOCKCHAIN -------------------------
struct Blockchain {
    chain: Vec<Block>,
}

impl Blockchain {
    fn new() -> Self {
        Blockchain {
            chain: vec![Block::new(0, String::from("0"), String::from("Genesis Block"))],
        }
    }

    fn add_block(&mut self, data: String) {
        let previous_block = self.chain.last().expect("There should be at least one block");
        let new_block = Block::new(previous_block.index + 1, previous_block.hash.clone(), data);
        self.chain.push(new_block);
    }

    fn validate_chain(&self) -> bool {
        for i in 1..self.chain.len() {
            let current_block = &self.chain[i];
            let previous_block = &self.chain[i - 1];
            if current_block.previous_hash != previous_block.hash {
                return false;
            }
            if current_block.hash != Block::calculate_hash(
                current_block.index,
                current_block.timestamp,
                &current_block.previous_hash,
                &current_block.data,
            ) {
                return false;
            }
        }
        true
    }

    fn atomic_swap(&mut self, blockchain: String, transaction: String, hash_lock: String) {
        println!(
            "Initiating atomic swap on {}: {} with hash lock {}",
            blockchain, transaction, hash_lock
        );
    }

    fn finalize_atomic_swap(&mut self, hash_lock: String, preimage: String) {
        if format!("{:x}", Sha256::digest(preimage.as_bytes())) == hash_lock {
            println!("Atomic swap finalized with preimage {}", preimage);
        } else {
            println!("Atomic swap failed: preimage does not match hash lock");
        }
    }
}

// ------------------------- DECENTRALIZED IDENTITY -------------------------
#[derive(Debug)]
struct DID {
    id: String,
    public_key: String,
    description: String,
}

struct DIDRegistry {
    registry: HashMap<String, DID>,
}

impl DIDRegistry {
    fn new() -> Self {
        DIDRegistry {
            registry: HashMap::new(),
        }
    }

    fn register_did(&mut self, id: String, public_key: String, description: String) {
        let did = DID {
            id: id.clone(),
            public_key,
            description,
        };
        self.registry.insert(id, did);
    }

    fn resolve_did(&self, id: &String) -> Option<&DID> {
        self.registry.get(id)
    }
}

// ------------------------- MAIN FUNCTION -------------------------

fn main() {
    let mut blockchain = Blockchain::new();
    let mut did_registry = DIDRegistry::new();

    // Adding transactions
    blockchain.add_block("First transaction".to_string());
    blockchain.add_block("Second transaction".to_string());

    println!("Blockchain valid: {}", blockchain.validate_chain());

    // Interoperability - Atomic Swap
    let hash_lock = format!("{:x}", Sha256::digest(b"secure_key"));
    blockchain.atomic_swap("Ethereum".to_string(), "Send 1 BTC for 50 ETH".to_string(), hash_lock.clone());
    blockchain.finalize_atomic_swap(hash_lock, "secure_key".to_string());

    // Decentralized Identity
    did_registry.register_did(
        "did:example:123".to_string(),
        "0xPublicKey".to_string(),
        "Alice's decentralized identity".to_string(),
    );

    if let Some(did) = did_registry.resolve_did(&"did:example:123".to_string()) {
        println!("Resolved DID: {:?}", did);
    }

    // Start the server in a new thread
    std::thread::spawn(|| {
        networking::start_server();
    });

    // Connect to a peer and send the latest block
    if let Some(latest_block) = blockchain.chain.last() {
        match networking::connect_to_peer("127.0.0.1:8080", latest_block) {
            Ok(_) => println!("Successfully sent block to peer"),
            Err(e) => println!("Failed to send block to peer: {}", e),
        }
    }
}