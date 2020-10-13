import urllib.error
from urllib.request import urlopen
from urllib.request import Request


req = Request('http://python.org')
urlopen(req)
req.get_header('User-agent')





