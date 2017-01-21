#!/bin/bash
sudo apt-get install nginx -y
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
sudo ln -s /home/pi/Poseidon_UI/html /var/www/html
cp /home/pi/Poseidon_UI/flows_raspberrypi.json /home/pi/.node-red/flows_raspberrypi.json
cd /home/pi/.node-red
sudo /etc/init.d/nginx start
node-red-start
