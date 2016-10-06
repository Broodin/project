'''
Calculates MapperGC heuristic
checks if GC/CPU ratio is in the limits of the threshold value.
Severity is set to low or high accordingly.
'''
from main import *

def MapperGC(i):	
	heuristic = heuristic_class()				#instance of heuristic class to call methods 
	thresh_val = getattr(heuristic,map_threshold)		
	val = getattr(heuristic,map_value)
	insert_query = getattr(heuristic,insert_data)
	
	gc_threshold =float( thresh_val(i,"GC_TIME_MILLIS"))
	cpu_threshold =float( thresh_val(i,"CPU_MILLISECONDS"))
	gc_time = val(i,"GC_TIME_MILLIS")
	cpu_time = val(i,"CPU_MILLISECONDS")
	
	if cpu_time==0 and cpu_threshold==0:
		ratio=0
		ratio_thres=0
	elif cpu_time!=0 and cpu_threshold==0:
		ratio_thres=0
		ratio = float(gc_time/cpu_time)
	elif cpu_time==0 and cpu_threshold!=0:	
		ratio = 0
		ratio_thres = float(gc_threshold/cpu_threshold)
	else:
		#print(gc_time,cpu_time,gc_threshold,cpu_threshold)
		ratio = float(gc_time/cpu_time)
		ratio_thres = float(gc_threshold/cpu_threshold)
		#print (ratio_thres,ratio,12766/219510)
	
	percent = 0.02*ratio_thres
	if  ratio_thres-percent <= ratio <= ratio_thres+percent:
		severity="LOW"
		score=ratio
	else:
		severity = "HIGH"
		score=ratio
	insert_query(i,score,severity,"MapperGC")
	print (severity,score,i[0],ratio,ratio_thres,cpu_threshold,gc_threshold,"MapperGC")
