#!/usr/bin/python -u

from flask import Flask, Blueprint, render_template, json, request

import subprocess

def getHello():
	data = 'Hello'
	return data

if __name__ == "__main__":
	pass