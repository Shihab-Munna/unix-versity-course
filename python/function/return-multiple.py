#!/usr/bin/env python3

# Define function to return multiple variables
def multiVarFunc():
    # Take a string data
    dept = input("Enter department name: ")
    # Take a numeric data
    stdnum = int(input("Enter the number of total students: "))
    # Take a numeric data
    facnum = int(input("Enter the number of total faculties: "))
    # Return multiple variables
    return dept, stdnum, facnum


# Call the function and store the return values in three variables
dept_name, total_std, total_fac = multiVarFunc()
# Print the formatted output of the return values
print(
    "\nDepartment:%s\nTotal students:%d\nTotal faculties:%d"
    % (dept_name, total_std, total_fac)
)
