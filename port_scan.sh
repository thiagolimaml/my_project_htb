#!/bin/bash

function def_handler(){
	echo -e "\n[!]Saindo...\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

declare -a hosts=(172.17.0.1 172.17.0.2 172.17.0.3 172.17.0.4)

for host in ${hosts[@]}; do
	echo -e "Port scan $host\n"
	for port in $(seq 1 10000); do
		timeout 1 bash -c "echo '' > /dev/tcp/$host/$port" 2>/dev/null && echo -e "[!]host: $host = port: $port" &
	done; wait
done
