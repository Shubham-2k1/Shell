#!/bin/python3

import socket #To run socket commands
from datetime import datetime #To import sysdate and time for banner

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating object named 'S' taking IPv4 and TCP

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #To stop client from putting script into cooldown after EXIT

s.bind(("127.0.0.1",8888)) #Sending SYN Request for connection

print("Listening....")
print("-"*50)

s.listen(1)
client,addr = s.accept() #To complete 3 way TCP handshake 

print("Connected on: "+str(datetime.now()))
print("-"*50)

while True: 
	cmd = input("$ ") #Taking command input
	client.send(cmd.encode()) #Sending command to client machine in byte format 
	if cmd=="exit":
		break
	output=(client.recv(1024)).decode() #Receiving the output from client in 1024 byte size and decoding those byte to human readable output
	print(output)

client.close() #Closing connection
s.close()   #Closing Socket
