#!/bin/bash

read -r -p "Enter id - name - subject - mark: " id name sub mark

if (("$mark" >= 90)); then
    echo "Id: $id, Name: $name, Grade: A+"
elif (("$mark" < 90 && "$mark" >= 80)); then
    echo "Id: $id, Name: $name, Grade: A-"
elif (("$mark" < 80 && "$mark" >= 70)); then
    echo "Id: $id, Name: $name, Grade: B+"
elif (("$mark" < 70 && "$mark" >= 60)); then
    echo "Id: $id, Name: $name, Grade: C+"
else
    echo "Id: $id, Name: $name, Grade: F"
fi
