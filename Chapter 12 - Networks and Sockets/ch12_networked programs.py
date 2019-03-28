print('chapter 12 Networked programs')
print('***********part 1***********')
print('1. transport control protocol (TCP)')
# buit on top of IP (internet protocol)
# assume IP may lose some data stores and retransmits data if it seems to be lost
# handle "flow control" using a transmit window
# provide a nice reliable "pipe"
# application A->transpotation A->pipe ->transpotation B ->application B
print('#####################################################')
print('2. PCP connections/sockets')
# In computer networking, an internet socket or network socket is a endpoint of a bidirectional 'inter-process'
# communication flow across an 'internet' Protocol-based computer network, such as the 'Internet'
print('#####################################################')
print('3. TCP port numbers')
# A port is an application-specific or process-specific software communications endpoint
# It allows multiple networked applications to co-exit in the same server
# see as telephone number extension
print(' you got a hostname/number -> connect to IP port ->connect to applications')
print('3.1 common TCP ports')
print('Telnet(23) - Login\nSSH(22) - Secure Login\nHTTP(80)\nHTTP(443) - Secure\n'
      'SMTP(25) - Mail\nIMAP(143/220/993) - Mail Retrieval\nDNS(53) - Domain Name\nFTP(21) - File Transfer', sep=" ")
print('#####################################################')
print('4. socket in Python')
print('Python has built-in support for TCP sockets')
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # it creates this endpoint that's inside your computer that's ready to connect out to
# # the far end, but it's not yet connected
# mysock.connect(('data.py4e.org', 80))
# # The actual connection happens when we say mysock.connect
print('#####################################################')
print('***********part 2***********')
print('5 HTTP Hypertetxt Tansfer Protocol')
# application protocols: include mail, world Wide Web
print('HTTP:\nthe dominant application layer protocol on the internet\nincented for the web - to Retrieve HTML, '
      'Images, Documents, etc\nExtended to be the data in addition to documents - RSS, Web Services, etc..\nBasic concept'
      ' - make connection - request a document - retrieve the document -colse the connection ', sep="")
print('"HTTP": the HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents'
      'from servers over the Internet')
print('#####################################################')
print('6. get data from the server')
# 'GET http://data.pr4e.org/romeo.txt'
print('7. an HTTP request in Python ')
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#\r\n表示回车+换行, encode converts from unicode to UTF-8 interally
mysock.send(cmd)

while True:
    data = mysock.recv(512) #recieve up to 512 characters
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
#  you will get:
# HTTP header as follows (metedata):

# HTTP/1.1 200 OK
# Date: Thu, 28 Mar 2019 07:06:09 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# HTTP body as follows:

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief
print('#####################################################')
print('***********part 3***********')

print('8. Using the Developer Console to Explore HTTP')
# use chrome: view - developer - Javascript - "network": can see header, response
