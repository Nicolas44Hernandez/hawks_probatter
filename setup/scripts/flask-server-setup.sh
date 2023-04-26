#!/bin/bash

echo "SETUP FOR FLASK SERVER"


echo "********STAGE 1: INSTALL FLASK SERVER DEPENDENCIES ********"
sudo apt-get install -y python3-pip
echo antes
pwd
cd ../../hawks_batter_server
echo desues
pwd
pip install -r hawks_batter_server/requirements.txt
echo export PATH="$PATH:/home/pi/.local/bin" >> ~/.bashrc
