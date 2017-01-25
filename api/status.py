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

		
	def diskSpace(self):
		result = subprocess.check_output("df -hl | grep '/dev/root'", shell=True)
		data = result.replace("/dev/root ","").split(" ")[14].replace("%","")
		return data
	
	def os(self):
		result = subprocess.check_output("cat /etc/os-release",shell=True)
		data =  result.split('"')[1]
		return data
		
	def CPUTemp(self):
		result = subprocess.check_output("sudo vcgencmd measure_temp",shell=True)
		data = round((float(result.replace("temp=","").replace("'C\n",""))* 1.8) + 32)
		return data
			
	def CPUMem(self):
		result = subprocess.check_output("free -h",shell=True)
		totalMemStr = result.split("\n")[1].split(" ")[10]
		availableMemStr = result.split("\n")[1].split(" ")[17]
		totalMemVal = totalMemStr[:-1]
		availMemVal = availableMemStr[:-1]
		percent = round(((float(availMemVal) / float(totalMemVal))*100),2)
		TotalMem = availableMemStr + " of " + totalMemStr
		return percent, TotalMem
    
		return {'totalMem': TotalMem, 'percent': percent }
	def CPUMemTotal(self):
		result = subprocess.check_output("free -h",shell=True)
		totalMemStr = result.split("\n")[1].split(" ")[10]
		availableMemStr = result.split("\n")[1].split(" ")[17]
		TotalMem = availableMemStr + " of " + totalMemStr
		return TotalMem
	
	def pixhawkStatus(self):
		#note:  this was not returning anything for me.... need to revisit
		try:
			p = subprocess.Popen(['ls', '/dev/serial/by-id'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			result, err = p.communicate()
			if ("usb-3D_Robotics_PX4_FMU_v2.x_0-if00" in result):
				data = "Connected"
			else:
				data = "Not Connected"
		except:
			data = "Error"
		return data

	def MAVProxyStatus(self):
		try:
			p = subprocess.Popen(['screen', '-ls'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			result, err = p.communicate()
			if ("mavproxy" in result):
				data = "Running"
			else:
				data = "Not Running"
		except:
			data = "Error"
		return data
		
	def videoStatus(self):
		try:
			p = subprocess.Popen(['screen', '-ls'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			result, err = p.communicate()
			if ("video" in result):
				data = "Running"
			else:
				data = "Not Running"
		except:
			data = "Error"
		return data

if __name__ == "__main__":
	pass