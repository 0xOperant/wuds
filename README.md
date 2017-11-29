# WUDS - Wifi User Detection System

This is my take on Tim Tomes' original WUDS project, from the original repo: [BitBucket.com](https://bitbucket.org/LaNMaSteR53/wuds)   

From Tim: "WUDS is a proximity detection system that uses Wi-Fi probe requests, signal strength, and a white list of MAC addresses to create a detection barrier and identify the presence of foreign devices within a protected zone. Designed with the Raspberry Pi in mind, WUDS can be installed and configured on any system with Python 2.x and a wireless card capable of Monitor mode. See [http://www.lanmaster53.com/2014/10/wifi-user-detection-system/](http://www.lanmaster53.com/2014/10/wifi-user-detection-system/) for more information."

Tim is no longer actively updating, so I have ported the project here and made a few changes:   
- the original mac vendor lookup API is gone, so I have moved to a new provider     
- added slack alerts
- added slash command integration for slack

## Setup

```bash
# install prerequisites
# iw      - control the wi-fi interface
# sqlite3 - interact with the database
# pycapy  - access full 802.11 frames
# screen  - (optional) daemonize WUDS
# python-pip - (optional) python package management
# flask - (optional) host Slack slash commands
# slackclient - (optional) interface with Slack API
# ngrok - (optional) allow tunneling to localhost
sudo apt install git iw python-pcapy sqlite3 screen vim python-pip
sudo pip install flask
sudo pip install slackclient
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
rm ngrok-stable-linux-arm.zip
# install WUDS
git clone https://github.com/belldavidr/WUDS.git
cd wuds
# edit the config file
vim config.py
# lauch a screen session
screen -S run
# execute the included run script
sudo ./run.sh
# Ctrl+A, D detaches from the screen session
screen -S flask
sudo python slack.py
# Ctrl+A, D detaches from the screen session
screen -S ngrok
./ngrok http 5000
# Ctrl+A, D detaches from the screen session
# screen -x <name> re-attaches to specified screen sessions
```

## File Summary

* alerts.py - custom alert modules
* config.py - configuration file
* core.py - core library
* run.sh - startup script
* README.md - this file
* slack.py - flask web server to host slack slash commands  
