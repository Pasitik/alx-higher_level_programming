#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if (i+1) % 3 == 0 and (i+1) % 5 == 0:
            print("FizzBuzz ", end='')
        if (i+1) % 3 == 0:
            print("Fizz ", end='')
        elif (i+1) % 5 == 0:
            print("Buzz ", end='')
        else:
            print(f"{i+1} ", end='')
