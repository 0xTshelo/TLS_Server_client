# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:49:42 2025

@author: Botshelo
"""
import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='C:/Users/User/Desktop/Uni/PNA/Assignment/server_files/server.crt', keyfile='C:/Users/User/Desktop/Uni/PNA/Assignment/server_files/server.crt')

HOST = "127.0.0.1"
PORT = 60000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server = ssl.wrap_socket(
    server, server_side=True, keyfile="C:/Users/User/Desktop/Uni/PNA/Assignment/server_files/server.crt", certfile="C:/Users/User/Desktop/Uni/PNA/Assignment/server_files/server.crt"
)

if __name__ == "__main__":
    server.bind((HOST, PORT))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
