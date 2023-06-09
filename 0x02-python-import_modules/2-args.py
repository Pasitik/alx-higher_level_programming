#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argLen = len(argv) - 1
    if argLen == 0:
        print("{} arguments.".format(argLen))
    if argLen == 1:
        print("{} argument:".format(argLen))
        print("{}: {}".format(argLen, argv[argLen]))

    else:
        print("{} arguments:".format(argLen))
        for i in range(1, argLen + 1):
            print("{}: {}".format(i, argv[i]))
