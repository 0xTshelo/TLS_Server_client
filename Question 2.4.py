# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:43:08 2025

@author: Botshelo
"""

import requests

url = "https://cloudflare-dns.com/dns-query"
headers = {"accept": "application/dns-json"}
params = {"name": "fun.com", "type": "A"}

response = requests.get(url, headers=headers, params=params)
print(response.json())
