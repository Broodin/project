'''
this contains common methods which are used by all the heuristic methods
'''
from init import *

class heuristic_class():
	#mapper thresholds from the threshold table
	def map_threshold(self,i,counter_name):
		job_id = i[0]
		name = i[1]
		user = i[2]
		stmt = select([threshold.c.VALUE]).where(and_(threshold.c.APPNAME == name, threshold.c.USER == user, threshold.c.H_NAME==counter_name,threshold.c.TASK_TYPE=="MAP"))
		cur = stmt.execute()
		result = cur.fetchone()
		if result is not None:
			return result[0]
		else:
			return 0
			
	# mapper value of the given job whose heuristics are being calculated
	def map_value(self,i,counter_name):
		job_id = i[0]
		name = i[1]
		user = i[2]
		stmt = select([func.avg(taskcounter.c.VALUE)]).where(and_(task.c.JOB_ID==i[0],taskcounter.c.TASK_ID == task.c.TASK_ID, taskcounter.c.NAME == counter_name,taskcounter.c.TYPE=="MAP"))
		cur=stmt.execute()
		result = cur.fetchone()
		if result[0] is not None:
			return result[0]
		else:
			return 0
	#reducer threshold from the threshold table	
	def reduce_threshold(self,i,counter_name):
		job_id = i[0]
		name = i[1]
		user = i[2]
		stmt = select([threshold.c.VALUE]).where(and_(threshold.c.APPNAME == name, threshold.c.USER == user, threshold.c.H_NAME==counter_name, threshold.c.TASK_TYPE=="REDUCE"))
		cur = stmt.execute()
		result = cur.fetchone()
		if result is not None:
			return result[0]
		else:
			return 0
	# reducer counter value of the given job whose threshold are being calculated
	def reduce_value(self,i,counter_name):
		job_id = i[0]
		name = i[1]
		user = i[2]
		stmt = select([func.avg(taskcounter.c.VALUE)]).where(and_(task.c.JOB_ID==i[0],taskcounter.c.TASK_ID == task.c.TASK_ID, taskcounter.c.NAME == counter_name,taskcounter.c.TYPE=="REDUCE"))
		cur=stmt.execute()
		result = cur.fetchone()
		if result[0] is not None:
			return result[0]
		else:
			return 0
	# inserts data into the heuristics table	
	def insert_data(self,i,score,severity,h_name):
		engine.execute("USE dbname")
		stmt = heuristic.insert().values(JOB_ID=i[0],H_NAME=h_name,SCORE=score,SEVERITY=severity)	
		stmt.execute()			

		
map_threshold = 'map_threshold'
method = getattr(heuristic_class,map_threshold)

map_value = 'map_value'
method = getattr(heuristic_class,map_value)

reduce_threshold  = "reduce_threshold"
method = getattr(heuristic_class,reduce_threshold)

reduce_value = 'reduce_value'
method = getattr(heuristic_class,reduce_value)

insert_data = 'insert_data'
method = getattr(heuristic_class,insert_data)
