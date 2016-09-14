from flask import Flask,render_template,request,jsonify
from flask_bootstrap import Bootstrap
from . import *
@routes.route("/heuristic/<job>",methods = ['GET', 'POST'])
def heuri(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(application.c.ID == job, heuristic.c.JOB_ID==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = application.select(application.c.NAME == rv[0][5])
			cur = stmt.execute()			
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/heuristic.html',job=job,form=form,rv=rv,rv2=rv2)



@routes.route("/heuristic/<job>/Mapper_Spill",methods = ['GET', 'POST'])
def map_spill(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			rv=cur.fetchall()
			
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper Spill"))
			cur = s.execute()
			rv1=cur.fetchall()
			
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper Spill'",(rv[0][5],rv[0][4]))
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			
			return render_template('heuristic/Mapper_Spill.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)

@routes.route("/heuristic/<job>/Mapper_GC",methods = ['GET', 'POST'])
def map_gc(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper GC"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper GC'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Mapper_GC.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)		    
    

@routes.route("/heuristic/<job>/Reducer_GC",methods = ['GET', 'POST'])
def red_gc(job):
			form = SearchForm()
			
			stmt = select([heuristic,application.c.USER,application.c.name]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Reducer GC"))
			cur = stmt.execute()			
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Reducer GC'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Reducer_GC.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)

@routes.route("/heuristic/<job>/Mapper_Speed",methods = ['GET', 'POST'])
def map_speed(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper Speed"))
			cur = stmt.execute()	
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper Speed'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()

			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Mapper_Speed.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)


@routes.route("/heuristic/<job>/Mapper_Time",methods = ['GET', 'POST'])
def map_time(job):
			form = SearchForm()
			
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper Time"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper Time'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Mapper_Time.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)

@routes.route("/heuristic/<job>/Reducer_Time",methods = ['GET', 'POST'])
def red_time(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Reducer Time"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Reducer Time'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Reducer_Time.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)


@routes.route("/heuristic/<job>/Mapper_Data_Skew",methods = ['GET', 'POST'])
def map_data(job):
			form = SearchForm()
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper Data Skew"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper Data Skew'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Mapper_Data_Skew.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)


@routes.route("/heuristic/<job>/Reducer_Data_Skew",methods = ['GET', 'POST'])
def red_data(job):
			form = SearchForm()
			
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Reducer Data Skew"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Reducer Data Skew'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Reducer_Data_Skew.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)


@routes.route("/heuristic/<job>/Mapper_Memory",methods = ['GET', 'POST'])
def map_mem(job):
			form = SearchForm()
			
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Mapper Memory"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Mapper Memory'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Mapper_Memory.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)

@routes.route("/heuristic/<job>/Reducer_Memory",methods = ['GET', 'POST'])
def red_mem(job):
			form = SearchForm()
			
			stmt = select([heuristic,application.c.USER,application.c.NAME]).where(and_(heuristic.c.JOB_ID==job,application.c.ID ==job))
			cur = stmt.execute()
			#cur.execute("SELECT A.*,B.USER,B.NAME FROM HEURISTIC A,APPLICATION B WHERE A.JOB_ID=%s AND B.ID=%s",(job,job))
			rv=cur.fetchall()
			
			stmt = select([heuristic.c.H_NAME,heuristic.c.SCORE,application]).where(and_(application.c.ID==heuristic.c.JOB_ID,application.c.NAME==rv[0][5],application.c.USER==rv[0][4],heuristic.c.H_NAME=="Reducer Memory"))
			cur = stmt.execute()
			#cur.execute("SELECT A.H_NAME,A.SCORE,B.* FROM HEURISTIC A,APPLICATION B WHERE B.ID=A.JOB_ID AND B.NAME = %s AND B.USER = %s AND A.H_NAME='Reducer Memory'",(rv[0][5],rv[0][4]))
			rv1=cur.fetchall()
			
			stmt = application.select(application.c.NAME==rv[0][5])
			cur = stmt.execute()
			#cur.execute("SELECT * FROM APPLICATION WHERE NAME=%s",rv[0][5])
			rv2=cur.fetchall()
			return render_template('heuristic/Reducer_Memory.html',job=job,form=form,rv=rv,rv1=rv1,rv2=rv2)