from http.server import BaseHTTPRequestHandler
from http import cookies
from urllib import parse, request
import time, uuid, os
from . import logger

class Router(BaseHTTPRequestHandler):
	"""
	Handles HTTP requests and serves the view corresponding to the request.
	"""	

	def do_GET(self):
		"""Override the GET method"""

		# request is either for a file to be served up or our test
		if self.path == "/contact/":
			self.processContactRequest()
		

	def processContactRequest(self):
		"""Process the /contact request"""

		self.send_response(200)

		# Get hold of the cookie (if any)
		cookie = cookies.SimpleCookie()
		cookie_string = self.headers.get('Cookie')
		# The first time the page is run there will be no cookies
		if not cookie_string:
			cookie['simpletracker-userid'] = uuid.uuid1()
			self.send_header('Set-Cookie:', cookie.get('simpletracker-userid'))
		else:
			cookie.load(cookie_string)

		self.send_header('Content-Type', 'text/html')
		self.end_headers()

		html = "<html><body>Server time: {}</body></html>".format(time.asctime(time.gmtime()))
		self.wfile.write(html.encode())

		# Log the page view
		self.log_page_view('/contact.html', cookie.output().split('=',1)[1])

	def static_vars(**kwargs):
		"""A generic decorator adding attributes to methods"""
		def decorate(func):
			for k in kwargs:
				setattr(func, k, kwargs[k])
			return func
		return decorate

	# Adding a logger..Logger attribute to the log_page_view method
	@static_vars(logger_=logger.Logger('SimpleTracker', 'server/simple_tracker.log'))
	def log_page_view(self, page, userid):
		"""Log the page and userid details to a log file"""
		self.log_page_view.logger_.log('{} {}'.format(page, userid))
