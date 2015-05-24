import display_report
import sys

def main():
	if len(sys.argv) < 5:
		print('Usage: report_generator <start-date> <start-time> <end-date> <end-time>')
		return
		
	report_engine = display_report.DisplayReport()

	from_time = '{} {},000UTC'.format(sys.argv[1], sys.argv[2])
	to_time = '{} {},000UTC'.format(sys.argv[3], sys.argv[4])

	report_engine.run_basic_report(from_time, to_time)

if __name__ == "__main__":
	main()
