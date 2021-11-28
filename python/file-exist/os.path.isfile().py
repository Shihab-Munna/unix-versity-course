#!/usr/bin/env python3
# Import os module
import os

# Take a filename
fn = input("Enter a filename to read:\n")
# Check the file exist or not
if os.path.isfile(fn):
    # print the message if file exists
    print("File exists")
else:
    # Print the message if the file does not exist
    print("File does not exist")
