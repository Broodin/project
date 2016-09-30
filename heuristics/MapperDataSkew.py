
from main import *
from heuristic import *
def MapperDataSkew(i):
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert_data)
	
	mapskew_threshold = thresh_val(i,"HDFS_BYTES_READ")
	mapskew_value = val(i,"HDFS_BYTES_READ")

	percent = 0.02*mapskew_threshold
	if  mapskew_threshold - percent <= mapskew_value <= mapskew_threshold + percent:
		severity="LOW"
		score=mapskew_value
	else:
		severity = "HIGH"
		score=mapskew_value
	
	insert(i,score,severity,"MapperDataSkew")
	print (severity,score,i[0],mapskew_threshold,mapskew_value,"MapperDataSkew")
