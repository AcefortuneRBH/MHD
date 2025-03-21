[package]
name = "blockchain_interop"
version = "0.1.0"
edition = "2021"

[dependencies]
sha2 = "0.10.6"
serde = { version = "1.0", features = ["derive"] }

fn main() {
    let mut blockchain = Blockchain::new();
    let mut did_registry = DIDRegistry::new();
    let mut interop_module = InteroperabilityModule::new();

    // Adding transactions
    blockchain.add_block("First transaction".to_string());
    blockchain.add_block("Second transaction".to_string());

    println!("Blockchain valid: {}", blockchain.validate_chain());

    // Interoperability - Atomic Swap
    let secret = "secure_key";
    let hash_lock = interop_module.atomic_swap(
        "Ethereum".to_string(),
        "Transaction Data".to_string(),
        secret
    );

    match interop_module.finalize_atomic_swap(secret) {
        Ok(_) => println!("Swap finalized successfully!"),
        Err(e) => println!("Error finalizing swap: {}", e),
    }

    // Decentralized Identity
    did_registry.register_did(
        "did:example:123".to_string(),
        "0xPublicKey".to_string(),
        "Alice's decentralized identity".to_string(),
    );

    if let Some(did) = did_registry.resolve_did(&"did:example:123".to_string()) {
        println!("Resolved DID: {:?}", did);
    }
}