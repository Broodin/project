from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
import pymysql
from . import *

@routes.route("/<user>",methods = ['GET', 'POST'])
def user(user):  
			form = SearchForm()
			stmt = select([application,heuristic]).where(and_(application.c.ID == user,heuristic.c.JOB_ID==user))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.* FROM APPLICATION A,HEURISTIC B WHERE A.ID=%s AND B.JOB_ID=%s",(job,job))
			result = cur.fetchall()
			return render_template('user/app.html',date=user,result=result,form=form)