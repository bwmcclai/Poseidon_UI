#!/usr/bin/python -u

from flask import jsonify
import serial.tools.list_ports
from terminalprocess import TerminalProcess

class CameraMonitor:
	def __init__(self):
		self.process = None
		self.readout = ''

	def start(self):
		cmd = "ls"
		self.process = TerminalProcess()
		self.process.run(cmd)

	def status(self):
		if self.process is not None:
			if self.process.running():
				self.readout += self.process.read()

		status = ''

		i = self.readout.find("ArduSub V")
		eol = self.readout.find('\n',i)
		if i != -1:
			status = self.readout[i:eol]
		else:
			status = "Unknown status"

		#print [status]
		return {"status":status}

	def stop(self):
		self.process.kill()

if __name__ == "__main__":
	import time
	cm = CameraMonitor()
	cm.start()
	loops = 0
	while loops < 30:
		loops += 1
		print cm.update()
		time.sleep(1)
	cm.stop()