from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
import pymysql
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy.sql import func
from . import *


parser = reqparse.RequestParser()
def admin_parser():
	parser.add_argument('min')
	parser.add_argument('max')

@routes.route("/url",methods = ['GET', 'POST'])
def custom():
	form = SearchForm()
	admin_parser()
	args = parser.parse_args()
	min = args['min']
	max = args['max']
	stmt = cluster.select().order_by(cluster.c.DATE.asc())
	cur = stmt.execute()
	res1=cur.fetchall()
	
	stmt = application.select().where(and_(application.c.FINISH_TIME>=min,application.c.START_TIME<max))
	cur = stmt.execute()
	res = cur.fetchall()
	

	list={}
	for i in range(cur.rowcount):
				stmt = heuristic.select(heuristic.c.JOB_ID==res[i][0])
				cur = stmt.execute()
				#cur.execute("SELECT * FROM HEURISTIC WHERE JOB_ID = %s",res[i][0])
				list.update({res[i][0]:cur.fetchall()})
	
	return render_template('admin/custom.html',res=res,form=form,res1=res1,list=list,min=min,max=max)


@routes.route("/",methods = ['GET', 'POST'])
def index():
		form = SearchForm()
		if request.method == 'POST':
			name = form.user.data
            
			rv = search(name)
			if not len(rv):
				return render_template('user/notfound.html',form=form)

			else:    
				a=len(rv)
				list={}
				for i in range(a):
					stmt = heuristic.select(heuristic.c.JOB_ID==rv[i][0])
					cur = stmt.execute()
					#cur.execute("SELECT * FROM HEURISTIC WHERE JOB_ID = %s",rv[i][0])
					list.update({rv[i][0]:cur.fetchall()})
				return render_template('user/user.html',rv=rv,name=name,form=form,list=list)

		else:
			#cur.execute("SELECT * FROM APPLICATION")
			stmt = cluster.select()
			cur = stmt.execute()
			res1=cur.fetchall()
			#cur.execute("SELECT * FROM APPLICATION ORDER BY START_TIME DESC LIMIT 5")
			stmt = application.select().order_by(application.c.START_TIME.desc()).limit(5)
			cur = stmt.execute()
			res=cur.fetchall()
			
			list={}
			for i in range(cur.rowcount):
				stmt = heuristic.select(heuristic.c.JOB_ID==res[i][0])
				cur = stmt.execute()
				#cur.execute("SELECT * FROM HEURISTIC WHERE JOB_ID = %s",res[i][0])
				list.update({res[i][0]:cur.fetchall()})
				
			return render_template('admin/admin.html',res=res,form=form,res1=res1,list=list)	