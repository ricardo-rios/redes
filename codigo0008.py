import urllib.error
from urllib.request import urlopen
from urllib.request import Request
import gzip

req = Request('http://www.debian.org')


req.add_header('Accept-Encoding', 'identity')

response = urlopen(req)

print(response.getheader('Content-Encoding'))
