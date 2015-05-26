import display_report
import sys

def main():
	from_time = to_time = ""
	if len(sys.argv) < 5:
		print('Usage: report_generator <start-date> <start-time> <end-date> <end-time>')
		print('Including all data records!')
		from_time = None
		to_time = None
	else:
		from_time = '{} {},000UTC'.format(sys.argv[1], sys.argv[2])
		to_time = '{} {},000UTC'.format(sys.argv[3], sys.argv[4])

	report_engine = display_report.DisplayReport()
	report = report_engine.run_basic_report(from_time, to_time, '../server/simple_tracker.log')
	# Finally print the report using a pretty print method.
	header = ['url', 'page views', 'visitors']
	report_engine.pretty_print_report(report, header)

if __name__ == "__main__":
	main()
