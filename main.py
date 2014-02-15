from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.pennapps
import string
import random
import json
import hashlib
from flask import Flask, session, redirect, url_for, request,render_template, flash
app = Flask(__name__)
APP_SECRET_KEY = 'pennapps'

def make_random_salt(length):
    return ''.join(random.choice(string.letters) for x in range(length))

def make_password_hash(username, password, salt):
    h = hashlib.sha256(username + password + salt).hexdigest()
    return '%s|%s' %(h, salt)



@app.route('/createAccount',methods=['POST'])
def createAccount():
	if request.method=='POST':
		#retreiving the user info
		username=request.form['username']
		password=request.form['password']
		phone=request.form['phone']
		print username
		print password
		print phone
		#
		hashPassword=make_password_hash(username, password, make_random_salt(5))
		#creating json data
		userAccount={
				"username":username,
				"password":password,
				"phone":phone
			}
		print userAccount
		#inserting into the MongoDB database, user collection
		collection=db['user']
		collection.insert(userAccount)
		#if insert successful redirect to the addExpense Page
		return render_template('main.htm')

@app.route('/addExpense',methods=['POST'])
def addExpense():
	print "test"
	if request.method =='POST':
		request.form['username']
		request.form['password']
		request.form['phone']

@app.route('/')
def home():
	return render_template('index.htm')
	#return redirect('/auth')
if __name__ == '__main__':
    app.secret_key = APP_SECRET_KEY
    app.run(host='0.0.0.0',port=80,debug=True)
