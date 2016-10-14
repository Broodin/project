from flask import Flask, jsonify, request
import pymysql,json
from flask_restful import reqparse, abort, Api, Resource
from flask import Blueprint
from routes import *
api_rest = Blueprint('api', __name__)
api = Api(api_rest)



#json_data = { 'id' : '', 'name' : '','user' : '', 'queue': '', 'start_time':'' , 'finish_time' : '', 'state': '','url':'', 'elapsed_time':''}
parser = reqparse.RequestParser()



def app_parser():
	
	parser.add_argument('id')
	parser.add_argument('name')
	parser.add_argument('user')
	parser.add_argument('type')
	parser.add_argument('queue')
	parser.add_argument('start_time')
	parser.add_argument('finish_time')
	parser.add_argument('state')
	parser.add_argument('url')
	parser.add_argument('elapsed_time')
	parser.add_argument('checked')
	
def cluster_parser():
	
	parser.add_argument('q_name')
	parser.add_argument('used_capacity')
	parser.add_argument('max_capacity')
	parser.add_argument('time')
	
def task_parser():
	parser.add_argument('task_id')
	parser.add_argument('app_id')
	parser.add_argument('start_time')
	parser.add_argument('finish_time')
	parser.add_argument('type')
	
def taskcounter_parser():
	parser.add_argument('task_id')
	parser.add_argument('name')
	parser.add_argument('value')
	parser.add_argument('type')

	
class Application(Resource):
	def get(self):
		s = application.select()
		cur = s.execute()
		#cur.execute("SELECT * FROM APPLICATION")
		rv = cur.fetchall()
		return len(rv)
	
	def post(self):
		app_parser()
		args = parser.parse_args()
		id = args['id']
		name = args['name']
		user = args['user']
		type= args['type']
		queue = args['queue']
		start_time = args['start_time']
		finish_time = args['finish_time']
		state = args['state']
		url = args['url']
		elapsed_time = args['elapsed_time']
		flag = args['checked']
		#stmt = application.insert()
		#stmt.execute(ID = id, NAME = name, USER = user,QUEUE = queue,START_TIME = start_time, FINISH_TIME = finish_time, STATE = state, URL = url, ELAPSED_TIME = elapsed_time)
		#cur.execute("INSERT INTO APPLICATION(ID,NAME,USER,QUEUE,START_TIME,FINISH_TIME,STATE,URL,ELAPSED_TIME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,user,queue,start_time,finish_time,state,url,elapsed_time))
		#conn.commit()
		return jsonify(id,name,user,queue,start_time,finish_time,state,url,elapsed_time)


		
class Cluster(Resource):
	def get(self):
		s = cluster.select()
		cur = s.execute()
		#cur.execute("SELECT * FROM HEURISTIC")
		rv=cur.fetchall()
		return len(rv)

	def post(self):
		cluster_parser()
		args = parser.parse_args()
		q_name=args['q_name']
		used_capacity = args['used_capacity']
		max_capacity = args['max_capacity']
		time = args['time']
		#stmt = cluster.insert()
		#stmt.execute(QUEUE_NAME = q_name,USED_CAPACITY = used_capacity, MAX_CAPACITY = max_capacity,DATE = time)
		return jsonify(q_name,used_capacity,max_capacity,time)

class Task(Resource):
	def get(self):
		return 0
	def post(self):
		task_parser()
		args = parser.parse_args()
		task_id = args['task_id']
		app_id = args['app_id']
		start_time = args['start_time']
		finish_time = args['finish_time']
		type = args['type']
		return 1

class TaskCounter(Resource):
	def get(self):
		return 0
	def post(self):
		taskcounter_parser()
		args = parser.parse_args()
		task_id = args['task_id']
		name = args['name']
		value = args['value']
		type = args['type']
		return 1
		
api.add_resource(Application, '/app/application/post')
api.add_resource(Cluster, '/app/cluster/post')
api.add_resource(Task, '/app/task/post')
api.add_resource(TaskCounter, '/app/counter/post')
