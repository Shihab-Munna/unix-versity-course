#!/usr/bin/env python3

# Import string module
import string

# Take any string data
stringVal = input("Enter any text: ")

# Inilialize error variable
error = False

# Iterate the loop to check any uppercase letter exists or not
for character in stringVal:
    if character not in string.ascii_lowercase:
        error = True

# Print message based on the value of error
if error == True:
    # Print error message
    print("All characters are not in lowercase")
else:
    # Print success message
    print("Text in correct format")
