#!/usr/bin/env python
import sys
from socket import *
serverhost = 'localhost'
serverport = 4411
message = [b'hello world']
if len(sys.argv)>1:
    serverhost = sys.argv[1]
    if len(sys.argv)>2:
        message = (x.encode() for x in sys.argv[2:])
sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.connect((serverhost,serverport))
for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print 'client received:',data
sockobj.close()
