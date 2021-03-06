# WUDS - Wifi User Detection System

This is my take on Tim Tomes' original WUDS project, from the original repo: [BitBucket.com](https://bitbucket.org/LaNMaSteR53/wuds)   

From Tim: "WUDS is a proximity detection system that uses Wi-Fi probe requests, signal strength, and a white list of MAC addresses to create a detection barrier and identify the presence of foreign devices within a protected zone. Designed with the Raspberry Pi in mind, WUDS can be installed and configured on any system with Python 2.x and a wireless card capable of Monitor mode. See [http://www.lanmaster53.com/2014/10/wifi-user-detection-system/](http://www.lanmaster53.com/2014/10/wifi-user-detection-system/) for more information."

Tim is no longer actively updating, so I have ported the project here and made a few changes:

- the original mac vendor lookup API is gone, so I have moved to a new provider     
- added slack alerts
- added Hubot (chatbot) alerts
- moved the whitelist to the database so it can be dynamically updated without restarting the process



## Setup

```bash
# install prerequisites
# iw      - control the wi-fi interface
# sqlite3 - interact with the database
# pycapy  - access full 802.11 frames
# screen  - (optional) daemonize WUDS
sudo apt install git iw python-pcapy python-pip sqlite3 screen vim
pip install slackclient
# install WUDS
git clone https://github.com/belldavidr/WUDS.git
cd wuds
# edit the config file
vim config.py
# lauch a screen session
screen
# execute the included run script
./run.sh
# Ctrl+A, D detaches from the screen session
```

## File Summary

* slack.py - runs a flask listener to handle slash command from slack
* example-config.py - example configuration file (update values and rename to config.py)
* alerts.py - custom alert modules
* core.py - core library
* run.sh - startup script
* README.md - this file
