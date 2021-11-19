# myString = 'welcome to LinuxHint'
#
# # Convert the string by capitalize method
# convertedString = myString.capitalize()
#
# # Print the original string
# print('The first original string is : %s' % myString)
#
# # Print the converted string
# print('The first converted string is : %s\n' % convertedString)
#
# # Define a string with all capital letter
# myString2 = 'I LIKE PYTHON PROGRAMMING'
#
# # Convert the string by capitalize method
# convertedString2 = myString2.capitalize()
#
# # Print the original string
# print('The second original string is : %s' % myString2)
#
# # Print the converted string
# print('The second converted string is : %s\n' % convertedString2)
#
# # Define a string starting with number
# myString3 = '7827 Ridgeview Court Summerville, SC 29483'
#
# # Convert the string by capitalize method
# convertedString3 = myString3.capitalize()
#
# # Print the original string
# print('The third original string is : %s' % myString3)
#
# # Print the converted string
# print('The third converted string is : %s\n' % convertedString3)
#
# text = input("Enter a text\n")
#
# # Split the text based on space
# strList = text.split()
#
# # Define a variable to store the converted string
# newString = ''
#
# # Iterate the list
# for val in strList:
#     # Capitalize each list item and merge
#     newString += val.capitalize() + ' '
#
# # Print the original string
# print('The original string is : %s' % text)
#
# # Print the converted string
# print('The converted string is : %s\n' % newString)


# Define a long text
text = 'python is an interpreted, high-level, general-purpose programming language. created by Guido van Rossum.it is first released in 1991.'

# Split the text based on space
lineList = text.split('.')

# Define a variable to store the converted string
newText = ''

# Iterate the list
for val in lineList:
    # Remove space from starting and ending
    val = val.strip()

    # Capitalize each list item and merge with '.'
    newText += val.capitalize() + '. '

# Remove the last dot
newText = newText[:-2]

# Print the original string
print('The original text is : \n%s' % text)

# Print the converted string
print('\nThe converted text is : \n%s' % newText)
