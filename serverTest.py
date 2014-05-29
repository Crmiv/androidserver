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
	
	def do_SOMETHING(self):
		self._writeheaders()
		self.wfile.write("""!!!""")

	def do_GET(self):
		self._writeheaders()
		self.wfile.write("""<html>nihao</html>""")
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
	serveraddr = ('',3003)
	#support ThreadingMixIn
	srvr = ThreadingHTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()	
