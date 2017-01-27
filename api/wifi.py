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


	def ipAddress(self,ifname):
		a = subprocess.check_output('ifconfig wlan0 | grep -w inet', shell=True)
		i = a.find("inet")
		a = a[i+5:i+18]
		return a
		
	def networkInfo(self):
		try:
			result = subprocess.check_output('iwconfig', shell=True)
			network = str.split(str.split(result,"\n")[0],'"')[1]
			signal = str.split(str.split(result,"Signal level=")[1],"/")[0]
			
			result2 = subprocess.check_output('ifconfig wlan0', shell=True)
			#ip = str.split(str.split(result2,"inet addr:")[1],'" ")[0]
			ip = str.split(str.split(result2,"inet addr:")[1]," ")[0]
		except:
			network = 'Not Connected'
			signal = 0
			ip = ''
		return network, signal, ip
		
		
		

if __name__ == "__main__":
	pass