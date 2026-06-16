import random

random_num = random.randrange(0, 101)
print("############################################")
print("Welcome to guess the number")
print("To get started, guess any number from 0-100")
print("############################################\n")
control = input("type s to start guessing and q to exit: ")
if control == "q":
    exit
elif control == "s":
    while True:
        guess = int(input("Enter your guess: "))

        if guess == random_num:
            print("You win")
            break

        elif guess > random_num:
            print("Lower!")

        else:
            print("Higher!")
else:
  print("Undefined input!")
