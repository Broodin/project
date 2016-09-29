from sqlalchemy import *
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:symantec@localhost:3306',echo=True)
engine.execute("USE dbname")
metadata = MetaData(bind=engine)


application = Table('APPLICATION_CHECKED', metadata, autoload=True)
heuristic = Table('HEURISTIC', metadata, autoload=True)
cluster = Table('CLUSTER',metadata,autoload=True)
task = Table('TASK',metadata,autoload=True)
task_counter = Table('TASKCOUNTER',metadata,autoload=True)