# Import string module
import string

# Take any string data
year = input("Enter a year: ")

# Inilialize error variable
error = False


# Iterate the loop to check any uppercase letter exists or not
for character in year:
    if character not in string.digits:
        error = True


if error == True:
    print("Invalid year value")
else:
    # Check the year is leap year or not
    year = int(year)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear = True
    else:
        leapYear = False

    if leapYear == True:
        print("%d is a leap year" % year)
    else:
        print("%d is not a leap year" % year)
