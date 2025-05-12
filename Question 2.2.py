# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:33:04 2025

@author: Botshelo
"""

import dns.resolver

resolver = dns.resolver.Resolver()
resolver.use_dnssec = True
resolver.resolve("fun.com", "A")
