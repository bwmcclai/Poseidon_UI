# Poseidon_UI
Raspberry Pi Hosted UI for Blue Robotics ROV. This project is currently under development. To join in discussion, check us out on gitter below.

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Poseidon_UI/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Screenshot](http://i.imgur.com/ISvipW9l.png?raw=true "Screenshot")

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

##Setup Guide:
Eventually everything will be wrapped up nicely into an install package for the Raspberry Pi, but for now initial setup is done manually until we get further in the build.

The following assumptions need to be followed for this to work:  
- Raspberry Pi IP address is set to 192.168.2.2 (or else you will need to change the .html code)
- Raspberry Pi has external internet access to be able to download nginx and node-red files.

####NGINX Web Server
Nginx is used to serve the files contained in this repository. First, SSH into the RPi and install nginx.  
`sudo apt-get install nginx`

Nginx will start on boot, but if you want to run it now without rebooting, enter the following code.  
`sudo /etc/init.d/nginx start`

When complete, you should be able to navigate to 192.168.2.2 (RPi IP address) in your webbrowser and see a sample file.
For more nginx information, visit the following page:   
https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

####Updating NGINX files with this repository  
In SSH, cd to the default nginx www folder:  
`cd /var/www/html/`

Then clone this repository to the folder:  
`sudo git clone https://github.com/bwmcclai/Poseidon_UI.git`

You should now be able to navigate again to 192.168.2.2 and see the UI properly.  The next section deals with the data backend.

####Node-Red
Node-Red is the backend of the UI and provides bi-directional communication.  It can be used to expand the functionality of the UI and allow users to customize the code for their application from within the web browser.

To install Node-Red, visit the following page and follow along:  
http://nodered.org/docs/hardware/raspberrypi.html

If everything worked properly, you should now be able to navigate to 192.168.2.2:1880 to see the node-red UI.

You can now add new modules to node-red and extend the functionality.  Currently, there is (1) additional packages that are in use.  
To install, first navigate to the node-red directory.  
`cd ~/.node-red`  
Then add the node-red-contrib-os package.  
`npm install node-red-contrib-os`

Note:  you will need to restart the Node-Red server once you add the new package for it to show up.





