#!/bin/bash

service hostapd start
ifconfig wlan0 up
ifconfig wlan 192.168.4.1