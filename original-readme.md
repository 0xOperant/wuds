# WUDS: Wi-Fi User Detection System

WUDS is a proximity detection system that uses Wi-Fi probe requests, signal strength, and a white list of MAC addresses to create a detection barrier and identify the presence of foreign devices within a protected zone. Designed with the Raspberry Pi in mind, WUDS can be installed and configured on any system with Python 2.x and a wireless card capable of Monitor mode. See [http://www.lanmaster53.com/2014/10/wifi-user-detection-system/](http://www.lanmaster53.com/2014/10/wifi-user-detection-system/) for more information.

## Setup

```bash
# install prerequisites
# iw      - control the wi-fi interface
# pycapy  - access full 802.11 frames
# sqlite3 - interact with the database
# screen  - (optional) daemonize WUDS
sudo apt-get install iw python-pcapy sqlite3 screen
# lauch a screen session
screen
# install WUDS
git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/wuds.git
cd wuds
# edit the config file
vim config.py
# execute the included run script
./run.sh
# Ctrl+A, D detaches from the screen session
```

## File Summary

* alerts.py - custom alert modules
* config.py - configuration file
* core.py - core library
* run.sh - startup script
* README.md - this file
