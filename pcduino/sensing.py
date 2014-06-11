import time, os
import httplib, urllib
import socket
import sys
import pickle
from pcduino import analog_read
from pymongo import MongoClient

ADC_PATH = os.path.normpath('/proc/')
ADC_FILENAME = "adc"
adcFiles = []

boardName = 'justins'

tempPinReading = 0
lightPinReading = 0

#headers = {}
serverURL = 'localhost'
#serverURL = 'mongodb://root:RemoteSensing!7@dbTemp.128.138.201.123:27017/'
serverPort = 10363
#mongoClient = MongoClient(serverURL)



def delay(ms):
	time.sleep(1.0*ms/1000)

def setup():
	#global headers
	for i in range(0,6):
		adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+str(i)))
	#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


def loop(s):
	while(1):
		updatePinReadings()
		sendData(s, tempPinReading)
		delay(5000)

'''
def upload(tempN, lightN):
	postParams = urllib.urlencode({'@boardTag': boardName, '@temperature': tempN, 'light': lightN})
	conn = httplib.HTTPConnection(serverURL)
	conn.request("POST", "", postParams, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	print data
	conn.close()
'''

def sendData(s, tempN):
	packetD = {'tag' : boardName, 'temperature': tempN }
	packetP = pickle.dumps(packetD)
	s.send(packetP)

'''
def updatePinReadings():
	num = 0
	for file in adcFiles:
		fd = open(file, 'r')
		fd.seek(0)
		if num == 2:
			tempPinReading = int(fd.read(32).split(':')[1].strip())
		if num == 4:
			lightPinReading = int(fd.read(32).split(':')[1].strip())
		fd.close()
		num = num + 1
'''

def updatePinReadings():
	global tempPinReading
	global lightPinReading
	tempPinReading = analog_read(2)
	lightPinReading = analog_read(4)

def main():
	setup()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print 'Failed to create socket.'
		sys.exit()
	try:
		remote_ip = socket.gethostbyname(serverURL)
	except socket.gaierror:
		print 'costname could not be resolved'
		sys.exit()

	s.connect((remote_ip, serverPort))
	loop(s)

if __name__ == "__main__":
	main()
