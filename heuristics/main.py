from init import *
from MapperGC import *
from MapperDataSkew import *
from MapperMemory import * 
from MapperSpeed import *
from MapperSpill import *
from MapperTime import *
from ReducerDataSkew import *
from ReducerGC import *
from ReducerMemory import *
from ReducerTime import *



def findHeuristics(i):
	MapperGC(i)
	MapperDataSkew(i)
	MapperMemory(i)
	MapperSpeed(i)
	MapperSpill(i)
	MapperTime(i)
	ReducerDataSkew(i)
	ReducerGC(i)
	ReducerMemory(i)
	ReducerTime(i)
	

def main():
	
	stmt = application.select().where(application.c.FLAG=="NO")
	cur = stmt.execute()
	result = cur.fetchall()
	#print(result)
	for i in result:
		findHeuristics(i)
		#print(len(i))
		stmt = application_checked.insert().values(ID = i[0],NAME=i[1],USER=i[2],TYPE=i[3],QUEUE=i[4],START_TIME=i[5],FINISH_TIME=i[6],STATE=i[7],URL=i[8],ELAPSED_TIME=i[9])
		stmt.execute()
		stmt=update(application).where(application.c.ID==i[0]).values(FLAG="YES")
		stmt.execute()

if __name__ == '__main__':
    main()		