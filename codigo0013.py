from http.cookiejar import CookieJar
cookie_jar = CookieJar()

from urllib.request import build_opener, HTTPCookieProcessor
opener = build_opener(HTTPCookieProcessor(cookie_jar))

opener.open('https://www.ues.edu.sv')

print(len(cookie_jar))




