#!/usr/bin/env python3
# Define function to return the multiple values as a dictionary
def dictFunc():
    # Declare a dictionary variable
    dictVar = dict()
    # Assign some values
    dictVar["name"] = "Kelli Ali"
    dictVar["age"] = 46
    dictVar["profession"] = "Singer"
    # Return the dictionary as return values
    return dictVar


# Call the function and store the return values in a dictionary variable
dictValues = dictFunc()
# Print the dictionary values
print("The values of dictionary are:\n", dictValues)
