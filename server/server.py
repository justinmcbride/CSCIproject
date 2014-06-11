#created using http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
from thread import *

HOST = ''
PORT = 10363

points = []

def clientthread(conn):
    #sending message to connected client
    conn.send('connected to the server')

    while True:
	
        #receiving data from client
        data = conn.recv(2048)
        command = pickle.loads(data)
        print "data[tag] = ", command['tag']
        print "data[temperature] = ", command['temperature']
	points.append(command['temperature'])
	plt.plot(points)
	plt.savefig('program/file.png', format="png")
	plt.clf()
        if not data:
            break

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
        print 'connected with ' + addr[0] + ':' + str(addr[1])
        start_new_thread(clientthread, (conn,))

    s.close()

if __name__ == "__main__":
    main()

