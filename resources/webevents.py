import json
from flask_restful import Resource, reqparse
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required
from kafka import KafkaProducer
import datetime

class WebEvents(Resource):
	parser = reqparse.RequestParser()

	parser.add_argument('pageUrl',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('lastPageVisited',
						type=str,
						required=True,
						help='This cannot be empty')
	
	parser.add_argument('timestamp',
						type=lambda x:datetime.datetime.fromtimestamp(x/1000.0).strftime('%Y-%m-%d %H:%M:%S'),
						required=True, 
						help='Input wasn\'t valid!')

	parser.add_argument('eventType',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('uiud',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('sessionId',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('referrer',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('landingPage',
						type=str,
						required=True,
						help='This cannot be empty')


	producer = KafkaProducer(bootstrap_servers=['10.128.0.28:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

	#parser.addar
	def post(self):
		data = WebEvents.parser.parse_args()
		page_url = data.pageUrl
		last_page_visited = data.lastPageVisited
		timestamp = data.timestamp
		eventType = data.eventType
		uiud = data.uiud
		#print(timestamp)
		#data = {"timestamp":timestamp,"lastPageVisited":"https://kickassdataprojects.com/complete-guide-to-mastering-and-optimizing-google-bigquery/","pageUrl":"https://kickassdataprojects.com/about-me/","eventType":"Pageview","uiud":data.uiud}
		WebEvents.producer.send("webevent", value = data)  
		print(data)
		return {'id': timestamp}, 200

