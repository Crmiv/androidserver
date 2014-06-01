#!/usr/bin/env python
import MySQLdb

def conMySQL():
	#connect function
	errorMessage = 'cannot connect database, please check it'
	try:
		#gbk code-confuse,utf8?
		conn = MySQLdb.connect( 
								host = 'localhost', 
			                    user = 'userinfo', 
								passwd = 'ljn7168396', 
				                db = 'userinfo',
								port = 3306, 
								charset = 'utf8'
								)
		
		return conn
		#run sql
		#cur.execute('')
	except MySQLdb.Error, e:
		print errorMessage

#Login 
#empty value user, passwd, db
#user = 
#passwd =
#db = 
def createNewAccount(cutename, username, userpasswd, sex, years):
	
	#return a connection
	conn = conMySQL()	

	cur = conn.cursor()
	
	value = ['',
			cutename, 
			username,
			userpasswd,
			sex,
			years
			]

	#search user existence
	cur.execute('SELECT * FROM 
			     userinfo WHERE 
				 username = %s', value[1])

	findresult = cur.fetchall()
	

	#exist user
	if not findresult:
		#php-style
		#cur.execute("INSERT INTO users VALUES (NULL, " + "'" + username + "'" + ", NULL, '" + sex + "'")
		cur.execute('INSERT INTO 
				     users 
					 VALUES(%s,%s,%s,%s,%s)' 
					 ,value
					 )
	else:
		print "You should create another user and change
		another username"

	#in order to insert it really,youshould
	conn.commit()
	#successful
	cur.close()
	conn.close()


#edit nickname
def EditAccountCutename(cutename, username, userpasswd):
	
	conn = conMySQL()
	cur = conn.cursor()
	cur.execute('SELECT * FROM userinfo WHERE 
			password = %s AND username = %s', username, userpasswd)
	findresult = cur.fetchall()
	if findresult:
		cur.execute('
		UPDATE userinfo SET cutename = %s WHERE 
		username = %s', cutename, username)
		conn.commit()
		
		#update edit-time
		cur.execute('
		UPDATE userinfo SET edit_date = CURRENT_DATE 
		WHERE username = %s', username
				)
		conn.commit()
	else:
		print "you input wrong username or password, 
		please try again"
	
	cur.close()
	conn.close()


def EditAccountYears(years, username, userpasswd):
	
	conn = conMySQL()
	cur = conn.cursor()
	cur.execute('SELECT * FROM userinfo WHERE 
			password = %s AND username = %s', username, userpasswd)
	findresult = cur.fetchall()
	if findresult:
		cur.execute('
		UPDATE userinfo SET years = %i WHERE 
		username = %s', years, username)
		conn.commit()
		
		#update edit-time
		cur.execute('
		UPDATE userinfo SET edit_date = CURRENT_DATE 
		WHERE username = %s', username
				)
		conn.commit()
	else:
		print "you input wrong username or password, 
		please try again"
	
	cur.close()
	conn.close()


def EditAccountPassword(password, username, userpasswd):
	
	conn = conMySQL()
	cur = conn.cursor()
	cur.execute('SELECT * FROM userinfo WHERE 
			password = %s AND username = %s', username, userpasswd)
	findresult = cur.fetchall()
	#no secure
	if findresult:
		cur.execute('
		UPDATE userinfo SET password = %s WHERE 
		username = %s', password, username)
		conn.commit()
		
		#update edit-time
		cur.execute('
		UPDATE userinfo SET edit_date = CURRENT_DATE 
		WHERE username = %s', username
				)
		conn.commit()
	else:
		print "you input wrong username or password, 
		please try again"
	
	cur.close()
	conn.close()


