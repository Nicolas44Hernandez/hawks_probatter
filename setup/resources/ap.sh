#!/bin/bash

sudo systemctl stop dnsmasq hostapd
sudo ifconfig wlan0 192.168.4.1
sudo ifconfig wlan0 up
sudo systemctl start dnsmasq hostapd