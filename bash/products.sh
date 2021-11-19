#!/bin/bash
read -r -p "Enter the product price: " price
read -r -p "Enter the quantity: " items

if (("$items" == 5)); then
    subTotal=$((price * items))
    discount=$(echo "scale = 2; (subTotal * 10) / 100" | bc)
    echo "Price: $price - Items: $items"
    echo "Total Price: $subTotal"
    echo "Total Price After 10% discount: $((subTotal - discount))"

elif (("$items" == 7)); then
    subTotal=$((price * items))
    discount=$((subTotal * 15 / 100))
    echo "Price: $price - Items: $items"
    echo "$discount"
    echo "Total Price: $subTotal"
    printf "Total Price After 15%% discount: %2f" $((subTotal - discount))

elif (("$items" == 10)); then
    subTotal=$((price * items))
    discount=$((subTotal * 20 / 100))
    echo "Price: $price - Items: $items"
    echo "Total Price: $subTotal"
    echo "Total Price After 20% discount: $((subTotal - discount))"

fi
