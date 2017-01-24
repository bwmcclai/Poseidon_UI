#!/usr/bin/python -u

from flask import Flask, Blueprint, render_template, json, request
import pixhawk, camera

import time

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
		a = subprocess.check_output('ifconfig wlan0 | grep -w inet', shell=True)
		i = a.find("inet")
		a = a[i+5:i+18]
		return a
		
	def upTime(self):
		a = subprocess.check_output('uptime', shell=True)
		uptime_string = a.split("up")[0]
		return uptime_string

if __name__ == "__main__":
	pass