/Applications/.app/Contents/MacOS/iMovie ; exit;
/Library/Application\ Support/iLifeMediaBrowser/Plug-Ins/iLMBPhotosPlugin.ilmbplugin/Contents/MacOS/iLMBPhotosPlugin ; exit;
/Applications/Python\ 3.13/Install\ Certificates.command ; exit;
/Applications/Python\ 3.13/Update\ Shell\ Profile.command ; exit;
python3 miner.py
cd "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app"
/usr/local/bin/python3 "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app/node.py"
npm install --save-dev hardhat @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers
mkdir -p contracts
mv MahdiCoin.sol contracts/
npx hardhat compile
npx hardhat run scripts/deploy.js --network hardhat
mv /Users/timxayamoungkhoun/flash%20blockchain/flash-blockchain-app/contracts/MahdiCoin_test_test.ts /Users/timxayamoungkhoun/flash%20blockchain/flash-blockchain-app/contracts/MahdiCoin_test_test.sol
npm install --save-dev hardhat
cd "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app"
mkdir -p contracts migrations
npm install @openzeppelin/contracts
truffle compile
truffle migrate --network development
npm run build
ssh username@203.0.113.0
ssh-keygen
/usr/local/bin/python3 /Users/timxayamoungkhoun/.vscode/extensions/ms-python.python-2025.0.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/timxayamoungkhoun/.vscode/extensions/ms-python.python-2025.0.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt
/Users/timxayamoungkhoun/FBC-9/.venv/bin/python -m pip install gunicorn
cat ~/.ssh/id_rsa.pub
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();
module.exports = {
    solidity: "0.8.20",
    networks: {
        sepolia: {
            url: `https://sepolia.infura.io/v3/${process.env.INFURA_PROJECT_ID}`,
            accounts: [process.env.PRIVATE_KEY]
        }
    },
    etherscan: {
        apiKey: process.env.ETHERSCAN_API_KEY
    }
};
async function main() {
    const MahdiCoin = await ethers.getContractFactory("MahdiCoin");
    const token = await MahdiCoin.deploy();
    await token.waitForDeployment();
    console.log("MahdiCoin deployed to:", await token.getAddress());
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract MahdiCoin is ERC20 {
    constructor() ERC20("MahdiCoin", "MC") {
        _mint(msg.sender, 9000000000 * 10**18);
    }
}
constructor(address _mahdiCoinAddress) {
    mahdiCoin = IERC20(_mahdiCoinAddress);
}
function lockMC(uint256 amount) public {
    require(mahdiCoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");
}
function releaseMC(address recipient, uint256 amount) public {
    require(mahdiCoin.transfer(recipient, amount), "Transfer failed");
}
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
npm install @openzeppelin/contracts dotenv
async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying bridge with account:", deployer.address);
    const Bridge = await ethers.getContractFactory("FlashBridge");
    const bridge = await Bridge.deploy("MAHDICOIN_ADDRESS_HERE");
    await bridge.waitForDeployment();
    console.log("Bridge deployed to:", await bridge.getAddress());
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
brew update
brew upgrade
brew install python@3.11
brew install postgresql
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.zshrc
nvm install 16
nvm use 16
brew install git
brew install wget
brew install jq
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask==2.3.3
web3==6.11.1
pytest==7.4.2
python-dotenv==1.0.0
requests==2.31.0
cryptography==41.0.3
psycopg2-binary==2.9.7
brew services start postgresql
createdb flash_blockchain
chmod +x scripts/system-setup.sh
chmod +x scripts/venv-setup.sh
chmod +x scripts/db-setup.sh
MNEMONIC=your_wallet_seed_phrase
INFURA_PROJECT_ID=your_infura_project_id
PRIVATE_KEY=your_private_key
ETHERSCAN_API_KEY=your_etherscan_api_key
NETWORK=sepolia
CHAIN_ID=11155111
require('dotenv').config();
const validateEnv = () => {
    const required = [
        'MNEMONIC',
        'INFURA_PROJECT_ID',
        'PRIVATE_KEY',
        'ETHERSCAN_API_KEY'
    ];
    for (const key of required) {
        if (!process.env[key]) {
            throw new Error(`Missing required env var: ${key}`);
        }
    }
};
module.exports = { validateEnv };/Applications/.app/Contents/MacOS/iMovie ; exit;
/Library/Application\ Support/iLifeMediaBrowser/Plug-Ins/iLMBPhotosPlugin.ilmbplugin/Contents/MacOS/iLMBPhotosPlugin ; exit;
/Applications/Python\ 3.13/Install\ Certificates.command ; exit;
/Applications/Python\ 3.13/Update\ Shell\ Profile.command ; exit;
python3 miner.py
cd "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app"
/usr/local/bin/python3 "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app/node.py"
npm install --save-dev hardhat @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers
mkdir -p contracts
mv MahdiCoin.sol contracts/
npx hardhat compile
npx hardhat run scripts/deploy.js --network hardhat
mv /Users/timxayamoungkhoun/flash%20blockchain/flash-blockchain-app/contracts/MahdiCoin_test_test.ts /Users/timxayamoungkhoun/flash%20blockchain/flash-blockchain-app/contracts/MahdiCoin_test_test.sol
npm install --save-dev hardhat
cd "/Users/timxayamoungkhoun/flash blockchain/flash-blockchain-app"
mkdir -p contracts migrations
npm install @openzeppelin/contracts
truffle compile
truffle migrate --network development
npm run build
ssh username@203.0.113.0
ssh-keygen
/usr/local/bin/python3 /Users/timxayamoungkhoun/.vscode/extensions/ms-python.python-2025.0.0-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/timxayamoungkhoun/.vscode/extensions/ms-python.python-2025.0.0-darwin-arm64/python_files/deactivate/zsh/envVars.txt
/Users/timxayamoungkhoun/FBC-9/.venv/bin/python -m pip install gunicorn
cat ~/.ssh/id_rsa.pub
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();
module.exports = {
    solidity: "0.8.20",
    networks: {
        sepolia: {
            url: `https://sepolia.infura.io/v3/${process.env.INFURA_PROJECT_ID}`,
            accounts: [process.env.PRIVATE_KEY]
        }
    },
    etherscan: {
        apiKey: process.env.ETHERSCAN_API_KEY
    }
};
async function main() {
    const MahdiCoin = await ethers.getContractFactory("MahdiCoin");
    const token = await MahdiCoin.deploy();
    await token.waitForDeployment();
    console.log("MahdiCoin deployed to:", await token.getAddress());
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract MahdiCoin is ERC20 {
    constructor() ERC20("MahdiCoin", "MC") {
        _mint(msg.sender, 9000000000 * 10**18);
    }
}
constructor(address _mahdiCoinAddress) {
    mahdiCoin = IERC20(_mahdiCoinAddress);
}
function lockMC(uint256 amount) public {
    require(mahdiCoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");
}
function releaseMC(address recipient, uint256 amount) public {
    require(mahdiCoin.transfer(recipient, amount), "Transfer failed");
}
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
npm install @openzeppelin/contracts dotenv
async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying bridge with account:", deployer.address);
    const Bridge = await ethers.getContractFactory("FlashBridge");
    const bridge = await Bridge.deploy("MAHDICOIN_ADDRESS_HERE");
    await bridge.waitForDeployment();
    console.log("Bridge deployed to:", await bridge.getAddress());
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
brew update
brew upgrade
brew install python@3.11
brew install postgresql
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.zshrc
nvm install 16
nvm use 16
brew install git
brew install wget
brew install jq
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask==2.3.3
web3==6.11.1
pytest==7.4.2
python-dotenv==1.0.0
requests==2.31.0
cryptography==41.0.3
psycopg2-binary==2.9.7
brew services start postgresql
createdb flash_blockchain
chmod +x scripts/system-setup.sh
chmod +x scripts/venv-setup.sh
chmod +x scripts/db-setup.sh
MNEMONIC=your_wallet_seed_phrase
INFURA_PROJECT_ID=your_infura_project_id
PRIVATE_KEY=your_private_key
ETHERSCAN_API_KEY=your_etherscan_api_key
NETWORK=sepolia
CHAIN_ID=11155111
require('dotenv').config();
const validateEnv = () => {
    const required = [
        'MNEMONIC',
        'INFURA_PROJECT_ID',
        'PRIVATE_KEY',
        'ETHERSCAN_API_KEY'
    ];
    for (const key of required) {
        if (!process.env[key]) {
            throw new Error(`Missing required env var: ${key}`);
        }
    }
};
module.exports = { validateEnv };