"""Create a text file manually with the following data. Write a python script to take the product name and new price using command line argument.Search the product in the file and update the old price with the new price. Print the sorted product list based on price."""

from os.path import exists
from sys import argv

script, productName, price = argv

fileName = "products.txt"
if not exists(fileName):
    print("File not found!")
else:
    OpenTheFile = open(fileName, "r")  # Open file on read mode
    lines = OpenTheFile.read().splitlines()
    OpenTheFile.close()
    index = 0
    for line in lines:
        if str(" " + productName + " ") in line:
            lines[index] = line.split("Tk.", 1)[0] + "Tk. " + price
        index += 1

    length = len(lines)

    for i in range(1, length):
        current_product_price = int(lines[i].split("Tk.", 1)[1])
        for j in range(i, length):
            next_product_price = int(lines[j].split("Tk.", 1)[1])
            if current_product_price > next_product_price:
                temp = lines[i]
                lines[i] = lines[j]
                lines[j] = temp

    targetFile = open(fileName, "w+")
    targetFile.truncate()
    targetFile.write("ID      Name      Price\n")
    lengthOfLines = len(lines)
    for i in range(1, lengthOfLines):
        product = "0" + str(i) + "." + lines[i].split(".", 1)[1] + "\n"
        targetFile.write(product)

    targetFile.close()
