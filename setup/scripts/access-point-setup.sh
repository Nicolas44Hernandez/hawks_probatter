#!/bin/bash

DNSMASQ_CONFIG_FILE="/etc/dnsmasq.conf"
HOSTAPD_CONFIG_FILE="/etc/hostapd/hostapd.conf"
DHCPCD_CONFIG_FILE="/etc/dhcpcd.conf"
INIT_FILE="/etc/init.d/ap.sh"
RESOURCES=../resources


source ../variables/wlan-addr.env
echo "SETUP FOR WIFI ACCESS POINT"

echo "********STAGE 1: UPDATE AND UPGRADE SYSTEM ********"
# Update packages
sudo apt -y update
sudo apt -y upgrade


echo "********STAGE 2: INSTALL PACKAGES ********"
# Install the necessary packages necessary
# to configure the PI as a Wifi access point
sudo apt -y install python3-pip dnsmasq iptables
sudo apt -y install hostapd
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent


echo "********STAGE 3: SETUP HOSTAPD********"
sudo cp $HOSTAPD_CONFIG_FILE $HOSTAPD_CONFIG_FILE.orig
echo "Old file backup in: $HOSTAPD_CONFIG_FILE.orig"
sudo cp $RESOURCES/hostapd.conf $HOSTAPD_CONFIG_FILE
echo "File created : $HOSTAPD_CONFIG_FILE"

echo "********STAGE 4: SETUP DNSMASQ********"
sudo cp $DNSMASQ_CONFIG_FILE $DNSMASQ_CONFIG_FILE.orig
echo "Old file backup in: $DNSMASQ_CONFIG_FILE.orig"
sudo cp $RESOURCES/dnsmasq.conf $DNSMASQ_CONFIG_FILE
echo "File created : $DNSMASQ_CONFIG_FILE"

echo "********STAGE 5: SETUP DHCPCD CONF INTERFACES ********"
sudo cp $DHCPCD_CONFIG_FILE $DHCPCD_CONFIG_FILE.orig
echo "Old file backup in: $DHCPCD_CONFIG_FILE.orig"
sudo cp $RESOURCES/dhcpcd.conf $DHCPCD_CONFIG_FILE
echo "File created : $DHCPCD_CONFIG_FILE"

echo "********STAGE 6: COPY SCRIPT TO ACTIVATE ACCESS POINT ********"
sudo cp $RESOURCES/ap.sh $INIT_FILE
echo "File created : $INIT_FILE"
cd /etc/init.d
sudo chmod 755 ./ap.sh
sudo update-rc.d ap.sh defaults
