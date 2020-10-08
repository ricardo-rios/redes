import urllib.error
from urllib.request import urlopen
from urllib.request import Request 

req = Request('http://www.debian.org')  

req.add_header('Accept-Language', 'sv')

response = urlopen(req)

print(response.readlines()) 

