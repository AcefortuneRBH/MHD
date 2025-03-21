use crate::blockchain::Blockchain;
use crate::networking;

fn main() {
    let mut blockchain = Blockchain::new();

    // Add some blocks
    blockchain.add_block("First transaction".to_string());
    blockchain.add_block("Second transaction".to_string());

    println!("Blockchain valid: {}", blockchain.validate_chain());

    // Start the networking server in a new thread
    std::thread::spawn(|| {
        networking::start_server();
    });

    // Try to connect to a peer
    if let Some(latest_block) = blockchain.chain.last() {
        match networking::connect_to_peer("127.0.0.1:8080", latest_block) {
            Ok(_) => println!("Successfully sent block to peer"),
            Err(e) => println!("Failed to send block to peer: {}", e),
        }
    }
}
