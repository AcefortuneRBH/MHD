use std::collections::HashMap;

#[derive(Debug, Clone)]
struct RollupTransaction {
    sender: String,
    receiver: String,
    amount: f64,
    is_valid: bool,
}

struct Layer2Rollup {
    pending_txns: Vec<RollupTransaction>,
    fraud_proof: HashMap<String, bool>,
}

impl Layer2Rollup {
    fn new() -> Self {
        Layer2Rollup {
            pending_txns: vec![],
            fraud_proof: HashMap::new(),
        }
    }

    // Add transaction to rollup
    fn add_transaction(&mut self, sender: String, receiver: String, amount: f64) {
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
    fn execute_rollup(&mut self) {
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
    fn submit_fraud_proof(&mut self, sender: String) {
        self.fraud_proof.insert(sender.clone(), true);
        println!("Fraud proof submitted for {}", sender);
    }
}

// ------------------------- MAIN FUNCTION (Demo) -------------------------

fn main() {
    let mut rollup = Layer2Rollup::new();

    // Adding transactions
    rollup.add_transaction("Alice".to_string(), "Bob".to_string(), 100.0);
    rollup.add_transaction("Charlie".to_string(), "Dave".to_string(), 50.0);

    // Executing batch
    rollup.execute_rollup();

    // Fraud proof submitted
    rollup.submit_fraud_proof("Alice".to_string());

    // New batch (Alice's transactions will be flagged)
    rollup.add_transaction("Alice".to_string(), "Eve".to_string(), 200.0);
    rollup.execute_rollup();
}
