"""Using % sign """

# name = input("Enter Your Name: ")
# print("Welcome to the world of python, %s!" % name)
#
# # Initialize two string variables
# employee = "John"
# profession = "Programmer"
# # Print the formatted values of the variables
# print("%s is a  %s" % (employee, profession))
#
# """Using format() method """
# color = input("what is your favorite color?")
# print('My Favorite Colors are {}'.format(color))
#
# """
#     String Formatting Using Multiple Positional Parameters
# """
# weight = float(input("What is your weight in Kg? -"))
# height = float(input("What is your height in meter? -"))
#
# BMI = round((weight / (height * height)), 2)
#
# print("Your height is {1} and weight is {0}\nYour BMI is {2}\n".format(weight, height, str(BMI)))

"""
    String Formatting Using the Keyword Parameter
"""

id = input("Enter your ID: ")


def result(id):
    switcher = {
        "1001": "A+",
        "1002": "B+",
        "1004": "C+"

    }
    return switcher.get(id, "Invalid")


if (result(id) != "Invalid"):
    print('{name} got {grade}'.format(name=id, grade=result(id)))
else:
    print('{0} got {grade}'.format(id, grade="F"))
