# Chapter - 13 guess the number game in python

import random

mynum = random.randint(0,9) # compurter guess number
print("I have a Number in My Mind, Can You Guess it?")

while True:
    userNum = int(input("Enter Your Guess: "))

    if userNum == mynum:
        print("Yes You are Right")
        break
    elif userNum > mynum:
        print("My number is greater than the number you entered,\nTry again")
    else:
        print("My number is less than the number you entered,\nTry again")