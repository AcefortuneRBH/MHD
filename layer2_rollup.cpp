/// This module provides functionality for Layer 2 rollups, including data structures
/// and methods for managing rollup batches, fraud proofs, and other related operations.
use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct RollupTransaction {
    pub sender: String,
    pub receiver: String,
    pub amount: f64,
    pub is_valid: bool,
}

pub struct Layer2Rollup {
    pending_txns: Vec<RollupTransaction>,
    fraud_proof: HashMap<String, bool>,
    batch_size: usize,
}

impl Layer2Rollup {
    pub fn new(batch_size: usize) -> Self {
        Layer2Rollup {
            pending_txns: vec![],
            fraud_proof: HashMap::new(),
            batch_size,
        }
    }

    pub fn add_transaction(&mut self, sender: String, receiver: String, amount: f64) -> bool {
        if self.pending_txns.len() >= self.batch_size {
            return false;
        }

        let txn = RollupTransaction {
            sender,
            receiver,
            amount,
            is_valid: true,
        };

        self.pending_txns.push(txn);
        true
    }

    pub fn execute_rollup(&mut self) -> String {
        let mut batch_data = String::new();
        
        for txn in &self.pending_txns {
            if let Some(&is_fraud) = self.fraud_proof.get(&txn.sender) {
                if is_fraud {
                    continue;
                }
            }
            batch_data.push_str(&format!("{}->{}:{},", txn.sender, txn.receiver, txn.amount));
        }

        self.pending_txns.clear();
        batch_data
    }

    pub fn submit_fraud_proof(&mut self, sender: String) {
        self.fraud_proof.insert(sender, true);
    }

    pub fn is_batch_ready(&self) -> bool {
        self.pending_txns.len() >= self.batch_size
    }
}
