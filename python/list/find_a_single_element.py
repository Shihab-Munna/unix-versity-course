#!/usr/bin/env python3
# Define a list of flowers
flowerList = ['rose', 'daffodil', 'sunflower', 'poppy', 'bluebell']

# Take the name of the flower that you want to search in the list
flowerName = input("Enter a flower name:")

# Search the element using 'in' operator
if flowerName.lower() in flowerList:

    # Print success message
    print("%s is found in the list" % (flowerName))
else:

    # Print not found message
    print("%s is not found in the list" % (flowerName))
