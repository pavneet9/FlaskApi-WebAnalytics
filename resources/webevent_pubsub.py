
import json
from flask_restful import Resource, reqparse
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required
from google.cloud import pubsub_v1
import datetime
import base64
from time import sleep

class WebEventsPubSub(Resource):
	project_id = "phrasal-bond-274216"
	topic_name = "webevents1"

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
						type=int,
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
  

	producer = pubsub_v1.PublisherClient()
	topic_path = producer.topic_path(project_id, topic_name)
    
	#parser.addar
	def post(self):
		try:
			data = WebEventsPubSub.parser.parse_args()
#\			data = data.encode("utf-8")
			str_body = json.dumps(data)
			print(str_body.encode('utf8'))
			data = base64.urlsafe_b64encode(bytearray(str_body, 'utf8'))
			print(data)
			while True:
					web_event = WebEventsPubSub.producer.publish(WebEventsPubSub.topic_path, data=str_body.encode('utf8'))
					sleep(15)
			print(json.dumps(web_event.result()))
			return {'id': web_event.result()},200
		except Exception as e:
			print(str(e))
			return {'message': e}, 400





