#!/bin/bash

function def_handler(){
	echo -e "\n\nSaindo...\n\n"
	exit 1
}

trap def_handler INT

declare -a hosts=(172.17.0.1 172.17.0.2 172.17.0.3 172.17.0.4)

for host in ${hosts[@]}; do
	echo -e "\n[+]PortScan $host:\n"
	for port in $(seq 1 1000); do
		timeout 1 bash -c "echo '' > /dev/tcp/$host/$port" 2>/dev/null && echo -e "\t[+]Port $port - OPEN"
done; wait
done
