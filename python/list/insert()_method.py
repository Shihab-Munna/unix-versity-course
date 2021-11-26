# Declare list
# list_data = [89, 56, 90, 34, 89, 12]
#
# # Insert data in the 2nd position
# list_data.insert(2, 23)
#
# # Displaying list after inserting
# print("The list elements are")
#
# for i in range(0, len(list_data)):
#     print(list_data[i])

###################### appand() #########################
# Define the list
listdata = ["Dell", "HP", "Leveno", "Asus"]

# Insert data using append method
listdata.append("Toshiba")

# Display the list after insert
print("The list elements are")

for i in range(0, len(listdata)):
    print(listdata[i])

##Insert item using extend() method
# initializing the first list
list1 = ['html', 'CSS', 'JavaScript', 'JQuery']

# initializing the second list
list2 = ['PHP', 'Laravel', 'CodeIgniter']

# Combine both lists using extend() method
list1.extend(list2)

# Display the list after combing
print("The list elements are :")

for i in range(0, len(list1)):
    print(list1[i])
