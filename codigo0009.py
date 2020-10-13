import urllib.error
from urllib.request import urlopen
from urllib.request import Request
import gzip



response = urlopen('http://debian.org')


print(response.getheader('Content-Type')


