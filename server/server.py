#created using http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
import matplotlib
matplotlib.use('Agg') #Required to tell the library that we do not have a display
import matplotlib.pyplot as plt
import pickle
from thread import *

HOST = ''

PLOT_OUTPUT = 'program/plot.png'

PORT = 10363

points = []

def clientthread(conn):
    #sending message to connected client
    conn.send('Connected to the reporting server')

    while True:
        #receiving data from client
        serializedData = conn.recv(2048)
        if not serializedData:
            break
        data = pickle.loads(serializedData)
        print "data[tag] = ", data['tag']
        print "data[temperature] = ", data['temperature']
		points.append(data['temperature'])
		plt.plot(points)
		plt.savefig(PLOT_OUTPUT, format="png")
		plt.clf()

    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except:
        print 'Bind failed.'
        sys.exit()

    print 'Socket bind complete'

    #start listening on socket
    s.listen(10)
    print 'Socket now listening'

    while 1:
        #wait to accept a connection
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        start_new_thread(clientthread, (conn,))

    s.close()

if __name__ == "__main__":
    main()

