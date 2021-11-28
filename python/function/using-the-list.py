#!/usr/bin/env python3

# Define function to return multiple values as a list
def listFunc():
    # Take a numeric data
    number1 = float(input("Enter any number:"))
    # Take a numeric data
    number2 = float(input("Enter any number:"))

    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    division = number1 / number2

    # Return multiple variables as a list
    return [number1, number2, addition, subtraction, multiplication, division]


# Call the function and store the return values in a tuple
listVar = listFunc()
# Print the formatted output of the list data
print("\n%5.2f + %5.2f = %5.2f" % (listVar[0], listVar[1], listVar[2]))
print("%5.2f - %5.2f = %5.2f" % (listVar[0], listVar[1], listVar[3]))
print("%5.2f x %5.2f = %5.2f" % (listVar[0], listVar[1], listVar[4]))
print("%5.2f / %5.2f = %5.2f" % (listVar[0], listVar[1], listVar[5]))
