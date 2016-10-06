'''
Calculates thresholds by job name and user name and stores in the threshold table.
'''
from sqlalchemy import *
import sqlalchemy

#database settings
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306',echo=True)
engine.execute("USE dbname")
metadata = MetaData(bind=engine)

#tables
application = Table('application', metadata, autoload=True)
taskcounter = Table('taskcounter',metadata,autoload=True)
task = Table('task',metadata,autoload=True)
threshold = Table('threshold',metadata,autoload=True)

delete = threshold.delete()
delete.execute()

#main method that calls other methods
def main():
	map_threshold()
	reduce_threshold()
	map_time_threshold()
	reduce_time_threshold()

#insert mapper thresholds in database
def map_insert(result):
	#engine.execute("USE symantec")
	H_NAME = "MAPPER_TIME"
	stmt2 = threshold.insert().values(APPNAME=result[0],H_NAME=H_NAME,USER=result[1],VALUE=result[2],TASK_TYPE="MAP")
	stmt2.execute()

#calculate and insert mapper time threshold in database
def map_time_threshold():
	
	stmt = select([func.avg(task.c.FINISH_TIME-task.c.START_TIME).label('average'),application.c.USER.label('USER'),application.c.NAME.label('APPNAME'),task.c.TYPE.label('TYPE')]).where(and_(application.c.ID==task.c.JOB_ID,task.c.TYPE=="MAP")).group_by(application.c.USER,application.c.NAME,task.c.JOB_ID)
	t1 = stmt.alias('t1')
	stmt1 = select([t1.c.APPNAME,t1.c.USER,func.avg(t1.c.average)]).group_by(t1.c.USER,t1.c.APPNAME)
	t2 = stmt1.alias('t2')
	
	cur = stmt1.execute()
	result = cur.fetchall()
	for i in result:
		map_insert(i)

#inserts reducer threshold in database	
def red_insert(result):
	#engine.execute("USE symantec")
	H_NAME = "REDUCER_TIME"
	stmt2 = threshold.insert().values(APPNAME=result[0],H_NAME=H_NAME,USER=result[1],VALUE=result[2],TASK_TYPE="REDUCE")
	stmt2.execute()

#calculates and insert reducer time threshold in database
def reduce_time_threshold():
	
	stmt = select([func.avg(task.c.FINISH_TIME-task.c.START_TIME).label('average'),application.c.USER.label('USER'),application.c.NAME.label('APPNAME'),task.c.TYPE.label('TYPE')]).where(and_(application.c.ID==task.c.JOB_ID,task.c.TYPE=="REDUCE")).group_by(application.c.USER,application.c.NAME,task.c.JOB_ID)
	t1 = stmt.alias('t1')
	stmt1 = select([t1.c.APPNAME,t1.c.USER,func.avg(t1.c.average)]).group_by(t1.c.USER,t1.c.APPNAME)
	t2 = stmt1.alias('t2')
	
	cur = stmt1.execute()
	result = cur.fetchall()
	for i in result:
		red_insert(i)

#calculate threshold for mapper task counters		
def map_threshold():
	average = taskcounter.c.VALUE.label('average')
	stmt1 = select([func.avg(average).label('aver'),application.c.NAME.label('APPNAME'),taskcounter.c.NAME.label('countername'),application.c.USER.label('USER'),taskcounter.c.TYPE.label('tasktype')]).where(and_(task.c.TASK_ID==taskcounter.c.TASK_ID,application.c.ID==task.c.JOB_ID,taskcounter.c.TYPE=="MAP")).group_by(application.c.ID,application.c.USER,application.c.NAME,taskcounter.c.NAME,taskcounter.c.TYPE)
	t1 = stmt1.alias('t1')
	stmt = select([t1.c.APPNAME.label('APPNAME'),t1.c.countername.label('H_NAME'),t1.c.USER.label('USER'),func.avg(t1.c.aver).label('VALUE'),t1.c.tasktype.label('TASK_TYPE')]).group_by(t1.c.countername,t1.c.APPNAME,t1.c.USER) 
	t2 = stmt.alias('t2')
	stmt2 = threshold.insert().from_select(names=['APPNAME','H_NAME','USER','VALUE','TASK_TYPE'],select=stmt)
	cur = stmt2.execute()
	#result = cur.fetchall()
	
	

	#select APPNAME,avg(average),countername from (select avg(VALUE) as average,id,application.NAME as APPNAME,taskcounter.NAME as countername from
	#taskcounter,application,task where task.TASK_ID=taskcounter.TASK_ID and application.id=task.JOB_ID group by id,application.USER,application.NAME,taskcounter.NAME) as t1 group by countername;

 
	print ("done")

#calculate thresholds for reducer task counters
def reduce_threshold():
	average = taskcounter.c.VALUE.label('average')
	stmt1 = select([func.avg(average).label('aver'),application.c.NAME.label('APPNAME'),taskcounter.c.NAME.label('countername'),application.c.USER.label('USER'),taskcounter.c.TYPE.label('tasktype')]).where(and_(task.c.TASK_ID==taskcounter.c.TASK_ID,application.c.ID==task.c.JOB_ID,taskcounter.c.TYPE=="REDUCE")).group_by(application.c.ID,application.c.USER,application.c.NAME,taskcounter.c.NAME,taskcounter.c.TYPE)
	t1 = stmt1.alias('t1')
	stmt = select([t1.c.APPNAME.label('APPNAME'),t1.c.countername.label('H_NAME'),t1.c.USER.label('USER'),func.avg(t1.c.aver).label('VALUE'),t1.c.tasktype.label('TASK_TYPE')]).group_by(t1.c.countername,t1.c.APPNAME,t1.c.USER) 
	t2 = stmt.alias('t2')
	stmt2 = threshold.insert().from_select(names=['APPNAME','H_NAME','USER','VALUE','TASK_TYPE'],select=stmt)
	cur = stmt2.execute()
	#result = cur.fetchall()

	#select APPNAME,avg(average),countername from (select avg(VALUE) as average,id,application.NAME as APPNAME,taskcounter.NAME as countername from
	#taskcounter,application,task where task.TASK_ID=taskcounter.TASK_ID and application.id=task.JOB_ID group by id,application.USER,application.NAME,taskcounter.NAME) as t1 group by countername;

 
	print ("done")
	
	
#main method	
if __name__ == '__main__':
	main()
