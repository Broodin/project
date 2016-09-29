
from main import *

def ReducerTime(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,reduce_threshold)
	val = getattr(heuristic,reduce_value)
	insert = getattr(heuristic,insert)
	
	redtime_threshold = thresh_val(i,"REDUCER_TIME")
	redtime_value = val(i,"REDUCER_TIME")
	
	percent = 0.02*redtime_threshold
	if  redtime_threshold - percent <= redtime_value <= redtime_threshold + percent:
		severity="LOW"
		score=redtime_value
	else:
		severity = "HIGH"
		score=redtime_value
	
	#insert(i,score,severity,"ReducerTime")
	print (severity,score,i[0],"ReducerTime")