#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

for ip in $(seq 1 254); do
	timeout 1 bash -c "ping -c 1 192.168.0.$ip" &>/dev/null && echo -e "HostUP = 192.168.0.$ip\n"
done; wait
