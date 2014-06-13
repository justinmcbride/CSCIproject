import sys
import matplotlib
matplotlib.use('Agg') #Required to tell the library that we do not have a display
import matplotlib.pyplot as plt
from flask import Flask, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
PLOT_OUTPUT = 'plot/plot.png'
points = []

mongoClient = MongoClient()
db = mongoClient.test
collection = db.recordings

def createPlot():
	plt.plot(points)
	plt.savefig(PLOT_OUTPUT, format="png")
	plt.clf()

def parseInput():
	boardName = request.form['boardName']
	temperature = request.form['temperature']
	points.append(temperature)
	date = datetime.utcnow()

	post = {'boardTag' : boardName, 'temperature' : temperature, 'time' : date}
	collection.insert(post)

@app.route('/')
def hello_world():
    return 'Thou shalt not pass!'

@app.route('/input', methods=['POST'])
def input():
    if (request.method == 'POST'):
        parseInput()
        return "Good request!"
    else:
        return "Bad request.."


if __name__ == '__main__':
    app.run(host='0.0.0.0')