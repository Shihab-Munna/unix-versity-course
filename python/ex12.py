age = input("How old are you?: ")
height = input("How tall are you?: ")
weight = input("How much do you weight?: ")

if int(age) > 1:
    years = 'years'
else:
    years = 'year'

print(f"So, you're {age} {years} old, {height} tall and {weight} heavy.")
