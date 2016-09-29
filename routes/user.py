from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
import pymysql
from . import *

def heuristic_query(h_name,name,user):
	stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application.c.ID,application.c.START_TIME]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==name,application.c.USER==user,heuristic.c.H_NAME==h_name))
	cur = stmt.execute()
	result = cur.fetchall()
	return result

@routes.route("/<app>",methods = ['GET', 'POST'])
def user(app):  
			form = SearchForm()
			stmt = select([application,heuristic]).where(and_(application.c.ID == app,heuristic.c.JOB_ID==app))
			cur = stmt.execute()
			result = cur.fetchall()
						
			name = result[0][1]
			stmt = select([application.c.ID,application.c.START_TIME,application.c.FINISH_TIME]).where(and_(application.c.NAME==name,application.c.USER==result[0][2]))
			cur = stmt.execute()
			result1 = cur.fetchall()
			
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(application.c.ID == app, heuristic.c.JOB_ID==app))
			cur = stmt.execute()
			rv=cur.fetchall()
			
			name=rv[0][5]
			user=rv[0][4]
			
			rv1=heuristic_query("MapperDataSkew",name,user)
			rv2=heuristic_query("MapperGC",name,user)
			rv3=heuristic_query("MapperMemory",name,user)
			rv4=heuristic_query("MapperSpeed",name,user)
			rv5=heuristic_query("MapperSpill",name,user)
			rv6=heuristic_query("MapperTime",name,user)
			rv7=heuristic_query("ReducerDataSkew",name,user)
			rv8=heuristic_query("ReducerGC",name,user)
			rv9=heuristic_query("ReducerMemory",name,user)
			rv10=heuristic_query("ReducerTime",name,user)
			
			
			return render_template('user/app.html',date=app,result=result,form=form,result1=result1,rv=rv,rv1=rv1,rv2=rv2,rv3=rv3,rv4=rv4,rv5=rv5,rv6=rv6,rv7=rv7,rv8=rv8,rv9=rv9,rv10=rv10)