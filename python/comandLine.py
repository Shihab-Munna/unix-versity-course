import math
from sys import argv

script, numbers = argv

li = [int(i) for i in numbers]

add = []
multi = []

for num in li:
    if(num % 2 == 0):
        if(num not in add):
            add.append(num)
    elif(num % 2 != 0):
        if(num not in multi):
            multi.append(num)

len_add = len(add)
len_multi = len(multi)

print("Addition :", end='')
for i in range(0, len_add):
    if(i != len_add-1):
        print(add[i], end=' + ')
    else:
        print(add[i], "=", sum(add), end='\n')

print("Multiplication :", end='')
for i in range(0, len_multi):
    if(i != len_multi-1):
        print(multi[i], end=' * ')
    else:
        print(multi[i], "=", math.prod(multi), end='\n')
