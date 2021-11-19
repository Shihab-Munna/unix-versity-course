# #!/usr/bin/env python3
# # Define to string values
# str1 = "I like "
# str2 = "Programming"
#
# # Combining a string value with another string value
# combineText1 = str1 + str2
#
# # Print the combined output
# print("Combining string with string:\n", combineText1)
#
# # Define a string value
# text = "The price of the book is "
#
# # Define a number value
# price = 50
#
# # Combining a string value with a number value
# combineText2 = text + "$" + str(price)
#
# # Print the combined output
# print("\nCombining string with number:\n", combineText2)
#
# """
#     String Concatenation using ‘%’ operator
# """
#
# str1 = "Python"
# str2 = "is a popular scripting language"
#
# # Combine the string values using '%' operator
# print("The output after combining strings:\n\n%s %s" % (str1, str2))

"""
    String Concatenation using format() method
"""
str1 = input("Enter the first string value\n")
str2 = input("Enter the second string value\n")

# Combine the string values using format() operator
combineText = "{} {}".format(str1, str2)

# Print the combined text
print("The output after combining strings:\n\n", combineText)

"""
    String Concatenation using join() method
"""

str1 = "Python Programming"
str2 = "Bash Programming"
str3 = "Java Programming"

combineText = "".join([str1, str2, str3])
# Print the output
print("\nOutput:\n%s" % combineText)

# Using join() method with comma to combine the strings
combineText = ",".join([str1, str2, str3])

# Print the output
print("\nOutput:\n%s" % combineText)

# Using join() method with newline to combine the strings
combineText = "\n".join([str1, str2, str3])

# Print the output
print("\nOutput:\n%s" % combineText)

"""
    Combining the string of tuple using join() method
"""
tupleString = ("Ubuntu", "Windows", "MacOS", "Fedora", "Android", "RedHat")

# Combine the string values of the tuple using join() method
combineText = "\n".join(tupleString)

# Print the output
print("\nThe list of operating systems are:\n\n%s" % combineText)

"""
    Generate a sequence of strings by combining two strings

"""
str1 = "ABCD "
str2 = "1 "

# Generate sequence of string using join() method
combineText = str2.join(str1)

# Print the output
print("\n%s" % combineText)
