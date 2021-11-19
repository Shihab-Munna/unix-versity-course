#!/bin/bash

# read -r first_name
# # arr=$($first_name | sed 's/ //g')

# # echo "${arr[0]}"

# removed_space=${first_name//[[:blank:]]/}
# IFS= read -r -a array <<<"$removed_space"

# echo "${array[1]}"

# # echo "${first_name//[[:blank:]]/}"
# # echo "${arr[0]}"
# # arr=($first_name="$first_name | sed 's/ //g'")

# # for ((i = 0; i < 5; i++)); do
# #     printf "%s, \n" "${arr[i]}"
# # done

# # echo "${arr[*]}"

string="wonkabars"
[[ "$string" =~ ${string//?/(.)} ]] # splits into array
# printf "%s\n" "${BASH_REMATCH[@]:1}"    # loop free: reuse fmtstr
declare -a arr=("${BASH_REMATCH[@]:1}") # copy array for later

echo "${arr[*]}"
