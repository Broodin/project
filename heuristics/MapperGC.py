from main import *

def MapperGC(i):	
	heuristic = heuristic_class()
	thresh_val = getattr(heuristic,map_threshold)
	val = getattr(heuristic,map_value)
	insert = getattr(heuristic,insert)
	
	gc_threshold = thresh_val(i,"GC_TIME_MILLIS")
	cpu_threshold = thresh_val(i,"CPU_MILLISECONDS")
	gc_time = val(i,"GC_TIME_MILLIS")
	cpu_time = val(i,"CPU_MILLISECONDS")
	
	
	gc_cpu_ratio = gc_time/cpu_time
	gc_cpu_thres = gc_threshold/cpu_threshold
	
	percent = 0.02*gc_cpu_thres
	if  gc_cpu_thres-percent <= gc_cpu_ratio <= gc_cpu_thres+percent:
		severity="LOW"
		score=gc_cpu_ratio
	else:
		severity = "HIGH"
		score=gc_cpu_ratio
	insert(i,score,severity,"MapperGC")
	print (severity,score,i[0],"MapperGC")