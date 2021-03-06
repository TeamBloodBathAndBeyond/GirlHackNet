from flask import Flask, request, render_template
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

@app.route('/')
def index():
	url_for('static', filename='css')
	return render_template('index.php')

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
		cursor.execute("INSERT INTO users(email,first_name,last_Name,password,school,bio,skills,isCollege) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)",(email,firstName,lastName,password,bio,school,email, isCollege))
		db.commit()
		#TODO remove this, testing only
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
			cursor.execute("SELECT count from hackathonAttendance WHERE id=%s",(id,))
			t['count'] = cursor.fetchone()[0]
			rowarray_list.append(t)
		results = json.dumps(rowarray_list)	
		return results 
	except MySQLdb.Error, e:
			print( "Run function Error %d: %s" % (e.args[0], e.args[1]))

#Internal API function
def getUserInfo(id):
	try:
		cursor.execute("SELECT email, first_name, last_name, school, bio, skills, isCollege FROM users where email = %s",(id,))
		rawUserInfo = cursor.fetchone()
		userInfo = dict(first_name=rawUserInfo[1], 
			last_name=rawUserInfo[2], 
			email=rawUserInfo[0], 
			school=rawUserInfo[3], 
			bio=rawUserInfo[4], 
			skills=rawUserInfo[5],
			isCollege=rawUserInfo[6]) 
		return userInfo
	except MySQLdb.Error, e:
			print( "Run function Error %d: %s" % (e.args[0], e.args[1]))

#External API function. Expected url = /getUser/?userId=userId#
@app.route('/getUser/', methods=['GET'])
def retrieveUserInfo():
	id = request.args.get('user')
	return json.dumps(getUserInfo(id))


@app.route('/updateEventAttendance/', methods=['POST'])	
def updateHackathonAttendance():
	hackathonId = request.get_json(force=True)['hackathonId']
	userId = request.get_json()['userId']
	try:
		cursor.execute("INSERT INTO usersAtHackathon(hackathonId, userId) VALUES(%s,%s)",(hackathonId, userId))
		cursor.execute("UPDATE hackathonAttendance SET count=count+1 WHERE id=%s",(hackathonId,))
		db.commit()
	except MySQLdb.Error, e:
		print("Run function Error %d: %s" % (e.args[0], e.args[1]))
		db.rollback()
	return json.dumps({})

#internal API function
def getHackathonUsers(id):
	try:
		cursor.execute("SELECT userId FROM usersAtHackathon WHERE hackathonId=%s",(id,))
		usersInfo = []
		for row in cursor:
			userId = row[0]
			usersInfo.append(getUserInfo(userId))
		return usersInfo
	except MySQLdb.Error, e:
		print( "Run function Error %d: %s" % (e.args[0], e.args[1]))


#External API function. Expected url = /getEvent/?event=eventID
@app.route('/getEvent/', methods=['GET'])
def getHackathonInfo():
	id = request.args.get('event')
	#Getting the hackathon event
	cursor.execute("SELECT name, location, link, date FROM hackathon where id =%s",(id,))
	hackathon = {}
	hackData = cursor.fetchone()
	hackathon['name'] = hackData[0]
	hackathon['location'] = hackData[1]
	hackathon['link'] = hackData[2]
	hackathon['date'] = hackData[3]
	#Now get the hackers info
	hackathon['hackers'] = getHackathonUsers(id)
	return json.dumps(hackathon)



