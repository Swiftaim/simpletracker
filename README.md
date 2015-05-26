# simpletracker
A simple tracker demo written in Python 3.4

Running the server
==================
The http server is started by running "python app.py" from the command line.
The server listens on port 8000

Valid URLs
==========
http://localhost:8000/contact.html -- displays a simple view for the contact page
http://localhost:8000/products.html -- displays a simple view for the products page
http://localhost:8000/report.html -- this page has a little bit more functionality as it displays a page tracking report

Running the unittests
=====================
python -m unittests.display_report_test -- runs some unittests for the reporting functionality
python -m unittests.router_test -- runs some router tests from a browser perspective. Requires Selenium!

Running the command line report tool
====================================
Run python report_generator.py <from-date> <from-time> <to-date> <to-time>
May also be run without arguments which will result in a report covering all collected data.

Example:
python report_generator.py 2015-05-26 09:00:00 2015-05-31 23:59:59
or
python report_generator.py

The report covering all collected data is also available from the URL http://localhost:8000/report.html


