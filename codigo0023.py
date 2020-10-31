from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode


data_dict = {'P': 'Python'}

data = urlencode(data_dict).encode('utf-8')

req = Request('http://search.debian.org/cgi-bin/omega',
data=data)

req.add_header('Content-Type', 'application/x-www-form-urlencode;charset=UTF-8')

response = urlopen(req)

print(response.read())

# We can write the response with the following code. 
# We must comment the above line of code. 
#html_file = open("search.html", "wb")
#html_file.write(response.read())
#html_file.close()
