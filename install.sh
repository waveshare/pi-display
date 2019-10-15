#!/bin/sh

set -e

password=$1

# install pip and some apt dependencies
echo $password | sudo -S apt-get update
echo $password | sudo -S apt install -y python3-pil python3-smbus

# install pidisplay
echo $password | sudo -S python3 setup.py install

# install picard display service
echo $password | sudo -S sed -i -e 's:#dtparam=i2c_arm=on:dtparam=i2c_arm=on:g'  /boot/config.txt || true
python3 -m pidisplay.create_display_service
echo $password | sudo -S mv picard_display.service /etc/systemd/system/picard_display.service
echo $password | sudo -S systemctl enable picard_display
echo $password | sudo -S systemctl start picard_display
