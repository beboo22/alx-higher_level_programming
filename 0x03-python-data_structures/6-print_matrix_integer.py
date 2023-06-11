#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for ele in row:
                print("{:d} ".format(ele),end="" if ele != row[-1] else "\n")print("\n")
    else:
        print()
