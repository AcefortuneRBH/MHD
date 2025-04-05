## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.
## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.
## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.
## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.
## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.
# MHD
The Coin that will bring prosperities to all 🤲

## MHD Blockchain Deployment Guide

### Prerequisites

*   Ubuntu Server
*   Node.js and npm
*   Git
*   Hardhat
*   Etherscan API Key

### Deployment Steps

1.  **Server Setup:**
    *   Create an Ubuntu server instance on your chosen cloud provider or VPS.
    *   Connect to the server via SSH.
    *   Update the server: `sudo apt update && sudo apt upgrade -y`
    *   Install necessary tools: `sudo apt install -y nodejs npm git`

2.  **Project Transfer:**
    *   On your local machine, navigate to the MHD-Blockchain project directory.
    *   Use `scp` to copy the project to the server:
        ```bash
        scp -r . username@server_ip:/path/to/destination
        ```

3.  **Environment Configuration:**
    *   On the server, navigate to the project directory.
    *   Create a `.env` file with the following variables:
        ```
        SEPOLIA_URL=YOUR_SEPOLIA_RPC_URL
        PRIVATE_KEY=YOUR_PRIVATE_KEY
        ETHERSCAN_API_KEY=YOUR_ETHERSCAN_API_KEY
        ```
        Replace `YOUR_SEPOLIA_RPC_URL` with your Sepolia RPC URL, `YOUR_PRIVATE_KEY` with your private key, and `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
    *   Install Hardhat dependencies: `npm install`

4.  **Contract Deployment:**
    *   Execute the `deploy.sh` script to deploy the contracts:
        ```bash
        chmod +x deploy.sh
        ./deploy.sh sepolia
        ```
        Replace `sepolia` with the desired network (e.g., `sepolia`).

5.  **Verification:**
    *   The script attempts to automatically verify the contract on Etherscan after deployment.

6.  **Execute MHD Node:**
    *   After contract deployment, the script executes the MHD node. Ensure the `mhd_node` executable is in the `./build/` directory.

7.  **Process Management:**
    *   Install PM2: `npm install -g pm2`
    *   Start the application using PM2: `pm2 start app.js` (or the relevant entry point).

8.  **Reverse Proxy Setup:**
    *   Install Nginx: `sudo apt install nginx -y`
    *   Configure Nginx to forward requests to the application.

9.  **Firewall Configuration:**
    *   Enable UFW: `sudo ufw enable`
    *   Allow SSH, HTTP, and HTTPS traffic: `sudo ufw allow OpenSSH`, `sudo ufw allow 'Nginx HTTP'`, `sudo ufw allow 'Nginx HTTPS'`

10.  **Monitoring:**
    *   Set up monitoring tools (e.g., Prometheus, Grafana) to track application performance and errors.
