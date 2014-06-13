import sys
import matplotlib
matplotlib.use('Agg') #Required to tell the library that we do not have a display
import matplotlib.pyplot as plt
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
PLOT_OUTPUT = 'plot/plot.png'
points = []

mongoClient = MongoClient()
db = mongoClient.records
collection = db.readings

def createPlot():
	plt.plot(points)
	plt.savefig(PLOT_OUTPUT, format="png")
	plt.clf()

#def parseInput():


@app.route('/')
def hello_world():
	return 'Thou shalt not pass!'

@app.route('/input', methods=['POST'])
def input():
	if (request.method == 'POST'):
		boardName = request.form['boardName']
		temperature = request.form['temperature']
		#points.append(temperature)
		date = datetime.utcnow()

		post = {'boardTag' : boardName, 'temperature' : temperature, 'time' : date}
		collection.insert(post)
		return "Good: " + boardName + " " + temperature
	else:
		return "Bad request.."


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)