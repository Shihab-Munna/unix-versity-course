#!/usr/bin/env python3
# Import os module
import os

# Take a filename
fn = input("Enter a filename to read:\n")
# Check the file path exist or not
if os.path.exists(fn):
    # print the message if path exists
    print("File exists")
else:
    # Print the message if the file path does not exist
    print("File does not exist")
