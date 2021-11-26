#!/usr/bin/env python3
# Define a list of persons
persons = ['Sophia', 'Isabella', 'Olivia', 'Alexzendra', 'Bella']

# Initialize thecounter
counter = 0
# Iterate the list using loop
for name in persons:
    # Check the length of the element
    if (len(name) >= 7):
        # Increment counter by one
        counter = counter + 1

# Check the counter value
if (counter > 0):
    print("%d person(s) name length is/are more than 7." % counter)
else:
    print("The name length of all persons are less than 7.")
