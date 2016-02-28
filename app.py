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
	print("made it to the function")
	print(str(request.get_data()))
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
	isCollege = request.form['isCollege']
	print(isCollege)
	#languages?
	try:
		cursor.execute("INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s)",(firstName,lastName,password,bio,school,isCollege))
		db.commit()
	except:
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
			t['id'] = row[0]
			t['name'] = row[1]
			t['date'] = row[2] 
			t['link'] = row[3] 
			t['location'] = row[4]
			rowarray_list.append(t)
		results = json.dumps(rowarray_list)	
		return results 
	except MySQLdb.Error, e:
            print( "Run function Error %d: %s" % (e.args[0], e.args[1]))