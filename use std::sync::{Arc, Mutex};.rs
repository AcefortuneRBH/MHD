use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data = Arc::new(Mutex::new(0));

    let data_clone = Arc::clone(&data);
    let handle = thread::spawn(move || {
        let mut num = data_clone.lock().unwrap();
        *num = 42;
    });

    handle.join().unwrap();

    println!("Data: {}", *data.lock().unwrap());
}