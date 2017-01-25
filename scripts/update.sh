#!/bin/bash
(cd /home/pi/Poseidon_UI && sudo git reset --hard)
(cd /home/pi/Poseidon_UI && sudo git pull)
sudo systemctl restart poseidon
