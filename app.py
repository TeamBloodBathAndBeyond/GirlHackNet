from flask import Flask
import MySQLdb
import json

app = Flask(__name__)

db = MySQLdb.connect(host="localhost",    
                     user="root",         
                     passwd="girlhack",  
                     db="girlHack_db")
cur = db.cursor()

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
    	cursor.execute("""INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s)""",(firstName,lastName, \
    		password,bio,school,isCollege))
    	db.commit()
	except:     
    	db.rollback()

#Assume US locations for now. Maybe EU someday
@app.route('/getEvents/', methods=['GET'])
def getEvents():
	cursor.execute("""SELECT name, date, link, location""" +
	 """is_US FROM hackathons WHERE isUS = true""")
	rows = cursor.fetchall()
	rowarray_list = []
	for row in rows:
	    t = (row.name, row.date, row.link, row.location)
    	rowarray_list.append(t)
	return json.dumps(rowarray_list)