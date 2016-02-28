from flask import Flask, request
import MySQLdb
import json

app = Flask(__name__)
#TODO remove this
app.debug = True
db = MySQLdb.connect(host="localhost",    
					 user="root",         
					 passwd="girlhack",  
					 db="GirlHack_DB")
cursor = db.cursor()


@app.route('/newUser/', methods=['POST'])
def newUser():
	#TODO remove prints
	firstName = request.form['firstName']
	print(firstName)
	lastName = request.form['lastName']
	print(lastName)
	#password will be SHA'd on the front end
	password = request.form['password']
	print(password)
	bio = request.form['bio']
	print(bio)
	school = request.form['school']
	print(school)
	email = request.form['email']
	print(email)
	skills = request.form['skills']
	print(skills)
	isCollege = request.form['isCollege']
	print(isCollege)
	#languages?
	try:
		#TODO update for actual table
		cursor.execute("INSERT INTO users(email,firstName,lastName,password,school,bio,skills,isCollege) VALUES (%s,%s,%s,%s,%s,%s,%s)",(email,firstName,lastName,password,bio,school,email))
		db.commit()
		#TODO remove this
		cursor.execute("SELECT * FROM users")
		cursorList = list(cursor)
		rowarray_list = []
		for row in cursorList:
			print(row)
	except MySQLdb.Error, e:
		print( "Run function Error %d: %s" % (e.args[0], e.args[1]))     
		db.rollback()
	return json.dumps({})


#Assume US locations for now. Maybe EU someday
@app.route('/getEvents/', methods=['GET'])
def getEvents():
	try:
		cursor.execute("SELECT id, name, date, link, location FROM hackathon where is_US = 1")
		rowarray_list = []
		cursorList = list(cursor)
		for row in cursorList:
			#building JSON object format
			t = {}
			id = row[0]
			t['id'] = id
			t['name'] = row[1]
			t['date'] = row[2] 
			t['link'] = row[3] 
			t['location'] = row[4]
			#Now go out and find the count of people at each event
			cursor.execute("SELECT count from hackathonAttendance WHERE id=?",(str(id))
			t['count'] = cursor.fetch()
			rowarray_list.append(t)
		results = json.dumps(rowarray_list)	
		return results 
	except MySQLdb.Error, e:
			print( "Run function Error %d: %s" % (e.args[0], e.args[1]))

#Internal API function
def getUserInfo(id):
	try:
		cursor.execute("SELECT email, firstname, lastName, school, bio, skills, isCollege FROM users where id = ?",id)
		rawUserInfo = cursor.fetch()
		userInfo = {}
		userInfo['firstName'] = rawUserInfo[1]
		userInfo['lastName'] = rawUserInfo[2]
		userInfo['email'] = rawUserInfo[0]
		userInfo['school'] = rawUserInfo[3]
		userInfo['bio'] = rawUserInfo[4]
		userInfo['skills'] = rawUserInfo[5]
		userInfo['isCollege'] = rawUserInfo[6]
		return json.dumps(userInfo) 
	except MySQLdb.Error, e:
			print( "Run function Error %d: %s" % (e.args[0], e.args[1]))

#External API function. Expected url = /getUser/?userId=userId#
@app.route('/getUser/', methods=['GET'])
def retrieveUserInfo():
	id = request.args.get('user')
	return getUserInfo(id)


@app.route('/updateEventAttendance/', methods=['POST'])	
def updateHackathonAttendance():
	hackathonId = request.data['hackathonId']
	userId = request.data['userId']
	cursor.execute("SELECT count FROM hackathonAttendance WHERE id=?",(hackathonId))
	oldCount = cursor.fetch()
	try:
		cursor.execute("INSERT INTO usersAtHackathon(hackathonId, userId) VALUES(?,?)",(hackathonId, userId))
		cursor.execute("UPDATE hackathonAttendance SET count=count+1 WHERE id=?",(hackathonId))
		db.commit()
	except MySQLdb.Error, e:
		print("Run function Error %d: %s" % (e.args[0], e.args[1]))
		db.rollback()

#internal API function
def getHackathonUsers(id):
	try:
		cursor.execute("SELECT userId FROM WHERE hackathonId=",(id))
		usersInfo = []
		for row in cursor:
			userId = row[0]
			usersInfo.append(getUserInfo(userId))
		return json.dumps(usersInfo)
	except MySQLdb.Error, e:
		print( "Run function Error %d: %s" % (e.args[0], e.args[1]))


#External API function. Expected url = /getEvent/?event=eventID
@app.route('/getEvent/', methods=['GET'])
def getHackathonInfo():
	id = request.args.get('event')
	#Getting the hackathon event
	cursor.execute("SELECT name, location, link, date FROM hackathon where id = ?"(id))
	hackathon = {}
	hackData = cursor.fetch()
	hackathon['name'] = hackData[0]
	hackathon['location'] = hackData[1]
	hackathon['link'] = hackData[2]
	hackathon['date'] = hackData[3]
	#Now get the hackers info
	#hackathon['hackers'] = 



