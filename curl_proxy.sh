#!/bin/bash

function def_handler(){
	echo -e "\n\nSaindo...\n"
	exit 1
}

trap def_handler INT

for port in $(seq 1 65535); do curl -s http://127.0.0.1:$port -U kalamari:ihateseafood -x http://10.10.10.21:3128 | grep -q "Stylesheet for Squid Error pages" || echo -e "\nPort open = $port\n"; done
