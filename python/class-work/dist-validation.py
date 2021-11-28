import string

employees = {
    1: {
        "name": "Shihab Uddin Munna",
        "phoneNumber": "01711907520",
        "email": "memunna2@gmail.com",
    },
    2: {
        "name": "Shahadat Hossain",
        "phoneNumber": "+01829092577",
        "email": "sha@gmail.com",
    },
    3: {
        "name": "Abdul karim",
        "phoneNumber": "+880 123657543",
        "email": "xyz_$gmail.com",
    },
    4: {
        "name": "Marina Mim",
        "phoneNumber": "s34256400907",
        "email": "mkinn@gmail.com",
    },
    5: {
        "name": "Toukir Hossain",
        "phoneNumber": "0990878909",
        "email": "toukir@gmail.com",
    },
}

for key in employees:
    isValidName = True
    isValidPhoneNumber = True
    isValidEmail = True

    # Iterate the loop to check the phone number is valid or not
    for character in employees[key]["name"]:
        if character not in (string.whitespace + string.ascii_letters):
            isValidName = False

    # Iterate the loop to check the email is valid or not
    for character in employees[key]["email"]:
        if character not in (string.ascii_letters + string.punctuation + string.digits):
            isValidPhoneNumber = False
    # Iterate the loop to check the email is valid or not
    for character in employees[key]["phoneNumber"]:
        if character not in (string.punctuation + string.digits + string.whitespace):
            isValidEmail = False

    # print(isValidName, isValidPhoneNumber, isValidEmail)
    if isValidName == True and isValidPhoneNumber == True and isValidEmail == True:
        print(employees[key])
