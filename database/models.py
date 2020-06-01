
from .db import db
from sqlalchemy.dialects.postgresql import JSON
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100))
	password = db.Column(db.String(200))

	def __init__(self, email, password):
			self.email = email
			self.password = password
			print(password)

	def save_record(self):
		 db.session.add(self)
		 db.session.commit()

    
	@classmethod
	def get_user_by_email(cls,email):
		return cls.query.filter_by(email=email).first()

	def __repr__(self):
 	     return '<User {}>'.format(self.username)    
 
	def check_password(self, password):
		return check_password_hash(self.password, password)


"""user = User("pavneettiwana90@gmail.com", password = "pavneet9")
user.save_record()"""