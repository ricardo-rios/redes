import requests 

s = requests.Session()

s.get('http://www.google.com')

response = s.get('http://www.google.com/preferences')

response = requests.head('http://www.google.com')
print(response.status_code)
print(response.text) 

headers = {'User-Agent': 'Mozilla/5.0 Firefox 24'}
response = requests.get('http://www.debian.org', headers=headers) 


# Making requests with query string. 

params = {':action': 'search', 'term': 'Are you quite sure this is a chesse pop?'} 

response = requests.get('http://pypi.python.org/pypi', params=params)

print(response.url)

# Posting 

data = {'P': 'Python'}

response = requests.post('http://search.debian.org/cgi-bin/omega', data=data)


