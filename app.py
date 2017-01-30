#!/usr/bin/env python
from flask import Flask, render_template, session, request, send_file
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import subprocess
import os
from api import status
from api import wifi



stat = status.Status()
wifistat = wifi.Status()

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None



def background_thread():
    """Example of how to send server generated events to clients."""
    from datetime import timedelta
    while True:
		socketio.sleep(1)	
		with open('/proc/uptime', 'r') as f:
			uptime_seconds = float(f.readline().split()[0])
			uptime_string = str(timedelta(seconds = uptime_seconds))
			uptime_string = uptime_string.split('.')[0]
			socketio.emit('uptime',{'data': uptime_string})

## UI Pages ##
@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/raspberry_pi')
def raspberry_pi():
    return render_template('raspberry_pi.html', async_mode=socketio.async_mode)

@app.route('/configuration')
def configuration():
    return render_template('configuration.html', async_mode=socketio.async_mode)

@app.route('/logs')
def logs():
    return render_template('logs.html', async_mode=socketio.async_mode)
	
## Communications ##
@socketio.on('my_ping')
def ping_pong():
    emit('my_pong')


@socketio.on('connect')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


### Commands from UI ###
#########################################################################################
@socketio.on('command_from_UI')
def command_message(message):
    if message['data'] == 'piReboot':
        os.system('sudo reboot')
    if message['data'] == 'piShutdown':
        os.system('sudo shutdown -r now')
    if message['data'] == 'reloadUI':
        os.system('sudo systemctl restart poseidon')
        #emit('my_repsonse',{'data': 'reloadComplete'})
    if message['data'] == 'checkForUpdates':
		result = subprocess.check_output("(cd /home/pi/Poseidon_UI && git status)",shell=True)
		results = 'Git status is still under development.  You can go ahead and download and install though if you know you want to do this.'
		emit('gitStatusResponse',{'data': str(results)})
    if message['data'] == 'updateApp':
		emit('updateResults',{'data': 'executed'})
		result = subprocess.check_output("(cd /home/pi/Poseidon_UI/scripts && bash update.sh)",shell=True)
		#result = 'ok'
	
    if message['data'] == 'getLogs':
		cmd = 'sudo find / -name "*.tlog"'
		ls = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
		for log in ls.stdout:
			emit('logsList',{'data':log})
		

@app.route('/downloadLog', methods=['GET'])
def download_log():
    path = request.args.get('path')
    #path = '/home/pi/companion/component.tlog'
    name = request.args.get('name')
    #name = 'component.tlog'
    return send_file(path,
                     mimetype='text/tlog',
                     attachment_filename=name,
                     as_attachment=True)
		
	#leave this here as an example
	#session['receive_count'] = session.get('receive_count', 0) + 1
    #emit('my_response',{'data': message['data'], 'count': session['receive_count']})



###  Sending data to the UI ###
#########################################################################################
@socketio.on('getPiData')
def PiData(message):
    emit('Disk_Space',{'data': stat.diskSpace()})
    emit('Pi_OS',{'data': stat.os()})
    emit('CPU_Temp',{'data': stat.CPUTemp()})
    emit('CPU_Mem',{'available': stat.CPUMem()[0],'total': stat.CPUMem()[1]})
    emit('MAVProxy_Status',{'data': stat.MAVProxyStatus()})
    emit('Video_Status',{'data': stat.videoStatus()})
    emit('Pixhawk_Status',{'data': stat.pixhawkStatus()})
    emit('Wifi_Network',{'network': wifistat.networkInfo()[0],'signal': wifistat.networkInfo()[1],'ip': wifistat.networkInfo()[2]})

#The Raspberry Pi page will request data refreshes every x seconds
@socketio.on('refreshPiData')
def refreshPiData(message):
    emit('CPU_Temp',{'data': stat.CPUTemp()})
    emit('CPU_Mem',{'available': stat.CPUMem()[0],'total': stat.CPUMem()[1]})
    emit('MAVProxy_Status',{'data': stat.MAVProxyStatus()})
    emit('Video_Status',{'data': stat.videoStatus()})
    emit('Pixhawk_Status',{'data': stat.pixhawkStatus()})
    emit('Wifi_Network',{'network': wifistat.networkInfo()[0],'signal': wifistat.networkInfo()[1],'ip': wifistat.networkInfo()[2]})


if __name__ == '__main__':
    socketio.run(app, debug=False,host='0.0.0.0',port=80)
