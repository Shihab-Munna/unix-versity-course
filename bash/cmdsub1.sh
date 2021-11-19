#!/bin/bash
# filename='weekday.txt'

# while read -r line; do
#     day=$(echo "$line" | cut -c 1-3)
#     if [ "$day" == "Sun" ]; then
#         echo "Sunday is the holiday"
#     else
#         echo "$day"
#     fi
# done <$filename

# for dirname in $(ls -d */); do
#     echo "$dirname"
# done

# var=`echo \`who\``
# echo "$var"

# output=$(/usr/bin/whoami)
# echo "$output"

# filename=$(basename "$_1")
# echo "The name of the file is $filename"

strval="Microsoft Internet Explorer"

if [[ $strval == *Internet* ]]; then
    echo "Partially Match"
else
    echo "No Match"
fi

if [[ $strval == *internet* ]]; then
    echo "Partially Match"
else
    echo "No Match"
fi

