# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:19:08 2025

@author: Botshelo
"""

import dns
import threading
import time

servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9"]
domain = "example.com"
responses = {}

def query_dns(server):
    start = time.time()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]
    try:
        resolver.resolve(domain)
        responses[server] = time.time() - start
    except:
        responses[server] = float('inf')

threads = [threading.Thread(target=query_dns, args=(server,)) for server in servers]
for t in threads: t.start()
for t in threads: t.join()

fastest = min(responses, key=responses.get)
print(f"Fastest DNS: {fastest}")
