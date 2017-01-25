#!/bin/bash
sudo git reset --hard
sudo git pull
import time
time.sleep(5)
sudo systemctl restart poseidon

