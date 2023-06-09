#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argLen = len(sys.argv)

    add = 0

    for i in range(1, argLen):
        add += int(sys.argv[i])
    print("{}".format(add))
