mystr = input("Enter your email address: \n")
# Initialize the character counter
char_counter = 0

# Iterate the text to find out the alphabet
for val in mystr:
    # Check the character is any alphabet or not
    if (val.isalpha() == True):
        # Print the character if it is a alphabet
        print("The alphabet found:", val)
        # Increment the counter by 1
    char_counter = char_counter + 1
# Print the total number of alphabets exist in the input
print("The input text contains : ", char_counter, 'alphabets')
