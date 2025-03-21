use sha2::{Sha256, Digest};
use rand::{thread_rng, Rng};
use rand::distributions::Alphanumeric;

pub struct InteroperabilityModule {
}

impl InteroperabilityModule {
    pub fn new() -> Self {
        InteroperabilityModule {}
    }

    pub fn atomic_swap(
        &mut self,
        target_chain: String,
        transaction_data: String,
        secret: &str,
    ) -> Result<String, String> {
        if secret.is_empty() {
            return Err("Secret cannot be empty".to_string());
        }

        let hash_lock = self.generate_hash_lock(secret);
        println!(
            "Initiating atomic swap to chain: {}, with hash lock: {}",
            target_chain, hash_lock
        );

        Ok(hash_lock)
    }

    fn generate_hash_lock(&self, secret: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(secret.as_bytes());
        let result = hasher.finalize();
        format!("{:x}", result)
    }

    pub fn finalize_atomic_swap(&self, secret: &str) -> Result<(), String> {
        if secret.len() < 8 {
            return Err("Secret must be at least 8 characters long".to_string());
        }

        println!("Atomic swap finalized with secret: {}", secret);
        Ok(())
    }
}
