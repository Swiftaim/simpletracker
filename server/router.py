from http.server import BaseHTTPRequestHandler
from http import cookies
from urllib import parse, request
import time, uuid, os
from reporting import display_report
from . import logger

class Router(BaseHTTPRequestHandler):
	"""
	Handles HTTP requests and serves the view corresponding to the request.
	"""	

	def do_GET(self):
		"""Override the GET method"""

		# Delegate the request to a specialised method appropriate for each route.
		# Creating a "switch" construct for choosing the right delegate method.
		delegates = {'/contact.html' : self.processContactRequest,
						'/products.html' : self.processProductsRequest,
						'/report.html' : self.processReportRequest}
		#try:
		delegates[self.path]()
		#except:
		#	self.page_not_found()
		

	def processContactRequest(self):
		"""Process the /contact request"""

		# Use the simple page renderer to create the body content
		self.wfile.write(self.render_simple_page('Contact').encode())

	def processProductsRequest(self):
		"""Process the /products request"""

		# Use the simple page renderer to create the body content
		self.wfile.write(self.render_simple_page('Products').encode())

	def processReportRequest(self):
		# Use the simple page renderer to create the body content
		page = self.render_simple_page('Report')
		# Finally run and print the report using a pretty print method.
		report_engine = display_report.DisplayReport()
		report = report_engine.run_basic_report(None, None, 'server/simple_tracker.log')
		header = ['url', 'page views', 'visitors']
		html_report = report_engine.pretty_html_report(report, header)
		page += html_report
		self.wfile.write(page.encode())

	def render_simple_page(self, title):
		# This is an ok route, so send 200
		self.send_response(200)
		self.send_header('Content-Type', 'text/html')

		# Handle cookies.
		cookie = cookies.SimpleCookie()
		cookie_string = self.headers.get('Cookie')
		# The first time the page is run there will be no cookies
		if not cookie_string:
			cookie['simpletracker-userid'] = uuid.uuid1()
			self.send_header('Set-Cookie:', '{}'.format(cookie.output()))
			print('place_pixel_image(), create cookie= userid:{}'.format(cookie.output().split('=',1)[1]))
		else:
			cookie.load(cookie_string)
		# All headers must be sent at this point.
		self.end_headers()
		
		# Generate HTML
		html = "<html><head>"
		html += self.read_css()
		html += "<title>{}</title>".format(title)
		# All routes uses a pixel image for tracking so let's add to the head.
		html += self.place_pixel_image(cookie.output().split('=',1)[1]) + "</head>"
		
		html += "<body bgcolor=\"#CADCA6\"><h1>Welcome to {}</h1>".format(title)
		html += "<p class=date>Server time: {} GMT</p></body></html>".format(time.asctime(time.gmtime()))
		return html

	def read_css(self):
		css_file = open('server/style.css')
		style = ""
		for line in css_file:
			style += line
		return style

	def place_pixel_image(self, id):
		"""Injects a fake pixel image"""
		# Log the page view
		self.log_page_view(self.path, id)
		return "<img src=data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==>"

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

	def page_not_found(self):
		self.send_response(404)

		self.send_header('Content-Type', 'text/html')
		self.end_headers()

		html = "<html><body>Page not found!</body></html>"
		self.wfile.write(html.encode())
