import urllib.error
from urllib.request import urlopen
from urllib.request import Request


req = Request('http://gmail.com')
response = urlopen(req)

print(response.url)

print(req.redirect_dict)




