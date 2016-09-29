from main import *

def MapperSpill(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert)
	
	spill_threshold = thresh_val(i,"SPILLED_RECORDS")
	mapoutput_threshold = thresh_val(i,"MAP_OUTPUT_RECORDS")
	spill_record = val(i,"SPILLED_RECORDS")
	mapoutput= val(i,"MAP_OUTPUT_RECORDS")

	
	if mapoutput==0 and mapoutput_threshold==0:
		ratio=0
		ratio_thres=0
	elif mapoutput!=0 and mapoutput_threshold==0:
		ratio_thres=0
		ratio=spill_record/mapoutput
	elif mapoutput==0 and mapoutput_threshold!=0:	
		ratio = 0
		ratio_thres = spill_threshold/mapoutput_threshold
	else:
		ratio=spill_record/mapoutput
		ratio_thres = spill_threshold/mapoutput_threshold
	
	percent = 0.02*ratio_thres
	if  ratio_thres-percent <= ratio <= ratio_thres+percent:
		severity="LOW"
		score=ratio
	else:
		severity = "HIGH"
		score=ratio
	
	#insert(i,score,severity,"MapperSpill")
	print (severity,score,i[0],"MapperSpill")