expression = input("Enter the math expression with at least one + sign(only + sign allowed): ")

number_from_expression = expression.split("+")

total = 0
all_digit = True
for num in number_from_expression:
    if num.isdigit():
        total += int(num)
    else:
        all_digit = False
        print('Invalid Expression!')

if all_digit:
    print(total)
