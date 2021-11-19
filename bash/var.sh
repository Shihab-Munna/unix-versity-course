#!/bin/bash
var1="The Price of bat is $"
var2=50

echo "$var1$var2"

var="BASH"
echo "$var Programming"
# echo '$var Programming'

n=100
echo $n

echo $n+20
((n = n + 20))
echo "Value of n is now = $n"
n=55
echo $n/10 | bc
echo $n/10 | bc -l

str="Learn BASH Programming"

#print string value
echo "$str"

num=120

#subtract 20 from numeric variable
((result = num - 20))

#print numeric value
echo "$result"

num=100

function add() {
    local num=10
    local num2=20

    ((num = num + num2))
    echo "$num"
}

add

echo "$num"

myarr=(HTML JavaScript PHP jQuery AngularJS CodeIgniter)

#count total number of element
total=${#myarr[*]}
echo "The Lenght of myarr =  $total"

echo "values of myarr"

for val in ${myarr[*]}; do
    printf "   %s\n" "$val"
done

for key in ${!myarr[*]}; do
    printf "%4d: %s\n" "$key" "${myarr[$key]}"
done

echo "Array values with key:"
for key in ${!myarr[*]}; do
    printf "%4d: %s\n" "$key" "${myarr[$key]}"
done

declare -A my_array
my_array=([name]=Shihab [sex]=male)
for key in "${!my_array[@]}"; do
    printf "%s = %s\n" "$key" "${my_array[$key]}"
done

declare -A my_array2

# Add single element
my_array2[foo]="bar"
echo "${my_array2[@]}"

#Add multiple elements at a time
my_array2+=([baz]=foobar [foobarbaz]=baz)
echo "${my_array2[@]}"

# echo "${my_array2[@]}"
unset "my_array2[baz]"
echo "${my_array2[@]}"
