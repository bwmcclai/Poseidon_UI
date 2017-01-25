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
		
	def upTime(self):
		a = subprocess.check_output('uptime', shell=True)
		uptime_string = a.split("up")[0]
		return uptime_string
	
	def diskSpace(self):
		a = subprocess.check_output("df -hl | grep '/dev/root'", shell=True)
		data = a.replace("/dev/root ","").split(" ")[14].replace("%","")
		return data
	
	def os(self):
		a = subprocess.check_output("cat /etc/os-release",shell=True)
		data =  a.split('"')[1]
		return data
		
	def CPUTemp(self):
		a = subprocess.check_output("sudo vcgencmd measure_temp",shell=True)
		data = round((float(a.replace("temp=","").replace("'C\n",""))* 1.8) + 32)
		return data
			
	def CPUMemPercent(self):
		a = subprocess.check_output("free -h",shell=True)
		totalMemStr = a.split("\n")[1].split(" ")[10]
		availableMemStr = a.split("\n")[1].split(" ")[17]
		totalMemVal = totalMemStr[:-1]
		availMemVal = availableMemStr[:-1]
		percent = round(((float(availMemVal) / float(totalMemVal))*100),2)
		return percent
    
		return {'totalMem': TotalMem, 'percent': percent }
	def CPUMemTotal(self):
		a = subprocess.check_output("free -h",shell=True)
		totalMemStr = a.split("\n")[1].split(" ")[10]
		availableMemStr = a.split("\n")[1].split(" ")[17]
		TotalMem = availableMemStr + " of " + totalMemStr
    
		return TotalMem

if __name__ == "__main__":
	pass