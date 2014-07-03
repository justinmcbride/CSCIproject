Remote Sensing App
=======


About
===========
A miniature internet of things, this project collects temperature and brightness data of remote sensors, stores this data in a NoSQL database, and displays the data to a user via an Angular web app and Android application. While functional, the application is still a work in progress.

A live demo can be found <a href="https://dsp-csci-project.cloud.dreamfactory.com/files/applications/RemoteSensing/app.html">here</a>.


Repository Organization
===========
The repository contains three distinct directories:

* AngularApp - contains the code for the web application written in AngularJS and hosted remotely.

* Android - contains the code for our Android application written in Java.

* pcDuino - contains the code for the client program (written in Python) that runs on the pcDuino hardware.

Documentation
===========

* pcDuino:
The documentation for the pcDuino application was written into the source files, and it is interpretted by Doxygen using the DoxyPy input filter. The already generated documentation lives in the pcDuino/docs/ directory, with index.html being the home page. A symbolic and relative link to the index page lives in the pcDuino subdirectory named "Documentation" that will direct to the documentation page. The documentation can be generated again using the DoxyPy filter with Doxygen, and the included doxyfile.

* AngularJS Web application:
	In-line comments are included to explain the functionality of this part of the project.

* Android application:
	No documentation provided due to the barebones and minimal functionality.

Building the code
===========
* pcDuino:
	Because the code is Python, the code does not need to be built. It will run on a pcDuino, but abort otherwise.

* AngularJS:
	This code does not need to be built either. The code can simply be run by viewing the app.html file in a web browser.

* Android application:
	This code needs to be built through the Eclipse SDK with the Android Developer Toolkit. However, an installable APK file
	is also included.

Running the code
===========
* pcDuino:
	To run this on a pcDuino, make sure to have the required module pypcduino on the device in the same directory as the sensing.py program. From the command line, simply invoking 
	````
	$python sensing.py "Name here"
	````
	with a string in the "Name here" to specify how the board should identify itself to the server will run the code. The code runs in an infinite loop and updates the server occasionally with its data.

* AngularJS:
	The code can simply be run by viewing the app.html file in a web browser, or by visiting the remotely hosted page linked to above.

* Android application:
	This code needs to be built through the Eclipse SDK with the Android Developer Toolkit. However, an installable APK file
	is also included.

Testing
===========
* pcDuino:
	Unit testing is provided. More information at the generated doxygen page.

* AngularJS:
	Manual testing was performed incrementally while creating this application. No unit testing is provided.

* Android application:
	No testing was done on this part of the project due to the barebones, minimal functionality.

Purpose
===========
This project was completed for CSCI 3308 - Software Engineering Methods and Tools with the goal of bettering our understanding of development tools related to: Agile, TDD, Static and Dynamic Analysis, Unit Testing, Deployment Environments, Continuous Integration, SQL/NoSQL Databases, Design Patterns, and Intellectual Property.


Licensing
===========

The MIT License (MIT)

Copyright (c) 2014. Reed Anderson, Austin Cerny, Aaron Holt, Justin McBride

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
