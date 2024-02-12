#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a identificação
  de sistemas operacionais usando a
  biblioteca 'scapy'
"""

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

if len(sys.argv) != 2:
    print ("Use - ./ttl_id.py [IP Address]")
    print ("Exemplo - ./ttl_id.py 10.0.0.5")
    print ("Esse exemplo realizará uma análise de TTL para tentar determinar se o sistema é o Windows ou Linux/Unix")
    sys.exit()

ip = sys.argv[1]
ans = sr1(IP(dst=str(ip))/ICMP(),timeout=1,verbose=0)

if ans == None:
    print ("Nenhuma resposta foi retornada")
elif int(ans[IP].ttl) <= 64:
    print ("O Host é Linux/Unix")
else:
    print ("O Host é Windows")
