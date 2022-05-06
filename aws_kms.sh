#!/bin/bash

declare -a algorithms=(SYMMTRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256)

for algorithm in ${algorithms[@]}; do
	aws --endpoint-url="http://127.0.0.1:4566" kms list-keys | grep KeyId | awk 'NF{print $NF}' | tr -d '"' | tr -d ',' | while read key_id; do
		echo -e "\n[+] Provando com key_id: $key_id o algoritmo $algorithm"
		aws --endpoint-url="http://127.0.0.1:4566" kms decrypt --ciphertext-blob fileb:///home/david/Projects/Prod_Deployment/servers.enc --key-id "$key_id" --encryption-algorithm $algorithm
	done
done
