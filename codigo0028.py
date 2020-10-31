import requests 

r = requests.get('http://www.google.com')

print(r.status_code)

print(r.raise_for_status())

r = requests.get('http://192.0.2.1') 
