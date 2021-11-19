#!/bin/bash
file="customer.txt"
cat "$file"

printf "\n\nId Name Address Mobile\n"
while IFS= read -r line; do
    readarray -d " " -t row <<<"$line"
    if [ "${row[2]^}" == "Dhanmondi" ]; then
        echo "$line"
    fi
done <"$file"
