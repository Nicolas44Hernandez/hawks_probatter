#!/bin/bash

service hostapd start
ifconfig wlan0 up
ifconfig wlan0 192.168.4.1