#!/usr/bin/python3
from sys import argv

argLen =  len(argv)

add = 0 

for i in range (1, argLen):
    add = add + int(argv[i])
print("{}".format(add))
