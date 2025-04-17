
# Install nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Reload shell configuration
source ~/.zshrc  # or source ~/.bash_profile

# Install and use Node.js 16
nvm install 16
nvm use 16

mkdir -p explorer
cd explorer
npm init -y