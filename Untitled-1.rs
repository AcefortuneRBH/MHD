mod did_registry;

use crate::did_registry::DIDRegistry;
use std::collections::HashMap;
use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct DID {
    pub did: String,
    pub public_key: String,
    pub metadata_hash: String,
}

pub struct DIDRegistry {
    registry: HashMap<String, DID>,
}

impl DIDRegistry {
    pub fn new() -> Self {
        DIDRegistry {
            registry: HashMap::new(),
        }
    }

    pub fn register_did(&mut self, did: String, public_key: String, metadata: String) {
        let metadata_hash = format!("{:x}", Sha256::digest(metadata.as_bytes()));

        let identity = DID {
            did: did.clone(),
            public_key,
            metadata_hash,
        };

        self.registry.insert(did.clone(), identity);
        println!("DID registered: {}", did);
    }

    pub fn resolve_did(&self, did: &String) -> Option<&DID> {
        self.registry.get(did)
    }
}