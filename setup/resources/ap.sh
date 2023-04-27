#!/bin/bash

sudo ifconfig wlan0 192.168.4.1
sudo ifconfig wlan0 up
sudo systemctl restart dnsmasq hostapd