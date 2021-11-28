#!/usr/bin/env python3

# Define the class to intialize the object
class Employees:
    def __init__(self):
        self.name = "Mosarof Karim"
        self.post = "Manager"
        self.salary = 50000


# Define the function to return values as an object
def objFunc():
    return Employees()


# Call the function to set the object variable
objVar = objFunc()

# Print the formatted output
print(
    "\n Employee Name:",
    objVar.name,
    "\n",
    "Post:",
    objVar.post,
    "\n",
    "Salary:",
    objVar.salary,
)
