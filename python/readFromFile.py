from sys import argv
from os.path import exists

script, filename = argv

if not exists(filename):
    print('File not found!')
else:
    want_to_override = input('Press Y if you want to override the file Press N if you dont want to: ')
    if want_to_override == 'y' or want_to_override == 'Y':
        target = open(filename, 'w+')
        target.truncate()
        print('Type to add data')
        line1 = input("line 1: ")
        line2 = input("line 2: ")
        line3 = input("line 3: ")
        line4 = input("line 4: ")
        print("I'm going to write these to the file.")
        target.write(line1)
        target.write("\n")
        target.write(line2)
        target.write("\n")
        target.write(line3)
        target.write("\n")
        target.write(line4)
        target.write("\n")
        target.close()
        print('Added the New Data')
    fileToOpen = open(filename)  # Open file on read mode
    lines = fileToOpen.read().splitlines()  # List with stripped line-breaks
    fileToOpen.close()
    print(lines)
    lines.pop(0)
    print('Id Name Price')
    for line in lines:
        print("line-> ", line)
        row = line.split(' ')
        print('row->', row)
        if int(row[2]) >= 100:
            print(row[0], " ", row[1], " ", row[2])
