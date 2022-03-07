#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

for port in $(seq 1 65535); do
	timeout 1 bash -c " echo '' > /dev/tcp/192.168.0.1/$port" 2>/dev/null && echo -e "PortUP = 192.168.0.1:$port\n"
done; wait
