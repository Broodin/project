import sqlalchemy
from sqlalchemy import *
	
 
engine = sqlalchemy.create_engine('mysql+pymysql://root:symantec@localhost:3306')
engine.execute("USE dbname")
metadata = MetaData(bind=engine)

application = Table('APPLICATION', metadata, autoload=True)
taskcounter = Table('TASKCOUNTER',metadata,autoload=True)
task = Table('TASK',metadata,autoload=True)
threshold = Table('THRESHOLD',metadata,autoload=True)
application_checked = Table('APPLICATION_CHECKED',metadata,autoload=True)
heuristic = Table('HEURISTIC',metadata,autoload=True)