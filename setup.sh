#!/bin/bash

#disable nginx to that we can use port 80 again
sudo systemctl stop nginx
sudo systemctl disable nginx

#install dependencies
sudo apt-get install python-pip
sudo pip install flask
sudo pip install flask-socketio
sudo pip install uwsgi flask

#starting up at boot using systemd
cp /home/pi/Poseidon_UI/setup/poseidon.service /etc/systemd/system/poseidon.service
sudo systemctl daemon-reload
sudo systemctl enable poseidon.service
sudo systemctl start poseidon.service

