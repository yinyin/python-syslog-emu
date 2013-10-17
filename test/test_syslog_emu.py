#!/usr/bin/python

# -*- coding: utf-8 -*-

import unittest
import logging
import os
import imp

syslog = imp.load_source("syslog", os.path.join("lib", "syslog.py"))



class MemoryLogHandler(logging.Handler):
	def __init__(self):
		logging.Handler.__init__(self)
		self.setFormatter(logging.Formatter(logging.BASIC_FORMAT, "DATETIME=(%Y%m%d%H%M)"))
		self.message_buffer = []
	def emit(self, record):
		try:
			msg = self.format(record)
			self.message_buffer.append(msg)
		except:
			self.handleError(record)
# ### class MemoryLogHandler



class TestOneMessage(unittest.TestCase):
	def setUp(self):
		self.hdlr = MemoryLogHandler()
		root_logger = logging.getLogger()
		root_logger.addHandler(self.hdlr)
		root_logger.setLevel(logging.DEBUG)
	# ### def setUp
	def tearDown(self):
		root_logger = logging.getLogger()
		root_logger.removeHandler(self.hdlr)
	# ### def tearDown

	def test_debug(self):
		syslog.openlog("test1", syslog.LOG_PID | syslog.LOG_PERROR)
		syslog.syslog(syslog.LOG_CRIT, "message for test1")

		self.assertEqual(self.hdlr.message_buffer[0], "CRITICAL:test1:[user] message for test1")
	# ### def test_debug

	def test_info(self):
		syslog.openlog("test1", syslog.LOG_PID | syslog.LOG_PERROR)
		syslog.syslog(syslog.LOG_INFO, "message for test1 info")

		self.assertEqual(self.hdlr.message_buffer[0], "INFO:test1:[user] message for test1 info")
	# ### def test_info
# ### class TestOneMessage



if __name__ == '__main__':
	unittest.main()
# <<< if __name__ == '__main__':


# vim: ts=4 sw=4 ai nowrap
