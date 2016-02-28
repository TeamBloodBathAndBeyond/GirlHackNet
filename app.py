from flask import Flask, request
import MySQLdb
import json

app = Flask(__name__)
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
	#print(isCollege)
	#languages?
	try:
		#TODO update for actual table
		cursor.execute("INSERT INTO users(email,firstName,lastName,password,school,bio,skills,isCollege) VALUES (%s,%s,%s,%s,%s,%s,%s)",(email,firstName,lastName,password,bio,school,email))
		db.commit()
		cursor.execute("SELECT * FROM users_test")
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
		cursorList = list(cursor)
		rowarray_list = []
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
			cursor.execute("SELECT count from hackathonAttendance WHERE id=?",(id))
			t['count'] = cursor.fetch()
			rowarray_list.append(t)
		results = json.dumps(rowarray_list)	
		return results 
	except MySQLdb.Error, e:
            print( "Run function Error %d: %s" % (e.args[0], e.args[1]))

def getUserInfo():
def getAttendendanceCount():
def updateHackathonAttendance():
	##TODO: add user and hackathon to Users at Hackathon
	##TODO increment hackathonAttendancecount
def getHackathonUsers():
