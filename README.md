# HAWKS PROBATTER

# OS installation
You can use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to flash the last 64-bit desktop version


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
## Clone repository

```bash
git clone https://github.com/Nicolas44Hernandez/hawks_probatter.git
```

# AUTOMATIC INSTALLATION

You can use the install script:
```bash
cd hawks_probatter/setup/scripts/
sudo chmod 755 install.sh 
sudo ./install.sh
```

## Set RPI as access point 
Create an access point in RPI network settings. 

# Hardware connection
Connect machine, and the sensors to the RPI.

![RPI connection](app_data/rpi-connection.png)