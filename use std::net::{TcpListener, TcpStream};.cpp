use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use serde_json;
use crate::Block;

pub fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    match stream.read(&mut buffer) {
        Ok(size) => {
            let message = String::from_utf8_lossy(&buffer[..size]);
            println!("Received: {}", message);

            // Deserialize the received data into a Block
            if let Ok(received_block) = serde_json::from_str::<Block>(&message) {
                println!("Received block: {:?}", received_block);
            } else {
                println!("Failed to deserialize block");
            }

            // Echo back the same message
            stream.write_all(&buffer[..size]).expect("Failed to send data");
        }
        Err(e) => println!("Failed to read from stream: {}", e),
    }
}

pub fn start_server() {
    let listener = TcpListener::bind("127.0.0.1:8080").expect("Failed to bind");
    println!("Server listening on 127.0.0.1:8080");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New connection: {}", stream.peer_addr().expect("msg"));
                handle_client(stream)
            }
            Err(e) => println!("Failed to establish connection: {}", e),
        }
    }
}

pub fn connect_to_peer(peer_address: &str, block: &Block) -> Result<(), Box<dyn std::error::Error>> {
    let mut stream = TcpStream::connect(peer_address)?;
    println!("Connected to peer: {}", peer_address);

    // Serialize the block into a JSON string
    let block_string = serde_json::to_string(block)?;

    // Send the block to the peer
    stream.write_all(block_string.as_bytes())?;
    println!("Sent block to peer: {}", peer_address);

    // Read the response from the peer
    let mut buffer = [0; 1024];
    let size = stream.read(&mut buffer)?;
    println!("Received response from peer: {}", String::from_utf8_lossy(&buffer[..size]));

    Ok(())
}
