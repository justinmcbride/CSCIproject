#!/usr/bin/env python

'''\mainpage Remote Sensing
\section information Information
This program collects data from the hardware sensors, then converts it to a readable unit (Celcius, etc), and uploads it to a server.

We only need one python file to accomplish this, and that file is sensing.py. This single file depends on the pypcduino library however, and that code is also included.

The appropriate documentation is included within.

\section authors Authors
Made by:
- Justin McBride
- Austin Cerny
- Reed Anderson
- Aaron Holt

\section hardwareinfo Hardware Information
This python script runs on several pcDuino v2 boards located in different places.
Each unit has various sensors attached to it, and for whatever sensor they have, the appropriate data is uploaded.

\section serverinfo Server Information
The server is a Ubuntu instance on Amazon's EC2 infrastructure. The server runs MongoDB and listens for input through a REST API generated by a DreamFactory instance. The server also utilizes Angular.JS andNode.JS to create a graphical frontend for the information.

'''

import time
#import os
import json
import requests
#import sys
from pypcduino import analog_read

## A unique board ID to identify the individual board
boardName = 'Justin'
## A global variable to hold the last reading of the last temperature measured
lastTemperature = 0
## A global variable to hold the last reading of the last light brightness measured
lastLight = 0
## This is the location of the REST API and it is where we will send our calls to.

class Sensor:
	sensorName = ''
	sensorValue = 0
	sensorReading = 0
	sensorPin = 0

	def __init__(self):
		self.sensorName = 'Invalid Sensor'
		
	def getReading(self):
		self.sensorReading = analog_read(self.sensorPin)

	def adToVoltage(self):
		voltage = self.sensorReading * 5.0
	 	voltage /= 1024.0
	 	self.sensorReading = voltage

	 def getValue(self):
	 	self.getReading()
	 	return { self.sensorName : self.sensorValue }

class TemperatureSensor(Sensor):
	def __init__(self):
		self.sensorName = 'Temperature'
		self.sensorPin = 2

	def getReading(self):
		self.sensorReading = analog_read(self.sensorPin)
		self.adToVoltage()
		self.sensorValue = self.voltageToTemperatureC()

	def voltageToTemperatureC(self):
		self.sensorValue = (self.sensorReading - 0.5) * 100

class LightSensor(Sensor):
	def __init__(self):
		self.sensorName = 'Light'
		self.sensorPin = 4



availableSensors = []


apiURI = 'http://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata'
## These are the headers that we need to send with our REST API calls
headers = {'content-type' : 'application/json', 'X-DreamFactory-Application-Name' : 'RemoteSensing'}

##Put the program to sleep for a specified number of seconds
def delay(ms):
	time.sleep(1.0*ms/1000)

## 
#This is where the program will spend the majority of its time, looping through indefinitely.
def loop():
	while(1):
		sensorData = updatePinReadings()
		sendData(sensorData)
		delay(5000)

##Here we actually ship off the information to the server.
def sendData(sensorData):
	data = {"boardName" : boardName, "sensorData" : sensorData}
	response = requests.post(apiURI, data=json.dumps(sensorData), headers=headers)
	#encodedData = urllib.urlencode(postParams)
	#request = urllib2.Request(serverURL, encodedData)
	#response = urllib2.urlopen(request)

##This function will read the values reported by the hardware, and then save that data to the appropriate sensor's variable

def updatePinReadings():
	sensorData = {}
	for sensor in availableSensors:
		sensorData.update(sensor.getValue())
	return sensorData


def setupSensors():
	global availableSensors
	temperatureSensor = TemperatureSensor()
	availableSensors.append(temperatureSensor)
	lightSensor = LightSensor()
	availableSensors.append(lightSensor)

##The entry point of the program
def main():
	loop()

if __name__ == "__main__":
	main()
