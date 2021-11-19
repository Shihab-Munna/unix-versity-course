value = input('Enter a 4 digit Number: ')
value.strip()
if len(value) != 4:
    print('Sorry The Number Must Have to be four digit')
else:
    sum = 0
    all_digit = True
    for num in value:
        if num.isdigit():
            sum += int(num)
        else:
            all_digit = False
            print('All must be string')
            break
    if all_digit:
        print("Sum =", sum)
