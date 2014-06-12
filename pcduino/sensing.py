import time, os
#import httplib, urllib
import socket
import sys
import pickle
from pypcduino import analog_read
from pymongo import MongoClient

boardName = 'Justin'
tempPinReading = 0
lightPinReading = 0

serverURL = 'localhost'
#serverURL = 'mongodb://128.138.201.123:27017/'
serverPort = 10363
#mongoClient = MongoClient(serverURL)

"""Put the program to sleep for a specified number
of seconds
"""
def delay(ms):
	time.sleep(1.0*ms/1000)

"""This is where the program will spend the majority
of its time, looping through indefinitely.
"""
def loop(s):
	while(1):
		updatePinReadings()
		sendData(s, tempPinReading)
		delay(5000)

"""Here we actually ship off the information to the server.
We need to serialize the data to send it effectively (using
pickle)
"""
def sendData(s, tempN):
	packetD = {'tag' : boardName, 'temperature': tempN }
	packetP = pickle.dumps(packetD)
	s.send(packetP)

'''This function will read the values reported by the hardware,
and then save that data to the appropriate sensor's variable
'''
def updatePinReadings():
	global tempPinReading
	global lightPinReading
	tempPinReading = analog_read(2)
	lightPinReading = analog_read(4)

'''The entry point of the program'''
def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print 'Failed to create a socket.'
		sys.exit()
	try:
		remote_ip = socket.gethostbyname(serverURL)
	except socket.gaierror:
		print 'Could not connect to the specified hostname.'
		sys.exit()

	s.connect((remote_ip, serverPort))
	loop(s)

if __name__ == "__main__":
	main()
