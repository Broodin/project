from main import *

def MapperMemory(i):
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert)
	
	phy_threshold = phy_thres(i,"PHYSICAL_MEMORY_BYTES")
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
	#insert(i,score,severity,"MapperMemory")
		
	print (severity,score,i[0],"MapperMemory")