#!/usr/bin/env python3
# Define a list of selected persons
selectedList = ['Sophia', 'Isabella', 'Olivia', 'Alexzendra', 'Bella']
# Define a list of searching person
searchList = ['Olivia', 'Chloe', 'Alexzendra']
# Define an empty list
foundList = []

# Iterate each element from the selected list
for index, sList in enumerate(selectedList):
    # Match the element with the element of searchList
    if sList in searchList:
        # Store the value in foundList if the match is found
        foundList.append(selectedList[index])

# iterate the searchList
for val in searchList:
    # Check the value exists in foundList or not
    if val in foundList:
        print("%s is selected.\n" % val)
    else:
        print("%s is not selected.\n" % val)
