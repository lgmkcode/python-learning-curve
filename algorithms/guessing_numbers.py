import random
import time

randnum = random.randint(1, 100)
hak = 3

while True:
    guessnum = int(input("Enter a guess:"))
    if guessnum < randnum:
        print("being checked")
        time.sleep(1)
        print("Enter a large number")
        hak -= 1
    elif guessnum > randnum:
        print("being checked")
        time.sleep(1)
        print("Enter a smaller number")
        hak -= 1
    else:
        print("correct answer")
        break
    if hak == 0:
        print("your guess is over")
        break
