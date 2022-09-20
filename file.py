
import random


answer = input("Type a range to guess between: ")

if answer.isdigit():
    answer = int(answer)
    if answer <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

randomNum = random.randrange(0, answer)
guesses = 0
print(randomNum)

while True:
    guesses += 1
    userGuess = input("Guess the random number: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number.")
        continue

    if userGuess == randomNum:
        print("Corret!")
        break
    else:
        if userGuess > randomNum:
            print("You were above the number.")
        else:
            print("You were below the number.")

print("You guessed" , guesses , "times. ")