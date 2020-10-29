from urllib.request import Request
from urllib.request import urlopen


req = Request('http://www.google.com', method='HEAD')

response = urlopen(req)

print(response.status)

print(response.read())


