# A simple reporting module for displaying page usage statistics.

class DisplayReport():
	"""
	Provides methods for producing reports on tracking data.
	"""

	def generate_basic_report(self, from_time, to_time, raw_data):
		"""
		Runs the basic report on the supplied data.
		
		Arguments:
		from_time -- start time of the reporting interval
		to_time -- stop time of the reporting interval
		data -- the data supplied to the report
		"""

		# Transform the raw data into something more reporting friendly
		structured_data = self.build_data_structure(from_time, to_time, raw_data)

		# Now build the report from the structured data.
		report = []
		for key, value in structured_data.items():
			report.append([key, len(value), len(set(value))])

		# Finally print the report using a pretty print method.
		header = ['url', 'page views', 'visitors']
		self.pretty_print_report(report, header)

		# Return the actual report data for further processing.
		return report

	def build_data_structure(self, from_time, to_time, raw_data):
		"""
		Extract all data-entries to build a more report-friendly data structure.
		The method will also filter data based on the time interval thus exluding
		data outside of the interval.
		The generated data structure will be on the format {<url> : [<userid_1>...<userid_N>]}

		Arguments:
		raw_data -- the raw data provided to the report generator.
		"""

		data_structure = {}
		for row in raw_data:
			if self.within_time_interval(from_time, to_time, row['timestamp']):
				if row['url'] not in data_structure:
					data_structure[row['url']] = [row['userid']]
				else:
					data_structure[row['url']].append(row['userid'])

		return data_structure

	def within_time_interval(self, from_time, to_time, time):
		"""Check wether a time is within a time interval or not"""

		return bool((time >= from_time) and (time <= to_time))
	
	def pretty_print_report(self, report, header):
		"""Prints a report in a formatted way"""

		for item in header:
			print('|{:<15}'.format(item), end='')
		print('|')

		for row in report:
			for column in row:
				print('|{:<15}'.format(column), end='')
			print('|')
