#!/usr/bin/env python
#Login 
#empty value user, passwd, db
#user = 
#passwd =
#db = 
def createNewAccount(username, userpasswd, sex):
	#cursor
	cur = MySQLConnect.conMySQL(user, passwd, db)
	#exist user
	value = ['NULL',username,userpasswd,'NULL',sex]
	#search user existence
	cur.execute('')
	if(findresult):
		#php-style
		#cur.execute("INSERT INTO users VALUES (NULL, " + "'" + username + "'" + ", NULL, '" + sex + "'")
		cur.execute('INSERT INTO users VALUES(%s,%s,%s,%s,%s)', value)

	#in order to insert it really,youshould
	conn.commit()
	#successful
	cur.close()
	conn.close()

	
	
