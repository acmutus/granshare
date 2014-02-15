from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.pennapps
from twilio import twiml
from twilio.rest import TwilioRestClient
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
@app.route('/sms',methods=['POST'])
def sms():
	print "hello"
	client = TwilioRestClient('AC30244638ab359ff346c2c26c324834a7','d499815d808aac1aaa5c2fe3306147c6')
	response = twiml.Response()
	client.messages.create(from_='+12674196426', to='+12153501452',body="hey Wassup!")
	response.message('message sent')
	return str(response)
	
@app.route('/login',methods=['POST'])
def doLogin():
         #if len(session['phone'])>0:
	   # return render_template('main.htm')
	username=request.form['login_username']
	password=request.form['login_password']
	print username
	print password
	#check if the username is correct
	collection=db['user']
	userInfo=collection.find_one({"username":username})
	print userInfo
	if userInfo == None:
		return render_template('index.htm') 
	storePassword=userInfo['password']
	print storePassword
	salt=storePassword.split('|')[1]
	print salt
	hashPassword=make_password_hash(username, password,salt)
	if hashPassword==storePassword:
		return render_template('main.htm')
	else:
		 return render_template('index.htm')
	

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
				"password":hashPassword,
				"phone":phone
			}
		print userAccount
		print hashPassword
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
