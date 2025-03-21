[dependencies]
sha2 = "0.10"
serde = { version = "1.0", features = ["derive"] }
rand = "0.8"

use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Debug, Serialize, Deserialize, Clone)]
struct Block {
    timestamp: u64,
    data: String,
    previous_hash: String,
    hash: String,
}

impl Block {
    fn new(timestamp: u64, data: String, previous_hash: String) -> Self {
        let block = Block {
            timestamp,
            data,
            previous_hash,
            hash: String::new(),
        };
        let hash = block.calculate_hash();
        Block { hash, ..block }
    }

    fn calculate_hash(&self) -> String {
        let mut hasher = Sha256::new();
        hasher.update(self.timestamp.to_string().as_bytes());
        hasher.update(self.data.as_bytes());
        hasher.update(self.previous_hash.as_bytes());
        let result = hasher.finalize();
        format!("{:x}", result)
    }
}

pub struct Blockchain {
    chain: Vec<Block>,
}

impl Blockchain {
    pub fn new() -> Self {
        let genesis_block = Block::new(
            SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs(),
            "Genesis Block".to_string(),
            "0".to_string(),
        );

        Blockchain {
            chain: vec![genesis_block],
        }
    }

    pub fn add_block(&mut self, data: String) {
        let previous_block = self.chain.last().unwrap();
        let new_block = Block::new(
            SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs(),
            data,
            previous_block.hash.clone(),
        );
        self.chain.push(new_block);
    }

    pub fn validate_chain(&self) -> bool {
        for i in 1..self.chain.len() {
            let current_block = &self.chain[i];
            let previous_block = &self.chain[i - 1];

            if current_block.hash != current_block.calculate_hash() {
                return false;
            }

            if current_block.previous_hash != previous_block.hash {
                return false;
            }
        }
        true
    }
}
