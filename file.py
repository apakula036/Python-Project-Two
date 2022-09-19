
import random


answer = input("Type a number: ")

if answer.isdigit():
    answer = int(answer)
    if answer <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

randomNum = random.randrange(-1, 10)

print(randomNum)