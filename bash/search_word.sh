#!/bin/bash

read -r -p "Enter the search string: " str
fileName="fruits.txt"
count=$(grep -o -i "$str" "$fileName" | wc -l)

echo "$str occurs $count times in $fileName"
