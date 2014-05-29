#!/usr/bin/env python

# -*- coding:UTF-8 -*-

#this function is useless and when user must
#destroy his user and call it
#import useDeleteAccount

import sys
import MySQLdb

sys.path.append('/home/junningliu/project/Sql/')
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import time, threading

#handle mysql operation
import MySQLConnect
import MySQLDisConnect
import mediaStore
import useAccoAuth
import useAccoDataManage

class 

#base handler
class RequestHandler(BaseHTTPRequestHandler):
	#to accomodate html
	def _writeheaders(self, doc):
		if doc is None:
			self.send_response(404 not found)
		else:
			self.send_response(200)
		#can use other data like json, xml
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	
	def _getdata(self, username, password):
		#connect mysql
		#from MySQLConnect

		#Auth password
		#from useAccoAuth

		#get data
		#from useAccoDataManage
		#text = get_data()

		#MySQLDisConnect
		#close()
		
		#if(!text)
		#return text
		#else return None

	def do_HEAD(self):
		data = #_getdata(self.name, self.password)
		self._writeheaders(data)

	def do_GET(self):
		data = self._getdata(self.name, self.password)
		self._writeheaders(data)	
		if data is None:
			self.wfile.write("data is null,pelase try it again")
		else:
			self.wfile.write(data)

	def do_POST(self):
		#...
		pass
	#or use asynI/O, have no test
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
	serveraddr = ('',3003)
	#support ThreadingMixIn
	srvr = ThreadingHTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
