#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = 0;
if number >= 0:
	lastdigit = number % 10
else:
	lastdigit = (-number % 10) * -1
if lastdigit < 6 and lastdigit != 0:
	print(f"the last digit of {number} is {lastdigit} and is less then 6 and not zero")
if lastdigit == 0:
	print(f"the last digit of {number} is {lastdigit} and is zero")
if lastdigit > 5:
	print(f"the last digit of {number} is {lastdigit} and is greater than 5")
