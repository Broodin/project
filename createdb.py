import sqlalchemy
from sqlalchemy import create_engine, MetaData,Table, Column, Integer, String,ForeignKey
import pymysql
engine = sqlalchemy.create_engine('mysql+pymysql://root:symantec@localhost:3306',echo=True) # connect to server
#engine.execute("CREATE DATABASE dbname") #create db
engine.execute("USE dbname") # select new db
metadata = MetaData()

application = Table('application',metadata,
						Column('ID',String(50),primary_key=True,nullable=False),
						Column('NAME',String(200)),
						Column('USER',String(20),nullable=False),
						Column('QUEUE',String(30)),
						Column('START_TIME',String(30)),
						Column('FINISH_TIME',String(30)),
						Column('STATE',String(10)),
						Column('URL',String(200)),
						Column('ELAPSED_TIME',String(20))
						)

heuristic = Table('heuristic',metadata,
					Column('JOB_ID',String(50),ForeignKey("application.ID"),nullable=False),
					Column('H_NAME',String(50)),
					Column('SCORE',Integer),
					Column('SEVERITY',String(5))
					)				
					
cluster = Table('cluster',metadata,
				Column('QUEUE_NAME',String(20),primary_key=True),
				Column('MAX_CAPACITY',Float),
				Column('USED_CAPACITY',Float),
				Column('DATE',BigInteger)
				)
metadata.create_all(engine)