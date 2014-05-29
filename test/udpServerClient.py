import socket

#server
port = 8081
s = socket.socket(AF_INET,socket.SOCK_DGRAM)
s.bind(("",port))
while True:
	data, addr = s.recvfrom(1024)
	
#client

s = socket.socket(AF_INET,socket.SOCK_DGRAM)
s.sendto("some thing"(host,port))
