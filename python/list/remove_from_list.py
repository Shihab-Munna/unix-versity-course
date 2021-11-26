# remove()
# Define the list
list = ['Cake', 'Pizza', 'Juice', 'Pasta', 'Burger']

# Print the list before delete
print("List before delete")
print(list)

# Remove an item
list.remove('Juice')

# Print the list after delete
print("List after delete")
print(list)

'''
pop()
'''
# Define the list
ldata = [34, 23, 90, 21, 90, 56, 87, 55]

# Print the before remove
print(ldata)

# Remove the third element
ldata.pop(2)

# Print the list after remove
print(ldata)

#########################################

'''
Del()
'''

# Define the list
ldata = [34, 23, 90, 21, 90, 56, 87, 55]

# Print the before remove
print(ldata)

# Delete the first item using del method
del ldata[0]

# Print the list after remove
print(ldata)

############################################
'''
Clear
'''
# Define the list
ldata = [34, 23, 90, 21, 90, 56, 87, 55]

# Print the before remove
print(ldata)

# Remove all items from the list
ldata.clear()

# Print the list after clear
print(ldata)
