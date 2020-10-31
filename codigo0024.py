import requests 

response = requests.get('http://www.debian.org')

print(response.status_code) 

print(response.reason)

print(response.url)

print(response.headers['content-type'])

print(response.ok)

print(response.is_redirect)

print(response.request.headers)

print(response.headers['content-encoding'])

#print(response.content)

#print(response.text)

print(response.encoding)

