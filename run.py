from flask import Flask
from resources.routes import initialize_routes
from flask_restful import Api
from flask_bcrypt import Bcrypt
from database.db import inititalize_db
from resources.errors import errors
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}},methods=['POST', 'GET','OPTIONS'], send_wildcard=True)
db = inititalize_db(app)
api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
app.secret_key = 'pavneet' 
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)
initialize_routes(api)


if __name__== "__main__":
	db.init_app(app)
	app.run(host='0.0.0.0',port='5000')