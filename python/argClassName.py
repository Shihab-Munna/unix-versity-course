import argparse

# Import sys module
import sys


# Declare function to define command-line arguments
def readOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="The parsing commands lists.")
    parser.add_argument("-n", "--name", help="Type your full name.")
    parser.add_argument("-b", "--batch", help="Type your batch.")
    parser.add_argument("-r", "--result", help="Type your result as cgpa.")
    opts = parser.parse_args(args)
    return opts


# Call the function to read the argument values
options = readOptions(sys.argv[1:])
newName = ''
splited_name = str(options.name).split()
for val in splited_name:
    newName += val.capitalize() + ' '
newName.strip()

print("Student Name: ", newName)
print("Student Batch: ", options.batch)
print("Student Result as CGPA: ", options.result)
