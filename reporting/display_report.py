# A simple reporting class for displaying page usage statistics.

class DisplayReport():
	"""
	"""
	def run_basic_report(self,from_time, to_time, data):
		"""
		Runs the basic report on the supplied data.
		
		Arguments:
		from_time -- start time of the reporting interval
		to_time -- stop time of the reporting interval
		data -- the data supplied to the report
		"""

		# Extract each data-entry build key statistics
		# Key statistics are 'time', 'url', 'page views' and unique 'visitors'.
		report = {}
		for row in data:
			time = row['timestamp']
			print(time)

		return report
			