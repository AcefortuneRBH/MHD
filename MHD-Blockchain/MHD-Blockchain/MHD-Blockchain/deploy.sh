#!/bin/bash

echo "🚀 Deploying MHD Blockchain to the server..."

# Check if network is provided
if [ -z "$1" ]; then
  echo "❌ Error: Network name is required. Usage: ./deploy.sh <network>"
  exit 1
fi

NETWORK=$1
echo "🌐 Deploying to network: $NETWORK"

# Step 1: Install dependencies
echo "🔧 Installing dependencies..."
npm install

# Step 2: Compile contracts
echo "🔧 Compiling contracts..."
npx hardhat compile

# Step 3: Deploy contracts to the network
echo "🔧 Deploying contracts to the $NETWORK network..."
npx hardhat run scripts/deploy.js --network $NETWORK

echo "✅ MHD Blockchain deployed successfully to $NETWORK!"
