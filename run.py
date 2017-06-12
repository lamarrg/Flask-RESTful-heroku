from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
	# this will create the defined DB and tables. only really works when you can create here...
	db.create_all()
