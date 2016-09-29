from init import *
def MapperTime(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert)
	
	maptime_threshold = thresh_val(i,"MAPPER_TIME")
	maptime_value = val(i,"MAPPER_TIME")
	
	
	percent = 0.02*maptime_threshold
	if  maptime_threshold - percent <= maptime_value <= maptime_threshold + percent:
		severity="LOW"
		score=maptime_value
	else:
		severity = "HIGH"
		score=maptime_value
	
	#insert(i,score,severity,"MapperTime")
	print (severity,score,i[0],"MapperTime")