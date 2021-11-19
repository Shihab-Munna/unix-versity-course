#!/bin/bash

read -r price

while IFS= read -r id name balance; do
    echo "??? ${id} ${name} ${balance}"

    # ((i++))
    if [[ ! $balance > $price ]]; then
        echo "${id} ${name} ${balance}"
    fi
done <products.txt
