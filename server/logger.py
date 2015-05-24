import logging
import time

class Logger():
	"""Provides simple logging to a file"""

	def __init__(self, app_name, file_name):
		self._logger = logging.getLogger(app_name)
		self._hdlr = logging.FileHandler(file_name)
		self._formatter = logging.Formatter('%(asctime)s %(message)s')
		# Always log GMT time
		self._formatter.converter = time.gmtime
		self._hdlr.setFormatter(self._formatter)
		self._logger.addHandler(self._hdlr) 
		self._logger.setLevel(logging.INFO)

	def log(self, message):
		"""Log the message to file"""
		self._logger.info(message)
