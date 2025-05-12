# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:33:23 2025

@author: Botshelo
"""

import dns.resolver
import itertools

servers = itertools.cycle(["8.8.8.8", "1.1.1.1", "9.9.9.9"])
resolver = dns.resolver.Resolver()

while True:
    resolver.nameservers = [next(servers)]
    print(f"Querying with {resolver.nameservers[0]}")
    try:
        answer = resolver.resolve("fun.com", "A")
        for rdata in answer:
            print(f"Resolved: {rdata}")
    except Exception as e:
        print(f"DNS resolution failed: {e}")
