#!/usr/bin/python

import socket

ip = input("Enter IP Address: ")
port = input("Please enter the port: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sock.connect_ex((ip, port)):
	print ("port", port, "port is closed")
else:
	print ("port", port, "port is open")

