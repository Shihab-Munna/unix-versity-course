def order(x, y):
    if int(x[1]) > int(y[1]):
        return x, y
    else:
        return y, x


def bubble(mydict):
    d_items = mydict.items()
    for j in range(len(d_items) - 1):
        for i in range(len(d_items) - 1):
            str(d_items)
            print(d_items)
            # d_items[i], d_items[i + 1] = order(d_items[i], d_items[i + 1])
    return d_items


if __name__ == '__main__':
    d = {}
    higher_1_lac = 0
    less_then_1_lac = 0
    for i in range(5):
        data = input().split(' ')
        d[data[0]] = data[1]
    for name, balance in d.items():
        if int(balance) >= 100000:
            higher_1_lac += 1
            print(name, ":", balance)
        else:
            less_then_1_lac += 1

    print('Grater Then 1 Lac: ', higher_1_lac)
    print('Less Then 1 Lac: ', less_then_1_lac)

    # print(dict.items(d))
    sorted_dict = bubble(d)
    print("Name     Balance")
    for x in sorted_dict:
        print(x)
