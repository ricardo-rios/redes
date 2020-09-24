
import ssl
import socket

#rfc_number = 2324
#template = "GET /rfc/rfc{}.txt HTTP/1.1\r\nHost: www.ietf.org\r\nConnection: close\r\n\r\n" 
template = "GET /ricardoues/finding_donors HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n" 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('github.com', 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
#s.sendall(template.format(rfc_number).encode('ascii'))
s.sendall(template.encode('ascii'))

rfc_raw = bytearray()

while True:

    new = s.recv(4096)
    if not new:
      s.close()
      break
    rfc_raw += new	
    
rfc = rfc_raw.decode('utf-8')
print(rfc)   
 
