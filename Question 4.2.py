# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:34:03 2025

@author: Botshelo
"""

import socket

# Server details
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    # Get input from user to send to the server
    msgFromClient = input("Enter message to send to server: ")
    
    # Convert the message to bytes
    bytesToSend = str.encode(msgFromClient)
    
    # Send message to server
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
    # Receive response from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
    # Print the message from the server
    print(f"Message from Server: {msgFromServer[0].decode()}")
    
    # If the user enters 'exit', terminate the loop
    if msgFromClient.lower() == "exit":
        print("Exiting client...")
        break

# Close the socket
UDPClientSocket.close()
