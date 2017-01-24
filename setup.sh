#!/bin/bash

#disable nginx to that we can use port 80 again
sudo systemctl stop nginx
sudo systemctl disable nginx

#install dependencies
sudo apt-get install python-pip
sudo pip install flask
sudo pip install flask-socketio
sudo pip install uwsgi flask

#starting up at boot
sudo apt-get -y install supervisor
cp /home/pi/Poseidon_UI/setup/poseidon.conf /etc/supervisor/conf.d/poseidon.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisor start poseidon
