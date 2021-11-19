#!/bin/bash
read str
read -r -a arr <<<"$(echo $str | sed 's/./& /g')"
length_of_arr=${#arr[@]}
declare -a frequency

for ((i = 0; i < length_of_arr; i++)); do
    count=1
    for ((j = i + 1; j <= length_of_arr; j++)); do
        if [ "${arr[i]}" == "${arr[j]}" ]; then
            ((count++))
            frequency[j]="done"
        fi

        if [ "${frequency[i]}" != "done" ]; then
            if [ "$count" -gt 1 ]; then
                frequency[i]="${arr[i]} - $count times"
            else
                frequency[i]="${arr[i]} - 1 time"
            fi

        fi
    done

done

for element in "${frequency[@]}"; do
    if [ "$element" != "done" ]; then
        echo "$element"
    fi
done

# for ((i = 0; i < length_of_arr; i++)); do
#     t_or_ts="time"

#     if [ "${frequency[i]}" -gt 1 ]; then
#         t_or_ts="times"
#     fi

#     if [ "${frequency[i]}" -ne "$visited" ]; then
#         printf "%s - %d %s\n" "${arr[i]}" "${frequency[i]}" "$t_or_ts"
#     fi

# done

# for ((i = 0; i < length_of_arr; i++)); do
#     t_or_ts="time"

#     if [ "${frequency[i]}" -gt 1 ]; then
#         t_or_ts="times"
#     fi

#     if [ "${frequency[i]}" -ne "$visited" ]; then
#         printf "%s - %d %s\n" "${arr[i]}" "${frequency[i]}" "$t_or_ts"
#     fi

# done
