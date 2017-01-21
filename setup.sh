#!/bin/bash
sudo apt-get install nginx -y
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
sudo ln -s /home/pi/Poseidon_UI/html /var/www/html
ln /home/pi/Poseidon_UI/flow_raspberrypi.json /home/pi/.node-red/flow_raspberrypi.json
cd /home/pi/.node-red
sudo /etc/init.d/nginx start
node-red-start
