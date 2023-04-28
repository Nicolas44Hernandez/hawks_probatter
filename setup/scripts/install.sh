#!/bin/bash

echo "Probatter V1.0"
echo "Installing.........................."

sudo chmod 755 opencv-installation.sh 
sudo chmod 755 probatter-install.sh 
sudo chmod 755 access-point-setup.sh 

echo "------------------------------- INSTALLING OPENCV -------------------------------"
sudo ./opencv-installation.sh

echo "------------------------------- INSTALLING PROBATTER -------------------------------"
sudo chmod 755 probatter-install.sh 

echo "------------------------------- SETTING AS WIFI ACCESS POINT -------------------------------"
sudo ./access-point-setup.sh

echo Rebooting.....
sudo reboot now