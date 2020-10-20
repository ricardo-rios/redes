import urllib.error
from urllib.request import urlopen
from urllib.request import Request


req = Request('http://python.org')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')

response = urlopen(req)

print(req.get_header('User-agent'))



