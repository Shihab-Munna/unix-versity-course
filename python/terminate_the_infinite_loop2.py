#!/usr/bin/env python3
# Declare a list of languages
languages = ['Bash', 'PHP', 'Java', 'Python', 'C#', 'C++']

# Print the list until the break statement is executed
print('List of different languages:')

# Iterate the list
for lang_name in languages:

    # Print the current list item
    print(lang_name)

    # Check the condition to exit from the loop
    if (lang_name == 'Python'):
        break

# Print the loop termination message
print('Terminated from the loop')
