from flask_restful import Resource, reqparse
from database.models import User
from flask import Response, request
from database.models import User
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from werkzeug.security import safe_str_cmp
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError

class SignupApi(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('email',
						type=str,
						required=True,
						help='This cannot be empty')

	parser.add_argument('password',
						type=str,
						required=True,
						help='This cannot be empty')

	def post(self):
		try:
			data = SignupApi.parser.parse_args()
			email = data.email
			password = data.password
			if User.get_user_by_email(email):
	        	    return {"message": "A user with that username already exists"}, 400
			user = User(email, password)
			user.save_record()
			user = User.get_user_by_email(email)
			access_token = create_access_token(identity=user.id, fresh = True)
			return {"access_token": access_token}, 200
		except Exception as e:
			print(str(e))

class LoginApi(Resource):
	parser = reqparse.RequestParser()

	parser.add_argument('email',
							type=str,
							required=True,
							help='This cannot be empty')

	parser.add_argument('password',
							type=str,
							required=True,
							help='This cannot be empty')

	def post(self):
		data = SignupApi.parser.parse_args()
		email = data.email
		password = data.password
        #hash the passwords
		user = User.get_user_by_email(email)
		if user and safe_str_cmp(user.password, password):	
					access_token = create_access_token(identity=user.id, fresh = True)
					return {"access_token" : access_token}, 200
		return {"message": "A user with that username already exists"}, 400
