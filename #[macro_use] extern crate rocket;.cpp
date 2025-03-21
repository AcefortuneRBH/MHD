#[macro_use] extern crate rocket;
use rocket::serde::{Serialize, Deserialize, json::Json};
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
struct NFT {
    id: u32,
    owner: String,
    metadata: String,
}

struct NFTMarketplace {
    nfts: Mutex<Vec<NFT>>,
}

#[post("/mint", format = "json", data = "<nft>")]
fn mint_nft(nft_marketplace: &rocket::State<NFTMarketplace>, nft: Json<NFT>) -> Json<NFT> {
    let mut nfts = nft_marketplace.nfts.lock().unwrap();
    let new_nft = NFT {
        id: nfts.len() as u32 + 1,
        owner: nft.owner.clone(),
        metadata: nft.metadata.clone(),
    };

    nfts.push(new_nft.clone());
    Json(new_nft)
}

#[get("/nfts")]
fn get_nfts(nft_marketplace: &rocket::State<NFTMarketplace>) -> Json<Vec<NFT>> {
    let nfts = nft_marketplace.nfts.lock().unwrap();
    Json(nfts.clone())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(NFTMarketplace {
            nfts: Mutex::new(vec![]),
        })
        .mount("/", routes![mint_nft, get_nfts])
}
