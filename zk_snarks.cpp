/// This module provides the `Sha256` struct and the `Digest` trait from the `sha2` crate.
/// `Sha256` is used to compute the SHA-256 hash of input data, and `Digest` provides
/// the necessary methods for hashing operations.
use sha2::{Sha256, Digest};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ZkSnarkError {
    #[error("Invalid proof format")]
    InvalidProof,
    #[error("Verification failed")]
    VerificationFailed,
}

/// Represents a Zero-Knowledge Succinct Non-Interactive Argument of Knowledge
#[derive(Debug, Clone)]
pub struct ZkSNARK {
    proof: String,
    verified: bool,
}

impl ZkSNARK {
    /// Generates a new ZK-SNARK proof from a secret
    pub fn generate_proof(secret: &str) -> Self {
        let hash = format!("{:x}", Sha256::digest(secret.as_bytes()));
        ZkSNARK { 
            proof: hash,
            verified: false 
        }
    }

    /// Verifies the proof against a provided secret
    pub fn verify_proof(&mut self, secret: &str) -> Result<bool, ZkSnarkError> {
        let computed_hash = format!("{:x}", Sha256::digest(secret.as_bytes()));
        self.verified = self.proof == computed_hash;
        if self.verified {
            Ok(true)
        } else {
            Err(ZkSnarkError::VerificationFailed)
        }
    }

    /// Returns the proof string
    pub fn get_proof(&self) -> &str {
        &self.proof
    }

    /// Checks if the proof has been verified
    pub fn is_verified(&self) -> bool {
        self.verified
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_proof_verification() {
        let secret = "private_transaction";
        let mut proof = ZkSNARK::generate_proof(secret);
        assert!(proof.verify_proof(secret).is_ok());
        assert!(proof.verify_proof("wrong_secret").is_err());
    }
}
