import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import time
from datetime import timedelta
class SimpleHandler(SimpleHTTPRequestHandler, object):
	lastModified = time.time()
	def do_GET(self):
		if "data.json" in self.path:
			json = "{\"one\": 1, \"two\": 2, \"three\": 3}"
			self.send_response(200)
			self.send_header("Content-length", len(json))
			self.send_header("Last-Modified", self.date_time_string(SimpleHandler.lastModified))
			self.send_header("Expires", self.date_time_string(SimpleHandler.lastModified + 1000))
			for header in self.headers:
				if "x-seq" in header:
					self.send_header(header, self.headers[header])
			# RFC2616 14.10
			self.send_header("Connection", "close")
			self.end_headers()
			self.wfile.write(json)
		else:
			super(SimpleHandler, self).do_GET()
	def do_POST(self):
		resp = "{\"status\":200}"
		self.send_response(200)
		SimpleHandler.lastModified = time.time()
		self.send_header("Last-Modified", self.date_time_string(SimpleHandler.lastModified))
		self.send_header("Content-length", len(resp))
		# RFC2616 14.10
		self.send_header("Connection", "close")
		self.end_headers()
		self.wfile.write(resp)


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.1"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('', port) 

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, SimpleHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()