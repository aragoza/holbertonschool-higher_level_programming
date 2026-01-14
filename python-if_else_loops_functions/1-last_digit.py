#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    positive = -(-number % 10)
elif number >= 0:
    positive = number % 10

if positive > 5:
    print(f"Last digit of {number} is {positive} and is greater than 5")
elif positive == 0:
    print(f"Last digit of {number} is {positive} and is 0")
elif positive < 6 and positive % 10 != 0:
    print(f"Last digit of {number} is {positive} and is less than 6 and not 0")
