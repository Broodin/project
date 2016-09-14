from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap

from routes import *
from restapi import *

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

app.register_blueprint(routes)
app.register_blueprint(api_rest)

bootstrap = Bootstrap(app)



if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',threaded=True)
