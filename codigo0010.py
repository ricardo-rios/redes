import urllib.error
from urllib.request import urlopen
from urllib.request import Request



response = urlopen('http://debian.org')

format, params = response.getheader('Content-Type').split(';')
print(params)
charset = params.split('=')[1]
print(charset)

content = response.read().decode(charset)



