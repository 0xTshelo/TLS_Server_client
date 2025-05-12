# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:51:06 2025

@author: Botshelo
"""

import socket
import ssl

from tls_server import HOST as SERVER_HOST
from tls_server import PORT as SERVER_PORT

HOST = "127.0.0.1"
PORT = 60002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client = ssl.wrap_socket("C:/Users/User/Desktop/Uni/PNA/Assignment/server_files/server.crt")

if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep

        client.send("Hello World!".encode("utf-8"))
        sleep(1)
