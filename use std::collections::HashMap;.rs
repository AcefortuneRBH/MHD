use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

// Import modules
mod atomic_swap;
mod blockchain;
mod did;
mod config;
mod logging;
pub mod interoperability;
mod fn;

use crate::atomic_swap::InteroperabilityModule;
use crate::blockchain::Blockchain;
use crate::did::DIDRegistry;
use crate::config::Config;
use crate::logging::log_message;
use crate::logging::log_error; // Import log_error

fn main() -> Result<(), String> {
    let config = Config::new().map_err(|e| {
        log_error(format!("Failed to load config: {}", e));
        e
    })?;

    logging::init_logger();

    log_message("Starting the application".to_string());

    let mut blockchain = Blockchain::new();
    let mut did_registry = DIDRegistry::new();
    let mut interop_module = InteroperabilityModule::new();

    // Adding transactions
    blockchain.add_block("First transaction".to_string()).map_err(|e| {
        log_error(format!("Failed to add block: {}", e));
        e
    })?;
    blockchain.add_block("Second transaction".to_string()).map_err(|e| {
        log_error(format!("Failed to add block: {}", e));
        e
    })?;

    println!("Blockchain valid: {}", blockchain.validate_chain());

    // Interoperability - Atomic Swap
    let secret = "secure_key";
    let hash_lock = interop_module.atomic_swap(
        "Ethereum".to_string(),
        "Transaction Data".to_string(),
        secret
    ).map_err(|e| {
        log_error(format!("Failed to perform atomic swap: {}", e));
        e
    })?;

    match interop_module.finalize_atomic_swap(secret) {
        Ok(_) => println!("Swap finalized successfully!"),
        Err(e) => {
            log_error(format!("Failed to finalize atomic swap: {}", e));
            println!("Error finalizing swap: {}", e);
        },
    }

    // Decentralized Identity
    did_registry.register_did(
        "did:example:123".to_string(),
        "0xPublicKey".to_string(),
        "Alice's decentralized identity".to_string(),
    ).map_err(|e| {
        log_error(format!("Failed to register DID: {}", e));
        e
    })?;

    if let Some(did) = did_registry.resolve_did(&"did:example:123".to_string()) {
        println!("Resolved DID: {:?}", did);
    }

    log_message("Application finished successfully".to_string());

    Ok(())
}