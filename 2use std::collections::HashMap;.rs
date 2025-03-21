use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

// ------------------------- MODULE DECLARATION -------------------------
mod networking;

// ------------------------- BLOCK STRUCTURE -------------------------
// ...existing code...

// ------------------------- BLOCKCHAIN -------------------------
// ...existing code...

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