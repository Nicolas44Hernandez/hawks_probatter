#!/bin/bash
LINE="export PATH="$PATH:/home/pi/.local/bin""
NGINX_CONFIG_FILE="/etc/nginx/sites-available/default"
RESOURCES=setup/resources

echo "SETUP FOR PROBATTER APP"


echo "********STAGE 1: INSTALL FLASK SERVER DEPENDENCIES ********"
sudo apt-get install -y python3-pip
cd ../../
pip install -r hawks_batter_server/requirements.txt
echo 'export PATH="\$PATH:/home/pi/.local/bin"' >> ~/.bashrc

echo "********STAGE 2: CREATE LOG FILES ********"
mkdir logs
mkdir logs/manager
mkdir logs/interface
touch logs/app.log 
touch logs/rest_api.log 
touch logs/manager/video.log logs/interface/video_capture.log
sudo chmod -R 777 logs

echo "********STAGE 3: INSTALL WEB SERVER DEPENDENCIES ********"
sudo apt install -y nginx
cd ~
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm install node
nvm alias default 19.9.0
sudo apt install build-essential


echo "********STAGE 4: INSTALL WEB SERVER ********"
cd -
cd web_server
npm install
npm run build


echo "********STAGE 5: SET FLASK APP AS A SERVICE ********"
cd ../
sudo cp services/probatter.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable probatter
sudo systemctl restart probatter

echo "********STAGE 6: SET WEBSERVICE AS A SERVICE ********"
cd -
sudo cp $NGINX_CONFIG_FILE $NGINX_CONFIG_FILE.orig
echo "Old file backup in: $NGINX_CONFIG_FILE.orig"
echo "now we are here:"
pwd
sudo cp $RESOURCES/nginx-config $NGINX_CONFIG_FILE
echo "File created : $NGINX_CONFIG_FILE"
sudo systemctl restart nginx


echo "********STAGE 7: REBOOT********"
sudo reboot now