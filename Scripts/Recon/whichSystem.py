#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess

# phython3 whichSystem.py 10.10.10.188

if len(sys.argv) != 2:
  print("\n[!] Uso: python3 " + sys.argv[0] + " <DIR_IP>\n")
  sys.exit(1)
  
def get_ttl(ip_address):
  proc = subprocess.Popen
