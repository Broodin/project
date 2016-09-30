
from main import *

def MapperSpeed(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert_data)


	maptime_threshold = float(thresh_val(i,"MAPPER_TIME"))
	maptime_value = float(maptime(i))
	
	mapskew_threshold =float( thresh_val(i,"HDFS_BYTES_READ"))
	mapskew_value = float(val(i,"HDFS_BYTES_READ"))
	
	
	if maptime_value==0 and maptime_threshold==0:
		print ("both zero")
		ratio=0
		ratio_thres=0
	elif maptime_value!=0 and maptime_threshold==0:
		ratio_thres=0
		ratio = mapskew_value/maptime_value
	elif maptime_value==0 and maptime_threshold!=0:	
		ratio = 0
		print("maptime zero")
		ratio_thres = mapskew_threshold/maptime_threshold
	else:
		ratio = mapskew_value/maptime_value
		ratio_thres = mapskew_threshold/maptime_threshold
		
		
	
	
	percent = 0.02*ratio_thres
	if  ratio_thres - percent <= ratio <= ratio_thres + percent:
		severity="LOW"
		score=ratio
	else:
		severity = "HIGH"
		score=ratio
	insert(i,score,severity,"MapperSpeed")
	print (severity,score,i[0],"MapperSpeed",ratio,ratio_thres,maptime_value,mapskew_value)

def maptime(i):
	stmt = select([func.avg(task.c.FINISH_TIME-task.c.START_TIME)]).where(and_(task.c.JOB_ID==i[0],taskcounter.c.TASK_ID == task.c.TASK_ID, task.c.TYPE=="MAP"))
	cur=stmt.execute()
	result = cur.fetchone()
	if result[0] is not None:
		return result[0]
	else:
		return 0	
