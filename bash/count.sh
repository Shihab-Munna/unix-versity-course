#!/bin/bash

read -r -p "Enter the filename: " file
word=$(cat "$file" | wc -w)
char=$(cat "$file" | wc -c)
line=$(cat "$file" | wc -l)
# line=$(grep -c "." "$file")

echo Number of characters in "$file" is "$char"
echo Number of words in "$file" is "$word"
echo Number of lines in "$file" is "$line"
