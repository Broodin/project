from sqlalchemy import *
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306',echo=True)
engine.execute("USE symantec")
metadata = MetaData(bind=engine)


application = Table('APPLICATION', metadata, autoload=True)
heuristic = Table('HEURISTIC', metadata, autoload=True)
#cluster = Table('CLUSTER',metadata,autoload=True)