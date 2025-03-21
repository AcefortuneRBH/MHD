use std::collections::HashMap;
use sha2::{Sha256, Digest};

#[derive(Debug, Clone)]
struct AtomicSwap {
    target_chain: String,
    tx_data: String,
    hash_lock: String,
}

struct InteroperabilityModule {
    active_swaps: HashMap<String, AtomicSwap>,
}

impl InteroperabilityModule {
    fn new() -> Self {
        InteroperabilityModule {
            active_swaps: HashMap::new(),
        }
    }

    // Initiate an atomic swap
    fn atomic_swap(&mut self, target_chain: String, tx_data: String, secret: &str) -> String {
        let hash_lock = format!("{:x}", Sha256::digest(secret.as_bytes()));

        let swap = AtomicSwap {
            target_chain,
            tx_data,
            hash_lock: hash_lock.clone(),
        };

        self.active_swaps.insert(hash_lock.clone(), swap);

        println!(
            "Atomic swap initiated with {} | TX: {} | Lock: {}",
            target_chain, tx_data, hash_lock
        );

        hash_lock
    }

    // Finalize an atomic swap
    fn finalize_atomic_swap(&mut self, secret: &str) -> bool {
        let computed_hash = format!("{:x}", Sha256::digest(secret.as_bytes()));

        if let Some(swap) = self.active_swaps.get(&computed_hash) {
            println!(
                "Atomic swap finalized! TX: {} on {}",
                swap.tx_data, swap.target_chain
            );
            self.active_swaps.remove(&computed_hash);
            return true;
        } else {
            println!("Invalid secret for atomic swap.");
            return false;
        }
    }
}

// ------------------------- MAIN FUNCTION (Demo) -------------------------

fn main() {
    let mut interop = InteroperabilityModule::new();

    // Initiating a swap
    let secret = "secure_key";
    let hash_lock = interop.atomic_swap(
        "Ethereum".to_string(),
        "Send 1 BTC for 50 ETH".to_string(),
        secret,
    );

    // Finalizing the swap
    interop.finalize_atomic_swap(secret);
}
