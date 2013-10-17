
# -*- coding: utf-8 -*-

""" Emulate syslog module on POSIX environment """

import logging


_log = logging.getLogger(None)

DEFAULT_FACILITY_TEXT = "user"
_default_facility_text = DEFAULT_FACILITY_TEXT


# {{{ Priorities
LOG_EMERG = 0	#: system is unusable
LOG_ALERT = 1	#: action must be taken immediately
LOG_CRIT = 2	#: critical conditions
LOG_ERR = 3		#: error conditions
LOG_WARNING = 4	#: warning conditions
LOG_NOTICE = 5	#: normal but significant condition
LOG_INFO = 6	#: informational
LOG_DEBUG = 7	#: debug-level messages

MASK_PRIORITY = 0x07
# }}} Priorities

# {{{ Facilities
LOG_KERN = (0 << 3)	#: kernel messages
LOG_USER = (1 << 3)	#: random user-level messages
LOG_MAIL = (2 << 3)	#: mail system
LOG_DAEMON = (3 << 3)	#: system daemons
LOG_AUTH = (4 << 3)	#: security/authorization messages
LOG_LPR = (5 << 3)	#: line printer subsystem
LOG_NEWS = (6 << 3)	#: network news subsystem
LOG_UUCP = (7 << 3)	#: UUCP subsystem
LOG_CRON = (8 << 3)	#: clock daemon
LOG_SYSLOG = (9 << 3)	#: messages generated internally by syslogd

LOG_LOCAL0 = (16 << 3)	#: reserved for local use
LOG_LOCAL1 = (17 << 3)	#: reserved for local use
LOG_LOCAL2 = (18 << 3)	#: reserved for local use
LOG_LOCAL3 = (19 << 3)	#: reserved for local use
LOG_LOCAL4 = (20 << 3)	#: reserved for local use
LOG_LOCAL5 = (21 << 3)	#: reserved for local use
LOG_LOCAL6 = (22 << 3)	#: reserved for local use
LOG_LOCAL7 = (23 << 3)	#: reserved for local use

MASK_FACILITY = 0x03f8
TEXTMAP_FACILITY = {
			LOG_KERN: "kern", LOG_USER: "user", LOG_MAIL: "mail",
			LOG_DAEMON: "daemon", LOG_AUTH: "auth", LOG_LPR: "lpr",
			LOG_NEWS: "news", LOG_UUCP: "uucp", LOG_CRON: "cron",
			LOG_SYSLOG: "syslog",
			LOG_LOCAL0: "local0", LOG_LOCAL1: "local1", LOG_LOCAL2: "local2",
			LOG_LOCAL3: "local3", LOG_LOCAL4: "local4", LOG_LOCAL5: "local5",
			LOG_LOCAL6: "local6", LOG_LOCAL7: "local7",}
# }}} Facilities

# {{{ Options
LOG_PID = 0x01	#: log the pid with each message
LOG_CONS = 0x02	#: log on the console if errors in sending
LOG_NDELAY = 0x08	#: don't delay open
LOG_NOWAIT = 0x10	#: don't wait for console forks
LOG_PERROR = 0x20	#: log to stderr as well
# }}} Options



def openlog(ident=None, logoption=0, facility=-1):
	global _log
	global _default_facility_text

	_log = logging.getLogger(ident)
	_default_facility_text = TEXTMAP_FACILITY.get(facility, DEFAULT_FACILITY_TEXT)
# ### def openlog


def _syslog_impl(priority_level, facility_text, msg):
	func = None
	if priority_level <= LOG_EMERG:
		func = _log.critical
	elif priority_level <= LOG_ALERT:
		func = _log.critical
	elif priority_level <= LOG_CRIT:
		func = _log.critical
	elif priority_level <= LOG_ERR:
		func = _log.error
	elif priority_level <= LOG_WARNING:
		func = _log.warning
	elif priority_level <= LOG_NOTICE:
		func = _log.info
	elif priority_level <= LOG_INFO:
		func = _log.info
	elif priority_level <= LOG_DEBUG:
		func = _log.debug

	func("[%s] %s", facility_text, msg)
# ### def _syslog_impl

def syslog(*args):
	priority_level = LOG_INFO
	facility_text = _default_facility_text
	msg = ""

	if 1 == len(args):
		msg = args[0]
	elif 2 == len(args):
		p = int(args[0])
		priority_level = p & MASK_PRIORITY
		facility_id = p & MASK_FACILITY
		facility_text = TEXTMAP_FACILITY.get(facility_id, DEFAULT_FACILITY_TEXT)
		msg = args[1]

	if isinstance(msg, unicode):
		msg = msg.encode("UTF-8", "ignore")
	else:
		msg = str(msg)

	_syslog_impl(priority_level, facility_text, msg)
# ### def syslog


def closelog():
	pass
# ### def closelog


def setlogmask(maskpri):
	pass
# ### def setlogmask



# vim: ts=4 sw=4 ai nowrap
