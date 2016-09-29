import sqlalchemy
from sqlalchemy import *
import pymysql
engine = sqlalchemy.create_engine('mysql+pymysql://root:symantec@localhost:3306',echo=True) # connect to server
#engine.execute("CREATE DATABASE dbname") #create db
engine.execute("USE dbname") # select new db
metadata = MetaData()

application = Table('application',metadata,
						Column('ID',String(50),primary_key=True,nullable=False),
						Column('NAME',String(200)),
						Column('USER',String(20),nullable=False),
						Column('TYPE',String(20)),
						Column('QUEUE',String(30)),
						Column('START_TIME',BigInteger),
						Column('FINISH_TIME',BigInteger),
						Column('STATE',String(10)),
						Column('URL',String(200)),
						Column('ELAPSED_TIME',String(20)),
						Column('FLAG',String(5),server_default="NO")
						)

heuristic = Table('heuristic',metadata,
					Column('JOB_ID',String(50),ForeignKey("application.ID"),nullable=False),
					Column('H_NAME',String(50)),
					Column('SCORE',Float),
					Column('SEVERITY',String(5)),
					)				
					
cluster = Table('cluster',metadata,
				Column('QUEUE_NAME',String(20)),
				Column('MAX_CAPACITY',Float),
				Column('USED_CAPACITY',Float),
				Column('DATE',BigInteger)
				)
				
task = Table('task',metadata,
			Column('TASK_ID',String(50),primary_key=True),
			Column('JOB_ID',String(50),ForeignKey("application.ID")),
			Column('START_TIME',BigInteger),
			Column('FINISH_TIME',BigInteger),
			Column('TYPE',String(10))
			)
			
taskcounter = Table('taskcounter',metadata,
					Column('TASK_ID',String(50),ForeignKey("task.TASK_ID")),
					Column('NAME',String(50)),
					Column('VALUE',BigInteger),
					Column('TYPE',String(10))
					)
					
threshold = Table('threshold',metadata,
				Column('APPNAME',String(200)),
				Column('H_NAME',String(50)),
				Column('USER',String(20)),
				Column('VALUE',BigInteger),
				Column('TASK_TYPE',String(10)),
				PrimaryKeyConstraint('APPNAME', 'H_NAME','TASK_TYPE','USER')
				)
				
application_checked = Table('application_checked',metadata,
						Column('ID',String(50),primary_key=True,nullable=False),
						Column('NAME',String(200)),
						Column('USER',String(20),nullable=False),
						Column('TYPE',String(20)),
						Column('QUEUE',String(30)),
						Column('START_TIME',BigInteger),
						Column('FINISH_TIME',BigInteger),
						Column('STATE',String(10)),
						Column('URL',String(200)),
						Column('ELAPSED_TIME',String(20)),
						)
metadata.create_all(engine)