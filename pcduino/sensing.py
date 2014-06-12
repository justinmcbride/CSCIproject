import time, os
import urllib
import urllib2
import sys
from pypcduino import analog_read

boardName = 'Justin'
tempPinReading = 0
lightPinReading = 0

serverURL = 'http://71.237.88.58/input'
serverPort = 10363

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
		sendData(s)
		delay(5000)

"""Here we actually ship off the information to the server."""
def sendData(s):
	postParams = { 'boardName' : boardName, 'tempPinReading' : tempPinReading}
	encodedData = urllib.urlencode(postParams)
	request = urllib2.Request(serverURL, encodedData)
	response = urllib2.urlopen(req)

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
	loop(s)

if __name__ == "__main__":
	main()
