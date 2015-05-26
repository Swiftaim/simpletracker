# The main application running a simple http server with tracking capabilities.

from http.server import HTTPServer
from server.router import Router
import reporting

def run(server_class=HTTPServer, handler_class=Router):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def main():
	"""Run the main http server application."""
	run()
	return 0

if (__name__ == "__main__"):
	main()
