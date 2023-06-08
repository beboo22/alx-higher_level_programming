#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    y = 0
    for i in range(1, n):
        y += int(argv[i])
    print(y)
