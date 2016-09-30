import sqlalchemy
from sqlalchemy import *
	
 
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306')
engine.execute("USE dbname")
metadata = MetaData(bind=engine)

application = Table('application', metadata, autoload=True)
taskcounter = Table('taskcounter',metadata,autoload=True)
task = Table('task',metadata,autoload=True)
threshold = Table('threshold',metadata,autoload=True)
application_checked = Table('application_checked',metadata,autoload=True)
heuristic = Table('heuristic',metadata,autoload=True)
