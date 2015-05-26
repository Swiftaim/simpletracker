# A simple reporting module for displaying page usage statistics.

class DisplayReport():
	"""
	Provides methods for producing reports on tracking data.
	"""

	def run_basic_report(self, from_time, to_time, file_name):
		"""Run the basic report on the server/simple_tracker.log file"""
		
		file = open(file_name)
		raw_data = []
		for line in file:
			columns = line.split(' ')
			row = {}
			row['timestamp'] = '{} {}UTC'.format(columns[0], columns[1])
			row['url'] = columns[2]
			row['userid'] = columns[3]
			raw_data.append(row)

		report = self.generate_basic_report(from_time, to_time, raw_data)
		return report

	def generate_basic_report(self, from_time, to_time, raw_data):
		"""
		Generates the basic report for the supplied data.
		
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
		if from_time == None:
			if to_time == None:
				return True
			else:
				return bool(time <= to_time)
		else:
			if to_time == None:
				return bool(time >= from_time)

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

	def pretty_html_report(self, report, header):
		"""Generates an html version of the report"""
		# Use a nice style for the table view

		# Build an html table from the report and it's header
		html_table = "<table id=\"t01\">"
		html_table += "<caption><b>Tracking Statistics</b></caption>"
		# Generate the html table header
		html_table_header = "<tr>"
		for item in header:
			html_table_header += "<th>{}</th>".format(item)
		html_table_header += "</tr>"

		# Generate the html data rows
		html_table_rows = ""
		for row in report:
			html_table_rows += "<tr>"
			for column in row:
				html_table_rows += "<td>{}</td>".format(column)
			html_table_rows += "</tr>"
		
		html_table += html_table_header
		html_table += html_table_rows
		html_table += "</table>"

		return html_table
