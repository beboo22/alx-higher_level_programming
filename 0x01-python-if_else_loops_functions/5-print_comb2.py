#!/usr/bin/python3
for i in range(0, 100):
    if i < 10 and i > 0:
        print("0{}, ".format(i),end='')
    elif i  == 99:
        print("{:d}".format(i))
    elif i >= 10:
        print("{:d}, ".format(i),end='')
