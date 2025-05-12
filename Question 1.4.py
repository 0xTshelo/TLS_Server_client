# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 19:17:18 2025
@author: Botshelo
"""
import socket
import ssl
import certifi
import os
# Create a place holder to consolidate SSL settings
# i.e., Create an SSLContext
contextInstance                 = ssl.SSLContext();
contextInstance.verify_mode     = ssl.CERT_REQUIRED;
# Load the CA certificates used for validating the peer's certificate
contextInstance.load_verify_locations(cafile=os.path.relpath(certifi.where()),
capath=None,
cadata=None);
# Create a client socket
socketInstance = socket.socket();

# Get an instance of SSLSocket
sslSocketInstance  = contextInstance.wrap_socket(socketInstance);
print(type(sslSocketInstance));
# Connect to a server
sslSocketInstance.connect(("www.eduvos.com", 443));
print("Version of the SSL Protocol:%s"%sslSocketInstance.version());
print("Cipher used:");
print(sslSocketInstance.cipher());
