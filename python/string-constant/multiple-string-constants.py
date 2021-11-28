#!/usr/bin/env python3

# Import string module
import string

# Take any string data
phone = input("Enter your phone number: ")
email = input("Enter your email: ")


# Inilialize error variable
error = False

# Iterate the loop to check the phone number is valid or not
for character in phone:
    if character not in (string.digits + string.punctuation + string.digits):
        error = True


# Iterate the loop to check the email is valid or not
for character in email:
    if character not in (string.ascii_lowercase + string.punctuation + string.number):
        error = True

# Print message based on the value of error
if error == True:
    print("Phone number or email is invalid")
else:
    print("Phone and email are in correct format")
