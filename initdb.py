'''
initialize database settings for running the web server.
'''
from sqlalchemy import *
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306',echo=True)
engine.execute("USE dbname")# use database
metadata = MetaData(bind=engine)

#tables
application = Table('application_checked', metadata, autoload=True)
heuristic = Table('heuristic', metadata, autoload=True)
cluster = Table('cluster',metadata,autoload=True)
task = Table('task',metadata,autoload=True)
task_counter = Table('taskcounter',metadata,autoload=True)
