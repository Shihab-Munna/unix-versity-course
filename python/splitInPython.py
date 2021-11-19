# # Define a string value
# text = "Hello, Welcome to LinuxHint"
#
# # Print message
# print("The list after splitting the string:\n")
#
# # Print the list based on white space
# print(text.split())

"""
    Split string based on comma

"""

country = input("Enter Few names of countries with comma\n")

# Split the string based on comma
listCountry = country.split(',')

# Print message
print("\nList of countries:")
for i in range(0, len(listCountry)):
    print(listCountry[i])

"""
    Split string based on the specific word
"""
text = "Bash and Python and PHP"

# Split the string based on " and "
languageValue = text.split(" and ")

# Print the list items by combining other string
for i in range(0, len(languageValue)):
    print("I like ", languageValue[i])

"""
     Split string based on the limit (maxSplit)
"""
person = "Jack:Manager:Bata Company:jack@gmail.com"
print("--------Split for 3 ':'---------")

val1 = person.split(":", 3)

# Print the list values
for i in range(0, len(val1)):
    print("part", i + 1, "-", val1[i])

print("--------Split for 2 ':'---------")

# Split the string based on ":" and limit 2
val2 = person.split(":", 2)

# Print the list values
for i in range(0, len(val2)):
    print("part", i + 1, "-", val2[i])

print("--------Split for 1 ':'---------")

# Split the string based on ":" and limit 1
val3 = person.split(":", 1)

# Print the list values
for i in range(0, len(val3)):
    print("part", i + 1, "-", val3[i])
