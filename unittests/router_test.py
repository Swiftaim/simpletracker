from selenium import webdriver
import unittest
from server.router import Router

class RouterTest(unittest.TestCase):
	"""
	Testing the router functionality from a web browser perspective.
	In order to run the tests the http server must be running.
	"""

	def setUp(self):
		self._browser = webdriver.Firefox()
		
	def test_contact_url(self):
		"""Testing that the correct page is loaded for the /contact.html url"""
		self._browser.get('http://localhost:8000/contact.html')
		assert('Contact' in self._browser.title)

	def test_products_url(self):
		"""Testing that the correct page is loaded for the /products.html path"""
		self._browser.get('http://localhost:8000/products.html')
		assert('Products' in self._browser.title)

	def test_report_url(self):
		"""Testing that the correct page is loaded for the /report.html url"""
		self._browser.get('http://localhost:8000/report.html')
		assert('Report' in self._browser.title)

	def test_got_cookie(self):
		"""Testing that a cookie is placed in the browser by the server"""
		self._browser.get('http://localhost:8000/contact.html')
		assert(bool(self._browser.get_cookies()))

	def test_got_simpletracker_userid_cookie(self):
		"""
		Testing that the simpletracker-userid cookie is placed in the browser
		by the server
		"""
		self._browser.get('http://localhost:8000/contact.html')
		assert(bool(self._browser.get_cookie(': Set-Cookie: simpletracker-userid')))

	def tearDown(self):
		self._browser.quit()

if __name__ == '__main__':
	unittest.main()
