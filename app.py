from flask import Flask
import MySQLdb
import json

app = Flask(__name__)

db = MySQLdb.connect(host="localhost",    
					 user="root",         
					 passwd="girlhack",  
					 db="GirlHack_DB")
cursor = db.cursor()

@app.route('/newUser/', methods=['POST'])
def newUser():
	firstName = request.form['firstName']
	lastName = request.form['lastName']
	#password will be SHA'd on the front end
	password = request.form['password']
	bio = request.form['bio']
	school = request.form['school']
	isCollege = request.form['isCollege']
	#languages?
	try:
		cursor.execute("INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s)",(firstName,lastName,password,bio,school,isCollege))
		db.commit()
	except:     
		db.rollback()

#Assume US locations for now. Maybe EU someday
@app.route('/getEvents/', methods=['GET'])
def getEvents():
	print "reached the function"
	try:
		cursor.execute("SELECT name, date, link, location FROM hackathon where is_US = 1")
		#rows = cursor.fetchall()
		cursorList = list(cursor)
		#print len(cursorList)
		rowarray_list = []
		for row in cursorList:
			#print row
			t = {}
			t['name'] = row[0]
			t['date'] = row[1] 
			t['link'] = row[2] 
			t['location'] = row[3]
			rowarray_list.append(t)
		results = json.dumps(rowarray_list)	
		return results 
	except MySQLdb.Error, e:
            print( "Run function Error %d: %s" % (e.args[0], e.args[1]))