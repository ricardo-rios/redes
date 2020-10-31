import requests 

response = requests.get('http://www.google.com/notawebpage')
print(response.status_code)

response.raise_for_status()


