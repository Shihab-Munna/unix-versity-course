#!/bin/bash

echo " >>>>>> Bash Case Example <<<<<<<"

# read -r -p "Enter Your Name: " name

# case $name in
# Shihab)
#     echo "Your favorite color is black"
#     ;;
# Luna)
#     echo "Your favorite drink is nimbupani"
#     ;;
# *)
#     echo "No entry Found"
#     ;;
# esac

read -r -p "Enter a number here:  " num

mod=$(("$num" % 2))

case $mod in
0)
    echo "$num is even"
    ;;
*)
    echo "$num is odd"
    ;;
esac



