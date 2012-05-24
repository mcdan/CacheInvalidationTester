import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import time
from datetime import timedelta
class SimpleHandler(SimpleHTTPRequestHandler, object):
	def do_GET(self):
		if "data.json" in self.path:
			json = "{\"one\": 1, \"two\": 2, \"three\": 3}"
			self.send_response(200)
			self.send_header("Content-length", len(json))
			self.send_header("Content-type", "application/json")
			# If the last modified time is equal to the current time,
			# the browser has a hard time creating a cache expiration
			# so set the time of last modification to be "a little 
			# while ago"
			self.send_header("Last-Modified", self.date_time_string(time.time() - 1000))
			if "?" in self.path:
				self.send_header("Cache-Control", "no-cache")
			for header in self.headers:
				if "x-seq" in header:
					self.send_header(header, self.headers[header])
			self.end_headers()
			self.wfile.write(json)
		else:
			super(SimpleHandler, self).do_GET()
	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write("{\"status\":200}")


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port) 

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, SimpleHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()