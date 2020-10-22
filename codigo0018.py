from urllib.parse import urljoin


print(urljoin('http://www.debian.org', 'intro/about'))


print(urljoin('http://www.debian.org/intro/', 'about'))


print(urljoin('http://www.debian.org/intro', 'about'))
