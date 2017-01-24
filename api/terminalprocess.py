#!/usr/bin/python -u

import subprocess
import fcntl, os

class TerminalProcess:
	def __init__(self):
		self.terminated = False
		self.process = None

	def running(self):
		return not self.terminated

	def read(self):
		response = ''
		if self.process:
			if self.process.poll() is not None and not self.terminated:
				a = self.process.communicate()
				self.terminated = True
				response += a[0] + a[1]
			while self.process.poll() is None:
				flags = fcntl.fcntl(self.process.stdout.fileno(), fcntl.F_GETFL)
				flags |= os.O_NONBLOCK
				fcntl.fcntl(self.process.stdout.fileno(), fcntl.F_SETFL, flags)
				try:
					response += self.process.stdout.read()
				except IOError:
					break
		return response

	def run(self,cmd):
		try:
			self.process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=False)
			self.terminated = False
			return True
		except Exception, error:
			print "Error: "+str(error)
			exit()

	def kill(self):
		self.process.kill()

import sys
import time

if __name__ == "__main__":
	tp = TerminalProcess()
	tp.run("ping -c 5 google.com")
	while tp.running():
		sys.stdout.write(tp.read())
		time.sleep(0.1)