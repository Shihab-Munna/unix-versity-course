#!/usr/bin/env python3
# Define the dictionary of 5 persons
persons = {'Mr. Micheal': 'Present', 'Mr. Robin': 'Absent', 'Mrs. Ella': 'Absent',
           'Miss Lara': 'Present', 'Mr. Hossain': 'Present'}

# Print message
print('The following persons are present in the meeting:')

# Iterate the dictionary
for name in persons:
    # Check the condition to run continue statement
    if (persons[name] == 'Absent'):
        continue
    # Print the name of the person
    else:
        print(name)
