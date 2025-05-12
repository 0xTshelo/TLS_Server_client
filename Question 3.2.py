# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:20:04 2025

@author: Botshelo
"""

import socket
import os

SERVER_HOST = "127.0.0.1"  # Change this to the server's IP if needed
SERVER_PORT = 443
BUFFER_SIZE = 1024

def upload_file(filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((SERVER_HOST, SERVER_PORT))
            client.sendall(f"UPLOAD {filename}".encode())
            
            with open(filename, "rb") as f:
                while chunk := f.read(BUFFER_SIZE):
                    client.sendall(chunk)
            print(f"File {filename} uploaded successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file(filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((SERVER_HOST, SERVER_PORT))
            client.sendall(f"DOWNLOAD {filename}".encode())
            
            response = client.recv(BUFFER_SIZE)
            if response.startswith(b"OK"):
                with open(filename, "wb") as f:
                    while True:
                        data = client.recv(BUFFER_SIZE)
                        if not data:
                            break
                        f.write(data)
                print(f"File {filename} downloaded successfully.")
            else:
                print("Error: File not found on server.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    action = input("Enter action (upload/download): ").strip().lower()
    filename = input("Enter filename: ").strip()
    
    if action == "upload":
        upload_file(filename)
    elif action == "download":
        download_file(filename)
    else:
        print("Invalid action. Use 'upload' or 'download'.")
