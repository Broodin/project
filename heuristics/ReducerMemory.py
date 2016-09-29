from main import *

def ReducerMemory(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,reduce_threshold)
	val = getattr(heuristic,reduce_value)
	insert = getattr(heuristic,insert)
	
	phy_threshold = thresh_val(i,"PHYSICAL_MEMORY_BYTES")
	phy_mem = val(i,"PHYSICAL_MEMORY_BYTES")
		
	ratio = phy_mem/4096
	ratio_thres = phy_threshold/4096
	
	percent = 0.02*ratio_thres
	if  ratio_thres-percent <= ratio <= ratio_thres+percent:
		severity="LOW"
		score=ratio
	else:
		severity = "HIGH"
		score=ratio
	#insert(i,score,severity,"ReducerMemory")	
	print (severity,score,i[0],"ReducerMemory")