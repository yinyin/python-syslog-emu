#!/usr/bin/python

# -*- coding: utf-8 -*-

import unittest
import sys
import logging

sys.path.insert(1, 'lib')

import syslog


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
	def tearDown(self):
		root_logger = logging.getLogger()
		root_logger.removeHandler(self.hdlr)
	def test_debug(self):
		syslog.openlog("test1", syslog.LOG_PID | syslog.LOG_PERROR)
		syslog.syslog(syslog.LOG_CRIT, "message for test1")

		self.assertEqual(self.hdlr.message_buffer[0], "hello")



if __name__ == '__main__':
	unittest.main()
# <<< if __name__ == '__main__':


# vim: ts=4 sw=4 ai nowrap
