str = input('Enter any two word string: ')

splited_str = str.split(" ")
if len(splited_str) <= 1:
    print("Sorry you have to input at least string")
else:
    for word in splited_str:
        reversed_str = word[::-1]
        print(reversed_str, end=" ")
