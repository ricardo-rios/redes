import requests 

response = requests.get('http://www.github.com')
print(response.cookies)
