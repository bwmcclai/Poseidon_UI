#!/usr/bin/python -u

def getUpTime():
	from datetime import timedelta
		while True:
			#socketio.sleep(1)	
			with open('/proc/uptime', 'r') as f:
				uptime_seconds = float(f.readline().split()[0])
				uptime_string = str(timedelta(seconds = uptime_seconds))
				uptime_string = uptime_string.split('.')[0]
	
	return uptime_string