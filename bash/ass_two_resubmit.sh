#!/bin/bash
file="customer.txt"
cat <"$file" | tr -d ,

printf "\n\nId      Name            Address        Mobile\n"
while IFS= read -r line; do
    readarray -d ", " -t row <<<"$line"

    address=$(echo "${row[2]}" | xargs | tr '[:upper:]' '[:lower:]')
    if [ "$address" == "dhanmondi" ]; then
        echo "$line" | tr -d ,
    fi
done <"$file"

#Shihab Uddin Munna - 011183017 - Bacth: 49
