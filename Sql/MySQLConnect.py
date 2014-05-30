#!/usr/bin/env python
import MySQLdb

def conMySQL(user, passwd, db):
	#connect function
	errorMessage = 'cannot connect database, please check it'
	try:
		#gbk code-confuse,utf8?
		conn = MySQLdb.connect(host='localhost', user, passwd, db, port=3306, charset='utf8')
		cur = conn.cursor()
		return cur
		#run sql
		#cur.execute('')
	except MySQLdb.Error, e:
		print errorMessage
