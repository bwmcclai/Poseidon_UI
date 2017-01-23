#!/bin/bash
cp /home/pi/Poseidon_UI/flows_raspberrypi.json /home/pi/.node-red/flows_raspberrypi.json
cd /home/pi/.node-red
sudo /etc/init.d/nginx start
node-red-stop
node-red-start
