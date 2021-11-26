#!/usr/bin/env python3
# Declare a list of numbers
numbers = [5, 10, 11, 15, 25, 30, 46, 45, 50]

# Print message
print('Numbers divisible by 3 and 5:')

# Iterate the list
for n in numbers:

    # Check the condition to run continue statement
    if (n % 3 != 0 or n % 5 != 0):
        continue

    # Print the numbers which are divisible by 3 and 5
    else:
        print(n)
