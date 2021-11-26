#!/usr/bin/env python3
# Define a list of food
food = ['pizza', 'cake', 'strawberry', 'chocolate', 'chicken fry', 'mango']
# Take a food name from the user
search = input('Type your favorite food : ')


# Define the custom function to find element in the list
def findElement(listName, searchElement):
    # Read the list using loop
    for value in listName:
        # Check the element value is equal to the search value or not
        if value == searchElement:
            return True

        # Return false if no match found
        return False


# Call the function with the list name and search value
if findElement(food, search.lower()):
    print("%s is found" % search)
else:
    print("%s is not found" % search)
