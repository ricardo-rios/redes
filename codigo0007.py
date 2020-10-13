import urllib.error
from urllib.request import urlopen
from urllib.request import Request
import gzip

req = Request('http://www.debian.org')


req.add_header('Accept-Encoding', 'gzip')

response = urlopen(req)

# Vemos si el servidor esta usando gzip compresion
# deberia de salir la cadena 'gzip'
print(response.getheader('Content-Encoding'))


content = gzip.decompress(response.read())
content.splitlines()[:5]


