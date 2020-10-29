from http.cookiejar import CookieJar
cookie_jar = CookieJar()

from urllib.request import build_opener, HTTPCookieProcessor
opener = build_opener(HTTPCookieProcessor(cookie_jar))

opener.open('https://www.ues.edu.sv')

cookies = list(cookie_jar)

print(cookies)

print(cookies[0].name)
print(cookies[0].value)

print(cookies[0].domain)
print(cookies[0].path)
print(cookies[0].expires)


import datetime
print(datetime.datetime.fromtimestamp(cookies[0].expires))

print(cookies[0].get_nonstandard_attr('HttpOnly'))

print(cookies[0].secure)

