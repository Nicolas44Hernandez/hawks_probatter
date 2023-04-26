#!/bin/bash
LINE="export PATH="$PATH:/home/pi/.local/bin""

echo "SETUP FOR FLASK SERVER"


echo "********STAGE 1: INSTALL FLASK SERVER DEPENDENCIES ********"
sudo apt-get install -y python3-pip
cd ../../
pip install -r hawks_batter_server/requirements.txt
echo 'export PATH="\$PATH:/home/pi/.local/bin"' >> ~/.bashrc

echo "********STAGE 2: INSTALL WEB SERVER DEPENDENCIES ********"
cd ~
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm install node
nvm alias default 19.9.0
sudo apt install build-essential

echo "********STAGE 2: INSTALL WEB SERVER ********"
cd -
cd web_server
npm install
