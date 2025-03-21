use std::collections::HashMap;
use thiserror::Error;
use serde::{Serialize, Deserialize};

#[derive(Error, Debug)]
pub enum NFTError {
    #[error("NFT not found")]
    NotFound,
    #[error("Not authorized")]
    NotAuthorized,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct NFT {
    id: u32,
    owner: String,
    metadata: String,
    timestamp: u64,
}

#[derive(Debug)]
pub struct NFTMarketplace {
    nfts: HashMap<u32, NFT>,
    next_id: u32,
}

impl NFTMarketplace {
    pub fn new() -> Self {
        NFTMarketplace {
            nfts: HashMap::new(),
            next_id: 1,
        }
    }

    pub fn mint_nft(&mut self, owner: String, metadata: String) -> u32 {
        let nft = NFT {
            id: self.next_id,
            owner: owner.clone(),
            metadata,
            timestamp: std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_secs(),
        };

        self.nfts.insert(self.next_id, nft);
        self.next_id += 1;
        self.next_id - 1
    }

    pub fn transfer_nft(&mut self, nft_id: u32, current_owner: &str, new_owner: String) -> Result<(), NFTError> {
        let nft = self.nfts.get_mut(&nft_id).ok_or(NFTError::NotFound)?;
        
        if nft.owner != current_owner {
            return Err(NFTError::NotAuthorized);
        }

        nft.owner = new_owner;
        Ok(())
    }

    pub fn get_nft(&self, nft_id: u32) -> Option<&NFT> {
        self.nfts.get(&nft_id)
    }

    pub fn get_owner_nfts(&self, owner: &str) -> Vec<&NFT> {
        self.nfts.values()
            .filter(|nft| nft.owner == owner)
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_nft_operations() {
        let mut marketplace = NFTMarketplace::new();
        let nft_id = marketplace.mint_nft("Alice".to_string(), "Test NFT".to_string());
        
        assert!(marketplace.transfer_nft(nft_id, "Alice", "Bob".to_string()).is_ok());
        assert!(marketplace.transfer_nft(nft_id, "Alice", "Charlie".to_string()).is_err());
    }
}
