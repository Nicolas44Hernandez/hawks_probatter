# HAWKS PROBATTER

# OS installation
You can use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to flash the last 64-bit Bullseye ligth version (no desktop)


# Initial setup

Use raspi-config to configure the RPI
```bash
sudo raspi-config
```
- Configure the SSH interface
- Connect to your Wi-Fi network (you must have an internet connection)

## Update OS

```bash
sudo apt update
sudo apt upgrade
```

## Install and configure git

```bash
sudo apt install git
git config --global user.name "Nicolas44Hernandez"
git config --global user.email n44hernandezp@gmail.com
```

## Create and add ssh key to your github account

Complete ssh key setup is explained in the following [link](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Clone repository

```bash
mkdir workspace
git clone git@github.com:Nicolas44Hernandez/hawks_probatter.git
```

## Install pip3

```bash
sudo apt-get install python3-pip
```

## Install opencv
The complete installation instruction could be found [here](https://qengineering.eu/install-opencv-lite-on-raspberry-pi.html)

## Install the dependencies
```bash
pip install -r hawks_batter_server/requirements.txt
```

To add the dependencies to PATH, edit the `bashrc` file

```bash
nano ~/.bashrc
```
add line
```
export PATH="$PATH:/home/pi/.local/bin"
```

## Install web server dependencies
install nvm
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

install node
```bash
nvm install node
nvm alias default 19.9.0
sudo apt install build-essential
```

## Install web server
```bash
cd web_server
npm install
```

## RUN server (TODO: delete)
```bash
npm run host
```

## TODO: set as Access point

## Create log files

Log files defined in configuration file located in *server_box/server/config/logging-config.yml* must be created before launching the application

```bash
mkdir logs
mkdir logs/manager
mkdir logs/interface
touch logs/app.log 
touch logs/rest_api.log 
touch logs/manager/video.log logs/interface/video_capture.log
```

# Hardware connection TODO: image

# Set app as a service
## Set web app as a service
build the web app
```bash
cd web_server
npm run build
```
modify nginx config
```bash
sudo nano /etc/nginx/sites-available/default
```
copy the following content to the file
```
server {
    listen      80;
    server_name example.com www.example.com;
    charset utf-8;
    root    /home/pi/workspace/hawks_probatter/web_server/dist;
    index   index.html;
    #Always serve index.html for any request
    location / {
        root /home/pi/workspace/hawks_probatter/web_server/dist;
        try_files $uri  /index.html;
    }
    error_log  /var/log/nginx/vue-app-error.log;
    access_log /var/log/nginx/vue-app-access.log;
}
```
Restart nginx service
```bash
sudo systemctl restart nginx
```

## Set flask app as a service
Copy the service file
```bash
sudo cp services/probatter.service /etc/systemd/system/
```

Register service
```bash
sudo systemctl daemon-reload
sudo systemctl enable probatter
sudo systemctl restart probatter
```