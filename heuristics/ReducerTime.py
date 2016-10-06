'''
Calculates ReducerTime heuristic
Checks for average time by reducers for the job.
'''
from main import *

def ReducerTime(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,reduce_threshold)
	val = getattr(heuristic,reduce_value)
	insert = getattr(heuristic,insert_data)
	
	redtime_threshold = float(thresh_val(i,"REDUCER_TIME"))
	redtime_value = redtime(i)
	
	percent = 0.02*redtime_threshold
	if  redtime_threshold - percent <= redtime_value <= redtime_threshold + percent:
		severity="LOW"
		score=redtime_value
	else:
		severity = "HIGH"
		score=redtime_value
	
	insert(i,score,severity,"ReducerTime")
	print (severity,score,i[0],"ReducerTime")

def redtime(i):
	stmt = select([func.avg(task.c.FINISH_TIME-task.c.START_TIME)]).where(and_(task.c.JOB_ID==i[0],taskcounter.c.TASK_ID == task.c.TASK_ID, task.c.TYPE=="REDUCE"))
	cur=stmt.execute()
	result = cur.fetchone()
	if result[0] is not None:
		return result[0]
	else:
		return 0

