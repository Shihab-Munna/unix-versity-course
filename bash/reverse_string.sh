#!/bin/bash

# read -r -p "Enter string: " string

# len=${#string}

# for ((i = len - 1; i >= 0; i--)); do
#     # "${string:$i:1}"extract single single character from string.
#     reverse="$reverse${string:$i:1}"
# done

# echo "$reverse"

# awk '{
#     for (i=NF; i>0; i--) {
#           printf "%s ", $i;
#     }
#     printf "\n"
#  }'

read -r str #reading string value

readarray -d " " -t strarr <<<"$str" #split a string based on the

#Print each value of Array with the help of loop
for ((n = 0; n < ${#strarr[*]}; n++)); do
    echo -n " ${strarr[n]}" | rev
done
