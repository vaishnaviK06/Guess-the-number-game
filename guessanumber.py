import random

name = input("What is your name?")
print("Hello! "+name+ " Guess a number between 1-30")
x = random.randint(1, 30)
count=0
for i in range(5):
    count+=1
    guess = int(input("Guess a number"))
    if(guess == x):
      print("Congratulations! You guessed it right")
      break;
    elif(x < guess):
      print(str(count)+" Guess is too high")
    else:
      print(str(count)+" Guess is too low")
if(count == 5):
  print("Random number"+ str(x))



import random

name = input("What is your name?")
print("Hello! "+name+ " Enter the lower and upper bound")
upper = int(input("Input upper bound"))
lower = int(input("Input lower bound"))

x = random.randint(lower, upper)
count=0
isguess = False
for i in range(5):
    count+=1
    guess = int(input("Guess a number"))
    if(guess == x):
      print("Congratulations! You guessed it right")
      isguess = True;
      break;
    elif(x < guess):
      print(str(count)+" Guess is too high")
    else:
      print(str(count)+" Guess is too low")
if(isguess == False):
  print("Guessed number was"+ str(x))

