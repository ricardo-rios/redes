from urllib.parse import urlparse
from urllib.parse import parse_qs

result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')

print(parse_qs(result.query))
