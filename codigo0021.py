from urllib.parse import quote
from urllib.parse import urlencode
from urllib.parse import urlunparse

print(quote('A duck?'))

path = 'pypi'

path_enc = quote(path)

query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}

query_enc = urlencode(query_dict)


netloc = 'pypi.python.org'

print(urlunparse(('http', netloc, path_enc, '', query_enc, '')))
