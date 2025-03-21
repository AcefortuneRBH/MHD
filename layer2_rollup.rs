/**
 * Import the `HashMap` collection from the Rust standard library.
 * 
 * `HashMap` is a hash map implementation that allows for the storage
 * and retrieval of key-value pairs. It provides efficient methods
 * for inserting, updating, and querying data based on keys.
 */
use std::collections::HashMap;

#[derive(Debug, Clone)]
struct RollupTransaction {
    sender: String,
    receiver: String,
    amount: f64,
    is_valid: bool,
}

pub struct Layer2Rollup {
    pending_txns: Vec<RollupTransaction>,
    fraud_proof: HashMap<String, bool>,
}

impl Layer2Rollup {
    pub fn new() -> Self {
        Layer2Rollup {
            pending_txns: vec![],
            fraud_proof: HashMap::new(),
        }
    }

    // Add transaction to rollup
    pub fn add_transaction(&mut self, sender: String, receiver: String, amount: f64) {
        let txn = RollupTransaction {
            sender,
            receiver,
            amount,
            is_valid: true, // Initially assumed valid
        };

        self.pending_txns.push(txn);
        println!("Transaction added to rollup batch.");
    }

    // Execute rollup batch
    pub fn execute_rollup(&mut self) {
        println!("Executing rollup batch with {} transactions...", self.pending_txns.len());

        for txn in &self.pending_txns {
            if let Some(&is_fraud) = self.fraud_proof.get(&txn.sender) {
                if is_fraud {
                    println!("Fraud detected! Transaction from {} is invalid.", txn.sender);
                } else {
                    println!("Transaction {} -> {}: ${} processed.", txn.sender, txn.receiver, txn.amount);
                }
            } else {
                println!("Transaction {} -> {}: ${} processed.", txn.sender, txn.receiver, txn.amount);
            }
        }

        self.pending_txns.clear();
    }

    // Submit fraud proof
    pub fn submit_fraud_proof(&mut self, sender: String) {
        self.fraud_proof.insert(sender.clone(), true);
        println!("Fraud proof submitted for {}", sender);
    }
}
