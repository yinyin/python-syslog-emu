#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup



setup(name='syslog-emu',
		version='1.0.0',
		url='http://goo.gl/lQ3DzE',
		description='Emulates the API of Python\'s built-in syslog module',
		py_modules=['syslog', ],
		package_dir={'': 'lib'},
		classifiers=['Development Status :: 5 - Production/Stable',
			'Environment :: Console',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: MIT License',
			'Operating System :: POSIX',
			'Programming Language :: Python :: 2.6',
			'Programming Language :: Python :: 2.7', ],
		license='MIT License',
	)


# vim: ts=4 sw=4 ai nowrap
