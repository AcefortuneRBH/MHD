use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Block {
    pub index: u64,
    pub timestamp: u128,
    pub previous_hash: String,
    pub hash: String,
    pub data: String,
    pub nonce: u64,
}

impl Block {
    pub fn new(index: u64, previous_hash: String, data: String) -> Self {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("Time went backwards")
            .as_millis();
            
        let nonce = 0;
        let hash = Block::calculate_hash(index, timestamp, &previous_hash, &data, nonce);
        
        Block {
            index,
            timestamp,
            previous_hash,
            hash,
            data,
            nonce,
        }
    }

    pub fn calculate_hash(index: u64, timestamp: u128, previous_hash: &str, data: &str, nonce: u64) -> String {
        let input = format!("{}{}{}{}{}", index, timestamp, previous_hash, data, nonce);
        let mut hasher = Sha256::new();
        hasher.update(input);
        format!("{:x}", hasher.finalize())
    }
}

pub struct Blockchain {
    pub chain: Vec<Block>,
}

impl Blockchain {
    pub fn new() -> Self {
        let genesis_block = Block::new(0, String::from("0"), String::from("Genesis Block"));
        Blockchain {
            chain: vec![genesis_block],
        }
    }

    pub fn add_block(&mut self, data: String) {
        let previous_block = self.chain.last().unwrap();
        let new_block = Block::new(
            previous_block.index + 1,
            previous_block.hash.clone(),
            data,
        );
        self.chain.push(new_block);
    }

    pub fn validate_chain(&self) -> bool {
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
                current_block.nonce,
            ) {
                return false;
            }
        }
        true
    }
}
