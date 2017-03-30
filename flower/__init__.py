from __future__ import absolute_import

dev1 = 'dev1'
VERSION = (1, 0, 0, dev1)
__version__ = '.'.join(map(str, VERSION)) + '-' + dev1
