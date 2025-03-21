use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use serde_json;
use crate::Block; // Assuming Block is in the root of your crate

pub fn start_server() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    println!("Server listening on 127.0.0.1:8080");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                std::thread::spawn(|| {
                    handle_connection(stream);
                });
            }
            Err(e) => {
                println!("Error: {}", e);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    match stream.read(&mut buffer) {
        Ok(size) => {
            let message = String::from_utf8_lossy(&buffer[..size]);
            println!("Received: {}", message);

            // Attempt to deserialize the message as a Block
            if let Ok(received_block) = serde_json::from_str::<Block>(&message) {
                println!("Received block: {:?}", received_block);
            } else {
                println!("Received data is not a valid Block.");
            }

            // Echo back the message
            stream.write_all(&buffer[..size]).unwrap();
        }
        Err(e) => {
            println!("Error reading from stream: {}", e);
        }
    }
}

pub fn connect_to_peer(peer_address: &str, block: &Block) -> Result<(), String> {
    match TcpStream::connect(peer_address) {
        Ok(mut stream) => {
            println!("Successfully connected to peer: {}", peer_address);

            // Serialize the block to JSON
            let block_json = serde_json::to_string(block).map_err(|e| e.to_string())?;

            // Send the block to the peer
            stream.write_all(block_json.as_bytes()).map_err(|e| e.to_string())?;
            println!("Sent block to peer");

            // Read the response from the peer
            let mut buffer = [0; 1024];
            let size = stream.read(&mut buffer).map_err(|e| e.to_string())?;
            let response = String::from_utf8_lossy(&buffer[..size]);
            println!("Received response: {}", response);

            Ok(())
        }
        Err(e) => {
            Err(format!("Failed to connect to peer {}: {}", peer_address, e))
        }
    }
}
