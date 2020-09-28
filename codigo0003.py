from urllib.request import urlopen

response = urlopen('https://www.ues.edu.sv')

print(response)

print(response.readline())
