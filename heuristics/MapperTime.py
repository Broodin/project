'''
Calculates MapperTime heuristic
checks for average mapper time of the job.
'''
from main import *
from init import *
def MapperTime(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert_data)
	
	maptime_threshold =float( thresh_val(i,"MAPPER_TIME"))
	maptime_value = maptime(i)
	
	
	percent = 0.02*maptime_threshold
	if  maptime_threshold - percent <= maptime_value <= maptime_threshold + percent:
		severity="LOW"
		score=maptime_value
	else:
		severity = "HIGH"
		score=maptime_value
	
	insert(i,score,severity,"MapperTime")
	print (severity,score,i[0],"MapperTime")

def maptime(i):
	stmt = select([func.avg(task.c.FINISH_TIME-task.c.START_TIME)]).where(and_(task.c.JOB_ID==i[0],taskcounter.c.TASK_ID == task.c.TASK_ID, task.c.TYPE=="MAP"))
	cur=stmt.execute()
	result = cur.fetchone()
	if result[0] is not None:
		return result[0]
	else:
		return 0
