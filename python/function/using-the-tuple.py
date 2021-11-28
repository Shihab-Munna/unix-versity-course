#!/usr/bin/env python3

# Define function to return multiple variables
def tupleFunc():
    # Take a string data
    stdID = input("Enter the student Id:")
    # Take a string data
    stdName = input("Enter the student name: ")
    # Take a integer data
    stdBatch = int(input("Enter the batch No: "))
    # Take a float data
    stdCGPA = float(input("Enter the CGPA: "))
    # Return multiple variables as a tuple
    return (stdID, stdName, stdBatch, stdCGPA)


# Call the function and store the return values in a tuple
tupleVar = tupleFunc()
# Print the formatted output of the tuple
print(
    "\n ID:%s\n Name:%s\n Batch:%d\n CGPA:%4.2f"
    % (tupleVar[0], tupleVar[1], tupleVar[2], tupleVar[3])
)
