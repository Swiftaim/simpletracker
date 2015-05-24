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
# When the report is run for the time range 2013-09-01 09:00:00 - 10:59:59
# the report should contain the data:
# |url           |page views |visitors|
# |/contact.html |3          |2       |

import unittest
import json
from reporting.display_report import DisplayReport

class DisplayReportTest(unittest.TestCase):
	"""
	Unittests for the "basic report" scenario.
	"""

	def setUp(self):
		"""Setup test data"""
		self._testdata = [
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/contact.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/contact.html', 'userid' : '12346'},
			{ 'timestamp' : '2013-09-01 10:00:00UTC', 'url' : '/contact.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 11:00:00UTC', 'url' : '/contact.html', 'userid' : '12347'},
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/home.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 09:00:00UTC', 'url' : '/home.html', 'userid' : '12346'},
			{ 'timestamp' : '2013-09-01 10:00:00UTC', 'url' : '/home.html', 'userid' : '12345'},
			{ 'timestamp' : '2013-09-01 11:00:00UTC', 'url' : '/home.html', 'userid' : '12347'}
		]

	def test_basic_report(self):
		"""Test the basic reporting method of DisplayReport"""

		# The report generating object.
		display_report = DisplayReport()
		# The time interval for which to generate the report
		from_time = '2013-09-01 09:00:00UTC'
		to_time = '2013-09-01 10:59:59UTC'
		# Generate the report from the _testdata for the time interval [from_time -> to_time]
		result = display_report.generate_basic_report(from_time, to_time, self._testdata)
		# Test success criteria
		assert(bool(result))
		# Page views should be 3
		assert(result[0][1] == 3)
		# Unique visitors should be 2
		assert(result[0][2] == 2)

	def test_within_time_interval(self):
		"""Testing the DisplayReport.within_time_interval() method"""

		# The report generating object.
		display_report = DisplayReport()

		# A time interval to test with
		from_time = '2013-09-01 09:00:00'
		to_time = '2013-09-01 10:59:59'
		
		# Timestamps inside the time interval
		time_left = '2013-09-01 10:00:00'
		time_middle = '2013-09-01 09:37:48' 
		time_right = '2013-09-01 10:59:59'

		result = display_report.within_time_interval(from_time, to_time, time_left)
		assert(bool(result))
		result = display_report.within_time_interval(from_time, to_time, time_middle)
		assert(bool(result))
		result = display_report.within_time_interval(from_time, to_time, time_right)
		assert(bool(result))

		# Timestamps outside the time interval
		time_before = '2013-09-01 08:59:59'
		date_before = '2013-08-31 09:37:48' 
		time_after = '2013-09-01 11:00:00'
		date_after = '2014-09-01 10:00:00'

		result = display_report.within_time_interval(from_time, to_time, time_before)
		assert(not bool(result))
		result = display_report.within_time_interval(from_time, to_time, date_before)
		assert(not bool(result))
		result = display_report.within_time_interval(from_time, to_time, time_after)
		assert(not bool(result))
		result = display_report.within_time_interval(from_time, to_time, date_after)
		assert(not bool(result))


	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()

