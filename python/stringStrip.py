# Take a string data as input
string1 = input("Enter a string\n")
# Take a character data as input
char1 = input("Enter a character to remove from the string\n")

# Remove the character from both side of the string data
newString = string1.strip(char1)

# print the original string
print("The original string is :\n%s" % string1)
# Print the string after stripping
print("The output after removing '%c' from the string is:\n%s" % (char1, newString))

# Define an infinite loop
while (True):
    # Take an url address as input
    url = input("Enter a URL address\n")
    # Take a string data as input
    charList = input("Enter the characters to remove\n")
    '''Remove the character from both side of the string data
       where matches'''
    newString = url.strip(charList)

    # print the original string
    print("The original string is :\n%s" % url)
    # Print the string after stripping
    print("The output after removing the characters\n%s" % newString)

    # ask user to continue the script or not

    answer = input("Do you want to quit(y/n)?")
    # Terminate the loop if the answer is 'y' or 'Y'
    if (answer == 'y' or answer == 'Y'):
        break

username = " admin"
password = " hello123 "

# Compare the strings without removing space
print("Output without strip method:")

if (username == "admin" and password == "hello123"):
    print("Authenticated user\n")
else:
    print("Not Authenticated user\n")

# Compare the strings by removing space
print("Output with strip method:")

if (username.strip() == "admin" and password.strip() == "hello123"):
    print("Authenticated user")
else:
    print("Not Authenticated user")
