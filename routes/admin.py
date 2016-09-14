from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
import pymysql
from sqlalchemy.sql import func
from . import *



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
			stmt = application.select()
			cur = stmt.execute()
			res1=cur.fetchall()
			#cur.execute("SELECT * FROM APPLICATION ORDER BY START_TIME DESC LIMIT 5")
			stmt = application.select().order_by(func.unix_timestamp(func.STR_TO_DATE(application.c.START_TIME,'%a %Y-%M-%e %T')).desc()).limit(5)
			cur = stmt.execute()
			res=cur.fetchall()
			
			list={}
			for i in range(cur.rowcount):
				stmt = heuristic.select(heuristic.c.JOB_ID==res[i][0])
				cur = stmt.execute()
				#cur.execute("SELECT * FROM HEURISTIC WHERE JOB_ID = %s",res[i][0])
				list.update({res[i][0]:cur.fetchall()})
				
			return render_template('admin/admin.html',res=res,form=form,res1=res1,list=list)
			

@routes.route("/admin/<time>",methods = ['GET', 'POST'])
def cluster(time):
			form = SearchForm()
			stmt = application.select(and_(func.unix_timestamp(func.STR_TO_DATE(application.c.START_TIME,'%a %Y-%M-%e %T'))>time,func.unix_timestamp(func.STR_TO_DATE(application.c.START_TIME,'%a %Y-%M-%e %T'))<str(int(time)+900)))
			cur = stmt.execute()
			#cur.execute("SELECT A.* FROM APPLICATION A WHERE UNIX_TIMESTAMP(STR_TO_DATE(A.START_TIME,'%%a %%Y-%%M-%%e %%T')) > %s && UNIX_TIMESTAMP(STR_TO_DATE(A.START_TIME,'%%a %%Y-%%M-%%e %%T')) < (%s +300) ORDER BY A.START_TIME DESC",(job,job))
			result=cur.fetchall()
			list={}
			for i in range(len(result)):
				stmt = heuristic.select(heuristic.c.JOB_ID == result[i][0])
				cur = stmt.execute()
				#cur.execute("SELECT * FROM HEURISTIC WHERE JOB_ID = %s",result[i][0])
				list.update({result[i][0]:cur.fetchall()})
				
			return render_template('admin/cluster.html',date=time,result=result,form=form,list=list)