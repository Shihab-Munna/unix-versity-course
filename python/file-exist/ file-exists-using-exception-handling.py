#!/usr/bin/env python3
# Take a filename
fn = input("Enter a filename to read:\n")
try:
    # Open the file for reading
    fileHandler = open(fn)
    # Print the following message if no exception occurs
    print("File exists")
    # close the file
    fileHandler.close()
except FileNotFoundError:
    # Print the following message if any error occurs
    print("File is not exist or accessible")
finally:
    # print the termination message
    print("End of the program! Thank You")
