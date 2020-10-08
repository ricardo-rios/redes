import urllib.error
from urllib.request import urlopen


response = urlopen('http://www.debian.org')
print(response.getheaders())

