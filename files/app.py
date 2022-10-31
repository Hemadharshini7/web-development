from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# Models
class Profile(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	name = db.Column(db.String(20), unique=False, nullable=False)
    contact = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.email, unique=False, nullable=False)
	username = db.Column(db.String(30), nullable=False)

	# repr method represents how one object of this datatable
	# will look like
	def __repr__(self):
		return name : {self.name}, username: {self.uname}"

# function to render index page
@app.route('/')
def index():
	profiles = Profile.query.all()
	return render_template('index.html', profiles=profiles)

@app.route('/add_data')
def add_data():
	return render_template('login.html')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
	# In this function we will input data from the
	# form page and store it in our database. Remember
	# that inside the get the name should exactly be the same
	# as that in the html input fields
	name = request.form.get("name")
	contact = request.form.get("cont")
	email = request.form.get("email")
	username = request.form.get("uname")

	# create an object of the Profile class of models and
	# store data as a row in our datatable
	if name != '' and contact != '' and email != ''and username is not None:
		p = Profile(name=name, contact=cont, email=email ,username=uname)
		db.session.add(p)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/delete/<int:id>')
def erase(id):
	
	# deletes the data on the basis of unique id and
	# directs to home page
	data = Profile.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run()


