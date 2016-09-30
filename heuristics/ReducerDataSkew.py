
from main import *

def ReducerDataSkew(i):	

	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,reduce_threshold)
	val = getattr(heuristic,reduce_value)
	insert = getattr(heuristic,insert_data)
	
	redskew_threshold = float(thresh_val(i,"REDUCE_SHUFFLE_BYTES"))
	redskew_value = val(i,"REDUCE_SHUFFLE_BYTES")
	
	percent = 0.02*redskew_threshold
	if  redskew_threshold - percent <= redskew_value <= redskew_threshold + percent:
		severity="LOW"
		score=redskew_value
	else:
		severity = "HIGH"
		score=redskew_value
	insert(i,score,severity,"ReducerDataSkew")
	print (severity,score,i[0],"ReducerDataSkew")
