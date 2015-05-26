import logging
import time

class Logger():
	"""Provides simple logging to a file"""

	def __init__(self, app_name, filename):
		self._app = app_name
		self._filename = filename
		self._logger = logging.getLogger(app_name)
		self._hdlr = logging.FileHandler(filename)
		self._formatter = logging.Formatter('%(asctime)s %(message)s')
		# Always log GMT time
		self._formatter.converter = time.gmtime
		self._hdlr.setFormatter(self._formatter)
		self._logger.addHandler(self._hdlr) 
		self._logger.setLevel(logging.INFO)

	def log(self, message):
		"""Log the message to file"""
		try:
			self._logger.info(message)
		except:
			# Something went wrong with the log file, perhaps it was removed?
			self._logger.handlers[0].stream.close()
			self._logger.removeHandler(self._logger.handlers[0])
			# Setup a new logger for the same file
			self._logger = logging.getLogger(self._app)
			self._hdlr = logging.FileHandler(self._filename)
			self._formatter = logging.Formatter('%(asctime)s %(message)s')
			# Always log GMT time
			self._formatter.converter = time.gmtime
			self._hdlr.setFormatter(self._formatter)
			self._logger.addHandler(self._hdlr) 
			self._logger.setLevel(logging.INFO)
