# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:04:42 2025

@author: Botshelo
"""

import socket
import threading
import os

HOST = "0.0.0.0"
PORT = 443
BUFFER_SIZE = 1024
SAVE_DIR = "server_files"

# Ensure the save directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def handle_client(client_socket):
    try:
        command = client_socket.recv(BUFFER_SIZE).decode()
        if command.startswith("UPLOAD"):
            _, filename = command.split()
            filepath = os.path.join(SAVE_DIR, filename)
            with open(filepath, "wb") as f:
                while True:
                    data = client_socket.recv(BUFFER_SIZE)
                    if not data:
                        break
                    f.write(data)
            print(f"File {filename} received and saved.")
        elif command.startswith("DOWNLOAD"):
            _, filename = command.split()
            filepath = os.path.join(SAVE_DIR, filename)
            if os.path.exists(filepath):
                client_socket.send(b"OK")
                with open(filepath, "rb") as f:
                    while chunk := f.read(BUFFER_SIZE):
                        client_socket.send(chunk)
                print(f"File {filename} sent to client.")
            else:
                client_socket.send(b"ERROR: File not found")
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"[+] Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
