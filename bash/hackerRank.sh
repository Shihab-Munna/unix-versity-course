#!/bin/bash

# count=0
# sum=0
# while IFS= read -r LINE || [[ -n "$LINE" ]]; do
#     ((count++))
#     sum=$(echo "$sum" + "$LINE" | bc)
#     echo "---- $sum"
# done

# echo "scale=3; $sum / $count" | bc

# read -r temp

# count=0
# sum=0

# for ((i = 0; i < temp; i++)); do
#     read -r num
#     ((count++))
#     sum=$(echo "$sum" + "$num" | bc)
# done

# echo "scale=3; $sum / $count" | bc

readarray -t arr
echo "${arr[*]}"
