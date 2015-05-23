# Unittests for the Display Report user story.
#
# The "basic report" scenario:
# Sample data:
# |timestamp              |url           |userid|
# |2013-09-01 09:00:00UTC |/contact.html |12345 |
# |2013-09-01 09:00:00UTC |/contact.html |12346 |
# |2013-09-01 10:00:00UTC |/contact.html |12345 |
# |2013-09-01 11:00:00UTC |/contact.html |12347 |
#
# When I view the report for the time range 2013-09-01 09:00:00 - 10:59:59
# The the report should contain the data:
# |url           |page views |visitors|
# |/contact.html |3          |2       |

import unittest

class BasicReportTest(unittest.TestCase):
	"""
	Unittests for the "basic report" scenario.
	"""
	def setUp(self):
		self._testdata = [
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/contact.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/contact.html', 'userid' : '12346'},
			{ 'timestamp' : '2013-09-01 10:00:00UTC', 'url' : '/contact.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 11:00:00UTC', 'url' : '/contact.html', 'userid' : '12347'}
		]

	def tearDown(self):
		print('BasicReportTest.tearDown()')

if __name__ == '__main__':
    unittest.main()

