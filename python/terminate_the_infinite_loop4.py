#!/usr/bin/env python3
# Define the list to store the names of the first three persons
topList = ['', '', '']

# Set the counter value to terminate the loop
counter = 0

# Define the dictionary of six elements
meritList = {'Mohammed': 1, 'Mila Rahman': 5, 'Shakib Al Hasan': 3, 'Brian Lara': 6,
             'Sachin Tendulkar': 2, 'Alif Hossain': 4}

# Iterate the values of the dictionary to retrieve the names of first three merit persons
for student_name in meritList:

    # Read the merit position
    merit_pos = meritList[student_name]

    # Store the index value in the list if the position is within 1 to 3 and counter by 1
    if (merit_pos < 4):
        topList[merit_pos - 1] = student_name
        counter = counter + 1

    # Terminate from the loop if the counter value is 3
    if (counter == 3):
        break

# Read and print the values of the list based on the position
for n in range(0, 3):
    print("%s is in the position %s" % (topList[n], n + 1))
