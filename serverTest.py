#!/usr/bin/env python
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import time, threading

class RequestHandler(BaseHTTPRequestHandler):
	def _writeheaders(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	
	def do_HEAD(self):
		self._writeheaders()
	
	def do_A(self):
		self._writeheaders()
		self.rfile(file("LIST"))
		textcont = self.rfile.read()
		print textcont
		self.wfile.write(rfile)

	def do_GET(self):
		self._writeheaders()
		textcont = self.rfile.readline().strip()
		self.wfile.write(textcont)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
	serveraddr = ('',3003)
	#support ThreadingMixIn
	srvr = ThreadingHTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()	
