# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:44:13 2025

@author: Botshelo
"""
import dns.resolver
import time

cache = {}  # Dictionary to store cached DNS results

def cached_resolve(domain):
    # Check if the domain is already cached and not expired (5 minutes = 300 seconds)
    if domain in cache and time.time() - cache[domain][1] < 300:
        print("Returning cached result")
        return cache[domain][0]

    try:
        # Perform DNS resolution
        answer = dns.resolver.resolve(domain, "A")
        result = [rdata.to_text() for rdata in answer]  # Convert response to text format
        cache[domain] = (result, time.time())  # Store result with timestamp
        return result
    except Exception as e:
        return f"DNS resolution failed: {e}"

# Test the function
print(cached_resolve("fun.com"))  # First request - should query DNS
time.sleep(2)
print(cached_resolve("fun.com"))  # Second request - should use cache

