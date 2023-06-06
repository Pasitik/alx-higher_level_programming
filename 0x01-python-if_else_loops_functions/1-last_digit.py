#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = 0;
if number >= 0:
	lastdigit = number % 10
else:
	lastdigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastdigit}"

if lastdigit > 5:
	print(f"{message} and is greater than 5")
elif lastdigit == 0:
	print(f"{message} and is zero")
else:
	print(f"{message} is less than 6 and is not zero")
