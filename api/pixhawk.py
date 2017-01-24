#!/usr/bin/python -u

from flask import jsonify
import serial.tools.list_ports
from terminalprocess import TerminalProcess

class PixhawkMonitor:
	def __init__(self):
		self.process = None
		self.readout = ''

	def device(self):
		ports = serial.tools.list_ports.comports()
		for port in ports:
			if port[1].find("PX4") != -1:
				return port
		return ['','','']

	def start(self):
		port = self.device()[0]
		cmd = "mavproxy.py --master "+port+",115200" # --out udpin:localhost:9000 --out udpbcast:192.168.2.255:14550"
		self.process = TerminalProcess()
		self.process.run(cmd)

	def status(self):
		if self.process is not None:
			if self.process.running():
				self.readout += self.process.read()

		status = ''
		board = self.device()[1]

		if self.readout.find("Ready to FLY") != -1:
			status = "Ready to Dive"
		else:
			status = "Initializing"

		i = self.readout.find("ArduSub V")
		eol = self.readout.find('\n',i)
		if i != -1:
			firmware = self.readout[i:eol]
		else:
			firmware = "Unknown firmware"

		i = self.readout.find("Frame")
		eol = self.readout.find('\n',i)
		if i != -1:
			frame = self.readout[i+7:eol]
		else:
			frame = "Unknown frame type"

		#print [board,firmware,frame,status]
		return {"board":board,"firmware":firmware,"frame":frame,"status":status}

	def stop(self):
		self.process.kill()

if __name__ == "__main__":
	import time
	px = PixhawkMonitor()
	px.start()
	loops = 0
	while loops < 30:
		loops += 1
		print px.update()
		time.sleep(1)
	px.stop()