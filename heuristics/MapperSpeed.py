
from main import *

def MapperSpeed(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert)


	maptime_threshold = thresh_val(i,"MAPPER_TIME")
	maptime_value = val(i,"MAPPER_TIME")
	
	mapskew_threshold = thresh_val(i,"HDFS_BYTES_READ")
	mapskew_value = val(i,"HDFS_BYTES_READ")
	
	
	if mapskew_value==0 and mapskew_threshold==0:
		ratio=0
		ratio_thres=0
	elif mapskew_value!=0 and mapskew_threshold==0:
		ratio_thres=0
		ratio = mapskew_value/maptime_value
	elif mapskew_value==0 and mapskew_threshold!=0:	
		ratio = 0
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
	print (severity,score,i[0],"MapperSpeed",ratio_thres,ratio)
	