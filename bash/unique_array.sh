#!/bin/bash

fruits=(apple banana apple guava mango dragon dragon apple mango banana)

declare -A unique_array

for fruit in "${fruits[@]}"; do
    unique_array["$fruit"]=1
done

printf '%s\n' "${!unique_array[@]}" | sort
