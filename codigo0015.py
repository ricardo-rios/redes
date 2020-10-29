import urllib.error
from urllib.request import urlopen
from urllib.request import Request


req = Request('http://www.ues.edu.sv')
response = urlopen(req)

print(response.url)

print(req.redirect_dict)




