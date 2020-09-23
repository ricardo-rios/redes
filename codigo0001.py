import sys, urllib.request

try:
    rfc_number = int(sys.argv[1])

except (IndexError, ValueError):
    print('Debes proporcionar un número RFC como primer argumento')
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)

