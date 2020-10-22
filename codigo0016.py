from urllib.parse import urlparse

result = urlparse('http://www.python.org/dev/peps')

print("El valor de result es {}".format(result))

print("El valor de netloc es {}".format(result.netloc))

print("El valor de path es {}".format(result.path))
