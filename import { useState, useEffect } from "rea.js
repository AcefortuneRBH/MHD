import { useState, useEffect } from "react";

function App() {
    const [nfts, setNfts] = useState([]);
    const [metadata, setMetadata] = useState("");

    useEffect(() => {
        fetch("http://localhost:8000/nfts")
            .then(res => res.json())
            .then(data => setNfts(data));
    }, []);

    const mintNFT = async () => {
        await fetch("http://localhost:8000/mint", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ owner: "User123", metadata }),
        });

        setMetadata("");
        window.location.reload();
    };

    return (
        <div>
            <h1>NFT Marketplace</h1>
            <input type="text" value={metadata} onChange={e => setMetadata(e.target.value)} />
            <button onClick={mintNFT}>Mint NFT</button>
            <ul>
                {nfts.map(nft => (
                    <li key={nft.id}>{nft.metadata} (Owner: {nft.owner})</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
