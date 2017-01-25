# Poseidon_UI
Raspberry Pi Hosted UI for Blue Robotics ROV. This project is currently under development. To join in discussion, check us out on gitter below.

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Poseidon_UI/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Screenshot](http://i.imgur.com/9kmJaQz.png?raw=true "Screenshot")

##About:
This is an early build of a user interface for a ROV that is hosted on the Raspberry Pi. This UI is designed around the use of the ArduSub software and Blue Robotics ROV builds.
Currently completed features are:  
- Raspberry Pi Status (cpu, gpu, temp, storage)
- Raspberry Pi System Info (OS, Wifi Status)
- Raspberry Pi Admin Functions (Reboot, Safe Shutdown)
- Raspberry Pi Software Update (mostly to update this software itself)

The anticipated upcoming features are :
- Wifi Configuration of the Pi (to connect to internet at home and download updates)
- Pixhawk Firmware Update
- Pixhawk Status (Alive, Firmware Version, etc.)
- Camera Config (RPi camera settings, external camera config)
- Configuration of Sensors (sonar connected to USB, etc.)
- Download of QGC binaries for in-field installs



##Setup Guide:
The following assumptions need to be followed for this to work:  
- Raspberry Pi IP address is set to 192.168.2.2 (or else you will need to change the .html code)
- Raspberry Pi has external internet access to be able to download nginx and node-red files.


#### New Install/Setup

###### Get The Code
On your Raspberry Pi, execute the following command to get the code.   
`sudo git clone http://github.com/bwmcclai/Poseidon_UI`

###### Run the Setup script
`cd Poseidon_UI`
`sudo bash setup.sh`

This will install flask, supervisor, and auto start on boot as well as move all files to their proper locations.  It will take a few minutes.

When complete, you should be able to navigate to 192.168.2.2 in your web browser and see the UI. 

The UI should show 'Connected' and the UpTime counter running.  If it is, then you have completed the initial setup successfully.



#### Updating Code from the UI
You can now check for updates and install them from the 'Configuration' section in the UI!  No SSH is needed.

#### Updating Code Manually
If you don't want to download and install updates from within the UI, follow the instructions below.

######Check the status of the repository vs what you currently have.
`cd Poseidon_UI`   
`git status`

###### Execute Update Script
`cd Poseidon_UI/scripts`   
`bash update.sh`


#####More Screenshots

Shutdown popup warning - with sound
![Flow](http://i.imgur.com/quYE6KQh.png?raw=true "Flow")







