a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

a_square = pow(a, 2)  # (a*a)
b_square = pow(b, 2)  # (b*b)
two_ab = (2.0 * (a * b))
result = round((a_square + two_ab + b_square), 2)

print('Result is', result)
