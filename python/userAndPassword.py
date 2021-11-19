def is_valid(passwd):
    global special_character
    SpecialSym = ['$', '#', '%', '!', '@', '%', '&']
    val = True

    if len(passwd) != 8:
        print('length should be 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one number')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


def main():
    user_name = input("Enter your user name: ")
    password = input("Enter a password which contains at least one number and one special char:  ")
    if (user_name.isalpha() and len(user_name) == 6):
        print("Valid Username")
    else:
        print("Invalid username- Use all char and length must be 6")

    if (is_valid(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")


# Driver Code
if __name__ == '__main__':
    main()
