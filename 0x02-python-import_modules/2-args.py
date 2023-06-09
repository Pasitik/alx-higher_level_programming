#!/usr/bin/python3
from sys import argv

argLen = len(argv) - 1

if argLen == 1:
    print("{} argument".format(argLen))
    print("{}: {}".format(argLen, argv[argLen]))

else:
    print("{} arguments".format(argLen))
    if argLen > 0:
        for i in range(1, argLen + 1):
            print("{}: {}".format(i, argv[i]))
