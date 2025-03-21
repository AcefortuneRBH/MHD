use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

mod networking;

#[derive(Debug, Serialize, Deserialize, Clone)]
struct Block {
    index: u64,
    timestamp: u128,
    previous_hash: String,
    hash: String,
    data: String,
    nonce: u64,
}

impl Block {
    // ...existing code...
}

struct Blockchain {
    chain: Vec<Block>,
    pending_transactions: Vec<String>,
}

impl Blockchain {
    // ...existing code...
}

fn main() {
    let mut blockchain = Blockchain::new();

    blockchain.add_block("First transaction".to_string());
    blockchain.add_block("Second transaction".to_string());

    println!("Blockchain valid: {}", blockchain.validate_chain());
    println!("{:#?}", blockchain.chain);

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