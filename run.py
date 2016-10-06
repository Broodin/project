'''
Main script to run the web server.
'''
from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
from routes import *
from restapi import *
import time
import datetime

app = Flask(__name__)

app.secret_key = 'secret'
api = Api(app)

#blueprint of the project
app.register_blueprint(routes)
app.register_blueprint(api_rest)

bootstrap = Bootstrap(app)

#custom template to convert UNIX timestamp to date time
@app.template_filter('ctime')
def timectime(s):
	s=s/1000
	return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S %Z')

@app.template_filter('ctime_string')
def timestringctime(s):
	s1 = int(s)
	s1=s1/1000
	return datetime.datetime.fromtimestamp(s1).strftime('%Y-%m-%d %H:%M:%S %Z')	

#main 
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',threaded=True)
