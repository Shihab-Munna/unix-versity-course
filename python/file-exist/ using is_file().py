#!/usr/bin/env python3
from pathlib import Path

# Take a filename
fn = input("Enter a filename to read:\n")

if Path(fn).is_file():
    # print the message if file path exists
    print("\nFile exist")
    print("The content of the file shown below:")
    # Open the file for reading
    fh = open(fn)
    # Print the file content
    print(fh.read())
else:
    # Print the message if the file path does not exist
    print("File does not exist")
