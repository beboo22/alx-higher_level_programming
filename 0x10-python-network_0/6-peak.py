#!/usr/bin/python3

def find_peak(list_of_integers):
    x = len(list_of_integers)
    if x == 0:
        return None

    if x == 1:
        return list_of_integers[0]

    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[x-1] > list_of_integers[x-2]:
        return list_of_integers[x-1]

    for i in range(1, x-1):
        if list_of_integers[i] > list_of_integers[i-1] and list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
        elif list_of_integers[i-1] == list_of_integers[i] and list_of_integers[i] == list_of_integers[i+1]:
            return list_of_integers[i]
