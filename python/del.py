li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(li)):
    if int(li[i]) % 2 != 0:
        del li[i]


for i in li:
    print(i)
