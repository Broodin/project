from flask import Blueprint
import pymysql
from flask_wtf import Form
from wtforms import TextField, SubmitField
from initdb import *




routes = Blueprint('routes', __name__)




#conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='symantec', db='symantec')
#cur = conn.cursor()

def search(name):
		s = application.select(application.c.USER==name).order_by(application.c.START_TIME)
		cur = s.execute()
		#cur.execute("SELECT * FROM APPLICATION WHERE USER=%s ORDER BY UNIX_TIMESTAMP(STR_TO_DATE(START_TIME,'%%a %%Y-%%M-%%e %%T')) DESC ",name)
		rv = cur.fetchall()
		return rv

class SearchForm(Form):
    user = TextField("user")
    submit= SubmitField("submit")


from .admin import *
from .user import *