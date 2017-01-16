# Poseidon_UI
Raspberry Pi Hosted UI for Blue Robotics ROV



##About:
This is an early build of a user interface for a ROV that is hosted on the Raspberry Pi. This UI is designed around the use of the ArduSub software and Blue Robotics ROV builds.
The anticipated features are :
- Wifi Configuration of the Pi (to connect to internet at home and download updates)
- Pixhawk Firmware Update
- Pixhawk Status (Alive, Firmware Version, etc.)
- Raspberry Pi Software Update (mostly to update this software itself)
- Raspberry Pi Status (cpu, gpu, temp, storage, software versions)
- Camera Config (RPi camera settings, external camera config)
- Configuration of Sensors (sonar connected to USB, etc.)
- Download of QGC binaries for in-field installs

##Prerequisites:
Eventually everything will be wrapped up nicely into an install package for the Raspberry Pi, but for now initial setup is done manually until we get further in the build.

####NGINX Web Server
Nginx is used to serve the files contained in this repository. First, SSH into the RPi and install nginx.
`sudo apt-get install nginx`

Nginx will start on boot, but if you want to run it now without rebooting, enter the following code.
`sudo /etc/init.d/nginx start`

For more nginx information, visit the following page: https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md




