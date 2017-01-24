#!/usr/bin/python -u

from flask import Flask, Blueprint, render_template, json, request
import pixhawk, camera

import subprocess

class Status:
	def __init__(self):
		self.px = pixhawk.PixhawkMonitor()
		self.cm = camera.CameraMonitor()
		self.px.start()
		self.cm.start()

	def discover(self):
		data = [{"name":"Ping1D","status":"Unknown"}]
		return data

	def ipAddress(self,ifname):
		a = subprocess.check_output('ifconfig en0 | grep -w inet', shell=True)
		i = a.find("inet")
		a = a[i+5:i+18]
		return a

if __name__ == "__main__":
	pass