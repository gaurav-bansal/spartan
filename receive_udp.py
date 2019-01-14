import socket

#udp_ip = "192.168.137.49"
udp_ip = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

while True:
	data, addr = sock.recvfrom(1024)
	print data
	print addr

