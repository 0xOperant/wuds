###Download the latest Raspbian, flash to an SD card
*  https://www.raspberrypi.org/downloads/
*  https://www.raspberrypi.org/documentation/installation/installing-images/README.md
*  *Note: add 'ssh' file to /boot in order to enable SSH server on first boot (headless)*
  
###Update firmware and software
*  `sudo raspi-config`
*  `sudo apt-get update && apt-get upgrade -y`
*  `sudo apt-get dist-upgrade`

###Install dependencies:
*  `sudo apt-get install iw python-pcapy screen vim git python-mysqldb`
*  `git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/wuds.git`

###Require SSL to RDS (replace `encrypted_user` with mysql username)
*  On the Pi: `wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem`
*  In mysql: `GRANT USAGE ON *.* TO 'encrypted_user'@'%' REQUIRE SSL;`
*  
