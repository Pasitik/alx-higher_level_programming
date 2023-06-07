#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = 0
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastdigit}"

if lastdigit == 0:
    print(f"{message} and is zero")
elif lastdigit > 5 and lastdigit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} is less than 6 and is not zero")
