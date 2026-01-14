#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positive = -number
else:
    positive = number
    
if positive % 10 > 5:
    print(f"Last digit of {number} is {positive % 10} and is greater than 5")
elif positive % 10 == 0:
    print(f"Last digit of {number} is {positive % 10} and is 0")
else:
    print(f"Last digit of {number} is {positive % 10} and is less than 6 and not 0")