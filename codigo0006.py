import urllib.error
from urllib.request import urlopen
from urllib.request import Request 

req = Request('http://www.debian.org')  

req.add_header('Accept-Language', 'sv')

# Ver los header que he agregado a la peticion.
print(req.header_items()) 

response = urlopen(req)

print(response.readlines())[:5] 

# El metodo urlopen agrega unas cabeceras 
print(req.header_items()) 

# Otra forma de agregar cabeceras
# headers = {'Accept-Language': 'sv'}
# req = Request('http://www.debian.org', headers=headers)



