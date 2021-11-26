#!/usr/bin/env python3
try:
    # Define a list of books
    bookList = ['The Cat in the Hat', 'Harold and the Purple Crayon',
                'The Very Hungry Caterpillar', 'Goodnight Moon', 'Harold and the Purple Crayon']

    # Take the name of the book that you want to search in the list
    bookName = input("Enter a book name:")
    # Search the element using index method
    search_pos = int(bookList.index(bookName))

    # Print found message
    print("%s book is found in the list" % (bookName))
except(ValueError):
    # Print not found message
    print("%s book is not found in the list" % (bookName))
