import sys
import matplotlib
matplotlib.use('Agg') #Required to tell the library that we do not have a display
import matplotlib.pyplot as plt
from flask import Flask, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
PLOT_OUTPUT = 'program/plot.png'
points = []

mongoClient = MongoClient()
db = mongoClient.test

post = {"board" : "justin", "temp" : 15, "time" : datetime.datetime.utcnow() }

posts = db.posts
post_id = posts.insert(post)

def clientthread(conn):
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

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/input', methods=['POST'])
def input():
    if (request.method == 'POST'):
        boardName = request.form['boardName']
        temperature = request.form['temperature']
        return "good request"
    else:
        return "bad request"


if __name__ == '__main__':
    app.run(host='0.0.0.0')