#!/usr/bin/env python
#import MySQLdb

errorMessage = 'cannot connect database, please check it'
try:
	conn = MySQLdb.connect(host='localhost', user='userinfo', passwd='ljn7168396', db='androidservice', port=3306)
	cur = conn.cursor()
	#run sql
	#cur.execute('')
except MySQLdb.Error, e:
	print errorMessage

