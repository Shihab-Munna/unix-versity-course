from random import randint

# Define a infinite while loop
while(True):

  # Generate a randon number from 10 to 99
  number = randint(10,99)

  # Print the currently generated number
  print("The newly generated number is %s" % number)

  # Terminate the loop if the number is more than 75
  if (number > 75 ):
    print("Better luck next time")
    break

  # Terminate the loop if the number is equal to 99
  elif(number == 99):
    print("Bingo!!!, You are the winner")
    break

  # Continue the loop
  else:
    print("You can try for another time")