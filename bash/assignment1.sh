#!/bin/bash

read y

x=$(echo $y | sed -f <(printf 's/%s//2g\n' {a..z}) <<<"$y" | tr -d ' ')

echo "$x"

for ((i = 0; i < ${#x}; i++)); do
    c2=${x:$i:1}
    echo "c2 = $c2"
    c1=$(echo $y | tr -cd $c2 | wc -c)
    echo "c1 = $c1"
    if [[ $c1 -gt 1 ]]; then
        echo "$c2 - $c1 times"
    else
        echo "$c2 - $c1 time"
    fi

done
