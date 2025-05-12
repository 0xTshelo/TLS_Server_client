# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:42:33 2025

@author: User
"""

import socket
import threading

# Server settings
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
clients = []

# Function to handle each client
def handle_client(client_socket, client_address):
    while True:
        try:
            # Receive message from client
            msgFromClient, clientAddr = client_socket.recvfrom(bufferSize)
            print(f"Message from {clientAddr}: {msgFromClient.decode()}")
            
            # Broadcast message to all connected clients
            for client in clients:
                if client != client_socket:
                    client.sendto(msgFromClient, client_address)
        except:
            # Remove client from list if they disconnect
            clients.remove(client_socket)
            client_socket.close()
            break

# Create UDP socket at server side
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind(serverAddressPort)
print("Server listening on port 20001")

while True:
    # Receive connection request from a new client
    msgFromClient, clientAddress = UDPServerSocket.recvfrom(bufferSize)
    print(f"Received message from {clientAddress}: {msgFromClient.decode()}")
    
    # Add the client to the list
    clients.append(UDPServerSocket)
    
    # Start a new thread to handle the client
    threading.Thread(target=handle_client, args=(UDPServerSocket, clientAddress)).start()
