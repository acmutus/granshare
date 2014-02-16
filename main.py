
from pymongo import MongoClient
from twilio import twiml
from twilio.rest import TwilioRestClient
import string
import random
import json
import hashlib
import datetime
from flask import Flask, session, redirect, url_for, request,render_template, flash
app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.pennapps
APP_SECRET_KEY = 'pennapps'


def make_random_salt(length):
    return ''.join(random.choice(string.letters) for x in range(length))

def make_password_hash(username, password, salt):
    h = hashlib.sha256(username + password + salt).hexdigest()
    return '%s|%s' %(h, salt)


@app.route('/sms',methods=['POST'])
def sms():
        print "hello"
	print "hello"
	client = TwilioRestClient('AC30244638ab359ff346c2c26c324834a7','d499815d808aac1aaa5c2fe3306147c6')
	response = twiml.Response()
        body = request.form['Body']
	print body
	outputMessage=''
	if 'display' in body.lower():
		print "Entered display "
		groupName=body.split('#')[1]
		print groupName
		#query the database using the group name and retrieve the group names
		collection=db['groups']
		results=collection.find({'groupName':groupName})
		message=''
		for  result in results:
			for user in  result['groupList']:
				#retrieve the data from the dataset Expense
				collection=db['expense']
				output=collection.find({'payee':user,'group':groupName})
								
				for outputresult in output:
					#print outputresult
					collection=db['user']
					phoneNumber=str(outputresult['payee'])
					print phoneNumber
					outputUser=collection.find({'phone':phoneNumber})
					for outputU in outputUser:
						username=str(outputU['username'])
					#outputUser=collection.find({'phone':str(outputresult['payee'])})
					message=message+username+' $'+str(outputresult['price'][0])+' '+str(outputresult['date'])[6:10]+'\n'
				outputMessage=outputMessage+message
				print message
				message=''
		response.message(outputMessage)
			#print str(json.loads(result)
		return str(response)
	else:
		#function to parse the data parse the data
		#############################################
		#############################################
		#############################################
		i=1
		groupList = []
		descList=[]
		s=''
		while i < len(body):
        		if body[i]==' ':
	            	    	break
        		if body[i]=='#':
                		groupList.append(s)
                		s=''
        		else:
                		s=s+body[i]
        		i=i+1
		groupList.append(s)
		desc=''
		while i < len(body):
        		if body[i]=='$':
                		i=i+1
                		break
        		desc=desc+body[i]
        		i=i+1;
		descList.append(desc)
		print groupList
		print descList
		price=' '
		priceList=[]
		while i < len(body):
        		price=price+body[i]
        		i=i+1
		priceList.append(float(price))
		print priceList

		#############################################
		#############################################
		userExpense={
				"payee":request.form['From'],
				"group":groupList,
				"desc":descList,
				"price":priceList,
				"date":datetime.datetime.utcnow()
			}
		collection=db['expense']
		print collection.insert(userExpense)
		#############################################

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
url_for('static', filename='login.js')
url_for('static', filename='main.js')
