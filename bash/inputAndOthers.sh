#!/bin/bash

# read -p 'Username: ' user
# read -sp 'Password: ' pass

# if (($user == "admin" && $pass == "12345")); then
#     echo -e "\nSuccessful login"
# else
#     echo -e "\nUnsuccessful login"
# fi

# multiple input in a row

# echo "Type four names of your favorite programming languages"
# read -r lan1 lan2 lan3 lan4
# echo "$lan1 is your first choice"
# echo "$lan2 is your second choice"
# echo "$lan3 is your third choice"
# echo "$lan4 is your fourth choice"

# read -r -t 5 -p "Type your favorite color: " color

# echo "$color"
# read -r -p "Enter the mark: " mark
# if (("$mark" >= 90)); then
#     echo "Grade - A+"
# elif (("$mark" < 90 && "$mark" >= 80)); then
#     echo "Grade - A"
# elif (("$mark" < 80 && "$mark" >= 70)); then
#     echo "Grade - B+"
# elif (("$mark" < 70 && "$mark" >= 60)); then
#     echo "Grade - C+"
# else
#     echo "Grade - F"
# fi

# current_date=$(date)
# echo "$current_date"

count_words=$(wc -w fruits.txt)
echo "$count_words"
