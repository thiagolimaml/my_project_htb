#!/bin/bash

function def_handler(){
	echo -e "\n[!]Saindo...\n"
	exit 1
}

# Ctrl + C
trap def_handler INT


for ip in $(seq 1 255); do
	timeout 1 bash -c "ping -c 1 172.17.0.$ip" &>/dev/null && echo -e "\n[!]host_up = 172.17.0.$ip\n" &
done; wait
